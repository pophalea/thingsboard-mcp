import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def tenant_has_white_label_read() -> str:
    """
    tenantHasWhiteLabelRead  # noqa: E501
    """
    try:
        client = get_client()
        result = client.tenant_has_white_label_read()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'tenant_has_white_label_read'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def tenant_has_white_label_write() -> str:
    """
    tenantHasWhiteLabelWrite  # noqa: E501
    """
    try:
        client = get_client()
        result = client.tenant_has_white_label_write()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'tenant_has_white_label_write'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def tenant_white_labeling_allowed() -> str:
    """
    tenantWhiteLabelingAllowed  # noqa: E501
    """
    try:
        client = get_client()
        result = client.tenant_white_labeling_allowed()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'tenant_white_labeling_allowed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( tenant_has_white_label_read )
    mcp.tool()( tenant_has_white_label_write )
    mcp.tool()( tenant_white_labeling_allowed )
