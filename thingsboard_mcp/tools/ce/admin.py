import json
import tb_rest_client.models.models_ce as models
from ...shared import get_client, deserialize_param, format_response, ApiException


def get_admin_settings(key: str) -> str:
    """
    Get the Administration Settings object using key (getAdminSettings)  # noqa: E501

Get the Administration Settings object using specified string key. Referencing non-existing key will cause an error.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_admin_settings(key=key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_admin_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_admin_settings(body_json: str) -> str:
    """
    Get the Administration Settings object using key (getAdminSettings)  # noqa: E501

Creates or Updates the Administration Settings. Platform generates random Administration Settings Id during settings creation. The Administration Settings Id will be present in the response. Specify the Administration Settings Id when you would like to update the Administration Settings. Referencing non-existing Administration Settings Id will cause an error.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_admin_settings(body=deserialize_param(body_json, 'AdminSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_admin_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def register(mcp):
    mcp.tool()( get_admin_settings )
    mcp.tool()( save_admin_settings )
