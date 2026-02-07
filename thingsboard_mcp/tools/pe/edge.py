import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def activate_instance(license_secret: str, release_date: str) -> str:
    """
    Activate edge instance (activateInstance)  # noqa: E501

Activates edge license on license portal.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.activate_instance(license_secret=license_secret, release_date=release_date)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'activate_instance'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def check_instance(body_json: str = None) -> str:
    """
    Check edge license (checkInstance)  # noqa: E501

Checks license request from edge service by forwarding request to license portal.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.check_instance(body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'check_instance'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_edge(edge_id_json: str) -> str:
    """
    Delete edge (deleteEdge)  # noqa: E501

Deletes the edge. Referencing non-existing edge Id will cause an error.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EdgeId):
    - `id` (str)
    - `entity_type` (str)
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

    ---------------------------
    Expected JSON Structure (EdgeSearchQuery):
    - `parameters` (RelationsSearchParameters)
    - `relation_type` (str)
    - `edge_types` (list[str])
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

    ---------------------------
    Expected JSON Structure (EdgeId):
    - `id` (str)
    - `entity_type` (str)
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


def get_customer_edges(customer_id_json: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Customer Edges (getCustomerEdges)  # noqa: E501

Returns a page of edges objects assigned to customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomerId):
    - `id` (str)
    - `entity_type` (str)
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

    ---------------------------
    Expected JSON Structure (EdgeId):
    - `id` (str)
    - `entity_type` (str)
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


def get_edge_install_instructions(edge_id_json: str, method: str) -> str:
    """
    Get Edge Install Instructions (getEdgeInstallInstructions)  # noqa: E501

Get an install instructions for provided edge id.If the user has the authority of 'Tenant Administrator', the server checks that the edge is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the edge is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EdgeId):
    - `id` (str)
    - `entity_type` (str)
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

Get an upgrade instructions for provided edge vesion.If the user has the authority of 'Tenant Administrator', the server checks that the edge is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the edge is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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


def get_user_edges(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Edges (getUserEdges)  # noqa: E501

Returns a page of edges available for current user. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_user_edges(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_user_edges'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def is_edge_upgrade_available(edge_id_json: str) -> str:
    """
    Is edge upgrade enabled (isEdgeUpgradeAvailable)  # noqa: E501

Returns 'true' if upgrade available for connected edge, 'false' - otherwise.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EdgeId):
    - `id` (str)
    - `entity_type` (str)
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

There's an ability to import the bulk of edges using the only .csv file.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (BulkImportRequest):
    - `file` (str)
    - `mapping` (Mapping)
    - `customer_id` (CustomerId)
    - `entity_group_id` (str)
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

Create or update the Edge. When creating edge, platform generates Edge Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created edge id will be present in the response. Specify existing Edge id to update the edge. Referencing non-existing Edge Id will cause 'Not Found' error.  Edge name is unique in the scope of tenant. Use unique identifiers like MAC or IMEI for the edge names and non-unique 'label' field for user-friendly visualization purposes.Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Edge entity.   # noqa: E501

    ---------------------------
    Expected JSON Structure (Edge):
    - `id` (EdgeId)
    - `created_time` (int)
    - `tenant_id` (TenantId)
    - `customer_id` (CustomerId)
    - `root_rule_chain_id` (RuleChainId)
    - `name` (str)
    - `type` (str)
    - `label` (str)
    - `routing_key` (str)
    - `secret` (str)
    - `edge_license_key` (str)
    - `cloud_endpoint` (str)
    - `version` (int)
    - `owner_id` (EntityId)
    - `additional_info` (JsonNode)
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

    ---------------------------
    Expected JSON Structure (EdgeId):
    - `id` (str)
    - `entity_type` (str)
    Expected JSON Structure (RuleChainId):
    - `id` (str)
    - `entity_type` (str)
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

    ---------------------------
    Expected JSON Structure (EdgeId):
    - `id` (str)
    - `entity_type` (str)
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


def register(mcp):
    mcp.tool()( activate_instance )
    mcp.tool()( check_instance )
    mcp.tool()( delete_edge )
    mcp.tool()( find_by_query_v2 )
    mcp.tool()( find_missing_to_related_rule_chains )
    mcp.tool()( get_customer_edges )
    mcp.tool()( get_edge_by_id )
    mcp.tool()( get_edge_install_instructions )
    mcp.tool()( get_edge_types )
    mcp.tool()( get_edge_upgrade_instructions )
    mcp.tool()( get_edges )
    mcp.tool()( get_edges_by_ids )
    mcp.tool()( get_tenant_edge )
    mcp.tool()( get_tenant_edges )
    mcp.tool()( get_user_edges )
    mcp.tool()( is_edge_upgrade_available )
    mcp.tool()( is_edges_support_enabled )
    mcp.tool()( process_edges_bulk_import )
    mcp.tool()( save_edge )
    mcp.tool()( set_edge_root_rule_chain )
    mcp.tool()( sync_edge )
