import inspect
import os
import shutil
import sys
import re
from typing import Any, get_type_hints, Dict, List, Set

# --- CONFIGURATION ---
TARGET_EDITION = "PE"
OUTPUT_DIR = "thingsboard_mcp"

# Methods we intentionally do not want to expose as tools
IGNORED_METHODS = {
    "login", "logout", "token_login", "get_token", "api_client", 
    "get_type", "get_id", "public_login", "get_user_token", 
    "get_basic_auth_token", "auth_settings", "to_debug_report"
}

# --- CATEGORY MAPPING ---
CATEGORIES = {
    "device": "device",
    "asset": "asset",
    "alarm": "alarm",
    "customer": "customer",
    "user": "user",
    "dashboard": "dashboard",
    "entity_group": "entity_group",
    "relation": "relation",
    "telemetry": "telemetry",
    "attribute": "telemetry",
    "timeseries": "telemetry",
    "tenant": "tenant",
    "widget": "widget",
    "rule_chain": "rule_chain",
    "ota": "ota",
    "audit": "audit",
    "edge": "edge",
    "resource": "resource",
    "queue": "queue",
    "report": "report",
    "admin": "admin",
    "converter": "integration",
    "integration": "integration",
    "scheduler": "scheduler",
    "role": "rbac",
    "permission": "rbac",
    "group": "entity_group",
    "two_fa": "security",
    "auth": "security",
    "oauth2": "security"
}
DEFAULT_CATEGORY = "common"

# --- SETUP IMPORTS ---
try:
    import tb_rest_client.api.api_ce as api_ce
    import tb_rest_client.models.models_ce as models_ce
    modules_to_scan = [api_ce]
    
    if TARGET_EDITION == "PE":
        try:
            from tb_rest_client.rest_client_pe import RestClientPE as RestClient
            import tb_rest_client.api.api_pe as api_pe
            import tb_rest_client.models.models_pe as models_pe
            modules_to_scan.append(api_pe)
            models = models_pe
        except ImportError:
            from tb_rest_client.rest_client_ce import RestClientCE as RestClient
            models = models_ce
            TARGET_EDITION = "CE"
    else:
        from tb_rest_client.rest_client_ce import RestClientCE as RestClient
        models = models_ce

except ImportError:
    print("Error: tb-rest-client not found.")
    sys.exit(1)

DOCSTRING_MAP = {}

# --- HELPER FUNCTIONS ---

def build_docstring_map():
    for module in modules_to_scan:
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if name.endswith("ControllerApi"):
                for method_name, method in inspect.getmembers(obj):
                    if not method_name.startswith("_") and method.__doc__:
                        DOCSTRING_MAP[method_name] = clean_docstring(method.__doc__)

def clean_docstring(doc: str) -> str:
    if not doc: return ""
    lines = [line for line in doc.split('\n') if "NOTE:" not in line and ">>>" not in line]
    return "\n".join(lines).strip()

def find_docstring(name: str) -> str:
    if name in DOCSTRING_MAP: return DOCSTRING_MAP[name]
    for suffix in ["_using_post", "_using_get", "_using_delete", "_using_put"]:
        if f"{name}{suffix}" in DOCSTRING_MAP: return DOCSTRING_MAP[f"{name}{suffix}"]
    return "No description available."

def get_param_type_name(annotation) -> str:
    return annotation.__name__ if hasattr(annotation, '__name__') else str(annotation).replace("typing.", "")

def is_complex_model(type_name: str) -> bool:
    return hasattr(models, type_name) or (TARGET_EDITION == "PE" and hasattr(models_ce, type_name))

def get_category(method_name: str) -> str:
    for keyword, category in CATEGORIES.items():
        if keyword in method_name:
            return category
    return DEFAULT_CATEGORY

# --- GENERATION LOGIC ---

def generate_tool_function(method_name: str, func: callable) -> str:
    docstring = find_docstring(method_name).replace('"""', "'''").replace("\\", "\\\\")
    sig = inspect.signature(func)
    type_hints = get_type_hints(func)
    
    args_def = []
    args_call = []
    
    for name, param in sig.parameters.items():
        if name == 'self': continue
        annotation = type_hints.get(name, Any)
        type_name = get_param_type_name(annotation)
        
        is_complex = is_complex_model(type_name) and type_name not in ['str', 'int', 'bool', 'list', 'dict', 'float', 'Any']

        if is_complex:
            args_def.append(f"{name}_json: str")
            args_call.append(f"{name}=deserialize_param({name}_json, '{type_name}')")
        else:
            py_type = "str"
            if annotation == int: py_type = "int"
            elif annotation == bool: py_type = "bool"
            elif annotation == float: py_type = "float"
            
            default_str = ""
            if param.default != inspect.Parameter.empty:
                val = f'"{param.default}"' if isinstance(param.default, str) else param.default
                default_str = " = None" if val is None else f" = {val}"
                if val is None: py_type = f"Optional[{py_type}]"

            if "list" in str(annotation).lower() and not is_complex:
                 args_def.append(f"{name}_json: str{default_str}")
                 args_call.append(f"{name}=json.loads({name}_json) if {name}_json else None")
            else:
                args_def.append(f"{name}: {py_type}{default_str}")
                args_call.append(f"{name}={name}")

    return f"""
def {method_name}({", ".join(args_def)}) -> str:
    \"\"\"
    {docstring}
    \"\"\"
    try:
        client = get_client()
        result = client.{method_name}({", ".join(args_call)})
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform '{method_name}'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {{e.status}}: {{e.reason}}\\n{{e.body}}"
    except Exception as e:
        return f"Error: {{str(e)}}"
"""

# --- SHARED FILE CONTENT ---
SHARED_CONTENT = f"""import os
import json
from typing import Any, Optional

try:
    if "{TARGET_EDITION}" == "PE":
        from tb_rest_client.rest_client_pe import RestClientPE as RestClient
        import tb_rest_client.models.models_pe as models_pe
        import tb_rest_client.models.models_ce as models_ce
        
        def get_model_class(name):
            if hasattr(models_pe, name): return getattr(models_pe, name)
            if hasattr(models_ce, name): return getattr(models_ce, name)
            return None
    else:
        from tb_rest_client.rest_client_ce import RestClientCE as RestClient
        import tb_rest_client.models.models_ce as models_ce
        
        def get_model_class(name):
            if hasattr(models_ce, name): return getattr(models_ce, name)
            return None

    from tb_rest_client.rest import ApiException
except ImportError:
    pass

TB_URL = os.getenv("TB_URL", "http://localhost:8080")
TB_USERNAME = os.getenv("TB_USERNAME", "tenant@thingsboard.org")
TB_PASSWORD = os.getenv("TB_PASSWORD", "tenant")

_client = None

def get_client():
    global _client
    if not _client:
        _client = RestClient(base_url=TB_URL)
        _client.login(username=TB_USERNAME, password=TB_PASSWORD)
    return _client

def deserialize_param(value: str, model_name: str):
    if not value: return None
    try:
        data = json.loads(value)
        clazz = get_model_class(model_name)
        if clazz: return clazz(**data)
        return data
    except: return value

def format_response(resp: Any) -> str:
    if hasattr(resp, 'to_dict'):
        return json.dumps(resp.to_dict(), indent=2, default=str)
    if isinstance(resp, list):
        return json.dumps([x.to_dict() if hasattr(x, 'to_dict') else x for x in resp], indent=2, default=str)
    return str(resp)
"""

def main():
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(f"{OUTPUT_DIR}/tools")

    build_docstring_map()
    mock_client = RestClient("http://localhost")
    # This gets all public methods from the client instance (including inherited ones)
    all_client_methods = inspect.getmembers(mock_client, predicate=inspect.ismethod)
    
    # Tracking Stats
    stats = {
        "total_sdk_methods": 0,
        "generated": [],
        "ignored": [],
        "failed": []
    }

    # 1. Group methods by category
    grouped_methods = {cat: [] for cat in CATEGORIES.values()}
    grouped_methods[DEFAULT_CATEGORY] = []

    print(f"Analyzing {TARGET_EDITION} SDK Methods...")

    for name, func in all_client_methods:
        if name.startswith("_"):
            continue
            
        stats["total_sdk_methods"] += 1
        
        if name in IGNORED_METHODS:
            stats["ignored"].append(name)
            continue
            
        try:
            tool_code = generate_tool_function(name, func)
            if tool_code:
                cat = get_category(name)
                grouped_methods[cat].append((name, tool_code))
                stats["generated"].append(name)
            else:
                # Should not happen if not ignored
                stats["failed"].append((name, "Code generation returned empty"))
        except Exception as e:
            stats["failed"].append((name, str(e)))

    # 2. Write Shared File
    with open(f"{OUTPUT_DIR}/tools/shared.py", "w") as f:
        f.write(SHARED_CONTENT)
    with open(f"{OUTPUT_DIR}/tools/__init__.py", "w") as f:
        f.write("")

    # 3. Write Category Files
    generated_modules = []
    
    for category, items in grouped_methods.items():
        if not items: continue
        
        filename = f"{OUTPUT_DIR}/tools/{category}.py"
        generated_modules.append(category)
        
        with open(filename, "w") as f:
            f.write("import json\nfrom typing import Optional\n")
            f.write("from .shared import get_client, deserialize_param, format_response, ApiException\n\n")
            for _, code in items:
                f.write(code)
                
            f.write("\n\ndef register(mcp):\n")
            f.write("    \"\"\"Register tools with FastMCP server\"\"\"\n")
            for name, _ in items:
                f.write(f"    mcp.tool()( {name} )\n")

    # 4. Write Main Entry Point
    with open(f"{OUTPUT_DIR}/main.py", "w") as f:
        f.write("from mcp.server.fastmcp import FastMCP\n")
        f.write(f"from tools import {', '.join(generated_modules)}\n\n")
        f.write(f"mcp = FastMCP('ThingsBoard MCP {TARGET_EDITION}')\n\n")
        f.write("# Register all modules\n")
        for mod in generated_modules:
            f.write(f"{mod}.register(mcp)\n")
        f.write("\nif __name__ == '__main__':\n")
        f.write("    mcp.run()\n")

    # 5. PRINT COVERAGE REPORT
    print("\n" + "="*50)
    print(f"   THINGSBOARD MCP COVERAGE REPORT ({TARGET_EDITION})")
    print("="*50)
    print(f"Total Public Methods in SDK:  {stats['total_sdk_methods']}")
    print(f"Tools Successfully Generated: {len(stats['generated'])}")
    print(f"Methods Intentionally Ignored: {len(stats['ignored'])}")
    print(f"Failed / Missing:             {len(stats['failed'])}")
    print("-" * 50)
    
    if len(stats["ignored"]) > 0:
        print("\n[IGNORED METHODS] (Auth/System internals):")
        print(", ".join(stats["ignored"]))
        
    if len(stats["failed"]) > 0:
        print("\n[FAILED METHODS] (Action Required):")
        for name, reason in stats["failed"]:
            print(f" - {name}: {reason}")
    else:
        print("\n[SUCCESS] 100% Coverage of eligible methods.")
        
    print("="*50)
    print(f"Server generated in: {OUTPUT_DIR}/main.py")

if __name__ == "__main__":
    main()