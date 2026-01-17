import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def t_mobile_iot_cdp_process_request_v12_post12(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v12_post12(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 't_mobile_iot_cdp_process_request_v12_post12'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def t_mobile_iot_cdp_process_request_v4_delete4(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_delete4(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 't_mobile_iot_cdp_process_request_v4_delete4'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def t_mobile_iot_cdp_process_request_v4_get4(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_get4(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 't_mobile_iot_cdp_process_request_v4_get4'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def t_mobile_iot_cdp_process_request_v4_head4(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_head4(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 't_mobile_iot_cdp_process_request_v4_head4'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def t_mobile_iot_cdp_process_request_v4_options4(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_options4(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 't_mobile_iot_cdp_process_request_v4_options4'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def t_mobile_iot_cdp_process_request_v4_patch4(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_patch4(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 't_mobile_iot_cdp_process_request_v4_patch4'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def t_mobile_iot_cdp_process_request_v4_put4(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_put4(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 't_mobile_iot_cdp_process_request_v4_put4'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( t_mobile_iot_cdp_process_request_v12_post12 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_delete4 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_get4 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_head4 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_options4 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_patch4 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_put4 )
