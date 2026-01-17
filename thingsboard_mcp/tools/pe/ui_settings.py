import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def get_help_base_url() -> str:
    """
    Get UI help base url (getHelpBaseUrl)  # noqa: E501

Get UI help base url used to fetch help assets. The actual value of the base url is configurable in the system configuration file.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_help_base_url()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_help_base_url'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( get_help_base_url )
