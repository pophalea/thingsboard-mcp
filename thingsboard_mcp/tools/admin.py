import json
from typing import Optional
from .shared import get_client, deserialize_param, format_response, ApiException


def get_admin_settings(key: str, system_by_default: Optional[str] = None) -> str:
    """
    Get the Administration Settings object using key (getAdminSettings)  # noqa: E501

Get the Administration Settings object using specified string key. Referencing non-existing key will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str key: A string value of the key (e.g. 'general' or 'mail'). (required)
:param bool system_by_default: Use system settings if settings are not defined on tenant level.
:return: AdminSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_admin_settings(key=key, system_by_default=system_by_default)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_admin_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_admin_settings(body: Optional[str] = None) -> str:
    """
    Get the Administration Settings object using key (getAdminSettings)  # noqa: E501

Creates or Updates the Administration Settings. Platform generates random Administration Settings Id during settings creation. The Administration Settings Id will be present in the response. Specify the Administration Settings Id when you would like to update the Administration Settings. Referencing non-existing Administration Settings Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'WRITE' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param AdminSettings body:
:return: AdminSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_admin_settings(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_admin_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    """Register tools with FastMCP server"""
    mcp.tool()( get_admin_settings )
    mcp.tool()( save_admin_settings )
