import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_converter(converter_id_json: str) -> str:
    """
    Delete converter (deleteConverter)  # noqa: E501

Deletes the converter and all the relations (from and to the converter). Referencing non-existing converter Id will cause an error. If the converter is associated with the integration, it will not be allowed for deletion.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_converter(converter_id=deserialize_param(converter_id_json, 'ConverterId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_converter'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_converter_by_id(converter_id_json: str) -> str:
    """
    Get Converter (getConverterById)  # noqa: E501

Fetch the Converter object based on the provided Converter Id. The server checks that the converter is owned by the same tenant.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_converter_by_id(converter_id=deserialize_param(converter_id_json, 'ConverterId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_converter_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_converters(page_size: int, page: int, is_edge_template: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Converters (getConverters)  # noqa: E501

Returns a page of converters owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_converters(page_size=page_size, page=page, is_edge_template=is_edge_template, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_converters'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_converters_by_ids(converter_ids_json: str) -> str:
    """
    Get Converters By Ids (getConvertersByIds)  # noqa: E501

Requested converters must be owned by tenant which is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_converters_by_ids(converter_ids=json.loads(converter_ids_json) if converter_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_converters_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_latest_converter_debug_input(converter_id_json: str, integration_json: str = None) -> str:
    """
    Get latest debug input event (getLatestConverterDebugInput)  # noqa: E501

Returns a JSON object of the latest debug event representing the input message the converter processed.   ## Uplink Converter Debug Input Event Example  ```json {    "inContentType":"JSON",    "inContent":"{\\"temp\\":40}",    "inMetadata":"{\\"Header:sec-ch-ua\\":\\"\\\\\\"Chromium\\\\\\";v=\\\\\\"94\\\\\\", \\\\\\"Google Chrome\\\\\\";v=\\\\\\"94\\\\\\", \\\\\\";Not A Brand\\\\\\";v=\\\\\\"99\\\\\\"\\",\\"Header:user-agent\\":\\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36\\",\\"integrationName\\":\\"Integration\\",\\"Header:cookie\\":\\"GUID=zYSs8hymSwZKv8kHALKY; redirect_to=%2F; JSESSIONID=B0A7C8E481409CE7924E738DB04F62F9\\",\\"Header:sec-ch-ua-platform\\":\\"\\\\\\"Linux\\\\\\"\\",\\"Header:accept\\":\\"*/*\\",\\"Header:origin\\":\\"http://localhost:8080\\",\\"Header:sec-fetch-site\\":\\"same-origin\\",\\"Header:connection\\":\\"keep-alive\\",\\"Header:accept-encoding\\":\\"gzip, deflate, br\\",\\"Header:content-type\\":\\"application/json\\",\\"Header:content-length\\":\\"16\\",\\"Header:sec-fetch-mode\\":\\"cors\\",\\"Header:sec-ch-ua-mobile\\":\\"?0\\",\\"Header:sec-fetch-dest\\":\\"empty\\",\\"Header:host\\":\\"localhost:8080\\",\\"Header:referer\\":\\"http://localhost:8080/swagger-ui.html\\",\\"Header:accept-language\\":\\"en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,uk;q=0.6,und;q=0.5\\"}" } ```   * 'inContentType' - content type of the message received by the integration;   * 'inContent' - message data received;   * 'inMetadata' - integration metadata (e.g. headers).  ## Downlink Converter Debug Input Event Example  ```json {    "inContentType":"JSON",    "inContent":"{\\"temp\\":42,\\"humidity\\":77}",    "inMsgType":"POST_TELEMETRY_REQUEST",    "inMetadata":"{\\"data\\":\\"40\\"}",    "inIntegrationMetadata":"{\\"integrationName\\":\\"Integration\\"}" } ```   * 'inContentType' - content type of the message received by the integration;   * 'inContent' - content of the message pushed from the rule engine;   * 'inMsgType' - type of the message pushed from the rule engine;   * 'inMetadata' - content of the message metadata pushed from the rule engine;   * 'inIntegrationMetadata' - integration metadata.     Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_latest_converter_debug_input(converter_id=deserialize_param(converter_id_json, 'ConverterId'), integration=deserialize_param(integration_json, 'Integration'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_latest_converter_debug_input'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_converter(body_json: str = None) -> str:
    """
    Create Or Update Converter (saveConverter)  # noqa: E501

Create or update the Converter. When creating converter, platform generates Converter Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created converter id will be present in the response. Specify existing Converter id to update the converter. Referencing non-existing converter Id will cause 'Not Found' error. Converter name is unique in the scope of tenant.   # Converter Configuration  Converter configuration (**'configuration'** field) is the JSON object that should contain one of two possible fields: **'decoder'** or **'encoder'**. The former is used when the converter has UPLINK type, the latter is used - when DOWNLINK type. It can contain both 'decoder' and 'encoder' fields, when the correct one is specified for the appropriate converter type, another one can be set to 'null'. See the examples of each one below.   ## Uplink Converter Configuration  ***Default converter may be different, depending on integration type***.  ```json {    "decoder":"// Decode an uplink message from a buffer\\n// payload - array of bytes\\n// metadata - key/value object\\n\\n/** Decoder **/\\n\\n// decode payload to string\\nvar payloadStr = decodeToString(payload);\\n\\n// decode payload to JSON\\n// var data = decodeToJson(payload);\\n\\nvar deviceName = 'Device A';\\nvar deviceType = 'thermostat';\\nvar customerName = 'customer';\\nvar groupName = 'thermostat devices';\\nvar manufacturer = 'Example corporation';\\n// use assetName and assetType instead of deviceName and deviceType\\n// to automatically create assets instead of devices.\\n// var assetName = 'Asset A';\\n// var assetType = 'building';\\n\\n// Result object with device/asset attributes/telemetry data\\nvar result = {\\n// Use deviceName and deviceType or assetName and assetType, but not both.\\n   deviceName: deviceName,\\n   deviceType: deviceType,\\n// assetName: assetName,\\n// assetType: assetType,\\n   customerName: customerName,\\n   groupName: groupName,\\n   contentAwareAttributeKeys: ['manufacturer'],\\n   attributes: {\\n       model: 'Model A',\\n       serialNumber: 'SN111',\\n       integrationName: metadata['integrationName'],\\n       manufacturer: manufacturer\\n   },\\n   telemetry: {\\n       temperature: 42,\\n       humidity: 80,\\n       rawData: payloadStr\\n   }\\n};\\n\\n/** Helper functions **/\\n\\nfunction decodeToString(payload) {\\n   return String.fromCharCode.apply(String, payload);\\n}\\n\\nfunction decodeToJson(payload) {\\n   // covert payload to string.\\n   var str = decodeToString(payload);\\n\\n   // parse string to JSON\\n   var data = JSON.parse(str);\\n   return data;\\n}\\n\\nreturn result;",    "encoder":null } ```  Decoder field in the more readable form:  ```text // Decode an uplink message from a buffer // payload - array of bytes // metadata - key/value object  /** Decoder **/  // decode payload to string var payloadStr = decodeToString(payload);  // decode payload to JSON // var data = decodeToJson(payload);  var deviceName = 'Device A'; var deviceType = 'thermostat'; var customerName = 'customer'; var groupName = 'thermostat devices'; var manufacturer = 'Example corporation'; // use assetName and assetType instead of deviceName and deviceType // to automatically create assets instead of devices. // var assetName = 'Asset A'; // var assetType = 'building';  // Result object with device/asset attributes/telemetry data var result = { // Use deviceName and deviceType or assetName and assetType, but not both.    deviceName: deviceName,    deviceType: deviceType, // assetName: assetName, // assetType: assetType,    customerName: customerName,    groupName: groupName,    attributes: {        model: 'Model A',        serialNumber: 'SN111',        integrationName: metadata['integrationName']        manufacturer: manufacturer,    },    telemetry: {        temperature: 42,        humidity: 80,        rawData: payloadStr    } };  /** Helper functions **/  function decodeToString(payload) {    return String.fromCharCode.apply(String, payload); }  function decodeToJson(payload) {    // covert payload to string.    var str = decodeToString(payload);     // parse string to JSON    var data = JSON.parse(str);    return data; }  return result; ```  ## Downlink Converter Configuration  ```json {    "decoder":null,    "encoder":"// Encode downlink data from incoming Rule Engine message\\n\\n// msg - JSON message payload downlink message json\\n// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.\\n// metadata - list of key-value pairs with additional data about the message\\n// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter\\n\\n/** Encoder **/\\n\\nvar data = {};\\n\\n// Process data from incoming message and metadata\\n\\ndata.tempFreq = msg.temperatureUploadFrequency;\\ndata.humFreq = msg.humidityUploadFrequency;\\n\\ndata.devSerialNumber = metadata['ss_serialNumber'];\\n\\n// Result object with encoded downlink payload\\nvar result = {\\n\\n    // downlink data content type: JSON, TEXT or BINARY (base64 format)\\n    contentType: \\"JSON\\",\\n\\n    // downlink data\\n    data: JSON.stringify(data),\\n\\n    // Optional metadata object presented in key/value format\\n    metadata: {\\n            topic: metadata['deviceType']+'/'+metadata['deviceName']+'/upload'\\n    }\\n\\n};\\n\\nreturn result;" } ```  Encoder field in the more readable form:  ```text // Encode downlink data from incoming Rule Engine message  // msg - JSON message payload downlink message json // msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc. // metadata - list of key-value pairs with additional data about the message // integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter  /** Encoder **/  var data = {};  // Process data from incoming message and metadata  data.tempFreq = msg.temperatureUploadFrequency; data.humFreq = msg.humidityUploadFrequency;  data.devSerialNumber = metadata['ss_serialNumber'];  // Result object with encoded downlink payload var result = {      // downlink data content type: JSON, TEXT or BINARY (base64 format)     contentType: "JSON",      // downlink data     data: JSON.stringify(data),      // Optional metadata object presented in key/value format     metadata: {             topic: metadata['deviceType']+'/'+metadata['deviceName']+'/upload'     }  };  return result; ```  Remove 'id', 'tenantId' from the request body example (below) to create new converter entity.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_converter(body=deserialize_param(body_json, 'Converter'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_converter'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def test_down_link_converter(body_json: str = None, script_lang: Optional[str] = None) -> str:
    """
    Test converter function (testDownLinkConverter)  # noqa: E501

Returns a JSON object representing the result of the processed incoming message.   ## Request Body Example  ```json {    "metadata":{       "data":"40"    },    "msg":"{\\n    \\"temp\\": 42,\\n    \\"humidity\\": 77\\n}",    "msgType":"POST_TELEMETRY_REQUEST",    "integrationMetadata":{       "integrationName":"Integration"    },    "encoder":"// Encode downlink data from incoming Rule Engine message\\n\\n// msg - JSON message payload downlink message json\\n// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.\\n// metadata - list of key-value pairs with additional data about the message\\n// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter\\n\\n/** Encoder **/\\n\\nvar data = {};\\n\\n// Process data from incoming message and metadata\\n\\ndata.tempValue = msg.temp;\\ndata.humValue = msg.humidity;\\n\\ndata.devSerialNumber = metadata['ss_serialNumber'];\\n\\n// Result object with encoded downlink payload\\nvar result = {\\n\\n    // downlink data content type: JSON, TEXT or BINARY (base64 format)\\n    contentType: \\"JSON\\",\\n\\n    // downlink data\\n    data: JSON.stringify(data),\\n\\n    // Optional metadata object presented in key/value format\\n    metadata: {\\n            topic: metadata['deviceType']+'/'+metadata['deviceName']+'/upload'\\n    }\\n\\n};\\n\\nreturn result;" } ```   * 'metadata' - message metadata pushed from the rule engine;   * 'msg' - message data pushed from the rule engine;   * 'msgType' - type of the message pushed from the rule engine;   * 'integrationMetadata' - integration metadata object;   * 'encoder' - string representation of the encoder configuration.  ## Response Body Example  ```json {    "contentType":"JSON",    "data":"{\\"tempValue\\":42,\\"humValue\\":77}",    "metadata":{       "topic":"sensor/Temp Sensor/upload"    } } ```   * 'contentType' - downlink data content type;   * 'data' - downlink data;   * 'metadata' - optional metadata object.    # noqa: E501
    """
    try:
        client = get_client()
        result = client.test_down_link_converter(body=json.loads(body_json) if body_json else None, script_lang=script_lang)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'test_down_link_converter'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def test_up_link_converter(body_json: str = None, script_lang: Optional[str] = None) -> str:
    """
    Test converter function (testUpLinkConverter)  # noqa: E501

Returns a JSON object representing the result of the processed incoming message.   ## Request Body Example  ```json {    "metadata":{    },    "payload":"ewogICAgImRhdGEiOiAiZGF0YSIKfQ==",    "decoder":"// Decode an uplink message from a buffer\\n// payload - array of bytes\\n// metadata - key/value object\\n\\n/** Decoder **/\\n\\n// decode payload to string\\nvar payloadStr = decodeToString(payload);\\n\\n// decode payload to JSON\\n// var data = decodeToJson(payload);\\n\\nvar deviceName = 'Device A';\\nvar deviceType = 'thermostat';\\nvar customerName = 'customer';\\nvar groupName = 'thermostat devices';\\nvar manufacturer = 'Example corporation';\\n// use assetName and assetType instead of deviceName and deviceType\\n// to automatically create assets instead of devices.\\n// var assetName = 'Asset A';\\n// var assetType = 'building';\\n\\n// Result object with device/asset attributes/telemetry data\\nvar result = {\\n// Use deviceName and deviceType or assetName and assetType, but not both.\\n   deviceName: deviceName,\\n   deviceType: deviceType,\\n// assetName: assetName,\\n// assetType: assetType,\\n   customerName: customerName,\\n   groupName: groupName,\\n   attributes: {\\n       model: 'Model A',\\n       serialNumber: 'SN111',\\n       integrationName: metadata['integrationName']\\n       manufacturer: manufacturer\\n   },\\n   telemetry: {\\n       temperature: 42,\\n       humidity: 80,\\n       rawData: payloadStr\\n   }\\n};\\n\\n/** Helper functions **/\\n\\nfunction decodeToString(payload) {\\n   return String.fromCharCode.apply(String, payload);\\n}\\n\\nfunction decodeToJson(payload) {\\n   // covert payload to string.\\n   var str = decodeToString(payload);\\n\\n   // parse string to JSON\\n   var data = JSON.parse(str);\\n   return data;\\n}\\n\\nreturn result;" } ```   * 'metadata' - integration metadata;   * 'payload' - base64 string representation of the data;   * 'decoder' - string representation of the decoder configuration.  ## Response Body Example  ```json {    "output":"{\\"deviceName\\":\\"Device A\\",\\"deviceType\\":\\"thermostat\\",\\"customerName\\":\\"customer\\",\\"groupName\\":\\"thermostat devices\\",\\"attributes\\":{\\"model\\":\\"Model A\\",\\"serialNumber\\":\\"SN111\\"},\\"telemetry\\":{\\"temperature\\":42,\\"humidity\\":80,\\"rawData\\":\\"{\\\\n    \\\\\\"data\\\\\\": \\\\\\"data\\\\\\"\\\\n}\\"}}",    "error":"" } ```   * 'output' - string representation of the output message;   * 'error' - string representation of the error message.    # noqa: E501
    """
    try:
        client = get_client()
        result = client.test_up_link_converter(body=json.loads(body_json) if body_json else None, script_lang=script_lang)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'test_up_link_converter'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_converter )
    mcp.tool()( get_converter_by_id )
    mcp.tool()( get_converters )
    mcp.tool()( get_converters_by_ids )
    mcp.tool()( get_latest_converter_debug_input )
    mcp.tool()( save_converter )
    mcp.tool()( test_down_link_converter )
    mcp.tool()( test_up_link_converter )
