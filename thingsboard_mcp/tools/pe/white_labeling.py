import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_current_login_white_label_params(customer_id_json: str) -> str:
    """
    Delete Login White Labeling configuration (deleteCurrentLoginWhiteLabelParams)  # noqa: E501

Delete the Login White Labeling configuration that corresponds to the authority of the user.   Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomerId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.delete_current_login_white_label_params(customer_id=deserialize_param(customer_id_json, 'CustomerId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_current_login_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_current_white_label_params(customer_id_json: str) -> str:
    """
    Delete General White Labeling configuration (deleteCurrentWhiteLabelParams)  # noqa: E501

Delete the White Labeling configuration that corresponds to the authority of the user.   Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomerId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.delete_current_white_label_params(customer_id=deserialize_param(customer_id_json, 'CustomerId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_current_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_current_login_white_label_params() -> str:
    """
    Get Login White Labeling configuration (getCurrentWhiteLabelParams)  # noqa: E501

Fetch the Login  White Labeling configuration that corresponds to the authority of the user. The API call is designed to load the Login White Labeling configuration for edition. So, the result is NOT merged with the parent level White Labeling configuration. Let's assume there is a custom White Labeling  configured on a system level. And there is no custom White Labeling  items configured on a tenant level. In such a case, the API call will return default object for the tenant administrator.   Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_current_login_white_label_params()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_current_login_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_current_white_label_params() -> str:
    """
    Get White Labeling configuration (getCurrentWhiteLabelParams)  # noqa: E501

Fetch the White Labeling configuration that corresponds to the authority of the user. The API call is designed to load the White Labeling configuration for edition. So, the result is NOT merged with the parent level White Labeling configuration. Let's assume there is a custom White Labeling  configured on a system level. And there is no custom White Labeling  items configured on a tenant level. In such a case, the API call will return default object for the tenant administrator.   Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_current_white_label_params()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_current_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_login_white_label_params(logo_image_checksum: str, favicon_checksum: str) -> str:
    """
    Get Login White Labeling parameters  # noqa: E501

Returns login white-labeling parameters based on the hostname from request.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_login_white_label_params(logo_image_checksum=logo_image_checksum, favicon_checksum=favicon_checksum)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_login_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_white_label_params(logo_image_checksum: str, favicon_checksum: str) -> str:
    """
    Get White Labeling parameters  # noqa: E501

Returns white-labeling parameters for the current user.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_white_label_params(logo_image_checksum=logo_image_checksum, favicon_checksum=favicon_checksum)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def is_customer_white_labeling_allowed() -> str:
    """
    Check Customer White Labeling Allowed  # noqa: E501

Check if the White Labeling is enabled for the customers of the current tenant  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.is_customer_white_labeling_allowed()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'is_customer_white_labeling_allowed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def is_white_labeling_allowed() -> str:
    """
    Check White Labeling Allowed  # noqa: E501

Check if the White Labeling is enabled for the current user owner (tenant or customer)  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.is_white_labeling_allowed()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'is_white_labeling_allowed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def preview_white_label_params(body_json: str = None) -> str:
    """
    Preview Login White Labeling configuration (saveWhiteLabelParams)  # noqa: E501

Merge the White Labeling configuration with the parent configuration and return the result.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501

    ---------------------------
    Expected JSON Structure (WhiteLabelingParams):
    - `logo_image_url` (str)
    - `logo_image_height` (int)
    - `app_title` (str)
    - `favicon` (Favicon)
    - `palette_settings` (PaletteSettings)
    - `help_link_base_url` (str)
    - `ui_help_base_url` (str)
    - `enable_help_links` (bool)
    - `white_labeling_enabled` (bool)
    - `show_name_version` (bool)
    - `platform_name` (str)
    - `platform_version` (str)
    - `custom_css` (str)
    - `hide_connectivity_dialog` (bool)
    """
    try:
        client = get_client()
        result = client.preview_white_label_params(body=deserialize_param(body_json, 'WhiteLabelingParams'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'preview_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_login_white_label_params(body_json: str = None) -> str:
    """
    Create Or Update Login White Labeling configuration (saveWhiteLabelParams)  # noqa: E501

Creates or Updates the White Labeling configuration.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501

    ---------------------------
    Expected JSON Structure (LoginWhiteLabelingParams):
    - `logo_image_url` (str)
    - `logo_image_height` (int)
    - `app_title` (str)
    - `favicon` (Favicon)
    - `palette_settings` (PaletteSettings)
    - `help_link_base_url` (str)
    - `ui_help_base_url` (str)
    - `enable_help_links` (bool)
    - `white_labeling_enabled` (bool)
    - `show_name_version` (bool)
    - `platform_name` (str)
    - `platform_version` (str)
    - `custom_css` (str)
    - `hide_connectivity_dialog` (bool)
    - `page_background_color` (str)
    - `dark_foreground` (bool)
    - `domain_name` (str)
    - `base_url` (str)
    - `prohibit_different_url` (bool)
    - `admin_settings_id` (str)
    - `show_name_bottom` (bool)
    """
    try:
        client = get_client()
        result = client.save_login_white_label_params(body=deserialize_param(body_json, 'LoginWhiteLabelingParams'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_login_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_white_label_params(body_json: str = None) -> str:
    """
    Create Or Update White Labeling configuration (saveWhiteLabelParams)  # noqa: E501

Creates or Updates the White Labeling configuration.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501

    ---------------------------
    Expected JSON Structure (WhiteLabelingParams):
    - `logo_image_url` (str)
    - `logo_image_height` (int)
    - `app_title` (str)
    - `favicon` (Favicon)
    - `palette_settings` (PaletteSettings)
    - `help_link_base_url` (str)
    - `ui_help_base_url` (str)
    - `enable_help_links` (bool)
    - `white_labeling_enabled` (bool)
    - `show_name_version` (bool)
    - `platform_name` (str)
    - `platform_version` (str)
    - `custom_css` (str)
    - `hide_connectivity_dialog` (bool)
    """
    try:
        client = get_client()
        result = client.save_white_label_params(body=deserialize_param(body_json, 'WhiteLabelingParams'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_current_login_white_label_params )
    mcp.tool()( delete_current_white_label_params )
    mcp.tool()( get_current_login_white_label_params )
    mcp.tool()( get_current_white_label_params )
    mcp.tool()( get_login_white_label_params )
    mcp.tool()( get_white_label_params )
    mcp.tool()( is_customer_white_labeling_allowed )
    mcp.tool()( is_white_labeling_allowed )
    mcp.tool()( preview_white_label_params )
    mcp.tool()( save_login_white_label_params )
    mcp.tool()( save_white_label_params )
