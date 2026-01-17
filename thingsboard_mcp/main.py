
import os, sys
from mcp.server.fastmcp import FastMCP
sys.path.append(os.path.dirname(__file__))

EDITION = os.getenv("TB_EDITION", "PE")
print(f"Starting ThingsBoard MCP ({EDITION})")
mcp = FastMCP(f"ThingsBoard MCP ({EDITION})")

try:
    tool_pkg_name = f"tools.{EDITION.lower()}"
    tool_pkg = __import__(tool_pkg_name, fromlist=["__path__"])
    import pkgutil
    if hasattr(tool_pkg, "__path__"):
        for _, name, _ in pkgutil.iter_modules(tool_pkg.__path__):
            try:
                mod = __import__(f"{tool_pkg_name}.{name}", fromlist=["register"])
                if hasattr(mod, "register"):
                    mod.register(mcp)
            except Exception as e:
                print(f"Failed module {name}: {e}")
except ImportError as e:
    print(f"Error: {e}")

if __name__ == '__main__':
    mcp.run()
