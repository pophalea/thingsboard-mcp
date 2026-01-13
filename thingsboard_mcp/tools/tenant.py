import json
from typing import Optional
from .shared import get_client, deserialize_param, format_response, ApiException


def change_owner_to_tenant(owner_id_json: str, entity_id_json: str, body_json: str = None) -> str:
    """
    Change owner to tenant (changeOwnerToTenant)  # noqa: E501

Tenant changes Owner from Customer or sub-Customer to Tenant.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str owner_id: A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param list[str] body:
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.change_owner_to_tenant(owner_id=deserialize_param(owner_id_json, 'UserId'), entity_id=deserialize_param(entity_id_json, 'EntityId'), body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'change_owner_to_tenant'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def check_tenant_can_update_plan(body: str) -> str:
    """
    checkTenantCanUpdatePlan  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str body: canUpdatePlanRequest (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.check_tenant_can_update_plan(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'check_tenant_can_update_plan'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_tenant(tenant_id_json: str) -> str:
    """
    Delete Tenant (deleteTenant)  # noqa: E501

Deletes the tenant, it's customers, rule chains, devices and all other related entities. Referencing non-existing tenant Id will cause an error.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str tenant_id: A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_tenant(tenant_id=deserialize_param(tenant_id_json, 'TenantId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_tenant'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_tenant_profile(tenant_profile_id_json: str) -> str:
    """
    Delete Tenant Profile (deleteTenantProfile)  # noqa: E501

Deletes the tenant profile. Referencing non-existing tenant profile Id will cause an error. Referencing profile that is used by the tenants will cause an error.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str tenant_profile_id: A string value representing the tenant profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_tenant_profile(tenant_profile_id=deserialize_param(tenant_profile_id_json, 'TenantProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_tenant_profile'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_tenant_o_auth2_client_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get OAuth2 Client infos (findTenantOAuth2ClientInfos)  # noqa: E501

  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: Case-insensitive 'substring' filter based on client's title
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataOAuth2ClientInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.find_tenant_o_auth2_client_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_tenant_o_auth2_client_infos'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_tenant_o_auth2_client_infos_by_ids(ids_json: str) -> str:
    """
    Get OAuth2 Client infos By Ids (findTenantOAuth2ClientInfosByIds)  # noqa: E501

Fetch OAuth2 Client info objects based on the provided ids.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str client_ids: A list of oauth2 ids, separated by comma ',' (required)
:return: list[OAuth2ClientInfo]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.find_tenant_o_auth2_client_infos_by_ids(ids=json.loads(ids_json) if ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_tenant_o_auth2_client_infos_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_default_tenant_profile_info() -> str:
    """
    Get default Tenant Profile Info (getDefaultTenantProfileInfo)  # noqa: E501

Fetch the default Tenant Profile Info object based. Tenant Profile Info is a lightweight object that contains only id and name of the profile.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: EntityInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_default_tenant_profile_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_default_tenant_profile_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_system_or_tenant_resources_by_ids(resource_ids_json: str) -> str:
    """
    Get Resource Infos by ids (getSystemOrTenantResourcesByIds)  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str resource_ids: A list of resource ids, separated by comma ',' (required)
:return: object
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_system_or_tenant_resources_by_ids(resource_ids=json.loads(resource_ids_json) if resource_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_system_or_tenant_resources_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_admins(tenant_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Users (getTenantAdmins)  # noqa: E501

Returns a page of users owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str tenant_id: A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on the user email.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataUser
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_admins(tenant_id=deserialize_param(tenant_id_json, 'TenantId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_admins'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_by_id(tenant_id_json: str) -> str:
    """
    Get Tenant (getTenantById)  # noqa: E501

Fetch the Tenant object based on the provided Tenant Id.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str tenant_id: A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: Tenant
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_by_id(tenant_id=deserialize_param(tenant_id_json, 'TenantId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_domain_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Domain infos (getTenantDomainInfos)  # noqa: E501

  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: Case-insensitive 'substring' filter based on domain's name
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataDomainInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_domain_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_domain_infos'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_edge(edge_name: str) -> str:
    """
    Get Tenant Edge (getTenantEdge)  # noqa: E501

Requested edge must be owned by tenant or customer that the user belongs to. Edge name is an unique property of edge. So it can be used to identify the edge.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str edge_name: Unique name of the edge (required)
:return: Edge
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_edge(edge_name=edge_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_edge'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_edges(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Edges (getTenantEdges)  # noqa: E501

Returns a page of edges owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str type: A string value representing the edge type. For example, 'default'
:param str text_search: The case insensitive 'substring' filter based on the edge name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataEdge
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_edges(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_edges'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_entity_view(entity_view_name: str) -> str:
    """
    Get Entity View by name (getTenantEntityView)  # noqa: E501

Fetch the Entity View object based on the tenant id and entity view name.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_view_name: Entity View name (required)
:return: EntityView
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_entity_view(entity_view_name=entity_view_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_entity_view'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_entity_views(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Entity Views (getTenantEntityViews)  # noqa: E501

Returns a page of entity views owned by tenant. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str type:   ## Entity View Filter  Allows to filter entity views based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Concrete Mixer' entity views which name starts with 'CAT':  ```json {   "type": "entityViewType",   "entityViewType": "Concrete Mixer",   "entityViewNameFilter": "CAT" } ```
:param str text_search: The case insensitive 'substring' filter based on the entity view name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataEntityView
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_entity_views(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_entity_views'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_info_by_id(tenant_id_json: str) -> str:
    """
    Get Tenant Info (getTenantInfoById)  # noqa: E501

Fetch the Tenant Info object based on the provided Tenant Id. The Tenant Info object extends regular Tenant object and includes Tenant Profile name.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str tenant_id: A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: TenantInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_info_by_id(tenant_id=deserialize_param(tenant_id_json, 'TenantId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenants Info (getTenants)  # noqa: E501

Returns a page of tenant info objects registered in the platform. The Tenant Info object extends regular Tenant object and includes Tenant Profile name. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on the tenant name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataTenantInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_infos'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_mobile_app_bundle_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get mobile app bundle infos (getTenantMobileAppBundleInfos)  # noqa: E501

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: Case-insensitive 'substring' filter based on app's name
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataMobileAppBundleInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_mobile_app_bundle_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_mobile_app_bundle_infos'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_mobile_app_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get mobile app infos (getTenantMobileAppInfos)  # noqa: E501

  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: Case-insensitive 'substring' filter based on app's name
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataMobileAppInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_mobile_app_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_mobile_app_infos'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_mobile_apps(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get mobile app infos (getTenantMobileAppInfos)  # noqa: E501

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str platform_type: Platform type: ANDROID or IOS
:param str text_search: Case-insensitive 'substring' filter based on app's name
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataMobileApp
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_mobile_apps(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_mobile_apps'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_profile_by_id(tenant_profile_id_json: str) -> str:
    """
    Get Tenant Profile (getTenantProfileById)  # noqa: E501

Fetch the Tenant Profile object based on the provided Tenant Profile Id.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str tenant_profile_id: A string value representing the tenant profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: TenantProfile
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_profile_by_id(tenant_profile_id=deserialize_param(tenant_profile_id_json, 'TenantProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_profile_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_profile_data() -> str:
    """
    getTenantProfileData  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: TenantProfileData
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_profile_data()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_profile_data'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_profile_data_by_id(tenant_profile_id_json: str) -> str:
    """
    getTenantProfileDataById  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str tenant_profile_id: tenantProfileId (required)
:return: TenantProfileData
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_profile_data_by_id(tenant_profile_id=deserialize_param(tenant_profile_id_json, 'TenantProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_profile_data_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_profile_info_by_id(tenant_profile_id_json: str) -> str:
    """
    Get Tenant Profile Info (getTenantProfileInfoById)  # noqa: E501

Fetch the Tenant Profile Info object based on the provided Tenant Profile Id. Tenant Profile Info is a lightweight object that contains only id and name of the profile.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str tenant_profile_id: A string value representing the tenant profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: EntityInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_profile_info_by_id(tenant_profile_id=deserialize_param(tenant_profile_id_json, 'TenantProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_profile_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_profile_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Profiles Info (getTenantProfileInfos)  # noqa: E501

Returns a page of tenant profile info objects registered in the platform. Tenant Profile Info is a lightweight object that contains only id and name of the profile. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on the tenant profile name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataEntityInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_profile_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_profile_infos'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_profiles(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Profiles (getTenantProfiles)  # noqa: E501

Returns a page of tenant profiles registered in the platform. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on the tenant profile name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataTenantProfile
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_profiles(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_profiles'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_profiles_by_ids(ids_json: str) -> str:
    """
    getTenantProfilesByIds  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str ids: ids (required)
:return: list[TenantProfile]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_profiles_by_ids(ids=json.loads(ids_json) if ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_profiles_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_queue_stats(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Queue Stats entities (getTenantQueueStats)  # noqa: E501

Returns a page of queue stats objects that are designed to collect queue statistics for every service. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on the queue name or service id.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataQueueStats
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_queue_stats(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_queue_stats'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_queues_by_service_type(service_type: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Queues (getTenantQueuesByServiceType)  # noqa: E501

Returns a page of queues registered in the platform. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str service_type: Service type (implemented only for the TB-RULE-ENGINE) (required)
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on the queue name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataQueue
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_queues_by_service_type(service_type=service_type, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_queues_by_service_type'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_resources(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get All Resource Infos (getAllResources)  # noqa: E501

Returns a page of Resource Info objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. Resource Info is a lightweight object that includes main information about the Resource excluding the heavyweight data.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on the resource title.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataTbResourceInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_resources(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_resources'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_subscription_usage() -> str:
    """
    getTenantSubscriptionUsage  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: SubscriptionUsage
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_subscription_usage()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_subscription_usage'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_usage_info() -> str:
    """
    getTenantUsageInfo  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: UsageInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenant_usage_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenant_usage_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenants(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenants (getTenants)  # noqa: E501

Returns a page of tenants registered in the platform. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on the tenant name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataTenant
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenants(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenants'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenants_by_ids(tenant_ids_json: str) -> str:
    """
    getTenantsByIds  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str tenant_ids: tenantIds (required)
:return: list[Tenant]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_tenants_by_ids(tenant_ids=json.loads(tenant_ids_json) if tenant_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_tenants_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def notify_tenant_plan_changed(body: str) -> str:
    """
    notifyTenantPlanChanged  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str body: tenantPlanChangedRequest (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.notify_tenant_plan_changed(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'notify_tenant_plan_changed'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def notify_tenant_state_changed(body: str) -> str:
    """
    notifyTenantStateChanged  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str body: tenantStateChangedRequest (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.notify_tenant_state_changed(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'notify_tenant_state_changed'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_tenant(body: Optional[str] = None) -> str:
    """
    Create Or update Tenant (saveTenant)  # noqa: E501

Create or update the Tenant. When creating tenant, platform generates Tenant Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). Default Rule Chain and Device profile are also generated for the new tenants automatically. The newly created Tenant Id will be present in the response. Specify existing Tenant Id id to update the Tenant. Referencing non-existing Tenant Id will cause 'Not Found' error.Remove 'id', 'tenantId' from the request body example (below) to create new Tenant entity.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param Tenant body:
:return: Tenant
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_tenant(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_tenant'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_tenant_profile(body: Optional[str] = None) -> str:
    """
    Create Or update Tenant Profile (saveTenantProfile)  # noqa: E501

Create or update the Tenant Profile. When creating tenant profile, platform generates Tenant Profile Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Tenant Profile Id will be present in the response. Specify existing Tenant Profile Id id to update the Tenant Profile. Referencing non-existing Tenant Profile Id will cause 'Not Found' error.   Update of the tenant profile configuration will cause immediate recalculation of API limits for all affected Tenants.   The **'profileData'** object is the part of Tenant Profile that defines API limits and Rate limits.   You have an ability to define maximum number of devices ('maxDevice'), assets ('maxAssets') and other entities. You may also define maximum number of messages to be processed per month ('maxTransportMessages', 'maxREExecutions', etc). The '*RateLimit' defines the rate limits using simple syntax. For example, '1000:1,20000:60' means up to 1000 events per second but no more than 20000 event per minute. Let's review the example of tenant profile data below:   ```json {   "name": "Default",   "description": "Default tenant profile",   "isolatedTbRuleEngine": false,   "profileData": {     "configuration": {       "type": "DEFAULT",       "maxDevices": 0,       "maxAssets": 0,       "maxCustomers": 0,       "maxUsers": 0,       "maxDashboards": 0,       "maxRuleChains": 0,       "maxResourcesInBytes": 0,       "maxOtaPackagesInBytes": 0,       "maxResourceSize": 0,       "transportTenantMsgRateLimit": "1000:1,20000:60",       "transportTenantTelemetryMsgRateLimit": "1000:1,20000:60",       "transportTenantTelemetryDataPointsRateLimit": "1000:1,20000:60",       "transportDeviceMsgRateLimit": "20:1,600:60",       "transportDeviceTelemetryMsgRateLimit": "20:1,600:60",       "transportDeviceTelemetryDataPointsRateLimit": "20:1,600:60",       "maxTransportMessages": 10000000,       "maxTransportDataPoints": 10000000,       "maxREExecutions": 4000000,       "maxJSExecutions": 5000000,       "maxDPStorageDays": 0,       "maxRuleNodeExecutionsPerMessage": 50,       "maxEmails": 0,       "maxSms": 0,       "maxCreatedAlarms": 1000,       "defaultStorageTtlDays": 0,       "alarmsTtlDays": 0,       "rpcTtlDays": 0,       "queueStatsTtlDays": 0,       "ruleEngineExceptionsTtlDays": 0,       "warnThreshold": 0     }   },   "default": true } ```Remove 'id', from the request body example (below) to create new Tenant Profile entity.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param TenantProfile body:
:return: TenantProfile
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_tenant_profile(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_tenant_profile'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def set_default_tenant_profile(tenant_profile_id_json: str) -> str:
    """
    Make tenant profile default (setDefaultTenantProfile)  # noqa: E501

Makes specified tenant profile to be default. Referencing non-existing tenant profile Id will cause an error.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str tenant_profile_id: A string value representing the tenant profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: TenantProfile
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.set_default_tenant_profile(tenant_profile_id=deserialize_param(tenant_profile_id_json, 'TenantProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'set_default_tenant_profile'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def tenant_has_billing_read() -> str:
    """
    tenantHasBillingRead  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: bool
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.tenant_has_billing_read()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'tenant_has_billing_read'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def tenant_has_billing_write() -> str:
    """
    tenantHasBillingWrite  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: bool
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.tenant_has_billing_write()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'tenant_has_billing_write'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def tenant_has_white_label_read() -> str:
    """
    tenantHasWhiteLabelRead  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: bool
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.tenant_has_white_label_read()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'tenant_has_white_label_read'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def tenant_has_white_label_write() -> str:
    """
    tenantHasWhiteLabelWrite  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: bool
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.tenant_has_white_label_write()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'tenant_has_white_label_write'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def tenant_white_labeling_allowed() -> str:
    """
    tenantWhiteLabelingAllowed  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.tenant_white_labeling_allowed()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'tenant_white_labeling_allowed'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    """Register tools with FastMCP server"""
    mcp.tool()( change_owner_to_tenant )
    mcp.tool()( check_tenant_can_update_plan )
    mcp.tool()( delete_tenant )
    mcp.tool()( delete_tenant_profile )
    mcp.tool()( find_tenant_o_auth2_client_infos )
    mcp.tool()( find_tenant_o_auth2_client_infos_by_ids )
    mcp.tool()( get_default_tenant_profile_info )
    mcp.tool()( get_system_or_tenant_resources_by_ids )
    mcp.tool()( get_tenant_admins )
    mcp.tool()( get_tenant_by_id )
    mcp.tool()( get_tenant_domain_infos )
    mcp.tool()( get_tenant_edge )
    mcp.tool()( get_tenant_edges )
    mcp.tool()( get_tenant_entity_view )
    mcp.tool()( get_tenant_entity_views )
    mcp.tool()( get_tenant_info_by_id )
    mcp.tool()( get_tenant_infos )
    mcp.tool()( get_tenant_mobile_app_bundle_infos )
    mcp.tool()( get_tenant_mobile_app_infos )
    mcp.tool()( get_tenant_mobile_apps )
    mcp.tool()( get_tenant_profile_by_id )
    mcp.tool()( get_tenant_profile_data )
    mcp.tool()( get_tenant_profile_data_by_id )
    mcp.tool()( get_tenant_profile_info_by_id )
    mcp.tool()( get_tenant_profile_infos )
    mcp.tool()( get_tenant_profiles )
    mcp.tool()( get_tenant_profiles_by_ids )
    mcp.tool()( get_tenant_queue_stats )
    mcp.tool()( get_tenant_queues_by_service_type )
    mcp.tool()( get_tenant_resources )
    mcp.tool()( get_tenant_subscription_usage )
    mcp.tool()( get_tenant_usage_info )
    mcp.tool()( get_tenants )
    mcp.tool()( get_tenants_by_ids )
    mcp.tool()( notify_tenant_plan_changed )
    mcp.tool()( notify_tenant_state_changed )
    mcp.tool()( save_tenant )
    mcp.tool()( save_tenant_profile )
    mcp.tool()( set_default_tenant_profile )
    mcp.tool()( tenant_has_billing_read )
    mcp.tool()( tenant_has_billing_write )
    mcp.tool()( tenant_has_white_label_read )
    mcp.tool()( tenant_has_white_label_write )
    mcp.tool()( tenant_white_labeling_allowed )
