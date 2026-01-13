import json
from typing import Optional
from .shared import get_client, deserialize_param, format_response, ApiException


def download_jks_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    Download JKS Resource (downloadJksResourceIfChanged)  # noqa: E501

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str resource_id: A string value representing the resource id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str if_none_match: If-None-Match
:return: ByteArrayResource
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.download_jks_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'download_jks_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_js_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    Download JS Resource (downloadJsResourceIfChanged)  # noqa: E501

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str resource_id: A string value representing the resource id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str if_none_match: If-None-Match
:return: ByteArrayResource
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.download_js_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'download_js_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_lwm2m_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    Download LWM2M Resource (downloadLwm2mResourceIfChanged)  # noqa: E501

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str resource_id: A string value representing the resource id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str if_none_match: If-None-Match
:return: ByteArrayResource
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.download_lwm2m_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'download_lwm2m_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_pkcs12_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    Download PKCS_12 Resource (downloadPkcs12ResourceIfChanged)  # noqa: E501

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str resource_id: A string value representing the resource id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str if_none_match: If-None-Match
:return: ByteArrayResource
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.download_pkcs12_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'download_pkcs12_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_resource(resource_id_json: str) -> str:
    """
    Download Resource (downloadResource)  # noqa: E501

Download Resource based on the provided Resource Id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str resource_id: A string value representing the resource id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: ByteArrayResource
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.download_resource(resource_id=deserialize_param(resource_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'download_resource'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_resource_if_changed(resource_type: str, scope: str, key: str, if_none_match: str = "") -> str:
    """
    Download resource (downloadResource)  # noqa: E501

Download resource with a given type and key for the given scope  Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param object resource_type: Type of the resource (required)
:param object scope: Scope of the resource (required)
:param object key: Key of the resource, e.g. 'extension.js' (required)
:param object if_none_match:
:return: object
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.download_resource_if_changed(resource_type=resource_type, scope=scope, key=key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'download_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_resource_by_id(resource_id_json: str) -> str:
    """
    Get Resource (getResourceById)  # noqa: E501

Fetch the Resource object based on the provided Resource Id. Resource is a heavyweight object that includes main information about the Resource and also data.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str resource_id: A string value representing the resource id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: TbResource
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_resource_by_id(resource_id=deserialize_param(resource_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_resource_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_resource_info_by_id(resource_id_json: str) -> str:
    """
    Get Resource Info (getResourceInfoById)  # noqa: E501

Fetch the Resource Info object based on the provided Resource Id. Resource Info is a lightweight object that includes main information about the Resource excluding the heavyweight data.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str resource_id: A string value representing the resource id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: TbResourceInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_resource_info_by_id(resource_id=deserialize_param(resource_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_resource_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_resources(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Resource Infos (getResources)  # noqa: E501

Returns a page of Resource Info objects owned by tenant or sysadmin. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. Resource Info is a lightweight object that includes main information about the Resource excluding the heavyweight data.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str resource_type: A string value representing the resource type.
:param str text_search: The case insensitive 'substring' filter based on the resource title.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataTbResourceInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_resources(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_resources'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_resource(body: Optional[str] = None) -> str:
    """
    Create Or Update Resource (saveResource)  # noqa: E501

Create or update the Resource. When creating the Resource, platform generates Resource id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Resource id will be present in the response. Specify existing Resource id to update the Resource. Referencing non-existing Resource Id will cause 'Not Found' error.   Resource combination of the title with the key is unique in the scope of tenant. Remove 'id', 'tenantId' from the request body example (below) to create new Resource entity.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param TbResource body:
:return: TbResourceInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_resource(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_resource'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    """Register tools with FastMCP server"""
    mcp.tool()( download_jks_resource_if_changed )
    mcp.tool()( download_js_resource_if_changed )
    mcp.tool()( download_lwm2m_resource_if_changed )
    mcp.tool()( download_pkcs12_resource_if_changed )
    mcp.tool()( download_resource )
    mcp.tool()( download_resource_if_changed )
    mcp.tool()( get_resource_by_id )
    mcp.tool()( get_resource_info_by_id )
    mcp.tool()( get_resources )
    mcp.tool()( save_resource )
