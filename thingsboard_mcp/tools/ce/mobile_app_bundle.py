import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_mobile_app_bundle(mobile_app_bundle_id_json: str) -> str:
    """
    Delete Mobile App Bundle by ID (deleteMobileAppBundle)  # noqa: E501

Deletes Mobile App Bundle by ID. Referencing non-existing mobile app bundle Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (MobileAppBundleId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.delete_mobile_app_bundle(mobile_app_bundle_id=deserialize_param(mobile_app_bundle_id_json, 'MobileAppBundleId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_mobile_app_bundle'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_mobile_app_bundle_info_by_id(mobile_app_bundle_id_json: str) -> str:
    """
    Get mobile app bundle info by id (getMobileAppBundleInfoById)  # noqa: E501

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (MobileAppBundleId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_mobile_app_bundle_info_by_id(mobile_app_bundle_id=deserialize_param(mobile_app_bundle_id_json, 'MobileAppBundleId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_app_bundle_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_mobile_app_bundle_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get mobile app bundle infos (getTenantMobileAppBundleInfos)  # noqa: E501

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_mobile_app_bundle_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_mobile_app_bundle_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_mobile_app_bundle(body_json: str, oauth2_client_ids_json: str = None) -> str:
    """
    Save Or update Mobile app bundle (saveMobileAppBundle)  # noqa: E501

Create or update the Mobile app bundle that represents tha pair of ANDROID and IOS app and mobile settings like oauth2 clients, self-registration and layout configuration.When creating mobile app bundle, platform generates Mobile App Bundle Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Mobile App Bundle Id will be present in the response. Referencing non-existing Mobile App Bundle Id will cause 'Not Found' error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (MobileAppBundle):
    - `id` (MobileAppBundleId)
    - `created_time` (int)
    - `tenant_id` (TenantId)
    - `title` (str)
    - `description` (str)
    - `android_app_id` (MobileAppId)
    - `ios_app_id` (MobileAppId)
    - `layout_config` (MobileLayoutConfig)
    - `oauth2_enabled` (bool)
    - `name` (str)
    """
    try:
        client = get_client()
        result = client.save_mobile_app_bundle(body=deserialize_param(body_json, 'MobileAppBundle'), oauth2_client_ids=json.loads(oauth2_client_ids_json) if oauth2_client_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_mobile_app_bundle'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_mobile_app_bundle )
    mcp.tool()( get_mobile_app_bundle_info_by_id )
    mcp.tool()( get_tenant_mobile_app_bundle_infos )
    mcp.tool()( save_mobile_app_bundle )
