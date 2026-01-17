import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def handle_one_way_device_rpc_request(device_id_json: str, body: Optional[str] = None) -> str:
    """
    Send one-way RPC request (handleOneWayDeviceRPCRequest)  # noqa: E501

Deprecated. See 'Rpc V 2 Controller' instead.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.handle_one_way_device_rpc_request(device_id=deserialize_param(device_id_json, 'DeviceId'), body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'handle_one_way_device_rpc_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def handle_two_way_device_rpc_request(device_id_json: str, body_json: str = None) -> str:
    """
    Send two-way RPC request (handleTwoWayDeviceRPCRequest)  # noqa: E501

Deprecated. See 'Rpc V 2 Controller' instead.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.handle_two_way_device_rpc_request(device_id=deserialize_param(device_id_json, 'DeviceId'), body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'handle_two_way_device_rpc_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( handle_one_way_device_rpc_request )
    mcp.tool()( handle_two_way_device_rpc_request )
