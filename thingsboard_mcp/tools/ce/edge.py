import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def assign_edge_to_customer(customer_id_json: str, edge_id_json: str) -> str:
    """
    Assign edge to customer (assignEdgeToCustomer)  # noqa: E501

Creates assignment of the edge to customer. Customer will be able to query edge afterwards.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_edge_to_customer(customer_id=deserialize_param(customer_id_json, 'CustomerId'), edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_edge_to_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def assign_edge_to_public_customer(edge_id_json: str) -> str:
    """
    Make edge publicly available (assignEdgeToPublicCustomer)  # noqa: E501

Edge will be available for non-authorized (not logged-in) users. This is useful to create dashboards that you plan to share/embed on a publicly available website. However, users that are logged-in and belong to different tenant will not be able to access the edge.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_edge_to_public_customer(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_edge_to_public_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_edge(edge_id_json: str) -> str:
    """
    Delete edge (deleteEdge)  # noqa: E501

Deletes the edge. Referencing non-existing edge Id will cause an error.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def find_by_query_v2(body_json: str = None) -> str:
    """
    Find related edges (findByQuery)  # noqa: E501

Returns all edges that are related to the specific entity. The entity id, relation type, edge types, depth of the search, and other query parameters defined using complex 'EdgeSearchQuery' object. See 'Model' tab of the Parameters for more info.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_by_query_v2(body=deserialize_param(body_json, 'EdgeSearchQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_query_v2'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def find_missing_to_related_rule_chains(edge_id_json: str) -> str:
    """
    Find missing rule chains (findMissingToRelatedRuleChains)  # noqa: E501

Returns list of rule chains ids that are not assigned to particular edge, but these rule chains are present in the already assigned rule chains to edge.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_missing_to_related_rule_chains(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_missing_to_related_rule_chains'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_customer_edge_infos(customer_id_json: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Customer Edge Infos (getCustomerEdgeInfos)  # noqa: E501

Returns a page of edges info objects assigned to customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. Edge Info is an extension of the default Edge object that contains information about the assigned customer name.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_customer_edge_infos(customer_id=deserialize_param(customer_id_json, 'CustomerId'), page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_customer_edge_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_customer_edges(customer_id_json: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Customer Edges (getCustomerEdges)  # noqa: E501

Returns a page of edges objects assigned to customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_customer_edges(customer_id=deserialize_param(customer_id_json, 'CustomerId'), page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_customer_edges'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_edge_by_id(edge_id_json: str) -> str:
    """
    Get Edge (getEdgeById)  # noqa: E501

Get the Edge object based on the provided Edge Id. If the user has the authority of 'Tenant Administrator', the server checks that the edge is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the edge is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_by_id(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_edge_info_by_id(edge_id_json: str) -> str:
    """
    Get Edge Info (getEdgeInfoById)  # noqa: E501

Get the Edge Info object based on the provided Edge Id. If the user has the authority of 'Tenant Administrator', the server checks that the edge is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the edge is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_info_by_id(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_edge_install_instructions(edge_id_json: str, method: str) -> str:
    """
    Get Edge Install Instructions (getEdgeInstallInstructions)  # noqa: E501

Get an install instructions for provided edge id.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_install_instructions(edge_id=deserialize_param(edge_id_json, 'EdgeId'), method=method)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_install_instructions'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_edge_types() -> str:
    """
    Get Edge Types (getEdgeTypes)  # noqa: E501

Returns a set of unique edge types based on edges that are either owned by the tenant or assigned to the customer which user is performing the request.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_types()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_types'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_edge_upgrade_instructions(edge_version: str, method: str) -> str:
    """
    Get Edge Upgrade Instructions (getEdgeUpgradeInstructions)  # noqa: E501

Get an upgrade instructions for provided edge version.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_upgrade_instructions(edge_version=edge_version, method=method)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_upgrade_instructions'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_edges(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Edges (getEdges)  # noqa: E501

Returns a page of edges owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edges(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edges'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_edges_by_ids(edge_ids_json: str) -> str:
    """
    Get Edges By Ids (getEdgesByIds)  # noqa: E501

Requested edges must be owned by tenant or assigned to customer which user is performing the request.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edges_by_ids(edge_ids=json.loads(edge_ids_json) if edge_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edges_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_edge(edge_name: str) -> str:
    """
    Get Tenant Edge (getTenantEdge)  # noqa: E501

Requested edge must be owned by tenant or customer that the user belongs to. Edge name is an unique property of edge. So it can be used to identify the edge.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_edge(edge_name=edge_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_edge_infos(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Edge Infos (getTenantEdgeInfos)  # noqa: E501

Returns a page of edges info objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. Edge Info is an extension of the default Edge object that contains information about the assigned customer name.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_edge_infos(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_edge_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_edges(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Edges (getTenantEdges)  # noqa: E501

Returns a page of edges owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_edges(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_edges'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def is_edge_upgrade_available(edge_id_json: str) -> str:
    """
    Is edge upgrade enabled (isEdgeUpgradeAvailable)  # noqa: E501

Returns 'true' if upgrade available for connected edge, 'false' - otherwise.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.is_edge_upgrade_available(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'is_edge_upgrade_available'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def is_edges_support_enabled() -> str:
    """
    Is edges support enabled (isEdgesSupportEnabled)  # noqa: E501

Returns 'true' if edges support enabled on server, 'false' - otherwise.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.is_edges_support_enabled()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'is_edges_support_enabled'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def process_edges_bulk_import(body_json: str = None) -> str:
    """
    Import the bulk of edges (processEdgesBulkImport)  # noqa: E501

There's an ability to import the bulk of edges using the only .csv file.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.process_edges_bulk_import(body=deserialize_param(body_json, 'BulkImportRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'process_edges_bulk_import'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_edge(body_json: str = None) -> str:
    """
    Create Or Update Edge (saveEdge)  # noqa: E501

Create or update the Edge. When creating edge, platform generates Edge Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created edge id will be present in the response. Specify existing Edge id to update the edge. Referencing non-existing Edge Id will cause 'Not Found' error.  Edge name is unique in the scope of tenant. Use unique identifiers like MAC or IMEI for the edge names and non-unique 'label' field for user-friendly visualization purposes.Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Edge entity.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_edge(body=deserialize_param(body_json, 'Edge'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def set_edge_root_rule_chain(edge_id_json: str, rule_chain_id_json: str) -> str:
    """
    Set root rule chain for provided edge (setEdgeRootRuleChain)  # noqa: E501

Change root rule chain of the edge to the new provided rule chain.  This operation will send a notification to update root rule chain on remote edge service.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.set_edge_root_rule_chain(edge_id=deserialize_param(edge_id_json, 'EdgeId'), rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'set_edge_root_rule_chain'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def sync_edge(edge_id_json: str) -> str:
    """
    Sync edge (syncEdge)  # noqa: E501

Starts synchronization process between edge and cloud.  All entities that are assigned to particular edge are going to be send to remote edge service.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sync_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sync_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def unassign_edge_from_customer(edge_id_json: str) -> str:
    """
    Unassign edge from customer (unassignEdgeFromCustomer)  # noqa: E501

Clears assignment of the edge to customer. Customer will not be able to query edge afterwards.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.unassign_edge_from_customer(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unassign_edge_from_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( assign_edge_to_customer )
    mcp.tool()( assign_edge_to_public_customer )
    mcp.tool()( delete_edge )
    mcp.tool()( find_by_query_v2 )
    mcp.tool()( find_missing_to_related_rule_chains )
    mcp.tool()( get_customer_edge_infos )
    mcp.tool()( get_customer_edges )
    mcp.tool()( get_edge_by_id )
    mcp.tool()( get_edge_info_by_id )
    mcp.tool()( get_edge_install_instructions )
    mcp.tool()( get_edge_types )
    mcp.tool()( get_edge_upgrade_instructions )
    mcp.tool()( get_edges )
    mcp.tool()( get_edges_by_ids )
    mcp.tool()( get_tenant_edge )
    mcp.tool()( get_tenant_edge_infos )
    mcp.tool()( get_tenant_edges )
    mcp.tool()( is_edge_upgrade_available )
    mcp.tool()( is_edges_support_enabled )
    mcp.tool()( process_edges_bulk_import )
    mcp.tool()( save_edge )
    mcp.tool()( set_edge_root_rule_chain )
    mcp.tool()( sync_edge )
    mcp.tool()( unassign_edge_from_customer )
