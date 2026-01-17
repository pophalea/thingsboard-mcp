import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def http_check_status_get(routing_key: str, request_params_json: str, request_headers_json: str) -> str:
    """
    checkStatus  # noqa: E501
    """
    try:
        client = get_client()
        result = client.http_check_status_get(routing_key=routing_key, request_params=json.loads(request_params_json) if request_params_json else None, request_headers=json.loads(request_headers_json) if request_headers_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'http_check_status_get'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def http_process_request_v1_post1(routing_key: str, suffix: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.http_process_request_v1_post1(routing_key=routing_key, suffix=suffix)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'http_process_request_v1_post1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def http_process_request_v2_post2(routing_key: str, suffix: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.http_process_request_v2_post2(routing_key=routing_key, suffix=suffix)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'http_process_request_v2_post2'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( http_check_status_get )
    mcp.tool()( http_process_request_v1_post1 )
    mcp.tool()( http_process_request_v2_post2 )
