import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_secret(secret_id_json: str) -> str:
    """
    Delete secret by ID (deleteSecret)  # noqa: E501

Deletes the secret. Referencing non-existing Secret Id will cause an error.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_secret(secret_id=deserialize_param(secret_id_json, 'SecretId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_secret'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_secret_info_by_id(secret_id_json: str) -> str:
    """
    Get Secret info by Id (getSecretInfoById)  # noqa: E501

  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_secret_info_by_id(secret_id=deserialize_param(secret_id_json, 'SecretId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_secret_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_secret_info_by_name(name: str) -> str:
    """
    Get Secret info by name (getSecretInfoByName)  # noqa: E501

  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_secret_info_by_name(name=name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_secret_info_by_name'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_secret_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Secret infos (getSecretInfos)  # noqa: E501

Returns a page of secret infos owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_secret_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_secret_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_secret_names() -> str:
    """
    Get Tenant Secret names (getSecretNames)  # noqa: E501

Returns a page of secret names owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_secret_names()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_secret_names'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_secret(body_json: str) -> str:
    """
    Save or Update Secret (saveSecret)  # noqa: E501

Create or update the Secret. When creating secret, platform generates Secret Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Secret Id will be present in the response. Specify existing Secret Id to update the secret. Secret name is not updatable, only value could be changed. Referencing non-existing Secret Id will cause 'Not Found' error.  Secret name is unique in the scope of tenant.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_secret(body=deserialize_param(body_json, 'Secret'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_secret'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def update_secret_description(id_json: str, description: str) -> str:
    """
    Update Secret Description  # noqa: E501

Updates the description of the existing Secret by secretId. Only the description can be updated. Referencing a non-existing Secret Id will cause a 'Not Found' error.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_secret_description(id=deserialize_param(id_json, 'SecretId'), description=description)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_secret_description'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def update_secret_value(id_json: str, value: str) -> str:
    """
    Update Secret value  # noqa: E501

Updates the value of the existing Secret by secretId. Referencing a non-existing Secret Id will cause a 'Not Found' error.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_secret_value(id=deserialize_param(id_json, 'SecretId'), value=value)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_secret_value'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_secret )
    mcp.tool()( get_secret_info_by_id )
    mcp.tool()( get_secret_info_by_name )
    mcp.tool()( get_secret_infos )
    mcp.tool()( get_secret_names )
    mcp.tool()( save_secret )
    mcp.tool()( update_secret_description )
    mcp.tool()( update_secret_value )
