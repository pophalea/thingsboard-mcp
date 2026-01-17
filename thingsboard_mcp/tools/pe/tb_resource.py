import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def download_jks_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    Download JKS Resource (downloadJksResourceIfChanged)  # noqa: E501

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_jks_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_jks_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def download_js_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    Download JS Resource (downloadJsResourceIfChanged)  # noqa: E501

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_js_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_js_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def download_lwm2m_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    Download LWM2M Resource (downloadLwm2mResourceIfChanged)  # noqa: E501

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_lwm2m_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_lwm2m_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def download_pkcs12_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    Download PKCS_12 Resource (downloadPkcs12ResourceIfChanged)  # noqa: E501

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_pkcs12_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_pkcs12_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def download_resource(resource_id_json: str) -> str:
    """
    Download Resource (downloadResource)  # noqa: E501

Download Resource based on the provided Resource Id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_resource(resource_id=deserialize_param(resource_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_resource'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def download_resource_if_changed(resource_type: str, scope: str, key: str, if_none_match: str = "") -> str:
    """
    Download resource (downloadResource)  # noqa: E501

Download resource with a given type and key for the given scope  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_resource_if_changed(resource_type=resource_type, scope=scope, key=key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_lwm2m_list_objects(sort_order: str, sort_property: str, object_ids_json: str) -> str:
    """
    Get LwM2M Objects (getLwm2mListObjects)  # noqa: E501

Returns a page of LwM2M objects parsed from Resources with type 'LWM2M_MODEL' owned by tenant or sysadmin. You can specify parameters to filter the results. LwM2M Object is a object that includes information about the LwM2M model which can be used in transport configuration for the LwM2M device profile.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_lwm2m_list_objects(sort_order=sort_order, sort_property=sort_property, object_ids=json.loads(object_ids_json) if object_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_lwm2m_list_objects'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_lwm2m_list_objects_page(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get LwM2M Objects (getLwm2mListObjectsPage)  # noqa: E501

Returns a page of LwM2M objects parsed from Resources with type 'LWM2M_MODEL' owned by tenant or sysadmin. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. LwM2M Object is a object that includes information about the LwM2M model which can be used in transport configuration for the LwM2M device profile.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_lwm2m_list_objects_page(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_lwm2m_list_objects_page'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_resource_by_id(resource_id_json: str) -> str:
    """
    Get Resource (getResourceById)  # noqa: E501

Fetch the Resource object based on the provided Resource Id. Resource is a heavyweight object that includes main information about the Resource and also data.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_resource_by_id(resource_id=deserialize_param(resource_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_resource_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_resource_info_by_id(resource_id_json: str) -> str:
    """
    Get Resource Info (getResourceInfoById)  # noqa: E501

Fetch the Resource Info object based on the provided Resource Id. Resource Info is a lightweight object that includes main information about the Resource excluding the heavyweight data.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_resource_info_by_id(resource_id=deserialize_param(resource_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_resource_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_resources(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Resource Infos (getResources)  # noqa: E501

Returns a page of Resource Info objects owned by tenant or sysadmin. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. Resource Info is a lightweight object that includes main information about the Resource excluding the heavyweight data.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_resources(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_resources'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_resources(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get All Resource Infos (getAllResources)  # noqa: E501

Returns a page of Resource Info objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. Resource Info is a lightweight object that includes main information about the Resource excluding the heavyweight data.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_resources(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_resources'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_resource(body_json: str = None) -> str:
    """
    Create Or Update Resource (saveResource)  # noqa: E501

Create or update the Resource. When creating the Resource, platform generates Resource id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Resource id will be present in the response. Specify existing Resource id to update the Resource. Referencing non-existing Resource Id will cause 'Not Found' error.   Resource combination of the title with the key is unique in the scope of tenant. Remove 'id', 'tenantId' from the request body example (below) to create new Resource entity.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_resource(body=deserialize_param(body_json, 'TbResource'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_resource'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( download_jks_resource_if_changed )
    mcp.tool()( download_js_resource_if_changed )
    mcp.tool()( download_lwm2m_resource_if_changed )
    mcp.tool()( download_pkcs12_resource_if_changed )
    mcp.tool()( download_resource )
    mcp.tool()( download_resource_if_changed )
    mcp.tool()( get_lwm2m_list_objects )
    mcp.tool()( get_lwm2m_list_objects_page )
    mcp.tool()( get_resource_by_id )
    mcp.tool()( get_resource_info_by_id )
    mcp.tool()( get_resources )
    mcp.tool()( get_tenant_resources )
    mcp.tool()( save_resource )
