import os
import sys
import json
import inspect
import importlib
import pkgutil
import logging
from unittest.mock import MagicMock, patch

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("ToolVerifier")
sys.path.append(os.getcwd())

class MockSDKObject:
    def __init__(self, n, d): self.d = d
    def to_dict(self): return self.d

def mock_deserialize(j, m):
    try: return MockSDKObject(m, json.loads(j))
    except: return MockSDKObject(m, {})

mock_client = MagicMock()

def generate_dummy(param):
    if "json" in param.name: return json.dumps({"test":1})
    if "int" in str(param.annotation): return 1
    if "bool" in str(param.annotation): return True
    if "float" in str(param.annotation): return 1.0
    return "dummy"

def verify_edition_folder(edition_name):
    base_pkg = f"thingsboard_mcp.tools.{edition_name}"
    base_path = os.path.join("thingsboard_mcp", "tools", edition_name)
    
    os.environ["TB_EDITION"] = edition_name.upper()
    
    report_lines = []
    report_lines.append(f"# Verification Report: {edition_name.upper()}\n")
    report_lines.append("| Tool Name | Status | Message |")
    report_lines.append("| :--- | :--- | :--- |")
    
    pass_count = 0
    fail_count = 0

    with patch('thingsboard_mcp.tools.shared.get_client', return_value=mock_client), \
         patch('thingsboard_mcp.tools.shared.deserialize_param', side_effect=mock_deserialize), \
         patch('thingsboard_mcp.tools.shared.format_response', lambda x: str(x)):

        for _, name, _ in pkgutil.iter_modules([base_path]):
            if name == "__init__": continue
            module_name = f"{base_pkg}.{name}"
            
            try:
                mod = importlib.import_module(module_name)
                # STRICT LAMBDA FILTER IN VERIFIER
                funcs = [
                    f for n, f in inspect.getmembers(mod, inspect.isfunction) 
                    if not n.startswith("_") and n != "register" and n != "<lambda>"
                ]
                
                for func in funcs:
                    func_name = func.__name__
                    if func_name == "<lambda>": continue # Double check

                    try:
                        doc = inspect.getdoc(func)
                        if not doc or not doc.strip():
                            report_lines.append(f"| `{func_name}` | 🔴 FAIL | Missing Docstring |")
                            fail_count += 1
                            continue

                        args = {p: generate_dummy(v) for p, v in inspect.signature(func).parameters.items()}
                        mock_client.reset_mock()
                        func(**args)
                        
                        if mock_client.method_calls:
                            report_lines.append(f"| `{func_name}` | 🟢 PASS | Verified |")
                            pass_count += 1
                        else:
                            report_lines.append(f"| `{func_name}` | 🔴 FAIL | Client not called |")
                            fail_count += 1

                    except Exception as e:
                        report_lines.append(f"| `{func_name}` | 💥 CRASH | {str(e)} |")
                        fail_count += 1

            except Exception as e:
                report_lines.append(f"| `{name}` | 💥 IMPORT ERROR | {str(e)} |")
    
    report_file = f"VERIFICATION_REPORT_{edition_name.upper()}.md"
    with open(report_file, "w") as f:
        f.write("\n".join(report_lines))
    
    logger.info(f"Verification {edition_name.upper()}: Pass={pass_count}, Fail={fail_count}. Report: {report_file}")

def main():
    tools_dir = "thingsboard_mcp/tools"
    if not os.path.exists(tools_dir): return
    
    for item in os.listdir(tools_dir):
        if os.path.isdir(os.path.join(tools_dir, item)) and not item.startswith("__") and item != "shared":
            verify_edition_folder(item)

if __name__ == "__main__":
    main()