
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
