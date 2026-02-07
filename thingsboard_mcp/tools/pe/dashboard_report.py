import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def download_dashboard_report(dashboard_id_json: str, body_json: str = None) -> str:
    """
    Download dashboard report (downloadDashboardReport)  # noqa: E501

Generate and download a report from the specified dashboard. The request payload is a JSON object with params of report. For example:  ```json {     "type": "pdf",     "timezone": "Europe/Kiev",     "timewindow": {         "displayValue": "",         "hideInterval": false,         "hideLastInterval": false,         "hideQuickInterval": false,         "hideAggregation": false,         "hideAggInterval": false,         "hideTimezone": false,         "selectedTab": 0,         "realtime": {             "realtimeType": 0,             "interval": 1000,             "timewindowMs": 60000,             "quickInterval": "CURRENT_DAY"         },         "history": {             "historyType": 0,             "interval": 1000,             "timewindowMs": 60000,             "fixedTimewindow": {                 "startTimeMs": 1703687976592,                 "endTimeMs": 1703774376592             },             "quickInterval": "CURRENT_DAY"         },         "aggregation": {             "type": "AVG",             "limit": 25000         }     },     "state": null } ```   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (DashboardId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.download_dashboard_report(dashboard_id=deserialize_param(dashboard_id_json, 'DashboardId'), body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_dashboard_report'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def download_test_report(body_json: str, reports_server_endpoint_url: Optional[str] = None) -> str:
    """
    Download test report (downloadTestReport)  # noqa: E501

Generate and download test report.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (ReportConfig):
    - `base_url` (str)
    - `dashboard_id` (str)
    - `state` (str)
    - `timezone` (str)
    - `use_dashboard_timewindow` (bool)
    - `timewindow` (JsonNode)
    - `name_pattern` (str)
    - `type` (str)
    - `use_current_user_credentials` (bool)
    - `user_id` (str)
    """
    try:
        client = get_client()
        result = client.download_test_report(body=deserialize_param(body_json, 'ReportConfig'), reports_server_endpoint_url=reports_server_endpoint_url)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_test_report'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( download_dashboard_report )
    mcp.tool()( download_test_report )
