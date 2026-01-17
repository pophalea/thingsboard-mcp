import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def thing_park_process_request_tpe_delete(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequestTPE  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_delete(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_tpe_delete'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def thing_park_process_request_tpe_get(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequestTPE  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_get(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_tpe_get'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def thing_park_process_request_tpe_head(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequestTPE  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_head(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_tpe_head'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def thing_park_process_request_tpe_options(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequestTPE  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_options(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_tpe_options'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def thing_park_process_request_tpe_patch(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequestTPE  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_patch(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_tpe_patch'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def thing_park_process_request_tpe_post(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequestTPE  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_post(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_tpe_post'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def thing_park_process_request_tpe_put(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequestTPE  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_put(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_tpe_put'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def thing_park_process_request_v13_post13(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v13_post13(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_v13_post13'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def thing_park_process_request_v5_delete5(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_delete5(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_v5_delete5'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def thing_park_process_request_v5_get5(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_get5(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_v5_get5'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def thing_park_process_request_v5_head5(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_head5(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_v5_head5'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def thing_park_process_request_v5_options5(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_options5(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_v5_options5'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def thing_park_process_request_v5_patch5(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_patch5(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_v5_patch5'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def thing_park_process_request_v5_put5(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_put5(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_v5_put5'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( thing_park_process_request_tpe_delete )
    mcp.tool()( thing_park_process_request_tpe_get )
    mcp.tool()( thing_park_process_request_tpe_head )
    mcp.tool()( thing_park_process_request_tpe_options )
    mcp.tool()( thing_park_process_request_tpe_patch )
    mcp.tool()( thing_park_process_request_tpe_post )
    mcp.tool()( thing_park_process_request_tpe_put )
    mcp.tool()( thing_park_process_request_v13_post13 )
    mcp.tool()( thing_park_process_request_v5_delete5 )
    mcp.tool()( thing_park_process_request_v5_get5 )
    mcp.tool()( thing_park_process_request_v5_head5 )
    mcp.tool()( thing_park_process_request_v5_options5 )
    mcp.tool()( thing_park_process_request_v5_patch5 )
    mcp.tool()( thing_park_process_request_v5_put5 )
