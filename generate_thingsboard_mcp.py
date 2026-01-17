import inspect
import os
import shutil
import sys
import json
import re
import pkgutil
import importlib
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Type, Tuple

# ==========================================
# 1. SETUP & CONFIG
# ==========================================

OUTPUT_DIR = "thingsboard_mcp"
LIB_NAME = "tb_rest_client"

@dataclass
class ToolMeta:
    name: str
    group: str
    desc: str
    signature: str

@dataclass
class IgnoredMeta:
    name: str
    reason: str
    details: str

def force_import_submodules(package):
    """Recursively imports submodules to ensure classes are loaded."""
    if hasattr(package, "__path__"):
        for _, name, _ in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
            try: importlib.import_module(name)
            except: continue

def load_edition_components(suffix: str):
    try:
        client_mod = importlib.import_module(f"{LIB_NAME}.rest_client_{suffix}")
        ClientClass = getattr(client_mod, f"RestClient{suffix.upper()}")
        
        api_pkg = importlib.import_module(f"{LIB_NAME}.api.api_{suffix}")
        force_import_submodules(api_pkg)
        
        model_pkg_name = f"{LIB_NAME}.models.models_{suffix}"
        return ClientClass, api_pkg, model_pkg_name
    except ImportError as e:
        print(f"Error loading {suffix}: {e}")
        return None, None, None

def discover_editions():
    try:
        lib = importlib.import_module(LIB_NAME)
        path = os.path.dirname(lib.__file__)
        editions = []
        for file in os.listdir(path):
            match = re.match(r"rest_client_(\w+)\.py", file)
            if match:
                suffix = match.group(1)
                if suffix != "base": editions.append(suffix)
        return editions
    except: return []

# ==========================================
# 2. INTELLIGENT TRACER
# ==========================================

class EditionTracer:
    def __init__(self, suffix: str, client_class, api_pkg):
        self.controllers: Dict[str, Type] = {}
        self.var_map: Dict[str, str] = {}
        self._scan_package(api_pkg)
        self._map_variables(client_class)

    def _scan_package(self, api_pkg):
        if hasattr(api_pkg, "__path__"):
            prefix = api_pkg.__name__ + "."
            for _, name, _ in pkgutil.walk_packages(api_pkg.__path__, prefix):
                if name in sys.modules:
                    mod = sys.modules[name]
                    for cls_name, cls_obj in inspect.getmembers(mod, inspect.isclass):
                        if cls_name.endswith("ControllerApi"):
                            self.controllers[cls_name] = cls_obj

    def _map_variables(self, client_class):
        def scan(cls):
            try:
                src = inspect.getsource(cls)
                matches = re.findall(r'self\.(\w+)\s*=\s*(\w+)\(', src)
                for var, cls_name in matches:
                    self.var_map[var] = cls_name
            except: pass

        for base in client_class.__mro__:
            scan(base)
            for name, member in inspect.getmembers(base):
                if name == "login" or "load_controllers" in name:
                    if inspect.isfunction(member): scan(member)

    def trace_method(self, client_func) -> Tuple[str, Optional[str], Optional[str], Optional[str]]:
        try:
            source = inspect.getsource(client_func)
            match = re.search(r'self\.(\w+)\.(\w+)\s*\(', source)
            
            if not match: 
                return "NO_API_CALL", None, None, "Does not call self.x.y()"
            
            var_name, target_method = match.groups()
            
            cls_name = self.var_map.get(var_name)
            if not cls_name:
                parts = var_name.replace("_controller", "").split("_")
                cls_name = "".join(p.capitalize() for p in parts) + "ControllerApi"

            ctrl_cls = self.controllers.get(cls_name)
            if not ctrl_cls:
                return "CONTROLLER_NOT_LOADED", None, None, f"Class {cls_name} not found"

            docstring = ""
            if hasattr(ctrl_cls, target_method):
                real_method = getattr(ctrl_cls, target_method)
                raw_doc = real_method.__doc__
                if raw_doc:
                    cleaned = raw_doc.split("This method makes a synchronous")[0]
                    cleaned = cleaned.split(">>> thread = api.")[0]
                    cleaned = cleaned.strip()
                    docstring = cleaned if cleaned else raw_doc.strip()

            if not docstring:
                return "MISSING_DOCS", None, None, f"{cls_name}.{target_method} docstring empty"

            group = cls_name.replace("ControllerApi", "")
            group = re.sub(r'(?<!^)(?=[A-Z])', '_', group).lower()
            
            return "SUCCESS", group, docstring, None

        except Exception as e:
            return "ERROR", None, None, str(e)

# ==========================================
# 3. GENERATION LOGIC
# ==========================================

PRIMITIVES = {"str", "int", "bool", "float", "None", "NoneType", "Any", "dict", "list", "object", "bytes"}

def get_type_str(t):
    s = str(t).replace("typing.", "").replace("Optional", "").replace("Union", "").replace("List", "")
    s = s.replace("<class", "").replace(">", "").replace("[", " ").replace("]", " ").replace(",", " ").replace("|", " ")
    for w in s.split():
        w = w.strip().strip("'").strip('"')
        if "." in w: w = w.split(".")[-1]
        if w in ["None", "NoneType", "Any"]: continue
        return w
    return "str"

def generate_tool_code(name: str, func: callable, tracer: EditionTracer) -> Tuple[Optional[str], str, Any]:
    outcome, group, docstring, error_details = tracer.trace_method(func)
    
    if outcome != "SUCCESS":
        return None, None, IgnoredMeta(name, outcome, error_details)

    docstring_safe = docstring.replace('"""', "'''").replace("\\", "\\\\")
    
    sig = inspect.signature(func)
    args_def, args_call, sig_desc = [], [], []
    
    for pname, param in sig.parameters.items():
        if pname == 'self': continue
        type_name = get_type_str(param.annotation)
        
        default_val = ""
        if param.default != inspect.Parameter.empty:
            if param.default is None: default_val = " = None"
            elif isinstance(param.default, str): default_val = f' = "{param.default}"'
            else: default_val = f" = {param.default}"

        is_model = type_name not in PRIMITIVES and "dict" not in str(param.annotation).lower() and "list" not in str(param.annotation).lower()
        is_json = "dict" in str(param.annotation).lower() or "list" in str(param.annotation).lower()

        if is_model:
            args_def.append(f"{pname}_json: str{default_val}")
            args_call.append(f"{pname}=deserialize_param({pname}_json, '{type_name}')")
            sig_desc.append(f"`{pname}_json` ({type_name})")
        elif is_json:
            args_def.append(f"{pname}_json: str{default_val}")
            args_call.append(f"{pname}=json.loads({pname}_json) if {pname}_json else None")
            sig_desc.append(f"`{pname}_json` (JSON)")
        else:
            py_type = "str"
            if "int" in type_name: py_type = "int"
            elif "bool" in type_name: py_type = "bool"
            elif "float" in type_name: py_type = "float"
            if default_val == " = None": py_type = f"Optional[{py_type}]"
            
            args_def.append(f"{pname}: {py_type}{default_val}")
            args_call.append(f"{pname}={pname}")
            sig_desc.append(f"`{pname}`")

    code = f"""
def {name}({", ".join(args_def)}) -> str:
    \"\"\"
    {docstring_safe}
    \"\"\"
    try:
        client = get_client()
        result = client.{name}({", ".join(args_call)})
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform '{name}'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {{e.status}}: {{e.reason}}\\n{{e.body}}"
    except Exception as e:
        return f"Error: {{str(e)}}"
"""
    desc_md = docstring.replace("\n", "<br>").replace("|", "&#124;")
    sig_md = ", ".join(sig_desc) if sig_desc else "None"
    
    meta = ToolMeta(name, group, desc_md, sig_md)
    return group, code, meta


# ==========================================
# 4. REPORT WRITER
# ==========================================

def write_markdown_report(suffix, tools: List[ToolMeta], ignored: List[IgnoredMeta]):
    filename = f"TOOLS_{suffix.upper()}.md"
    grouped = {}
    for t in tools:
        if t.group not in grouped: grouped[t.group] = []
        grouped[t.group].append(t)
    
    # Sort groups for consistent TOC
    sorted_groups = sorted(grouped.keys())
    top_anchor = f"thingsboard-mcp-tools-{suffix.lower()}"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# ThingsBoard MCP Tools ({suffix.upper()})\n\n")
        f.write("## 📊 Summary\n")
        f.write(f"- **Total Tools:** {len(tools)}\n")
        f.write(f"- **Tool Categories:** {len(grouped)}\n\n")
        
        # TOC
        f.write("## 📑 Table of Contents\n")
        for group in sorted_groups:
            title = group.replace("_", " ").title() + " Tools"
            slug = title.lower().replace(" ", "-")
            f.write(f"- [{title}](#{slug})\n")
        f.write("- [🚫 Ignored Methods](#-ignored-methods)\n\n")
        
        f.write("---\n")

        # Groups
        for group in sorted_groups:
            title = group.replace("_", " ").title() + " Tools"
            f.write(f"## {title}\n\n")
            f.write("| Tool Name | Description | Parameters |\n")
            f.write("| :--- | :--- | :--- |\n")
            for t in sorted(grouped[group], key=lambda x: x.name):
                sig = t.signature.replace("|", "&#124;")
                desc = t.desc.replace("|", "&#124;")
                f.write(f"| `{t.name}` | {desc} | {sig} |\n")
            # Navigate back to main title
            f.write(f"\n[⬆ Back to Top](#{top_anchor})\n\n")
            
        f.write("## 🚫 Ignored Methods\n\n")
        f.write("| Method Name | Reason | Details |\n")
        f.write("| :--- | :--- | :--- |\n")
        for i in sorted(ignored, key=lambda x: x.reason):
            f.write(f"| `{i.name}` | {i.reason} | {i.details} |\n")
            
    print(f" > Report generated: {filename}")


# ==========================================
# 5. EXECUTION
# ==========================================

def process_edition(suffix: str):
    print(f"--- Processing Edition: {suffix.upper()} ---")
    ClientClass, api_pkg, model_pkg_name = load_edition_components(suffix)
    if not ClientClass: return

    tracer = EditionTracer(suffix, ClientClass, api_pkg)
    
    base_path = f"{OUTPUT_DIR}/tools/{suffix}"
    if os.path.exists(base_path): shutil.rmtree(base_path)
    os.makedirs(base_path)
    
    files_content: Dict[str, List[str]] = {}
    valid_tools = []
    ignored_items = []
    
    mock_instance = ClientClass("http://localhost")
    IGNORED_PREFIXES = ["_", "api_client", "get_type", "get_id"]
    
    for name, func in inspect.getmembers(mock_instance, predicate=inspect.ismethod):
        if any(name.startswith(x) for x in IGNORED_PREFIXES): continue
        
        # STRICT LAMBDA FILTER
        if name == "<lambda>": continue
        
        if name in ['login', 'logout', 'token_login', 'get_token', 'run', 'start', 'join', 'is_alive']: 
            ignored_items.append(IgnoredMeta(name, "UTILITY", "Internal SDK Utility"))
            continue

        group, code, meta = generate_tool_code(name, func, tracer)
        
        if group and code:
            if group not in files_content: files_content[group] = []
            files_content[group].append(code)
            valid_tools.append(meta)
        else:
            ignored_items.append(meta)

    for group, codes in files_content.items():
        with open(f"{base_path}/{group}.py", "w") as f:
            f.write("import json\n")
            f.write("from typing import Optional\n")
            f.write(f"import {model_pkg_name} as models\n")
            f.write("from ..shared import get_client, deserialize_param, format_response, ApiException\n\n")
            for c in codes: f.write(c + "\n")
            f.write("\ndef register(mcp):\n")
            for c in codes:
                tool_name = re.search(r'def (\w+)\(', c).group(1)
                f.write(f"    mcp.tool()( {tool_name} )\n")

    with open(f"{base_path}/__init__.py", "w") as f: f.write("")
    write_markdown_report(suffix, valid_tools, ignored_items)

def write_static_files(editions):
    with open(f"{OUTPUT_DIR}/tools/shared.py", "w") as f:
        imports = ""
        for suffix in editions:
            imports += f"""
    if EDITION == "{suffix.upper()}":
        from {LIB_NAME}.rest_client_{suffix} import RestClient{suffix.upper()} as RestClient
        import {LIB_NAME}.models.models_{suffix} as models
"""
        f.write(f"""
import os, json, time
from typing import Any

TB_URL = os.getenv("TB_URL", "http://localhost:8080")
TB_USERNAME = os.getenv("TB_USERNAME", "tenant@thingsboard.org")
TB_PASSWORD = os.getenv("TB_PASSWORD", "tenant")
EDITION = os.getenv("TB_EDITION", "{editions[0].upper()}")

try:
    {imports}
    from {LIB_NAME}.rest import ApiException
except ImportError:
    pass

_client = None
_last_login = 0

def get_client():
    global _client, _last_login
    if _client is None:
        print(f"Logging in to {{TB_URL}} as {{TB_USERNAME}} ({{EDITION}})...")
        _client = RestClient(base_url=TB_URL)
        _client.login(username=TB_USERNAME, password=TB_PASSWORD)
        _last_login = time.time()
    
    if time.time() - _last_login > 7200:
         try:
             _client.login(username=TB_USERNAME, password=TB_PASSWORD)
             _last_login = time.time()
         except: pass

    return _client

def deserialize_param(value: str, model_name: str):
    if not value: return None
    try:
        data = json.loads(value)
        if hasattr(models, model_name):
            clazz = getattr(models, model_name)
            return clazz(**data)
        return data
    except: return value

def format_response(resp: Any) -> str:
    if hasattr(resp, 'to_dict'): return json.dumps(resp.to_dict(), indent=2, default=str)
    if isinstance(resp, list): return json.dumps([x.to_dict() if hasattr(x, 'to_dict') else x for x in resp], indent=2, default=str)
    return str(resp)
""")
    with open(f"{OUTPUT_DIR}/main.py", "w") as f:
        f.write(f"""
import os, sys
from mcp.server.fastmcp import FastMCP
sys.path.append(os.path.dirname(__file__))

EDITION = os.getenv("TB_EDITION", "{editions[0].upper()}")
print(f"Starting ThingsBoard MCP ({{EDITION}})")
mcp = FastMCP(f"ThingsBoard MCP ({{EDITION}})")

try:
    tool_pkg_name = f"tools.{{EDITION.lower()}}"
    tool_pkg = __import__(tool_pkg_name, fromlist=["__path__"])
    import pkgutil
    if hasattr(tool_pkg, "__path__"):
        for _, name, _ in pkgutil.iter_modules(tool_pkg.__path__):
            try:
                mod = __import__(f"{{tool_pkg_name}}.{{name}}", fromlist=["register"])
                if hasattr(mod, "register"):
                    mod.register(mcp)
            except Exception as e:
                print(f"Failed module {{name}}: {{e}}")
except ImportError as e:
    print(f"Error: {{e}}")

if __name__ == '__main__':
    mcp.run()
""")

def main():
    if os.path.exists(OUTPUT_DIR): shutil.rmtree(OUTPUT_DIR)
    os.makedirs(f"{OUTPUT_DIR}/tools")
    with open(f"{OUTPUT_DIR}/__init__.py", "w") as f: f.write("")
    with open(f"{OUTPUT_DIR}/tools/__init__.py", "w") as f: f.write("")

    editions = discover_editions()
    write_static_files(editions)
    for suffix in editions:
        process_edition(suffix)
    print("\nGeneration Complete.")

if __name__ == "__main__":
    main()