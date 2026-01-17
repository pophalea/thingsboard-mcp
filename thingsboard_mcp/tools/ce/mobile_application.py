import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def get_application_redirect(user_agent: str) -> str:
    """
    getApplicationRedirect  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_application_redirect(user_agent=user_agent)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_application_redirect'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_mobile_app_deep_link() -> str:
    """
    Get the deep link to the associated mobile application (getMobileAppDeepLink)  # noqa: E501

Fetch the url that takes user to linked mobile application   Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_app_deep_link()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_app_deep_link'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_mobile_app_settings() -> str:
    """
    Get Mobile application settings (getMobileAppSettings)  # noqa: E501

The response payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_app_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_app_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_user_token_by_mobile_secret(secret: str) -> str:
    """
    Get User Token (getUserTokenByMobileSecret)  # noqa: E501

Returns the token of the User based on the provided secret key.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_user_token_by_mobile_secret(secret=secret)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_user_token_by_mobile_secret'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_mobile_app_settings(body_json: str) -> str:
    """
    Create Or Update the Mobile application settings (saveMobileAppSettings)  # noqa: E501

The request payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_mobile_app_settings(body=deserialize_param(body_json, 'MobileAppSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_mobile_app_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( get_application_redirect )
    mcp.tool()( get_mobile_app_deep_link )
    mcp.tool()( get_mobile_app_settings )
    mcp.tool()( get_user_token_by_mobile_secret )
    mcp.tool()( save_mobile_app_settings )
