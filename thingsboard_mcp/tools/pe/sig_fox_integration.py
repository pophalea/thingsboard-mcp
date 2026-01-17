import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def sig_fox_process_request_v11_post11(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v11_post11(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sig_fox_process_request_v11_post11'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def sig_fox_process_request_v3_delete3(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_delete3(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sig_fox_process_request_v3_delete3'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def sig_fox_process_request_v3_get3(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_get3(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sig_fox_process_request_v3_get3'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def sig_fox_process_request_v3_head3(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_head3(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sig_fox_process_request_v3_head3'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def sig_fox_process_request_v3_options3(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_options3(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sig_fox_process_request_v3_options3'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def sig_fox_process_request_v3_patch3(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_patch3(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sig_fox_process_request_v3_patch3'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def sig_fox_process_request_v3_put3(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_put3(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sig_fox_process_request_v3_put3'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( sig_fox_process_request_v11_post11 )
    mcp.tool()( sig_fox_process_request_v3_delete3 )
    mcp.tool()( sig_fox_process_request_v3_get3 )
    mcp.tool()( sig_fox_process_request_v3_head3 )
    mcp.tool()( sig_fox_process_request_v3_options3 )
    mcp.tool()( sig_fox_process_request_v3_patch3 )
    mcp.tool()( sig_fox_process_request_v3_put3 )
