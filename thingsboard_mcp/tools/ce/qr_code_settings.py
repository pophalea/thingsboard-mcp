import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def get_qr_code_settings() -> str:
    """
    Get Mobile application settings (getMobileAppSettings)  # noqa: E501

The response payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_qr_code_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_qr_code_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_qr_code_settings(body_json: str) -> str:
    """
    Create Or Update the Mobile application settings (saveMobileAppSettings)  # noqa: E501

The request payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_qr_code_settings(body=deserialize_param(body_json, 'QrCodeSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_qr_code_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( get_qr_code_settings )
    mcp.tool()( save_qr_code_settings )
