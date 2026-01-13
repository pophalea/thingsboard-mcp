import json
from typing import Optional
from .shared import get_client, deserialize_param, format_response, ApiException


def check_integration_connection(body: Optional[str] = None) -> str:
    """
    Check integration connectivity (checkIntegrationConnection)  # noqa: E501

Checks if the connection to the integration is established. Throws an error if the connection is not established. Example: Failed to connect to MQTT broker at host:port.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param Integration body:
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.check_integration_connection(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'check_integration_connection'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_converter(converter_id_json: str) -> str:
    """
    Delete converter (deleteConverter)  # noqa: E501

Deletes the converter and all the relations (from and to the converter). Referencing non-existing converter Id will cause an error. If the converter is associated with the integration, it will not be allowed for deletion.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str converter_id: A string value representing the converter id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_converter(converter_id=deserialize_param(converter_id_json, 'ConverterId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_converter'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_integration(integration_id_json: str) -> str:
    """
    Delete integration (deleteIntegration)  # noqa: E501

Deletes the integration and all the relations (from and to the integration). Referencing non-existing integration Id will cause an error.    Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str integration_id: A string value representing the integration id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_integration(integration_id=deserialize_param(integration_id_json, 'IntegrationId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_integration'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_converter_by_id(converter_id_json: str) -> str:
    """
    Get Converter (getConverterById)  # noqa: E501

Fetch the Converter object based on the provided Converter Id. The server checks that the converter is owned by the same tenant.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str converter_id: A string value representing the converter id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: Converter
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_converter_by_id(converter_id=deserialize_param(converter_id_json, 'ConverterId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_converter_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_converters(page_size: int, page: int, is_edge_template: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Converters (getConverters)  # noqa: E501

Returns a page of converters owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param bool is_edge_template: Fetch edge template converters
:param str text_search: The case insensitive 'startsWith' filter based on the converter name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataConverter
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_converters(page_size=page_size, page=page, is_edge_template=is_edge_template, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_converters'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_converters_by_ids(converter_ids_json: str) -> str:
    """
    Get Converters By Ids (getConvertersByIds)  # noqa: E501

Requested converters must be owned by tenant which is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str converter_ids: A list of converter ids, separated by comma ',' (required)
:return: list[Converter]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_converters_by_ids(converter_ids=json.loads(converter_ids_json) if converter_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_converters_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_downlink_converter(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get downlink converter (getDownlinkConverter)  # noqa: E501

Returns downlink converter body for the vendor, integration type and model  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str integration_type: (required)
:param str vendor_name: (required)
:param str model: (required)
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_downlink_converter(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_downlink_converter'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_downlink_converter_metadata(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get downlink converter metadata (getDownlinkConverterMetadata)  # noqa: E501

Returns downlink converter metadata for the vendor, integration type and model  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str integration_type: (required)
:param str vendor_name: (required)
:param str model: (required)
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_downlink_converter_metadata(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_downlink_converter_metadata'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_integration_by_id(integration_id_json: str) -> str:
    """
    Get Integration (getIntegrationById)  # noqa: E501

Fetch the Integration object based on the provided Integration Id. The server checks that the integration is owned by the same tenant.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str integration_id: A string value representing the integration id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: Integration
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_integration_by_id(integration_id=deserialize_param(integration_id_json, 'IntegrationId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_integration_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_integration_by_routing_key(routing_key: str) -> str:
    """
    Get Integration by Routing Key (getIntegrationByRoutingKey)  # noqa: E501

Fetch the Integration object based on the provided routing key. The server checks that the integration is owned by the same tenant.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str routing_key: A string value representing the integration routing key. For example, '542047e6-c1b2-112e-a87e-e49247c09d4b' (required)
:return: Integration
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_integration_by_routing_key(routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_integration_by_routing_key'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_integration_infos(page_size: int, page: int, is_edge_template: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Integration Infos (getIntegrationInfos)  # noqa: E501

Returns a page of integration infos owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param bool is_edge_template: Fetch edge template integrations
:param str text_search: The case insensitive 'startsWith' filter based on the integration name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataIntegrationInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_integration_infos(page_size=page_size, page=page, is_edge_template=is_edge_template, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_integration_infos'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_integrations(page_size: int, page: int, is_edge_template: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Integrations (getIntegrations)  # noqa: E501

Returns a page of integrations owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param bool is_edge_template: Fetch edge template integrations
:param str text_search: The case insensitive 'startsWith' filter based on the integration name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataIntegration
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_integrations(page_size=page_size, page=page, is_edge_template=is_edge_template, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_integrations'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_integrations_by_ids(integration_ids_json: str) -> str:
    """
    Get Integrations By Ids (getIntegrationsByIds)  # noqa: E501

Requested integrations must be owned by tenant which is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str integration_ids: A list of integration ids, separated by comma ',' (required)
:return: list[Integration]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_integrations_by_ids(integration_ids=json.loads(integration_ids_json) if integration_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_integrations_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_integrations_converters_info() -> str:
    """
    Get Integrations Converters info (getIntegrationsConvertersInfo)  # noqa: E501

Returns a JSON object containing information about existing tenant converters and converters available in library.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: dict(str, IntegrationConvertersInfo)
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_integrations_converters_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_integrations_converters_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_latest_converter_debug_input(converter_id_json: str, integration: Optional[str] = None) -> str:
    """
    Get latest debug input event (getLatestConverterDebugInput)  # noqa: E501

Returns a JSON object of the latest debug event representing the input message the converter processed.   ## Uplink Converter Debug Input Event Example  ```json {    "inContentType":"JSON",    "inContent":"{\\"temp\\":40}",    "inMetadata":"{\\"Header:sec-ch-ua\\":\\"\\\\\\"Chromium\\\\\\";v=\\\\\\"94\\\\\\", \\\\\\"Google Chrome\\\\\\";v=\\\\\\"94\\\\\\", \\\\\\";Not A Brand\\\\\\";v=\\\\\\"99\\\\\\"\\",\\"Header:user-agent\\":\\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36\\",\\"integrationName\\":\\"Integration\\",\\"Header:cookie\\":\\"GUID=zYSs8hymSwZKv8kHALKY; redirect_to=%2F; JSESSIONID=B0A7C8E481409CE7924E738DB04F62F9\\",\\"Header:sec-ch-ua-platform\\":\\"\\\\\\"Linux\\\\\\"\\",\\"Header:accept\\":\\"*/*\\",\\"Header:origin\\":\\"http://localhost:8080\\",\\"Header:sec-fetch-site\\":\\"same-origin\\",\\"Header:connection\\":\\"keep-alive\\",\\"Header:accept-encoding\\":\\"gzip, deflate, br\\",\\"Header:content-type\\":\\"application/json\\",\\"Header:content-length\\":\\"16\\",\\"Header:sec-fetch-mode\\":\\"cors\\",\\"Header:sec-ch-ua-mobile\\":\\"?0\\",\\"Header:sec-fetch-dest\\":\\"empty\\",\\"Header:host\\":\\"localhost:8080\\",\\"Header:referer\\":\\"http://localhost:8080/swagger-ui.html\\",\\"Header:accept-language\\":\\"en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,uk;q=0.6,und;q=0.5\\"}" } ```   * 'inContentType' - content type of the message received by the integration;   * 'inContent' - message data received;   * 'inMetadata' - integration metadata (e.g. headers).  ## Downlink Converter Debug Input Event Example  ```json {    "inContentType":"JSON",    "inContent":"{\\"temp\\":42,\\"humidity\\":77}",    "inMsgType":"POST_TELEMETRY_REQUEST",    "inMetadata":"{\\"data\\":\\"40\\"}",    "inIntegrationMetadata":"{\\"integrationName\\":\\"Integration\\"}" } ```   * 'inContentType' - content type of the message received by the integration;   * 'inContent' - content of the message pushed from the rule engine;   * 'inMsgType' - type of the message pushed from the rule engine;   * 'inMetadata' - content of the message metadata pushed from the rule engine;   * 'inIntegrationMetadata' - integration metadata.     Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str converter_id: A string value representing the converter id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str converter_type: A string value representing the converter type. One of the following: UPLINK, DOWNLINK
:param str integration_type: A string value representing the integration type. One of the following: APACHE_PULSAR, AWS_IOT, AWS_KINESIS, AWS_SQS, AZURE_EVENT_HUB, AZURE_IOT_HUB, AZURE_SERVICE_BUS, CHIRPSTACK, COAP, CUSTOM, HTTP, IBM_WATSON_IOT, KAFKA, LORIOT, MQTT, OCEANCONNECT, OPC_UA, PUB_SUB, RABBITMQ,  SIGFOX,  TCP,  THINGPARK,  TMOBILE_IOT_CDP,  TPE,  TTI,  TTN,  TUYA,  UDP
:param str integration_name: A string value representing the integration name. For example, 'My New Integration'
:return: JsonNode
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_latest_converter_debug_input(converter_id=deserialize_param(converter_id_json, 'ConverterId'), integration=integration)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_latest_converter_debug_input'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_uplink_converter(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get uplink converter (getUplinkConverter)  # noqa: E501

Returns uplink converter body for the vendor, integration type and model  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str integration_type: (required)
:param str vendor_name: (required)
:param str model: (required)
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_uplink_converter(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_uplink_converter'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_uplink_converter_metadata(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get uplink converter metadata (getUplinkConverterMetadata)  # noqa: E501

Returns uplink converter metadata for the vendor, integration type and model  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str integration_type: (required)
:param str vendor_name: (required)
:param str model: (required)
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_uplink_converter_metadata(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_uplink_converter_metadata'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_converter(body: Optional[str] = None) -> str:
    """
    Create Or Update Converter (saveConverter)  # noqa: E501

Create or update the Converter. When creating converter, platform generates Converter Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created converter id will be present in the response. Specify existing Converter id to update the converter. Referencing non-existing converter Id will cause 'Not Found' error. Converter name is unique in the scope of tenant.   # Converter Configuration  Converter configuration (**'configuration'** field) is the JSON object that should contain one of two possible fields: **'decoder'** or **'encoder'**. The former is used when the converter has UPLINK type, the latter is used - when DOWNLINK type. It can contain both 'decoder' and 'encoder' fields, when the correct one is specified for the appropriate converter type, another one can be set to 'null'. See the examples of each one below.   ## Uplink Converter Configuration  ***Default converter may be different, depending on integration type***.  ```json {    "decoder":"// Decode an uplink message from a buffer\\n// payload - array of bytes\\n// metadata - key/value object\\n\\n/** Decoder **/\\n\\n// decode payload to string\\nvar payloadStr = decodeToString(payload);\\n\\n// decode payload to JSON\\n// var data = decodeToJson(payload);\\n\\nvar deviceName = 'Device A';\\nvar deviceType = 'thermostat';\\nvar customerName = 'customer';\\nvar groupName = 'thermostat devices';\\nvar manufacturer = 'Example corporation';\\n// use assetName and assetType instead of deviceName and deviceType\\n// to automatically create assets instead of devices.\\n// var assetName = 'Asset A';\\n// var assetType = 'building';\\n\\n// Result object with device/asset attributes/telemetry data\\nvar result = {\\n// Use deviceName and deviceType or assetName and assetType, but not both.\\n   deviceName: deviceName,\\n   deviceType: deviceType,\\n// assetName: assetName,\\n// assetType: assetType,\\n   customerName: customerName,\\n   groupName: groupName,\\n   contentAwareAttributeKeys: ['manufacturer'],\\n   attributes: {\\n       model: 'Model A',\\n       serialNumber: 'SN111',\\n       integrationName: metadata['integrationName'],\\n       manufacturer: manufacturer\\n   },\\n   telemetry: {\\n       temperature: 42,\\n       humidity: 80,\\n       rawData: payloadStr\\n   }\\n};\\n\\n/** Helper functions **/\\n\\nfunction decodeToString(payload) {\\n   return String.fromCharCode.apply(String, payload);\\n}\\n\\nfunction decodeToJson(payload) {\\n   // covert payload to string.\\n   var str = decodeToString(payload);\\n\\n   // parse string to JSON\\n   var data = JSON.parse(str);\\n   return data;\\n}\\n\\nreturn result;",    "encoder":null } ```  Decoder field in the more readable form:  ```text // Decode an uplink message from a buffer // payload - array of bytes // metadata - key/value object  /** Decoder **/  // decode payload to string var payloadStr = decodeToString(payload);  // decode payload to JSON // var data = decodeToJson(payload);  var deviceName = 'Device A'; var deviceType = 'thermostat'; var customerName = 'customer'; var groupName = 'thermostat devices'; var manufacturer = 'Example corporation'; // use assetName and assetType instead of deviceName and deviceType // to automatically create assets instead of devices. // var assetName = 'Asset A'; // var assetType = 'building';  // Result object with device/asset attributes/telemetry data var result = { // Use deviceName and deviceType or assetName and assetType, but not both.    deviceName: deviceName,    deviceType: deviceType, // assetName: assetName, // assetType: assetType,    customerName: customerName,    groupName: groupName,    attributes: {        model: 'Model A',        serialNumber: 'SN111',        integrationName: metadata['integrationName']        manufacturer: manufacturer,    },    telemetry: {        temperature: 42,        humidity: 80,        rawData: payloadStr    } };  /** Helper functions **/  function decodeToString(payload) {    return String.fromCharCode.apply(String, payload); }  function decodeToJson(payload) {    // covert payload to string.    var str = decodeToString(payload);     // parse string to JSON    var data = JSON.parse(str);    return data; }  return result; ```  ## Downlink Converter Configuration  ```json {    "decoder":null,    "encoder":"// Encode downlink data from incoming Rule Engine message\\n\\n// msg - JSON message payload downlink message json\\n// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.\\n// metadata - list of key-value pairs with additional data about the message\\n// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter\\n\\n/** Encoder **/\\n\\nvar data = {};\\n\\n// Process data from incoming message and metadata\\n\\ndata.tempFreq = msg.temperatureUploadFrequency;\\ndata.humFreq = msg.humidityUploadFrequency;\\n\\ndata.devSerialNumber = metadata['ss_serialNumber'];\\n\\n// Result object with encoded downlink payload\\nvar result = {\\n\\n    // downlink data content type: JSON, TEXT or BINARY (base64 format)\\n    contentType: \\"JSON\\",\\n\\n    // downlink data\\n    data: JSON.stringify(data),\\n\\n    // Optional metadata object presented in key/value format\\n    metadata: {\\n            topic: metadata['deviceType']+'/'+metadata['deviceName']+'/upload'\\n    }\\n\\n};\\n\\nreturn result;" } ```  Encoder field in the more readable form:  ```text // Encode downlink data from incoming Rule Engine message  // msg - JSON message payload downlink message json // msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc. // metadata - list of key-value pairs with additional data about the message // integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter  /** Encoder **/  var data = {};  // Process data from incoming message and metadata  data.tempFreq = msg.temperatureUploadFrequency; data.humFreq = msg.humidityUploadFrequency;  data.devSerialNumber = metadata['ss_serialNumber'];  // Result object with encoded downlink payload var result = {      // downlink data content type: JSON, TEXT or BINARY (base64 format)     contentType: "JSON",      // downlink data     data: JSON.stringify(data),      // Optional metadata object presented in key/value format     metadata: {             topic: metadata['deviceType']+'/'+metadata['deviceName']+'/upload'     }  };  return result; ```  Remove 'id', 'tenantId' from the request body example (below) to create new converter entity.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param Converter body:
:return: Converter
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_converter(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_converter'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_integration(body: Optional[str] = None) -> str:
    """
    Create Or Update Integration (saveIntegration)  # noqa: E501

Create or update the Integration. When creating integration, platform generates Integration Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created integration id will be present in the response. Specify existing Integration id to update the integration. Referencing non-existing integration Id will cause 'Not Found' error. Integration configuration is validated for each type of the integration before it can be created.   # Integration Configuration  Integration configuration (**'configuration'** field) is the JSON object representing the special configuration per integration type with the connectivity fields and other important parameters dependent on the specific integration type. Let's review the configuration object for the MQTT Integration type below.   ```json {    "clientConfiguration":{       "host":"broker.hivemq.com",       "port":1883,       "cleanSession":false,       "ssl":false,       "connectTimeoutSec":10,       "clientId":"",       "maxBytesInMessage":32368,       "credentials":{          "type":"anonymous"       }    },    "downlinkTopicPattern":"${topic}",    "topicFilters":[       {          "filter":"tb/mqtt-integration-tutorial/sensors/+/temperature",          "qos":0       }    ],    "metadata":{    } } ```  Remove 'id', 'tenantId' from the request body example (below) to create new Integration entity.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param Integration body:
:return: Integration
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_integration(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_integration'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def test_down_link_converter(body_json: str = None, script_lang: Optional[str] = None) -> str:
    """
    Test converter function (testDownLinkConverter)  # noqa: E501

Returns a JSON object representing the result of the processed incoming message.   ## Request Body Example  ```json {    "metadata":{       "data":"40"    },    "msg":"{\\n    \\"temp\\": 42,\\n    \\"humidity\\": 77\\n}",    "msgType":"POST_TELEMETRY_REQUEST",    "integrationMetadata":{       "integrationName":"Integration"    },    "encoder":"// Encode downlink data from incoming Rule Engine message\\n\\n// msg - JSON message payload downlink message json\\n// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.\\n// metadata - list of key-value pairs with additional data about the message\\n// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter\\n\\n/** Encoder **/\\n\\nvar data = {};\\n\\n// Process data from incoming message and metadata\\n\\ndata.tempValue = msg.temp;\\ndata.humValue = msg.humidity;\\n\\ndata.devSerialNumber = metadata['ss_serialNumber'];\\n\\n// Result object with encoded downlink payload\\nvar result = {\\n\\n    // downlink data content type: JSON, TEXT or BINARY (base64 format)\\n    contentType: \\"JSON\\",\\n\\n    // downlink data\\n    data: JSON.stringify(data),\\n\\n    // Optional metadata object presented in key/value format\\n    metadata: {\\n            topic: metadata['deviceType']+'/'+metadata['deviceName']+'/upload'\\n    }\\n\\n};\\n\\nreturn result;" } ```   * 'metadata' - message metadata pushed from the rule engine;   * 'msg' - message data pushed from the rule engine;   * 'msgType' - type of the message pushed from the rule engine;   * 'integrationMetadata' - integration metadata object;   * 'encoder' - string representation of the encoder configuration.  ## Response Body Example  ```json {    "contentType":"JSON",    "data":"{\\"tempValue\\":42,\\"humValue\\":77}",    "metadata":{       "topic":"sensor/Temp Sensor/upload"    } } ```   * 'contentType' - downlink data content type;   * 'data' - downlink data;   * 'metadata' - optional metadata object.    # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param JsonNode body:
:param str script_lang: Script language: JS or TBEL
:return: JsonNode
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.test_down_link_converter(body=json.loads(body_json) if body_json else None, script_lang=script_lang)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'test_down_link_converter'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def test_up_link_converter(body_json: str = None, script_lang: Optional[str] = None) -> str:
    """
    Test converter function (testUpLinkConverter)  # noqa: E501

Returns a JSON object representing the result of the processed incoming message.   ## Request Body Example  ```json {    "metadata":{    },    "payload":"ewogICAgImRhdGEiOiAiZGF0YSIKfQ==",    "decoder":"// Decode an uplink message from a buffer\\n// payload - array of bytes\\n// metadata - key/value object\\n\\n/** Decoder **/\\n\\n// decode payload to string\\nvar payloadStr = decodeToString(payload);\\n\\n// decode payload to JSON\\n// var data = decodeToJson(payload);\\n\\nvar deviceName = 'Device A';\\nvar deviceType = 'thermostat';\\nvar customerName = 'customer';\\nvar groupName = 'thermostat devices';\\nvar manufacturer = 'Example corporation';\\n// use assetName and assetType instead of deviceName and deviceType\\n// to automatically create assets instead of devices.\\n// var assetName = 'Asset A';\\n// var assetType = 'building';\\n\\n// Result object with device/asset attributes/telemetry data\\nvar result = {\\n// Use deviceName and deviceType or assetName and assetType, but not both.\\n   deviceName: deviceName,\\n   deviceType: deviceType,\\n// assetName: assetName,\\n// assetType: assetType,\\n   customerName: customerName,\\n   groupName: groupName,\\n   attributes: {\\n       model: 'Model A',\\n       serialNumber: 'SN111',\\n       integrationName: metadata['integrationName']\\n       manufacturer: manufacturer\\n   },\\n   telemetry: {\\n       temperature: 42,\\n       humidity: 80,\\n       rawData: payloadStr\\n   }\\n};\\n\\n/** Helper functions **/\\n\\nfunction decodeToString(payload) {\\n   return String.fromCharCode.apply(String, payload);\\n}\\n\\nfunction decodeToJson(payload) {\\n   // covert payload to string.\\n   var str = decodeToString(payload);\\n\\n   // parse string to JSON\\n   var data = JSON.parse(str);\\n   return data;\\n}\\n\\nreturn result;" } ```   * 'metadata' - integration metadata;   * 'payload' - base64 string representation of the data;   * 'decoder' - string representation of the decoder configuration.  ## Response Body Example  ```json {    "output":"{\\"deviceName\\":\\"Device A\\",\\"deviceType\\":\\"thermostat\\",\\"customerName\\":\\"customer\\",\\"groupName\\":\\"thermostat devices\\",\\"attributes\\":{\\"model\\":\\"Model A\\",\\"serialNumber\\":\\"SN111\\"},\\"telemetry\\":{\\"temperature\\":42,\\"humidity\\":80,\\"rawData\\":\\"{\\\\n    \\\\\\"data\\\\\\": \\\\\\"data\\\\\\"\\\\n}\\"}}",    "error":"" } ```   * 'output' - string representation of the output message;   * 'error' - string representation of the error message.    # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param JsonNode body:
:param str script_lang: Script language: JS or TBEL
:return: JsonNode
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.test_up_link_converter(body=json.loads(body_json) if body_json else None, script_lang=script_lang)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'test_up_link_converter'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    """Register tools with FastMCP server"""
    mcp.tool()( check_integration_connection )
    mcp.tool()( delete_converter )
    mcp.tool()( delete_integration )
    mcp.tool()( get_converter_by_id )
    mcp.tool()( get_converters )
    mcp.tool()( get_converters_by_ids )
    mcp.tool()( get_downlink_converter )
    mcp.tool()( get_downlink_converter_metadata )
    mcp.tool()( get_integration_by_id )
    mcp.tool()( get_integration_by_routing_key )
    mcp.tool()( get_integration_infos )
    mcp.tool()( get_integrations )
    mcp.tool()( get_integrations_by_ids )
    mcp.tool()( get_integrations_converters_info )
    mcp.tool()( get_latest_converter_debug_input )
    mcp.tool()( get_uplink_converter )
    mcp.tool()( get_uplink_converter_metadata )
    mcp.tool()( save_converter )
    mcp.tool()( save_integration )
    mcp.tool()( test_down_link_converter )
    mcp.tool()( test_up_link_converter )
