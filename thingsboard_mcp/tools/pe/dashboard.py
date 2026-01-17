import json
import tb_rest_client.models.models_pe as models
from ...shared import get_client, deserialize_param, format_response, ApiException


def delete_dashboard(dashboard_id_json: str) -> str:
    """
    Delete the Dashboard (deleteDashboard)  # noqa: E501

Delete the Dashboard. Only users with 'TENANT_ADMIN') authority may delete the dashboards.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_dashboard(dashboard_id=deserialize_param(dashboard_id_json, 'DashboardId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_dashboard'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_dashboard_report(dashboard_id_json: str, body_json: str = None) -> str:
    """
    Download dashboard report (downloadDashboardReport)  # noqa: E501

Generate and download a report from the specified dashboard. The request payload is a JSON object with params of report. For example:  ```json {     "type": "pdf",     "timezone": "Europe/Kiev",     "timewindow": {         "displayValue": "",         "hideInterval": false,         "hideLastInterval": false,         "hideQuickInterval": false,         "hideAggregation": false,         "hideAggInterval": false,         "hideTimezone": false,         "selectedTab": 0,         "realtime": {             "realtimeType": 0,             "interval": 1000,             "timewindowMs": 60000,             "quickInterval": "CURRENT_DAY"         },         "history": {             "historyType": 0,             "interval": 1000,             "timewindowMs": 60000,             "fixedTimewindow": {                 "startTimeMs": 1703687976592,                 "endTimeMs": 1703774376592             },             "quickInterval": "CURRENT_DAY"         },         "aggregation": {             "type": "AVG",             "limit": 25000         }     },     "state": null } ```   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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

def export_group_dashboards(entity_group_id_json: str, limit: int) -> str:
    """
    Export Dashboards (exportGroupDashboards)  # noqa: E501

Export the dashboards that belong to specified group id.The Dashboard object is a heavyweight object that contains information about the dashboard (e.g. title, image, assigned customers) and also configuration JSON (e.g. layouts, widgets, entity aliases).  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.export_group_dashboards(entity_group_id=deserialize_param(entity_group_id_json, 'EntityGroupId'), limit=limit)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'export_group_dashboards'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_all_dashboards(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, include_customers: Optional[bool] = None) -> str:
    """
    Get All Dashboards for current user (getAllDashboards)  # noqa: E501

Returns a page of dashboard info objects owned by the tenant or the customer of a current user. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_all_dashboards(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, include_customers=include_customers)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_all_dashboards'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_dashboard_by_id(dashboard_id_json: str, inline_images: Optional[bool] = None) -> str:
    """
    Get Dashboard (getDashboardById)  # noqa: E501

Get the dashboard based on 'dashboardId' parameter. The Dashboard object is a heavyweight object that contains information about the dashboard (e.g. title, image, assigned customers) and also configuration JSON (e.g. layouts, widgets, entity aliases).  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_dashboard_by_id(dashboard_id=deserialize_param(dashboard_id_json, 'DashboardId'), inline_images=inline_images)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_dashboard_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_dashboard_info_by_id(dashboard_id_json: str) -> str:
    """
    Get Dashboard Info (getDashboardInfoById)  # noqa: E501

Get the information about the dashboard based on 'dashboardId' parameter. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_dashboard_info_by_id(dashboard_id=deserialize_param(dashboard_id_json, 'DashboardId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_dashboard_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_dashboards_by_entity_group_id(entity_group_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get dashboards by Entity Group Id (getDashboardsByEntityGroupId)  # noqa: E501

Returns a page of Dashboard objects that belongs to specified Entity Group Id. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_dashboards_by_entity_group_id(entity_group_id=deserialize_param(entity_group_id_json, 'EntityGroupId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_dashboards_by_entity_group_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_dashboards_by_ids(dashboard_ids_json: str) -> str:
    """
    Get dashboards by Dashboard Ids (getDashboardsByIds)  # noqa: E501

Returns a list of DashboardInfo objects based on the provided ids. Filters the list based on the user permissions.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_dashboards_by_ids(dashboard_ids=json.loads(dashboard_ids_json) if dashboard_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_dashboards_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_home_dashboard() -> str:
    """
    Get Home Dashboard (getHomeDashboard)  # noqa: E501

Returns the home dashboard object that is configured as 'homeDashboardId' parameter in the 'additionalInfo' of the User. If 'homeDashboardId' parameter is not set on the User level and the User has authority 'CUSTOMER_USER', check the same parameter for the corresponding Customer. If 'homeDashboardId' parameter is not set on the User and Customer levels then checks the same parameter for the Tenant that owns the user. The Dashboard object is a heavyweight object that contains information about the dashboard (e.g. title, image, assigned customers) and also configuration JSON (e.g. layouts, widgets, entity aliases).  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_home_dashboard()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_home_dashboard'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_home_dashboard_info() -> str:
    """
    Get Home Dashboard Info (getHomeDashboardInfo)  # noqa: E501

Returns the home dashboard info object that is configured as 'homeDashboardId' parameter in the 'additionalInfo' of the User. If 'homeDashboardId' parameter is not set on the User level and the User has authority 'CUSTOMER_USER', check the same parameter for the corresponding Customer. If 'homeDashboardId' parameter is not set on the User and Customer levels then checks the same parameter for the Tenant that owns the user.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_home_dashboard_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_home_dashboard_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_dashboards(page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Dashboards (getTenantDashboards)  # noqa: E501

Returns a page of dashboard info objects owned by the tenant of a current user. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_dashboards(page_size=page_size, page=page, mobile=mobile, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_dashboards'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_dashboards_v1(tenant_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Dashboards by System Administrator (getTenantDashboards)  # noqa: E501

Returns a page of dashboard info objects owned by tenant. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_dashboards_v1(tenant_id=deserialize_param(tenant_id_json, 'TenantId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_dashboards_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_home_dashboard_info() -> str:
    """
    Get Tenant Home Dashboard Info (getTenantHomeDashboardInfo)  # noqa: E501

Returns the home dashboard info object that is configured as 'homeDashboardId' parameter in the 'additionalInfo' of the corresponding tenant.   Available for users with 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_home_dashboard_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_home_dashboard_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def import_group_dashboards(entity_group_id_json: str, body_json: str, overwrite: Optional[bool] = None) -> str:
    """
    Import Dashboards (importGroupDashboards)  # noqa: E501

Import the dashboards to specified group.The Dashboard object is a heavyweight object that contains information about the dashboard (e.g. title, image, assigned customers) and also configuration JSON (e.g. layouts, widgets, entity aliases).  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for specified group.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.import_group_dashboards(entity_group_id=deserialize_param(entity_group_id_json, 'EntityGroupId'), body=deserialize_param(body_json, 'Dashboard'), overwrite=overwrite)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'import_group_dashboards'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_dashboard(body_json: str) -> str:
    """
    Create Or Update Dashboard (saveDashboard)  # noqa: E501

Create or update the Dashboard. When creating dashboard, platform generates Dashboard Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Dashboard id will be present in the response. Specify existing Dashboard id to update the dashboard. Referencing non-existing dashboard Id will cause 'Not Found' error. Only users with 'TENANT_ADMIN') authority may create the dashboards.Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Dashboard entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_dashboard(body=deserialize_param(body_json, 'Dashboard'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_dashboard'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def set_tenant_home_dashboard_info(body_json: str) -> str:
    """
    Update Tenant Home Dashboard Info (getTenantHomeDashboardInfo)  # noqa: E501

Update the home dashboard assignment for the current tenant.   Available for users with 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.set_tenant_home_dashboard_info(body=deserialize_param(body_json, 'HomeDashboardInfo'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'set_tenant_home_dashboard_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def register(mcp):
    mcp.tool()( delete_dashboard )
    mcp.tool()( download_dashboard_report )
    mcp.tool()( export_group_dashboards )
    mcp.tool()( get_all_dashboards )
    mcp.tool()( get_dashboard_by_id )
    mcp.tool()( get_dashboard_info_by_id )
    mcp.tool()( get_dashboards_by_entity_group_id )
    mcp.tool()( get_dashboards_by_ids )
    mcp.tool()( get_home_dashboard )
    mcp.tool()( get_home_dashboard_info )
    mcp.tool()( get_tenant_dashboards )
    mcp.tool()( get_tenant_dashboards_v1 )
    mcp.tool()( get_tenant_home_dashboard_info )
    mcp.tool()( import_group_dashboards )
    mcp.tool()( save_dashboard )
    mcp.tool()( set_tenant_home_dashboard_info )
