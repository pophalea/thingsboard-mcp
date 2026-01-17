import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def add_dashboard_customers(dashboard_id_json: str, body_json: str = None) -> str:
    """
    Adds the Dashboard Customers (addDashboardCustomers)  # noqa: E501

Adds the list of Customers to the existing list of assignments for the Dashboard. Keeps previous assignments to customers that are not in the provided list. Returns the Dashboard object.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.add_dashboard_customers(dashboard_id=deserialize_param(dashboard_id_json, 'DashboardId'), body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'add_dashboard_customers'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def assign_dashboard_to_customer(customer_id_json: str, dashboard_id_json: str) -> str:
    """
    Assign the Dashboard (assignDashboardToCustomer)  # noqa: E501

Assign the Dashboard to specified Customer or do nothing if the Dashboard is already assigned to that Customer. Returns the Dashboard object.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_dashboard_to_customer(customer_id=deserialize_param(customer_id_json, 'CustomerId'), dashboard_id=deserialize_param(dashboard_id_json, 'DashboardId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_dashboard_to_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def assign_dashboard_to_edge(edge_id_json: str, dashboard_id_json: str) -> str:
    """
    Assign dashboard to edge (assignDashboardToEdge)  # noqa: E501

Creates assignment of an existing dashboard to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment dashboard (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once dashboard will be delivered to edge service, it's going to be available for usage on remote edge instance.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_dashboard_to_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), dashboard_id=deserialize_param(dashboard_id_json, 'DashboardId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_dashboard_to_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def assign_dashboard_to_public_customer(dashboard_id_json: str) -> str:
    """
    Assign the Dashboard to Public Customer (assignDashboardToPublicCustomer)  # noqa: E501

Assigns the dashboard to a special, auto-generated 'Public' Customer. Once assigned, unauthenticated users may browse the dashboard. This method is useful if you like to embed the dashboard on public web pages to be available for users that are not logged in. Be aware that making the dashboard public does not mean that it automatically makes all devices and assets you use in the dashboard to be public.Use [assign Asset to Public Customer](#!/asset-controller/assignAssetToPublicCustomerUsingPOST) and [assign Device to Public Customer](#!/device-controller/assignDeviceToPublicCustomerUsingPOST) for this purpose. Returns the Dashboard object.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_dashboard_to_public_customer(dashboard_id=deserialize_param(dashboard_id_json, 'DashboardId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_dashboard_to_public_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_dashboard(dashboard_id_json: str) -> str:
    """
    Delete the Dashboard (deleteDashboard)  # noqa: E501

Delete the Dashboard.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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


def get_customer_dashboards(customer_id_json: str, page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Customer Dashboards (getCustomerDashboards)  # noqa: E501

Returns a page of dashboard info objects owned by the specified customer. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_customer_dashboards(customer_id=deserialize_param(customer_id_json, 'CustomerId'), page_size=page_size, page=page, mobile=mobile, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_customer_dashboards'."
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


def get_edge_dashboards(edge_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Edge Dashboards (getEdgeDashboards)  # noqa: E501

Returns a page of dashboard info objects assigned to the specified edge. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_dashboards(edge_id=deserialize_param(edge_id_json, 'EdgeId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_dashboards'."
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


def get_max_datapoints_limit() -> str:
    """
    Get max data points limit (getMaxDatapointsLimit)  # noqa: E501

Get the maximum number of data points that dashboard may request from the server per in a single subscription command. This value impacts the time window behavior. It impacts 'Max values' parameter in case user selects 'None' as 'Data aggregation function'. It also impacts the 'Grouping interval' in case of any other 'Data aggregation function' is selected. The actual value of the limit is configurable in the system configuration file.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_max_datapoints_limit()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_max_datapoints_limit'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_server_time() -> str:
    """
    Get server time (getServerTime)  # noqa: E501

Get the server time (milliseconds since January 1, 1970 UTC). Used to adjust view of the dashboards according to the difference between browser and server time.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_server_time()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_server_time'."
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

Returns the home dashboard info object that is configured as 'homeDashboardId' parameter in the 'additionalInfo' of the corresponding tenant.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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


def remove_dashboard_customers(dashboard_id_json: str, body_json: str = None) -> str:
    """
    Remove the Dashboard Customers (removeDashboardCustomers)  # noqa: E501

Removes the list of Customers from the existing list of assignments for the Dashboard. Keeps other assignments to customers that are not in the provided list. Returns the Dashboard object.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.remove_dashboard_customers(dashboard_id=deserialize_param(dashboard_id_json, 'DashboardId'), body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'remove_dashboard_customers'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_dashboard(body_json: str = None) -> str:
    """
    Create Or Update Dashboard (saveDashboard)  # noqa: E501

Create or update the Dashboard. When creating dashboard, platform generates Dashboard Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Dashboard id will be present in the response. Specify existing Dashboard id to update the dashboard. Referencing non-existing dashboard Id will cause 'Not Found' error. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Dashboard entity.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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


def set_tenant_home_dashboard_info(body_json: str = None) -> str:
    """
    Update Tenant Home Dashboard Info (getTenantHomeDashboardInfo)  # noqa: E501

Update the home dashboard assignment for the current tenant.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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


def unassign_dashboard_from_customer(customer_id_json: str, dashboard_id_json: str) -> str:
    """
    Unassign the Dashboard (unassignDashboardFromCustomer)  # noqa: E501

Unassign the Dashboard from specified Customer or do nothing if the Dashboard is already assigned to that Customer. Returns the Dashboard object.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.unassign_dashboard_from_customer(customer_id=deserialize_param(customer_id_json, 'CustomerId'), dashboard_id=deserialize_param(dashboard_id_json, 'DashboardId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unassign_dashboard_from_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def unassign_dashboard_from_edge(edge_id_json: str, dashboard_id_json: str) -> str:
    """
    Unassign dashboard from edge (unassignDashboardFromEdge)  # noqa: E501

Clears assignment of the dashboard to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove dashboard (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove dashboard locally.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.unassign_dashboard_from_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), dashboard_id=deserialize_param(dashboard_id_json, 'DashboardId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unassign_dashboard_from_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def unassign_dashboard_from_public_customer(dashboard_id_json: str) -> str:
    """
    Unassign the Dashboard from Public Customer (unassignDashboardFromPublicCustomer)  # noqa: E501

Unassigns the dashboard from a special, auto-generated 'Public' Customer. Once unassigned, unauthenticated users may no longer browse the dashboard. Returns the Dashboard object.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.unassign_dashboard_from_public_customer(dashboard_id=deserialize_param(dashboard_id_json, 'DashboardId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unassign_dashboard_from_public_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def update_dashboard_customers(dashboard_id_json: str, body_json: str = None) -> str:
    """
    Update the Dashboard Customers (updateDashboardCustomers)  # noqa: E501

Updates the list of Customers that this Dashboard is assigned to. Removes previous assignments to customers that are not in the provided list. Returns the Dashboard object.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_dashboard_customers(dashboard_id=deserialize_param(dashboard_id_json, 'DashboardId'), body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_dashboard_customers'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( add_dashboard_customers )
    mcp.tool()( assign_dashboard_to_customer )
    mcp.tool()( assign_dashboard_to_edge )
    mcp.tool()( assign_dashboard_to_public_customer )
    mcp.tool()( delete_dashboard )
    mcp.tool()( get_customer_dashboards )
    mcp.tool()( get_dashboard_by_id )
    mcp.tool()( get_dashboard_info_by_id )
    mcp.tool()( get_edge_dashboards )
    mcp.tool()( get_home_dashboard )
    mcp.tool()( get_home_dashboard_info )
    mcp.tool()( get_max_datapoints_limit )
    mcp.tool()( get_server_time )
    mcp.tool()( get_tenant_dashboards )
    mcp.tool()( get_tenant_dashboards_v1 )
    mcp.tool()( get_tenant_home_dashboard_info )
    mcp.tool()( remove_dashboard_customers )
    mcp.tool()( save_dashboard )
    mcp.tool()( set_tenant_home_dashboard_info )
    mcp.tool()( unassign_dashboard_from_customer )
    mcp.tool()( unassign_dashboard_from_edge )
    mcp.tool()( unassign_dashboard_from_public_customer )
    mcp.tool()( update_dashboard_customers )
