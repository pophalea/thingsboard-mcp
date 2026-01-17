import inspect
import os
import shutil
import sys
import json
import re
from typing import Any

# --- 1. CONFIGURATION ---
OUTPUT_DIR = "thingsboard_mcp"

# Try CE (Mandatory)
try:
    import tb_rest_client.api.api_ce as api_ce
    import tb_rest_client.models.models_ce as models_ce
    from tb_rest_client.rest_client_ce import RestClientCE
except ImportError:
    print("CRITICAL ERROR: tb-rest-client CE not found.")
    sys.exit(1)

# Try PE (Optional)
try:
    import tb_rest_client.api.api_pe as api_pe
    import tb_rest_client.models.models_pe as models_pe
    from tb_rest_client.rest_client_pe import RestClientPE
    HAS_PE = True
except ImportError:
    HAS_PE = False
    print("NOTICE: PE SDK not found. Skipping PE generation.")

CATEGORIES = {
    "device": "device", "asset": "asset", "alarm": "alarm", "customer": "customer",
    "user": "user", "dashboard": "dashboard", "relation": "relation",
    "telemetry": "telemetry", "attribute": "telemetry", "timeseries": "telemetry",
    "tenant": "tenant", "widget": "widget", "rule_chain": "rule_chain",
    "admin": "admin", "integration": "integration", "scheduler": "scheduler",
    "audit": "audit", "entity_group": "entity_group", "ota": "ota", 
    "oauth2": "security", "auth": "security", "two_fa": "security"
}
DEFAULT_CATEGORY = "common"
IGNORED_METHODS = {
    "login", "logout", "token_login", "get_token", "api_client", 
    "get_type", "get_id", "public_login", "get_user_token", 
    "get_basic_auth_token", "auth_settings", "to_debug_report"
}

# --- 2. LOGIC: PRIMITIVE DETECTION ---

PRIMITIVES = {
    "str", "int", "bool", "float", "None", "NoneType", "Any", "dict", "list", "object", "bytes"
}

def extract_type_name_from_string(type_str: str) -> str:
    """
    Extracts the core type name, ignoring wrappers.
    "Optional[Asset]" -> "Asset"
    """
    s = str(type_str)
    # Clean wrappers
    s = s.replace("typing.", "").replace("Optional", "").replace("Union", "").replace("List", "")
    s = s.replace("<class", "").replace(">", "") 
    # Clean punctuation
    s = s.replace("[", " ").replace("]", " ").replace(",", " ").replace("|", " ")
    
    words = s.split()
    for word in words:
        word = word.strip().strip("'").strip('"')
        if "." in word: word = word.split(".")[-1]
        
        # Skip generic markers
        if word in ["None", "NoneType", "Any"]:
            continue
            
        return word
        
    return "str"

def is_model(type_name: str) -> bool:
    """
    INVERTED LOGIC: If it's not a primitive, it's a model.
    This guarantees Asset, Device, EntityGroupId are treated as models.
    """
    if type_name in PRIMITIVES:
        return False
    # If it looks like a Dict or List, treat as primitive JSON handling
    if "dict" in type_name.lower() or "list" in type_name.lower():
        return False
    return True

def get_controller_docstring(rest_method, api_module):
    if rest_method.__doc__: return inspect.cleandoc(rest_method.__doc__)
    try: source = inspect.getsource(rest_method)
    except: return "No description available."
    
    match = re.search(r'self\.(\w+)_controller\.(\w+)\(', source)
    if match:
        controller_name = match.group(1) + "_controller_api"
        method_name = match.group(2)
        for name, obj in inspect.getmembers(api_module, inspect.isclass):
            if name.lower().replace("_", "") == controller_name.replace("_", ""):
                if hasattr(obj, method_name):
                    target_method = getattr(obj, method_name)
                    if target_method.__doc__:
                        doc = inspect.cleandoc(target_method.__doc__)
                        return doc.split("This method makes a synchronous")[0].strip()
    return "No description available."

# --- 3. GENERATOR ---

def generate_tool_code(method_name: str, func: callable, api_module) -> str:
    docstring = get_controller_docstring(func, api_module)
    docstring = docstring.replace('"""', "'''").replace("\\", "\\\\")

    sig = inspect.signature(func)
    args_def = []
    args_call = []
    
    for name, param in sig.parameters.items():
        if name == 'self': continue
        
        # 1. Analyze Type
        annotation_str = str(param.annotation)
        type_name = extract_type_name_from_string(annotation_str)
        
        # 2. Path A: MODEL (Asset, Device, etc.)
        if is_model(type_name):
            args_def.append(f"{name}_json: str")
            args_call.append(f"{name}=deserialize_param({name}_json, '{type_name}')")
            
        # 3. Path B: LIST/DICT (JSON load)
        elif "list" in annotation_str.lower() or "dict" in annotation_str.lower():
             default_str = " = None" if param.default is None else ""
             args_def.append(f"{name}_json: str{default_str}")
             args_call.append(f"{name}=json.loads({name}_json) if {name}_json else None")
             
        # 4. Path C: PRIMITIVE (str, int, bool)
        else:
            py_type = "str"
            if type_name == "int": py_type = "int"
            elif type_name == "bool": py_type = "bool"
            elif type_name == "float": py_type = "float"
            
            default_str = ""
            if param.default != inspect.Parameter.empty:
                val = f'"{param.default}"' if isinstance(param.default, str) else param.default
                default_str = " = None" if val is None else f" = {val}"
                if val is None: py_type = f"Optional[{py_type}]"
            
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
            return "PERMISSION DENIED: You do not have permission to perform '{method_name}'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {{e.status}}: {{e.reason}}\\n{{e.body}}"
    except Exception as e:
        return f"Error: {{str(e)}}"
"""

# --- 4. PROCESSING ---

def process_edition(edition_name, client_class, api_module):
    print(f"--- Generating {edition_name} Tools ---")
    base_path = f"{OUTPUT_DIR}/tools/{edition_name.lower()}"
    os.makedirs(base_path, exist_ok=True)

    mock_client = client_class("http://localhost")
    grouped = {cat: [] for cat in CATEGORIES.values()}
    grouped[DEFAULT_CATEGORY] = []
    
    count = 0
    for name, func in inspect.getmembers(mock_client, predicate=inspect.ismethod):
        if name in IGNORED_METHODS or name.startswith("_"): continue
        cat = DEFAULT_CATEGORY
        for kw, c in CATEGORIES.items():
            if kw in name: cat = c; break
        
        code = generate_tool_code(name, func, api_module)
        grouped[cat].append((name, code))
        count += 1

    for cat, items in grouped.items():
        if not items: continue
        with open(f"{base_path}/{cat}.py", "w") as f:
            f.write(f"import json\n")
            f.write(f"import tb_rest_client.models.models_{edition_name.lower()} as models\n")
            f.write(f"from ...shared import get_client, deserialize_param, format_response, ApiException\n\n")
            for _, code in items: f.write(code)
            f.write("\ndef register(mcp):\n")
            for name, _ in items: f.write(f"    mcp.tool()( {name} )\n")
    
    with open(f"{base_path}/__init__.py", "w") as f: f.write("")
    print(f" > Generated {count} tools in {base_path}/")

# --- 5. STATIC FILES ---

FILE_SHARED = f"""
import os, json, time
from typing import Any

TB_URL = os.getenv("TB_URL", "http://localhost:8080")
TB_USERNAME = os.getenv("TB_USERNAME", "tenant@thingsboard.org")
TB_PASSWORD = os.getenv("TB_PASSWORD", "tenant")
EDITION = os.getenv("TB_EDITION", "PE")

try:
    if EDITION == "PE":
        from tb_rest_client.rest_client_pe import RestClientPE as RestClient
        import tb_rest_client.models.models_pe as models
    else:
        from tb_rest_client.rest_client_ce import RestClientCE as RestClient
        import tb_rest_client.models.models_ce as models
    from tb_rest_client.rest import ApiException
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
            # Some models expect kwargs, some might be enums
            # We assume it's a Pydantic-like or Dictionary model
            return clazz(**data)
        return data
    except: return value

def format_response(resp: Any) -> str:
    if hasattr(resp, 'to_dict'): return json.dumps(resp.to_dict(), indent=2, default=str)
    if isinstance(resp, list): return json.dumps([x.to_dict() if hasattr(x, 'to_dict') else x for x in resp], indent=2, default=str)
    return str(resp)
"""

FILE_MAIN = """
import os
import sys
from mcp.server.fastmcp import FastMCP
from tools.shared import get_client

EDITION = os.getenv("TB_EDITION", "PE")
print(f"Starting ThingsBoard MCP ({EDITION})")
mcp = FastMCP(f"ThingsBoard MCP ({EDITION})")

if EDITION == "PE":
    try:
        from tools.pe import device, asset, alarm, customer, user, dashboard, telemetry, tenant, relation, entity_group
        device.register(mcp); asset.register(mcp); alarm.register(mcp); customer.register(mcp);
        user.register(mcp); dashboard.register(mcp); telemetry.register(mcp); tenant.register(mcp);
        relation.register(mcp); entity_group.register(mcp)
    except ImportError as e: print(f"Error loading PE tools: {e}")
else:
    try:
        from tools.ce import device, asset, alarm, customer, user, dashboard, telemetry, tenant, relation
        device.register(mcp); asset.register(mcp); alarm.register(mcp); customer.register(mcp);
        user.register(mcp); dashboard.register(mcp); telemetry.register(mcp); tenant.register(mcp);
        relation.register(mcp)
    except ImportError as e: print(f"Error loading CE tools: {e}")

if __name__ == '__main__':
    mcp.run()
"""

def main():
    if os.path.exists(OUTPUT_DIR): shutil.rmtree(OUTPUT_DIR)
    os.makedirs(f"{OUTPUT_DIR}/tools")

    with open(f"{OUTPUT_DIR}/tools/shared.py", "w") as f: f.write(FILE_SHARED)
    with open(f"{OUTPUT_DIR}/tools/__init__.py", "w") as f: f.write("")
    with open(f"{OUTPUT_DIR}/main.py", "w") as f: f.write(FILE_MAIN)

    process_edition("CE", RestClientCE, api_ce)
    if HAS_PE: process_edition("PE", RestClientPE, api_pe)

    print("\nGeneration Complete.")
    print("Run PE:  export TB_EDITION=PE && python thingsboard_mcp/main.py")

if __name__ == "__main__":
    main()