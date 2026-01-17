import json
import tb_rest_client.models.models_ce as models
from ...shared import get_client, deserialize_param, format_response, ApiException


def assign_rule_chain_to_edge(edge_id_json: str, rule_chain_id_json: str) -> str:
    """
    Assign rule chain to edge (assignRuleChainToEdge)  # noqa: E501

Creates assignment of an existing rule chain to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment rule chain (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once rule chain will be delivered to edge service, it's going to start processing messages locally.   Only rule chain with type 'EDGE' can be assigned to edge.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_rule_chain_to_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_rule_chain_to_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_rule_chain(rule_chain_id_json: str) -> str:
    """
    Delete rule chain (deleteRuleChain)  # noqa: E501

Deletes the rule chain. Referencing non-existing rule chain Id will cause an error. Referencing rule chain that is used in the device profiles will cause an error.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_rule_chain(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_rule_chain'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def export_rule_chains(limit: int) -> str:
    """
    Export Rule Chains  # noqa: E501

Exports all tenant rule chains as one JSON.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.export_rule_chains(limit=limit)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'export_rule_chains'."
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

def get_auto_assign_to_edge_rule_chains() -> str:
    """
    Get Auto Assign To Edge Rule Chains (getAutoAssignToEdgeRuleChains)  # noqa: E501

Returns a list of Rule Chains that will be assigned to a newly created edge. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_auto_assign_to_edge_rule_chains()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_auto_assign_to_edge_rule_chains'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edge_rule_chains(edge_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Edge Rule Chains (getEdgeRuleChains)  # noqa: E501

Returns a page of Rule Chains assigned to the specified edge. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_rule_chains(edge_id=deserialize_param(edge_id_json, 'EdgeId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_rule_chains'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_rule_chain_by_id(rule_chain_id_json: str) -> str:
    """
    Get Rule Chain (getRuleChainById)  # noqa: E501

Fetch the Rule Chain object based on the provided Rule Chain Id. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_rule_chain_by_id(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_rule_chain_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_rule_chain_meta_data(rule_chain_id_json: str) -> str:
    """
    Get Rule Chain (getRuleChainById)  # noqa: E501

Fetch the Rule Chain Metadata object based on the provided Rule Chain Id. The metadata object contains information about the rule nodes and their connections.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_rule_chain_meta_data(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_rule_chain_meta_data'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_rule_chain_output_labels(rule_chain_id_json: str) -> str:
    """
    Get Rule Chain output labels (getRuleChainOutputLabels)  # noqa: E501

Fetch the unique labels for the "output" Rule Nodes that belong to the Rule Chain based on the provided Rule Chain Id. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_rule_chain_output_labels(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_rule_chain_output_labels'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_rule_chain_output_labels_usage(rule_chain_id_json: str) -> str:
    """
    Get output labels usage (getRuleChainOutputLabelsUsage)  # noqa: E501

Fetch the list of rule chains and the relation types (labels) they use to process output of the current rule chain based on the provided Rule Chain Id. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_rule_chain_output_labels_usage(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_rule_chain_output_labels_usage'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_rule_chains(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Rule Chains (getRuleChains)  # noqa: E501

Returns a page of Rule Chains owned by tenant. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_rule_chains(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_rule_chains'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def import_rule_chains(body_json: str, overwrite: Optional[bool] = None) -> str:
    """
    Import Rule Chains  # noqa: E501

Imports all tenant rule chains as one JSON.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.import_rule_chains(body=deserialize_param(body_json, 'RuleChainData'), overwrite=overwrite)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'import_rule_chains'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_rule_chain(body_json: str) -> str:
    """
    Create Default Rule Chain  # noqa: E501

Create rule chain from template, based on the specified name in the request. Creates the rule chain based on the template that is used to create root rule chain.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_rule_chain(body=deserialize_param(body_json, 'DefaultRuleChainCreateRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_rule_chain'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_rule_chain_meta_data(body_json: str, update_related: Optional[bool] = None) -> str:
    """
    Update Rule Chain Metadata  # noqa: E501

Updates the rule chain metadata. The metadata object contains information about the rule nodes and their connections.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_rule_chain_meta_data(body=deserialize_param(body_json, 'RuleChainMetaData'), update_related=update_related)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_rule_chain_meta_data'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_rule_chain_v1(body_json: str) -> str:
    """
    Create Or Update Rule Chain (saveRuleChain)  # noqa: E501

Create or update the Rule Chain. When creating Rule Chain, platform generates Rule Chain Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Rule Chain Id will be present in the response. Specify existing Rule Chain id to update the rule chain. Referencing non-existing rule chain Id will cause 'Not Found' error.  The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.Remove 'id', 'tenantId' from the request body example (below) to create new Rule Chain entity.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_rule_chain_v1(body=deserialize_param(body_json, 'RuleChain'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_rule_chain_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def set_auto_assign_to_edge_rule_chain(rule_chain_id_json: str) -> str:
    """
    Set Auto Assign To Edge Rule Chain (setAutoAssignToEdgeRuleChain)  # noqa: E501

Makes the rule chain to be automatically assigned for any new edge that will be created. Does not assign this rule chain for already created edges.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.set_auto_assign_to_edge_rule_chain(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'set_auto_assign_to_edge_rule_chain'."
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

def set_edge_template_root_rule_chain(rule_chain_id_json: str) -> str:
    """
    Set Edge Template Root Rule Chain (setEdgeTemplateRootRuleChain)  # noqa: E501

Makes the rule chain to be root rule chain for any new edge that will be created. Does not update root rule chain for already created edges.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.set_edge_template_root_rule_chain(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'set_edge_template_root_rule_chain'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def set_root_rule_chain(rule_chain_id_json: str) -> str:
    """
    Set Root Rule Chain (setRootRuleChain)  # noqa: E501

Makes the rule chain to be root rule chain. Updates previous root rule chain as well.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.set_root_rule_chain(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'set_root_rule_chain'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def unassign_rule_chain_from_edge(edge_id_json: str, rule_chain_id_json: str) -> str:
    """
    Unassign rule chain from edge (unassignRuleChainFromEdge)  # noqa: E501

Clears assignment of the rule chain to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove rule chain (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove rule chain locally.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.unassign_rule_chain_from_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unassign_rule_chain_from_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def unset_auto_assign_to_edge_rule_chain(rule_chain_id_json: str) -> str:
    """
    Unset Auto Assign To Edge Rule Chain (unsetAutoAssignToEdgeRuleChain)  # noqa: E501

Removes the rule chain from the list of rule chains that are going to be automatically assigned for any new edge that will be created. Does not unassign this rule chain for already assigned edges.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.unset_auto_assign_to_edge_rule_chain(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unset_auto_assign_to_edge_rule_chain'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def register(mcp):
    mcp.tool()( assign_rule_chain_to_edge )
    mcp.tool()( delete_rule_chain )
    mcp.tool()( export_rule_chains )
    mcp.tool()( find_missing_to_related_rule_chains )
    mcp.tool()( get_auto_assign_to_edge_rule_chains )
    mcp.tool()( get_edge_rule_chains )
    mcp.tool()( get_rule_chain_by_id )
    mcp.tool()( get_rule_chain_meta_data )
    mcp.tool()( get_rule_chain_output_labels )
    mcp.tool()( get_rule_chain_output_labels_usage )
    mcp.tool()( get_rule_chains )
    mcp.tool()( import_rule_chains )
    mcp.tool()( save_rule_chain )
    mcp.tool()( save_rule_chain_meta_data )
    mcp.tool()( save_rule_chain_v1 )
    mcp.tool()( set_auto_assign_to_edge_rule_chain )
    mcp.tool()( set_edge_root_rule_chain )
    mcp.tool()( set_edge_template_root_rule_chain )
    mcp.tool()( set_root_rule_chain )
    mcp.tool()( unassign_rule_chain_from_edge )
    mcp.tool()( unset_auto_assign_to_edge_rule_chain )
