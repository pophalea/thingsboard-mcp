import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def get_trendz_settings() -> str:
    """
    Get Trendz Settings (getTrendzSettings)  # noqa: E501

Retrieves Trendz settings for this tenant.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_trendz_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_trendz_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_trendz_settings(body_json: str) -> str:
    """
    Save Trendz settings (saveTrendzSettings)  # noqa: E501

Saves Trendz settings for this tenant.   Here is an example of the Trendz settings: ```json {   "enabled": true,   "baseUrl": "https://some.domain.com:18888/also_necessary_prefix" } ```  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_trendz_settings(body=deserialize_param(body_json, 'TrendzSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_trendz_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( get_trendz_settings )
    mcp.tool()( save_trendz_settings )
