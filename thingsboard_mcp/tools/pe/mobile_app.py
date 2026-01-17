import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_mobile_app(mobile_app_id_json: str) -> str:
    """
    Delete Mobile App by ID (deleteMobileApp)  # noqa: E501

Deletes Mobile App by ID. Referencing non-existing mobile app Id will cause an error.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_mobile_app(mobile_app_id=deserialize_param(mobile_app_id_json, 'MobileAppId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_mobile_app'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_login_mobile_info(pkg_name: str, platform: str) -> str:
    """
    Get mobile app login info (getLoginMobileInfo)  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_login_mobile_info(pkg_name=pkg_name, platform=platform)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_login_mobile_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_mobile_app_by_id(mobile_app_id_json: str) -> str:
    """
    Get mobile info by id (getMobileAppInfoById)  # noqa: E501

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_app_by_id(mobile_app_id=deserialize_param(mobile_app_id_json, 'MobileAppId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_app_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_mobile_app_info_by_id(mobile_app_id_json: str) -> str:
    """
    Get mobile info by id (getMobileAppInfoById)  # noqa: E501

  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_app_info_by_id(mobile_app_id=deserialize_param(mobile_app_id_json, 'MobileAppId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_app_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_mobile_app_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get mobile app infos (getTenantMobileAppInfos)  # noqa: E501

  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_mobile_app_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_mobile_app_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_mobile_apps(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get mobile app infos (getTenantMobileAppInfos)  # noqa: E501

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_mobile_apps(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_mobile_apps'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_user_mobile_info(pkg_name: str, platform: str) -> str:
    """
    Get user mobile app basic info (getUserMobileInfo)  # noqa: E501

  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_user_mobile_info(pkg_name=pkg_name, platform=platform)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_user_mobile_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def mobile_app_update_oauth2_clients(body_json: str, id: str) -> str:
    """
    Update oauth2 clients (updateOauth2Clients)  # noqa: E501

Update oauth2 clients of the specified mobile app.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.mobile_app_update_oauth2_clients(body=json.loads(body_json) if body_json else None, id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'mobile_app_update_oauth2_clients'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_mobile_app(body_json: str, oauth2_client_ids: Optional[str] = None) -> str:
    """
    Save Or update Mobile app (saveMobileApp)  # noqa: E501

Create or update the Mobile app. When creating mobile app, platform generates Mobile App Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Mobile App Id will be present in the response. Specify existing Mobile App Id to update the mobile app. Referencing non-existing Mobile App Id will cause 'Not Found' error.  Mobile app package name is unique for entire platform setup.    Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_mobile_app(body=deserialize_param(body_json, 'MobileApp'), oauth2_client_ids=oauth2_client_ids)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_mobile_app'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_mobile_app )
    mcp.tool()( get_login_mobile_info )
    mcp.tool()( get_mobile_app_by_id )
    mcp.tool()( get_mobile_app_info_by_id )
    mcp.tool()( get_tenant_mobile_app_infos )
    mcp.tool()( get_tenant_mobile_apps )
    mcp.tool()( get_user_mobile_info )
    mcp.tool()( mobile_app_update_oauth2_clients )
    mcp.tool()( save_mobile_app )
