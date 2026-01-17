import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def assign_entity_view_to_customer(customer_id_json: str, entity_view_id_json: str) -> str:
    """
    Assign Entity View to customer (assignEntityViewToCustomer)  # noqa: E501

Creates assignment of the Entity View to customer. Customer will be able to query Entity View afterwards.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_entity_view_to_customer(customer_id=deserialize_param(customer_id_json, 'CustomerId'), entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_entity_view_to_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def assign_entity_view_to_edge(edge_id_json: str, entity_view_id_json: str) -> str:
    """
    Assign entity view to edge (assignEntityViewToEdge)  # noqa: E501

Creates assignment of an existing entity view to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment entity view (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once entity view will be delivered to edge service, it's going to be available for usage on remote edge instance.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_entity_view_to_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_entity_view_to_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def assign_entity_view_to_public_customer(entity_view_id_json: str) -> str:
    """
    Make entity view publicly available (assignEntityViewToPublicCustomer)  # noqa: E501

Entity View will be available for non-authorized (not logged-in) users. This is useful to create dashboards that you plan to share/embed on a publicly available website. However, users that are logged-in and belong to different tenant will not be able to access the entity view.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_entity_view_to_public_customer(entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_entity_view_to_public_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_entity_view(entity_view_id_json: str) -> str:
    """
    Delete entity view (deleteEntityView)  # noqa: E501

Delete the EntityView object based on the provided entity view id.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_entity_view(entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_entity_view'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def find_by_query_v4(body_json: str) -> str:
    """
    Find related entity views (findByQuery)  # noqa: E501

Returns all entity views that are related to the specific entity. The entity id, relation type, entity view types, depth of the search, and other query parameters defined using complex 'EntityViewSearchQuery' object. See 'Model' tab of the Parameters for more info.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_by_query_v4(body=deserialize_param(body_json, 'EntityViewSearchQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_query_v4'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_customer_entity_view_infos(customer_id_json: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Customer Entity View info (getCustomerEntityViewInfos)  # noqa: E501

Returns a page of Entity View info objects assigned to customer. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_customer_entity_view_infos(customer_id=deserialize_param(customer_id_json, 'CustomerId'), page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_customer_entity_view_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_customer_entity_views(customer_id_json: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Customer Entity Views (getCustomerEntityViews)  # noqa: E501

Returns a page of Entity View objects assigned to customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_customer_entity_views(customer_id=deserialize_param(customer_id_json, 'CustomerId'), page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_customer_entity_views'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_edge_entity_views(edge_id_json: str, page: int, page_size: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    getEdgeEntityViews  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_entity_views(edge_id=deserialize_param(edge_id_json, 'EdgeId'), page=page, page_size=page_size, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_entity_views'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_entity_view_by_id(entity_view_id_json: str) -> str:
    """
    Get entity view (getEntityViewById)  # noqa: E501

Fetch the EntityView object based on the provided entity view id. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. See the 'Model' tab for more details.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_entity_view_by_id(entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_entity_view_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_entity_view_info_by_id(entity_view_id_json: str) -> str:
    """
    Get Entity View info (getEntityViewInfoById)  # noqa: E501

Fetch the Entity View info object based on the provided Entity View Id. Entity Views Info extends the Entity View with customer title and 'is public' flag. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. See the 'Model' tab for more details.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_entity_view_info_by_id(entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_entity_view_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_entity_view_types() -> str:
    """
    Get Entity View Types (getEntityViewTypes)  # noqa: E501

Returns a set of unique entity view types based on entity views that are either owned by the tenant or assigned to the customer which user is performing the request.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_entity_view_types()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_entity_view_types'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_entity_view(entity_view_name: str) -> str:
    """
    Get Entity View by name (getTenantEntityView)  # noqa: E501

Fetch the Entity View object based on the tenant id and entity view name.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_entity_view(entity_view_name=entity_view_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_entity_view'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_entity_view_infos(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Entity Views (getTenantEntityViews)  # noqa: E501

Returns a page of entity views info owned by tenant. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_entity_view_infos(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_entity_view_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_entity_views(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Entity Views (getTenantEntityViews)  # noqa: E501

Returns a page of entity views owned by tenant. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_entity_views(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_entity_views'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_entity_view(body_json: str = None) -> str:
    """
    Save or update entity view (saveEntityView)  # noqa: E501

Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. See the 'Model' tab for more details.Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Entity View entity.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_entity_view(body=deserialize_param(body_json, 'EntityView'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_entity_view'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def unassign_entity_view_from_customer(entity_view_id_json: str) -> str:
    """
    Unassign Entity View from customer (unassignEntityViewFromCustomer)  # noqa: E501

Clears assignment of the Entity View to customer. Customer will not be able to query Entity View afterwards.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.unassign_entity_view_from_customer(entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unassign_entity_view_from_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def unassign_entity_view_from_edge(edge_id_json: str, entity_view_id_json: str) -> str:
    """
    Unassign entity view from edge (unassignEntityViewFromEdge)  # noqa: E501

Clears assignment of the entity view to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove entity view (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove entity view locally.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.unassign_entity_view_from_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unassign_entity_view_from_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( assign_entity_view_to_customer )
    mcp.tool()( assign_entity_view_to_edge )
    mcp.tool()( assign_entity_view_to_public_customer )
    mcp.tool()( delete_entity_view )
    mcp.tool()( find_by_query_v4 )
    mcp.tool()( get_customer_entity_view_infos )
    mcp.tool()( get_customer_entity_views )
    mcp.tool()( get_edge_entity_views )
    mcp.tool()( get_entity_view_by_id )
    mcp.tool()( get_entity_view_info_by_id )
    mcp.tool()( get_entity_view_types )
    mcp.tool()( get_tenant_entity_view )
    mcp.tool()( get_tenant_entity_view_infos )
    mcp.tool()( get_tenant_entity_views )
    mcp.tool()( save_entity_view )
    mcp.tool()( unassign_entity_view_from_customer )
    mcp.tool()( unassign_entity_view_from_edge )
