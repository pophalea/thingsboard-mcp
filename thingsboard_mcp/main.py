from mcp.server.fastmcp import FastMCP
from tools import device, asset, alarm, customer, user, dashboard, entity_group, relation, telemetry, tenant, widget, rule_chain, ota, audit, edge, resource, queue, report, admin, integration, scheduler, rbac, security, common

mcp = FastMCP('ThingsBoard MCP PE')

# Register all modules
device.register(mcp)
asset.register(mcp)
alarm.register(mcp)
customer.register(mcp)
user.register(mcp)
dashboard.register(mcp)
entity_group.register(mcp)
relation.register(mcp)
telemetry.register(mcp)
tenant.register(mcp)
widget.register(mcp)
rule_chain.register(mcp)
ota.register(mcp)
audit.register(mcp)
edge.register(mcp)
resource.register(mcp)
queue.register(mcp)
report.register(mcp)
admin.register(mcp)
integration.register(mcp)
scheduler.register(mcp)
rbac.register(mcp)
security.register(mcp)
common.register(mcp)

if __name__ == '__main__':
    mcp.run()
