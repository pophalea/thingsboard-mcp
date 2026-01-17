import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_rpc(rpc_id_json: str) -> str:
    """
    Delete persistent RPC  # noqa: E501

Deletes the persistent RPC request.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_rpc(rpc_id=deserialize_param(rpc_id_json, 'RpcId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_rpc'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_persisted_rpc(rpc_id_json: str) -> str:
    """
    Get persistent RPC request  # noqa: E501

Get information about the status of the RPC call.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_persisted_rpc(rpc_id=deserialize_param(rpc_id_json, 'RpcId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_persisted_rpc'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_persisted_rpc_by_device(device_id_json: str, page_size: int, page: int, rpc_status: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get persistent RPC requests  # noqa: E501

Allows to query RPC calls for specific device using pagination.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_persisted_rpc_by_device(device_id=deserialize_param(device_id_json, 'DeviceId'), page_size=page_size, page=page, rpc_status=rpc_status, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_persisted_rpc_by_device'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def handle_one_way_device_rpc_request_v1(device_id_json: str, body: Optional[str] = None) -> str:
    """
    Send one-way RPC request  # noqa: E501

Sends the one-way remote-procedure call (RPC) request to device. Sends the one-way remote-procedure call (RPC) request to device. The RPC call is A JSON that contains the method name ('method'), parameters ('params') and multiple optional fields. See example below. We will review the properties of the RPC call one-by-one below.   ```json {   "method": "setGpio",   "params": {     "pin": 7,     "value": 1   },   "persistent": false,   "timeout": 5000 } ```  ### Server-side RPC structure  The body of server-side RPC request consists of multiple fields:  * **method** - mandatory, name of the method to distinct the RPC calls.   For example, "getCurrentTime" or "getWeatherForecast". The value of the parameter is a string. * **params** - mandatory, parameters used for processing of the request. The value is a JSON. Leave empty JSON "{}" if no parameters needed. * **timeout** - optional, value of the processing timeout in milliseconds. The default value is 10000 (10 seconds). The minimum value is 5000 (5 seconds). * **expirationTime** - optional, value of the epoch time (in milliseconds, UTC timezone). Overrides **timeout** if present. * **persistent** - optional, indicates persistent RPC. The default value is "false". * **retries** - optional, defines how many times persistent RPC will be re-sent in case of failures on the network and/or device side. * **additionalInfo** - optional, defines metadata for the persistent RPC that will be added to the persistent RPC events.  ### RPC Result In case of persistent RPC, the result of this call is 'rpcId' UUID. In case of lightweight RPC, the result of this call is either 200 OK if the message was sent to device, or 504 Gateway Timeout if device is offline.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.handle_one_way_device_rpc_request_v1(device_id=deserialize_param(device_id_json, 'DeviceId'), body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'handle_one_way_device_rpc_request_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def handle_two_way_device_rpc_request_v1(device_id_json: str, body: Optional[str] = None) -> str:
    """
    Send two-way RPC request  # noqa: E501

Sends the two-way remote-procedure call (RPC) request to device. Sends the one-way remote-procedure call (RPC) request to device. The RPC call is A JSON that contains the method name ('method'), parameters ('params') and multiple optional fields. See example below. We will review the properties of the RPC call one-by-one below.   ```json {   "method": "setGpio",   "params": {     "pin": 7,     "value": 1   },   "persistent": false,   "timeout": 5000 } ```  ### Server-side RPC structure  The body of server-side RPC request consists of multiple fields:  * **method** - mandatory, name of the method to distinct the RPC calls.   For example, "getCurrentTime" or "getWeatherForecast". The value of the parameter is a string. * **params** - mandatory, parameters used for processing of the request. The value is a JSON. Leave empty JSON "{}" if no parameters needed. * **timeout** - optional, value of the processing timeout in milliseconds. The default value is 10000 (10 seconds). The minimum value is 5000 (5 seconds). * **expirationTime** - optional, value of the epoch time (in milliseconds, UTC timezone). Overrides **timeout** if present. * **persistent** - optional, indicates persistent RPC. The default value is "false". * **retries** - optional, defines how many times persistent RPC will be re-sent in case of failures on the network and/or device side. * **additionalInfo** - optional, defines metadata for the persistent RPC that will be added to the persistent RPC events.  ### RPC Result In case of persistent RPC, the result of this call is 'rpcId' UUID. In case of lightweight RPC, the result of this call is the response from device, or 504 Gateway Timeout if device is offline.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.handle_two_way_device_rpc_request_v1(device_id=deserialize_param(device_id_json, 'DeviceId'), body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'handle_two_way_device_rpc_request_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def rpc_v2_get_persisted_rpc(rpc_id_json: str) -> str:
    """
    Get persistent RPC request  # noqa: E501

Get information about the status of the RPC call.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.rpc_v2_get_persisted_rpc(rpc_id=deserialize_param(rpc_id_json, 'RpcId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'rpc_v2_get_persisted_rpc'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_rpc )
    mcp.tool()( get_persisted_rpc )
    mcp.tool()( get_persisted_rpc_by_device )
    mcp.tool()( handle_one_way_device_rpc_request_v1 )
    mcp.tool()( handle_two_way_device_rpc_request_v1 )
    mcp.tool()( rpc_v2_get_persisted_rpc )
