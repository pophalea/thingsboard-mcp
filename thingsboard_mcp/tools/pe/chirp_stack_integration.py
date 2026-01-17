import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def chirp_stack_process_request_delete(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_delete(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'chirp_stack_process_request_delete'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def chirp_stack_process_request_get(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_get(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'chirp_stack_process_request_get'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def chirp_stack_process_request_head(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_head(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'chirp_stack_process_request_head'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def chirp_stack_process_request_options(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_options(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'chirp_stack_process_request_options'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def chirp_stack_process_request_patch(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_patch(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'chirp_stack_process_request_patch'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def chirp_stack_process_request_post(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_post(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'chirp_stack_process_request_post'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def chirp_stack_process_request_put(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_put(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'chirp_stack_process_request_put'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( chirp_stack_process_request_delete )
    mcp.tool()( chirp_stack_process_request_get )
    mcp.tool()( chirp_stack_process_request_head )
    mcp.tool()( chirp_stack_process_request_options )
    mcp.tool()( chirp_stack_process_request_patch )
    mcp.tool()( chirp_stack_process_request_post )
    mcp.tool()( chirp_stack_process_request_put )
