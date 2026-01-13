import json
from typing import Optional
from .shared import get_client, deserialize_param, format_response, ApiException


def assign_rule_chain_to_edge(edge_id_json: str, rule_chain_id_json: str) -> str:
    """
    Assign rule chain to edge (assignRuleChainToEdge)  # noqa: E501

Creates assignment of an existing rule chain to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment rule chain (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once rule chain will be delivered to edge service, it's going to start processing messages locally.   Only rule chain with type 'EDGE' can be assigned to edge.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str edge_id: edgeId (required)
:param str rule_chain_id: ruleChainId (required)
:return: RuleChain
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.assign_rule_chain_to_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'assign_rule_chain_to_edge'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_rule_chain(rule_chain_id_json: str) -> str:
    """
    Delete rule chain (deleteRuleChain)  # noqa: E501

Deletes the rule chain. Referencing non-existing rule chain Id will cause an error. Referencing rule chain that is used in the device profiles will cause an error.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str rule_chain_id: A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_rule_chain(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_rule_chain'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def export_rule_chains(limit: int) -> str:
    """
    Export Rule Chains  # noqa: E501

Exports all tenant rule chains as one JSON.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int limit: A limit of rule chains to export. (required)
:return: RuleChainData
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.export_rule_chains(limit=limit)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'export_rule_chains'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_missing_to_related_rule_chains(edge_id_json: str) -> str:
    """
    Find missing rule chains (findMissingToRelatedRuleChains)  # noqa: E501

Returns list of rule chains ids that are not assigned to particular edge, but these rule chains are present in the already assigned rule chains to edge.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str edge_id: A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.find_missing_to_related_rule_chains(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_missing_to_related_rule_chains'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_auto_assign_to_edge_rule_chains() -> str:
    """
    Get Auto Assign To Edge Rule Chains (getAutoAssignToEdgeRuleChains)  # noqa: E501

Returns a list of Rule Chains that will be assigned to a newly created edge. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: list[RuleChain]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_auto_assign_to_edge_rule_chains()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_auto_assign_to_edge_rule_chains'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edge_rule_chains(edge_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Edge Rule Chains (getEdgeRuleChains)  # noqa: E501

Returns a page of Rule Chains assigned to the specified edge. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str edge_id: A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on the rule chain name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataRuleChain
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_edge_rule_chains(edge_id=deserialize_param(edge_id_json, 'EdgeId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_edge_rule_chains'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_rule_chain_by_id(rule_chain_id_json: str) -> str:
    """
    Get Rule Chain (getRuleChainById)  # noqa: E501

Fetch the Rule Chain object based on the provided Rule Chain Id. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str rule_chain_id: A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: RuleChain
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_rule_chain_by_id(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_rule_chain_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_rule_chain_meta_data(rule_chain_id_json: str) -> str:
    """
    Get Rule Chain (getRuleChainById)  # noqa: E501

Fetch the Rule Chain Metadata object based on the provided Rule Chain Id. The metadata object contains information about the rule nodes and their connections.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str rule_chain_id: A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: RuleChainMetaData
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_rule_chain_meta_data(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_rule_chain_meta_data'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_rule_chain_output_labels(rule_chain_id_json: str) -> str:
    """
    Get Rule Chain output labels (getRuleChainOutputLabels)  # noqa: E501

Fetch the unique labels for the "output" Rule Nodes that belong to the Rule Chain based on the provided Rule Chain Id. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str rule_chain_id: A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: list[str]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_rule_chain_output_labels(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_rule_chain_output_labels'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_rule_chain_output_labels_usage(rule_chain_id_json: str) -> str:
    """
    Get output labels usage (getRuleChainOutputLabelsUsage)  # noqa: E501

Fetch the list of rule chains and the relation types (labels) they use to process output of the current rule chain based on the provided Rule Chain Id. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str rule_chain_id: A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: list[RuleChainOutputLabelsUsage]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_rule_chain_output_labels_usage(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_rule_chain_output_labels_usage'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_rule_chains(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Rule Chains (getRuleChains)  # noqa: E501

Returns a page of Rule Chains owned by tenant. The rule chain object is lightweight and contains general information about the rule chain. List of rule nodes and their connection is stored in a separate 'metadata' object.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str type: Rule chain type (CORE or EDGE)
:param str text_search: The case insensitive 'substring' filter based on the rule chain name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataRuleChain
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_rule_chains(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_rule_chains'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_rule_chains_by_ids(rule_chain_ids_json: str) -> str:
    """
    Get Rule Chains By Ids (getRuleChainsByIds)  # noqa: E501

Requested rule chains must be owned by tenant which is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str rule_chain_ids: A list of rule chain ids, separated by comma ',' (required)
:return: list[str]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_rule_chains_by_ids(rule_chain_ids=json.loads(rule_chain_ids_json) if rule_chain_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_rule_chains_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def import_rule_chains(body: str, overwrite: Optional[str] = None) -> str:
    """
    Import Rule Chains  # noqa: E501

Imports all tenant rule chains as one JSON.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param RuleChainData body:
:param bool overwrite: Enables overwrite for existing rule chains with the same name.
:return: list[RuleChainImportResult]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.import_rule_chains(body=body, overwrite=overwrite)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'import_rule_chains'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_rule_chain(body: str) -> str:
    """
    Create Default Rule Chain  # noqa: E501

Create rule chain from template, based on the specified name in the request. Creates the rule chain based on the template that is used to create root rule chain.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param DefaultRuleChainCreateRequest body:
:return: RuleChain
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_rule_chain(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_rule_chain'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_rule_chain_meta_data(body: Optional[str] = None, update_related: Optional[str] = None) -> str:
    """
    Update Rule Chain Metadata  # noqa: E501

Updates the rule chain metadata. The metadata object contains information about the rule nodes and their connections.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param RuleChainMetaData body:
:param bool update_related: Update related rule nodes.
:return: RuleChainMetaData
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_rule_chain_meta_data(body=body, update_related=update_related)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_rule_chain_meta_data'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_rule_chain_v1(body: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.save_rule_chain_v1(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_rule_chain_v1'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def set_auto_assign_to_edge_rule_chain(rule_chain_id_json: str) -> str:
    """
    Set Auto Assign To Edge Rule Chain (setAutoAssignToEdgeRuleChain)  # noqa: E501

Makes the rule chain to be automatically assigned for any new edge that will be created. Does not assign this rule chain for already created edges.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str rule_chain_id: A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: RuleChain
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.set_auto_assign_to_edge_rule_chain(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'set_auto_assign_to_edge_rule_chain'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def set_edge_root_rule_chain(edge_id_json: str, rule_chain_id_json: str) -> str:
    """
    Set root rule chain for provided edge (setEdgeRootRuleChain)  # noqa: E501

Change root rule chain of the edge to the new provided rule chain.  This operation will send a notification to update root rule chain on remote edge service.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str edge_id: A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str rule_chain_id: A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: Edge
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.set_edge_root_rule_chain(edge_id=deserialize_param(edge_id_json, 'EdgeId'), rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'set_edge_root_rule_chain'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def set_edge_template_root_rule_chain(rule_chain_id_json: str) -> str:
    """
    Set Edge Template Root Rule Chain (setEdgeTemplateRootRuleChain)  # noqa: E501

Makes the rule chain to be root rule chain for any new edge that will be created. Does not update root rule chain for already created edges.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str rule_chain_id: A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: RuleChain
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.set_edge_template_root_rule_chain(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'set_edge_template_root_rule_chain'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def set_root_rule_chain(rule_chain_id_json: str) -> str:
    """
    Set Root Rule Chain (setRootRuleChain)  # noqa: E501

Makes the rule chain to be root rule chain. Updates previous root rule chain as well.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str rule_chain_id: A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: RuleChain
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.set_root_rule_chain(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'set_root_rule_chain'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def unassign_rule_chain_from_edge(edge_id_json: str, rule_chain_id_json: str) -> str:
    """
    Unassign rule chain from edge (unassignRuleChainFromEdge)  # noqa: E501

Clears assignment of the rule chain to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove rule chain (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove rule chain locally.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str edge_id: edgeId (required)
:param str rule_chain_id: ruleChainId (required)
:return: RuleChain
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.unassign_rule_chain_from_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'unassign_rule_chain_from_edge'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def unset_auto_assign_to_edge_rule_chain(rule_chain_id_json: str) -> str:
    """
    Unset Auto Assign To Edge Rule Chain (unsetAutoAssignToEdgeRuleChain)  # noqa: E501

Removes the rule chain from the list of rule chains that are going to be automatically assigned for any new edge that will be created. Does not unassign this rule chain for already assigned edges.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str rule_chain_id: A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: RuleChain
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.unset_auto_assign_to_edge_rule_chain(rule_chain_id=deserialize_param(rule_chain_id_json, 'RuleChainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'unset_auto_assign_to_edge_rule_chain'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    """Register tools with FastMCP server"""
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
    mcp.tool()( get_rule_chains_by_ids )
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
