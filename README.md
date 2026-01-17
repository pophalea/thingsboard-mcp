# ThingsBoard MCP Server

A **Model Context Protocol (MCP)** server for [ThingsBoard](https://thingsboard.io/). This project allows AI assistants (like Claude Desktop) to interact directly with your ThingsBoard instance to manage assets, devices, telemetry, alarms, and more.

The tools are **auto-generated** from the official Python SDK (`tb-rest-client`), ensuring 100% API coverage, strict type checking, and rich documentation derived directly from the source code.

## 🚀 Features

* **Auto-Discovery:** Automatically detects installed ThingsBoard SDK editions (`CE` or `PE`) and adapts accordingly.
* **Smart Tracing:** Maps high-level Client methods (`rest_client_ce.py`) to their underlying API Controllers to extract accurate docstrings and signatures.
* **Strict Verification:** Includes a test suite (`verify_tools.py`) that mocks the SDK to ensure every generated tool has valid inputs, docstrings, and execution logic.
* **Comprehensive Reporting:** Generates detailed Markdown documentation (`TOOLS_CE.md`) and verification audits (`VERIFICATION_REPORT_CE.md`).

---

## 📋 Prerequisites

* **Python 3.10+**
* **ThingsBoard Python REST Client**

```bash
pip install tb-rest-client
```

## 🛠️ Setup & Generation
1. Generate the Tools
Run the generator script. This will scan your installed `tb-rest-client` library, trace the method calls, and generate the MCP tool code.

```bash
python3 generate_thingsboard_mcp.py
```
__What happens?__
* Creates thingsboard_mcp/tools/ce/ (and pe/ if installed).
* Generates a TOOLS_CE.md file listing all available tools, their descriptions, and parameters.
* Filters out internal utility methods and lambdas automatically.

2. Verify the Tools
Run the verification suite to ensure the generated code is valid and adheres to strict quality standards.
```bash
python3 verify_final.py
```

__What happens?__
* Mocks the ThingsBoard SDK (no real connection required).
* Tests every tool with dummy data to ensure it calls the client correctly.
* Generates `VERIFICATION_REPORT_CE.md` with a pass/fail status for every tool.

## ⚙️ Configuration
The server requires the following environment variables to connect to your ThingsBoard instance.
| Variable    | Description                   | Default               |
| --------    | ----------------------------  | --------------------- |
| TB_URL      | Your ThingsBoard URL          | http://localhost:8080 |
| TB_USERNAME | Tenant Administrator Username | tenant@thingsboard.org|
| TB_PASSWORD | Tenant Administrator Password | tenant                |
| TB_EDITION  | Edition to load (CE or PE)    | PE                    |

## 🏃‍♂️ Usage
### Option A: Use with Claude Desktop
Add the following configuration to your Claude Desktop config file:
MacOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```JSON
{
  "mcpServers": {
    "thingsboard": {
      "command": "python3",
      "args": ["/absolute/path/to/thingsboard-mcp/thingsboard_mcp/main.py"],
      "env": {
        "TB_URL": "http://YOUR_TB_IP:8080",
        "TB_USERNAME": "tenant@thingsboard.org",
        "TB_PASSWORD": "your_password",
        "TB_EDITION": "CE"
      }
    }
  }
}
```

### Option B: Run Manually (Testing)
You can run the server directly in your terminal to test connections or debug.
```bash
export TB_URL="http://localhost:8080"
export TB_USERNAME="tenant@thingsboard.org"
export TB_PASSWORD="tenant"
export TB_EDITION="CE"

python3 thingsboard_mcp/main.py
```


## 📂 Project Structure.
```text
├── generate_thingsboard_mcp.py # Scans SDK and generates tool code
├── verify_tools.py             # Mocks SDK and verifies generated tools
├── TOOLS_CE.md                 # Documentation of all generated tools
├── VERIFICATION_REPORT_CE.md   # Audit log of tool health
├── README.md                   # This file
└── thingsboard_mcp/            # The generated package
    ├── main.py                 # Entry point for MCP Server
    └── tools/
        ├── shared.py           # Shared utilities (Auth, JSON parsing)
        ├── ce/                 # Community Edition tools (Asset, Device, etc.)
        └── pe/                 # Professional Edition tools (if applicable)
```

## 🛡️ Troubleshooting
**Missing Tools?** Check `TOOLS_CE.md` or the console output of `generate_thingsboard_mcp.py`. Tools are skipped if: 
1. They correspond to internal internal threading methods (join, start).
2. The source SDK is missing a docstring for that method.
3. The method is a lambda or partial function.
**Connection Errors?** The server attempts to log in immediately upon the first tool call. Ensure your `TB_URL` is reachable from the machine running the MCP server and that credentials are correct.