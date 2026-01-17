import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_custom_translation(locale_code: str) -> str:
    """
    Delete Custom Translation for specified locale (deleteCustomTranslation)  # noqa: E501

Delete entire custom translation settings for end-user  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_custom_translation(locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_custom_translation_key(locale_code: str, key_path: str) -> str:
    """
    Delete specified key of Custom Translation (deleteCustomTranslationKey)   # noqa: E501

The API call is designed to delete specified key of the custom translation and return as a result parent translation.(e.g. if tenant translation for key is 'value1' and customer translation is 'value2' then by deletinf key onn customer level you will get 'value1' in response)   Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_custom_translation_key(locale_code=locale_code, key_path=key_path)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_custom_translation_key'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_custom_translation(locale_code: str) -> str:
    """
    Get end-user Custom Translation configuration (getCustomTranslation)  # noqa: E501

Fetch the Custom Translation map for the end user. The custom translation is configured in the white labeling parameters. If custom translation translation is defined on the tenant level, it overrides the custom translation of the system level. Similar, if the custom translation is defined on the customer level, it overrides the translation configuration of the tenant level.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_custom_translation(locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_merged_custom_translation(locale_code: str) -> str:
    """
    Get end-user Custom Translation configuration (getMergedCustomTranslation)  # noqa: E501

Fetch end-user Custom Translation for specified locale. The custom translation is configured in the white labeling parameters. If custom translation translation is defined on the tenant level, it overrides the custom translation of the system level. Similar, if the custom translation is defined on the customer level, it overrides the translation configuration of the tenant level.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_merged_custom_translation(locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_merged_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def patch_custom_translation(body_json: str, locale_code: str) -> str:
    """
    Update Custom Translation for specified translation keys only (patchCustomTranslation)  # noqa: E501

The API call is designed to update the custom translation for specified key only.    Request example:   ```json {"notification.active":"active"} ```  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.patch_custom_translation(body=deserialize_param(body_json, 'CustomTranslation'), locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'patch_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_custom_translation(locale_code: str, body_json: str) -> str:
    """
    Create Or Update Custom Translation (saveCustomTranslation)  # noqa: E501

Creates or Updates the Custom Translation map.   Request example:   ```json {"translationMap":{"es_ES":"{\\"home\\":\\"MyHome\\"}"}} ```  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_custom_translation(locale_code=locale_code, body=deserialize_param(body_json, 'CustomTranslation'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def upload_custom_translation(locale_code: str, file_json: str) -> str:
    """
    Upload Custom Translation (uploadCustomTranslation)  # noqa: E501

Upload the Custom Translation for specified locale.   Request example:   ```json {"home":"MyHome"} ```  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.upload_custom_translation(locale_code=locale_code, file=deserialize_param(file_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'upload_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_custom_translation )
    mcp.tool()( delete_custom_translation_key )
    mcp.tool()( get_custom_translation )
    mcp.tool()( get_merged_custom_translation )
    mcp.tool()( patch_custom_translation )
    mcp.tool()( save_custom_translation )
    mcp.tool()( upload_custom_translation )
