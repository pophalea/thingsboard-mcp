import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def claim_device(device_token: str, body: Optional[str] = None) -> str:
    """
    Save claiming information (claimDevice)  # noqa: E501

Saves the information required for user to claim the device. See more info about claiming in the corresponding 'Claiming devices' platform documentation.  Example of the request payload:   ```json {"secretKey":"value", "durationMs":60000} ```  Note: both 'secretKey' and 'durationMs' is optional parameters. In case the secretKey is not specified, the empty string as a default value is used. In case the durationMs is not specified, the system parameter device.claim.duration is used.  The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.claim_device(device_token=device_token, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'claim_device'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_device_attributes(device_token: str, client_keys: str, shared_keys: str) -> str:
    """
    Get attributes (getDeviceAttributes)  # noqa: E501

Returns all attributes that belong to device. Use optional 'clientKeys' and/or 'sharedKeys' parameter to return specific attributes.   Example of the result:   ```json {  "stringKey":"value1",   "booleanKey":true,   "doubleKey":42.0,   "longKey":73,   "jsonKey": {     "someNumber": 42,     "someArray": [1,2,3],     "someNestedObject": {"key": "value"}  } } ```  The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_device_attributes(device_token=device_token, client_keys=client_keys, shared_keys=shared_keys)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_device_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_firmware(device_token: str, title: str, version: str, size: Optional[int] = None, chunk: Optional[int] = None) -> str:
    """
    Get Device Firmware (getFirmware)  # noqa: E501

Downloads the current firmware package.When the platform initiates firmware update, it informs the device by updating the 'fw_title', 'fw_version', 'fw_checksum' and 'fw_checksum_algorithm' shared attributes.The 'fw_title' and 'fw_version' parameters must be supplied in this request to double-check that the firmware that device is downloading matches the firmware it expects to download. This is important, since the administrator may change the firmware assignment while device is downloading the firmware.   Optional 'chunk' and 'size' parameters may be used to download the firmware in chunks. For example, device may request first 16 KB of firmware using 'chunk'=0 and 'size'=16384. Next 16KB using 'chunk'=1 and 'size'=16384. The last chunk should have less bytes then requested using 'size' parameter.   The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_firmware(device_token=device_token, title=title, version=version, size=size, chunk=chunk)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_firmware'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_software(device_token: str, title: str, version: str, size: Optional[int] = None, chunk: Optional[int] = None) -> str:
    """
    Get Device Software (getSoftware)  # noqa: E501

Downloads the current software package.When the platform initiates software update, it informs the device by updating the 'sw_title', 'sw_version', 'sw_checksum' and 'sw_checksum_algorithm' shared attributes.The 'sw_title' and 'sw_version' parameters must be supplied in this request to double-check that the software that device is downloading matches the software it expects to download. This is important, since the administrator may change the software assignment while device is downloading the software.   Optional 'chunk' and 'size' parameters may be used to download the software in chunks. For example, device may request first 16 KB of software using 'chunk'=0 and 'size'=16384. Next 16KB using 'chunk'=1 and 'size'=16384. The last chunk should have less bytes then requested using 'size' parameter.   The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_software(device_token=device_token, title=title, version=version, size=size, chunk=chunk)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_software'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def post_device_attributes(device_token: str, body: Optional[str] = None) -> str:
    """
    Post attributes (postDeviceAttributes)  # noqa: E501

Post client attribute updates on behalf of device.   Example of the request:   ```json {  "stringKey":"value1",   "booleanKey":true,   "doubleKey":42.0,   "longKey":73,   "jsonKey": {     "someNumber": 42,     "someArray": [1,2,3],     "someNestedObject": {"key": "value"}  } } ```  The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.post_device_attributes(device_token=device_token, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'post_device_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def post_rpc_request(device_token: str, body_json: str = None) -> str:
    """
    Send the RPC command (postRpcRequest)  # noqa: E501

Send the RPC request to server. The request payload is a JSON document that contains 'method' and 'params'. For example:  ```json {"method": "sumOnServer", "params":{"a":2, "b":2}} ```  The response contains arbitrary JSON with the RPC reply. For example:   ```json {"result": 4} ```  The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.post_rpc_request(device_token=device_token, body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'post_rpc_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def post_telemetry(device_token: str, body: Optional[str] = None) -> str:
    """
    Post time-series data (postTelemetry)  # noqa: E501

Post time-series data on behalf of device.   Example of the request: The request payload is a JSON document with three possible formats:  Simple format without timestamp. In such a case, current server time will be used:     ```json {  "stringKey":"value1",   "booleanKey":true,   "doubleKey":42.0,   "longKey":73,   "jsonKey": {     "someNumber": 42,     "someArray": [1,2,3],     "someNestedObject": {"key": "value"}  } } ```     Single JSON object with timestamp:     ```json {"ts":1634712287000,"values":{"temperature":26, "humidity":87}} ```     JSON array with timestamps:     ```json [ {"ts":1634712287000,"values":{"temperature":26, "humidity":87}},  {"ts":1634712588000,"values":{"temperature":25, "humidity":88}} ] ```  The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.post_telemetry(device_token=device_token, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'post_telemetry'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def provision_device(body: Optional[str] = None) -> str:
    """
    Provision new device (provisionDevice)  # noqa: E501

Exchange the provision request to the device credentials. See more info about provisioning in the corresponding 'Device provisioning' platform documentation.Requires valid JSON request with the following format:   ```json {   "deviceName": "NEW_DEVICE_NAME",   "provisionDeviceKey": "u7piawkboq8v32dmcmpp",   "provisionDeviceSecret": "jpmwdn8ptlswmf4m29bw" } ```  Where 'deviceName' is the name of enw or existing device which depends on the provisioning strategy. The 'provisionDeviceKey' and 'provisionDeviceSecret' matches info configured in one of the existing device profiles. The result of the successful call is the JSON object that contains new credentials:  ```json {   "credentialsType":"ACCESS_TOKEN",   "credentialsValue":"DEVICE_ACCESS_TOKEN",   "status":"SUCCESS" } ```    # noqa: E501
    """
    try:
        client = get_client()
        result = client.provision_device(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'provision_device'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def reply_to_command(device_token: str, request_id: int, body: Optional[str] = None) -> str:
    """
    Reply to RPC commands (replyToCommand)  # noqa: E501

Replies to server originated RPC command identified by 'requestId' parameter. The response is arbitrary JSON.  The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.reply_to_command(device_token=device_token, request_id=request_id, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'reply_to_command'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def subscribe_to_attributes(device_token: str, timeout: Optional[int] = None) -> str:
    """
    Subscribe to attribute updates (subscribeToAttributes) (Deprecated)  # noqa: E501

Subscribes to client and shared scope attribute updates using http long polling. Deprecated, since long polling is resource and network consuming. Consider using MQTT or CoAP protocol for light-weight real-time updates.   The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.subscribe_to_attributes(device_token=device_token, timeout=timeout)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'subscribe_to_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def subscribe_to_commands(device_token: str, timeout: Optional[int] = None) -> str:
    """
    Subscribe to RPC commands (subscribeToCommands) (Deprecated)  # noqa: E501

Subscribes to RPC commands using http long polling. Deprecated, since long polling is resource and network consuming. Consider using MQTT or CoAP protocol for light-weight real-time updates.   The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.subscribe_to_commands(device_token=device_token, timeout=timeout)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'subscribe_to_commands'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( claim_device )
    mcp.tool()( get_device_attributes )
    mcp.tool()( get_firmware )
    mcp.tool()( get_software )
    mcp.tool()( post_device_attributes )
    mcp.tool()( post_rpc_request )
    mcp.tool()( post_telemetry )
    mcp.tool()( provision_device )
    mcp.tool()( reply_to_command )
    mcp.tool()( subscribe_to_attributes )
    mcp.tool()( subscribe_to_commands )
