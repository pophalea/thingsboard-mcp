import json
from typing import Optional
from .shared import get_client, deserialize_param, format_response, ApiException


def delete_entity_attributes(entity_id_json: str, scope: str, keys: str) -> str:
    """
    Delete entity attributes (deleteEntityAttributes)  # noqa: E501

Delete entity attributes using provided Entity Id, scope and a list of keys. Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str scope: A string value representing the attributes scope. For example, 'SERVER_SCOPE'. (required)
:param str keys: A string value representing the comma-separated list of attributes keys. For example, 'active,inactivityAlarmTime'. (required)
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_entity_attributes(entity_id=deserialize_param(entity_id_json, 'EntityId'), scope=scope, keys=keys)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_entity_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_entity_timeseries(entity_id_json: str, keys: str, delete_all_data_for_keys: Optional[str] = None, start_ts: Optional[str] = None, end_ts: Optional[str] = None, delete_latest: Optional[str] = None, rewrite_latest_if_deleted: Optional[str] = None) -> str:
    """
    Delete entity time-series data (deleteEntityTimeseries)  # noqa: E501

Delete time-series for selected entity based on entity id, entity type and keys. Use 'deleteAllDataForKeys' to delete all time-series data. Use 'startTs' and 'endTs' to specify time-range instead.  Use 'deleteLatest' to delete latest value (stored in separate table for performance) if the value's timestamp matches the time-range.  Use 'rewriteLatestIfDeleted' to rewrite latest value (stored in separate table for performance) if the value's timestamp matches the time-range and 'deleteLatest' param is true. The replacement value will be fetched from the 'time-series' table, and its timestamp will be the most recent one before the defined time-range.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str keys: A string value representing the comma-separated list of telemetry keys. If keys are not selected, the result will return all latest timeseries. For example, 'temperature,humidity'. (required)
:param bool delete_all_data_for_keys: A boolean value to specify if should be deleted all data for selected keys or only data that are in the selected time range.
:param int start_ts: A long value representing the start timestamp of removal time range in milliseconds.
:param int end_ts: A long value representing the end timestamp of removal time range in milliseconds.
:param bool delete_latest: If the parameter is set to true, the latest telemetry can be removed, otherwise, in case that parameter is set to false the latest value will not removed.
:param bool rewrite_latest_if_deleted: If the parameter is set to true, the latest telemetry will be rewritten in case that current latest value was removed, otherwise, in case that parameter is set to false the new latest value will not set.
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_entity_timeseries(entity_id=deserialize_param(entity_id_json, 'EntityId'), keys=keys, delete_all_data_for_keys=delete_all_data_for_keys, start_ts=start_ts, end_ts=end_ts, delete_latest=delete_latest, rewrite_latest_if_deleted=rewrite_latest_if_deleted)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_entity_timeseries'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_all_related_edges_missing_attributes(integration_id_json: str) -> str:
    """
    Find missing attributes for all related edges (findAllRelatedEdgesMissingAttributes)  # noqa: E501

Returns list of attribute names of all related edges that are missing in the integration configuration.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str integration_id: A string value representing the integration id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.find_all_related_edges_missing_attributes(integration_id=deserialize_param(integration_id_json, 'IntegrationId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_all_related_edges_missing_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_edge_missing_attributes_get(edge_id_json: str, integration_ids: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_edge_missing_attributes_get(edge_id=deserialize_param(edge_id_json, 'EdgeId'), integration_ids=integration_ids)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_edge_missing_attributes_get'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_entity_timeseries_and_attributes_keys_by_query(timeseries: bool, attributes: bool, body: str, scope: Optional[str] = None) -> str:
    """
    Find Entity Keys by Query  # noqa: E501

Uses entity data query (see 'Find Entity Data by Query') to find first 100 entities. Then fetch and return all unique time-series and/or attribute keys. Used mostly for UI hints.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param bool timeseries: Include all unique time-series keys to the result. (required)
:param bool attributes: Include all unique attribute keys to the result. (required)
:param EntityDataQuery body:
:param str scope: A string value representing the attributes scope. For example, 'SERVER_SCOPE'.
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.find_entity_timeseries_and_attributes_keys_by_query(timeseries=timeseries, attributes=attributes, body=body, scope=scope)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_entity_timeseries_and_attributes_keys_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_attribute_keys(entity_id_json: str) -> str:
    """
    Get all attribute keys (getAttributeKeys)  # noqa: E501

Returns a set of unique attribute key names for the selected entity. The response will include merged key names set for all attribute scopes:   * SERVER_SCOPE - supported for all entity types;  * CLIENT_SCOPE - supported for devices;  * SHARED_SCOPE - supported for devices.   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_attribute_keys(entity_id=deserialize_param(entity_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_attribute_keys'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_attribute_keys_by_scope(entity_id_json: str, scope: str) -> str:
    """
    Get all attribute keys by scope (getAttributeKeysByScope)  # noqa: E501

Returns a set of unique attribute key names for the selected entity and attributes scope:    * SERVER_SCOPE - supported for all entity types;  * CLIENT_SCOPE - supported for devices;  * SHARED_SCOPE - supported for devices.   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str scope: A string value representing the attributes scope. For example, 'SERVER_SCOPE'. (required)
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_attribute_keys_by_scope(entity_id=deserialize_param(entity_id_json, 'EntityId'), scope=scope)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_attribute_keys_by_scope'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_attributes(entity_id_json: str, keys: Optional[str] = None) -> str:
    """
    Get attributes (getAttributes)  # noqa: E501

Returns all attributes that belong to specified entity. Use optional 'keys' parameter to return specific attributes.  Example of the result:   ```json [   {"key": "stringAttributeKey", "value": "value", "lastUpdateTs": 1609459200000},   {"key": "booleanAttributeKey", "value": false, "lastUpdateTs": 1609459200001},   {"key": "doubleAttributeKey", "value": 42.2, "lastUpdateTs": 1609459200002},   {"key": "longKeyExample", "value": 73, "lastUpdateTs": 1609459200003},   {"key": "jsonKeyExample",     "value": {       "someNumber": 42,       "someArray": [1,2,3],       "someNestedObject": {"key": "value"}     },     "lastUpdateTs": 1609459200004   } ] ```   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str keys: A string value representing the comma-separated list of attributes keys. For example, 'active,inactivityAlarmTime'.
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_attributes(entity_id=deserialize_param(entity_id_json, 'EntityId'), keys=keys)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_attributes_by_scope(entity_id_json: str, scope: str, keys: Optional[str] = None) -> str:
    """
    Get attributes by scope (getAttributesByScope)  # noqa: E501

Returns all attributes of a specified scope that belong to specified entity. List of possible attribute scopes depends on the entity type:    * SERVER_SCOPE - supported for all entity types;  * SHARED_SCOPE - supported for devices;  * CLIENT_SCOPE - supported for devices.   Use optional 'keys' parameter to return specific attributes.  Example of the result:   ```json [   {"key": "stringAttributeKey", "value": "value", "lastUpdateTs": 1609459200000},   {"key": "booleanAttributeKey", "value": false, "lastUpdateTs": 1609459200001},   {"key": "doubleAttributeKey", "value": 42.2, "lastUpdateTs": 1609459200002},   {"key": "longKeyExample", "value": 73, "lastUpdateTs": 1609459200003},   {"key": "jsonKeyExample",     "value": {       "someNumber": 42,       "someArray": [1,2,3],       "someNestedObject": {"key": "value"}     },     "lastUpdateTs": 1609459200004   } ] ```   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str scope: A string value representing the attributes scope. For example, 'SERVER_SCOPE'. (required)
:param str keys: A string value representing the comma-separated list of attributes keys. For example, 'active,inactivityAlarmTime'.
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_attributes_by_scope(entity_id=deserialize_param(entity_id_json, 'EntityId'), scope=scope, keys=keys)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_attributes_by_scope'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_attributes_keys(device_profile_id: Optional[str] = None) -> str:
    """
    Get attribute keys (getAttributesKeys)  # noqa: E501

Get a set of unique attribute keys used by devices that belong to specified profile. If profile is not set returns a list of unique keys among all profiles. The call is used for auto-complete in the UI forms. The implementation limits the number of devices that participate in search to 100 as a trade of between accurate results and time-consuming queries.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str device_profile_id: A string value representing the device profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
:return: list[str]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_attributes_keys(device_profile_id=device_profile_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_attributes_keys'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_latest_timeseries(entity_id_json: str, keys: Optional[str] = None, use_strict_data_types: Optional[str] = None) -> str:
    """
    Get latest time-series value (getLatestTimeseries)  # noqa: E501

Returns all time-series that belong to specified entity. Use optional 'keys' parameter to return specific time-series. The result is a JSON object. The format of the values depends on the 'useStrictDataTypes' parameter. By default, all time-series values are converted to strings:   ```json {   "stringTsKey": [{ "value": "value", "ts": 1609459200000}],   "booleanTsKey": [{ "value": "false", "ts": 1609459200000}],   "doubleTsKey": [{ "value": "42.2", "ts": 1609459200000}],   "longTsKey": [{ "value": "73", "ts": 1609459200000}],   "jsonTsKey": [{ "value": "{\\"someNumber\\": 42,\\"someArray\\": [1,2,3],\\"someNestedObject\\": {\\"key\\": \\"value\\"}}", "ts": 1609459200000}] }  ```   However, it is possible to request the values without conversion ('useStrictDataTypes'=true):   ```json {   "stringTsKey": [{ "value": "value", "ts": 1609459200000}],   "booleanTsKey": [{ "value": false, "ts": 1609459200000}],   "doubleTsKey": [{ "value": 42.2, "ts": 1609459200000}],   "longTsKey": [{ "value": 73, "ts": 1609459200000}],   "jsonTsKey": [{      "value": {       "someNumber": 42,       "someArray": [1,2,3],       "someNestedObject": {"key": "value"}     },      "ts": 1609459200000}] }  ```   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str keys: A string value representing the comma-separated list of telemetry keys. If keys are not selected, the result will return all latest timeseries. For example, 'temperature,humidity'.
:param bool use_strict_data_types: Enables/disables conversion of telemetry values to strings. Conversion is enabled by default. Set parameter to 'true' in order to disable the conversion.
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_latest_timeseries(entity_id=deserialize_param(entity_id_json, 'EntityId'), keys=keys, use_strict_data_types=use_strict_data_types)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_latest_timeseries'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_timeseries(entity_id_json: str, keys: str, start_ts: int, end_ts: int, interval_type: Optional[str] = None, interval: Optional[str] = None, time_zone: Optional[str] = None, limit: Optional[str] = None, agg: Optional[str] = None, order_by: Optional[str] = None, use_strict_data_types: Optional[str] = None) -> str:
    """
    Get time-series data (getTimeseries)  # noqa: E501

Returns a range of time-series values for specified entity. Returns not aggregated data by default. Use aggregation function ('agg') and aggregation interval ('interval') to enable aggregation of the results on the database / server side. The aggregation is generally more efficient then fetching all records.   ```json {   "temperature": [     {       "value": 36.7,       "ts": 1609459200000     },     {       "value": 36.6,       "ts": 1609459201000     }   ] } ```  Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str keys: A string value representing the comma-separated list of telemetry keys. (required)
:param int start_ts: A long value representing the start timestamp of the time range in milliseconds, UTC. (required)
:param int end_ts: A long value representing the end timestamp of the time range in milliseconds, UTC. (required)
:param str interval_type: A string value representing the type fo the interval.
:param int interval: A long value representing the aggregation interval range in milliseconds.
:param str time_zone: A string value representing the timezone that will be used to calculate exact timestamps for 'WEEK', 'WEEK_ISO', 'MONTH' and 'QUARTER' interval types.
:param int limit: An integer value that represents a max number of timeseries data points to fetch. This parameter is used only in the case if 'agg' parameter is set to 'NONE'.
:param str agg: A string value representing the aggregation function. If the interval is not specified, 'agg' parameter will use 'NONE' value.
:param str order_by: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:param bool use_strict_data_types: Enables/disables conversion of telemetry values to strings. Conversion is enabled by default. Set parameter to 'true' in order to disable the conversion.
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_timeseries(entity_id=deserialize_param(entity_id_json, 'EntityId'), keys=keys, start_ts=start_ts, end_ts=end_ts, interval_type=interval_type, interval=interval, time_zone=time_zone, limit=limit, agg=agg, order_by=order_by, use_strict_data_types=use_strict_data_types)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_timeseries'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_timeseries_keys(device_profile_id: Optional[str] = None) -> str:
    """
    Get time-series keys (getTimeseriesKeys)  # noqa: E501

Get a set of unique time-series keys used by devices that belong to specified profile. If profile is not set returns a list of unique keys among all profiles. The call is used for auto-complete in the UI forms. The implementation limits the number of devices that participate in search to 100 as a trade of between accurate results and time-consuming queries.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str device_profile_id: A string value representing the device profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
:return: list[str]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_timeseries_keys(device_profile_id=device_profile_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_timeseries_keys'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_timeseries_keys_v1(entity_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_timeseries_keys_v1(entity_id=deserialize_param(entity_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_timeseries_keys_v1'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def post_telemetry(device_token: str, body: Optional[str] = None) -> str:
    """
    Post time-series data (postTelemetry)  # noqa: E501

Post time-series data on behalf of device.   Example of the request: The request payload is a JSON document with three possible formats:  Simple format without timestamp. In such a case, current server time will be used:     ```json {  "stringKey":"value1",   "booleanKey":true,   "doubleKey":42.0,   "longKey":73,   "jsonKey": {     "someNumber": 42,     "someArray": [1,2,3],     "someNestedObject": {"key": "value"}  } } ```     Single JSON object with timestamp:     ```json {"ts":1634712287000,"values":{"temperature":26, "humidity":87}} ```     JSON array with timestamps:     ```json [ {"ts":1634712287000,"values":{"temperature":26, "humidity":87}},  {"ts":1634712588000,"values":{"temperature":25, "humidity":88}} ] ```  The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str device_token: Your device access token. (required)
:param str body:
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.post_telemetry(device_token=device_token, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'post_telemetry'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_entity_attributes_v1(entity_id_json: str, scope: str, body_json: str = None) -> str:
    """
    Save entity attributes (saveEntityAttributesV1)  # noqa: E501

Creates or updates the entity attributes based on Entity Id and the specified attribute scope.  List of possible attribute scopes depends on the entity type:    * SERVER_SCOPE - supported for all entity types;  * SHARED_SCOPE - supported for devices.  The request payload is a JSON object with key-value format of attributes to create or update. For example:  ```json {  "stringKey":"value1",   "booleanKey":true,   "doubleKey":42.0,   "longKey":73,   "jsonKey": {     "someNumber": 42,     "someArray": [1,2,3],     "someNestedObject": {"key": "value"}  } } ``` Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str scope: A string value representing the attributes scope. For example, 'SERVER_SCOPE'. (required)
:param JsonNode body:
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_entity_attributes_v1(entity_id=deserialize_param(entity_id_json, 'EntityId'), scope=scope, body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_entity_attributes_v1'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_entity_attributes_v2(entity_id_json: str, scope: str, body_json: str = None) -> str:
    """
    Save entity attributes (saveEntityAttributesV2)  # noqa: E501

Creates or updates the entity attributes based on Entity Id and the specified attribute scope.  List of possible attribute scopes depends on the entity type:    * SERVER_SCOPE - supported for all entity types;  * SHARED_SCOPE - supported for devices.  The request payload is a JSON object with key-value format of attributes to create or update. For example:  ```json {  "stringKey":"value1",   "booleanKey":true,   "doubleKey":42.0,   "longKey":73,   "jsonKey": {     "someNumber": 42,     "someArray": [1,2,3],     "someNestedObject": {"key": "value"}  } } ``` Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str scope: A string value representing the attributes scope. For example, 'SERVER_SCOPE'. (required)
:param JsonNode body:
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_entity_attributes_v2(entity_id=deserialize_param(entity_id_json, 'EntityId'), scope=scope, body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_entity_attributes_v2'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_entity_telemetry(entity_id_json: str, scope: str, body: Optional[str] = None) -> str:
    """
    Save or update time-series data (saveEntityTelemetry)  # noqa: E501

Creates or updates the entity time-series data based on the Entity Id and request payload.The request payload is a JSON document with three possible formats:  Simple format without timestamp. In such a case, current server time will be used:   ```json {"temperature": 26} ```   Single JSON object with timestamp:   ```json {"ts":1634712287000,"values":{"temperature":26, "humidity":87}} ```   JSON array with timestamps:   ```json [{"ts":1634712287000,"values":{"temperature":26, "humidity":87}}, {"ts":1634712588000,"values":{"temperature":25, "humidity":88}}] ```   The scope parameter is not used in the API call implementation but should be specified whatever value because it is used as a path variable. Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str scope: Value is deprecated, reserved for backward compatibility and not used in the API call implementation. Specify any scope for compatibility (required)
:param str body:
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_entity_telemetry(entity_id=deserialize_param(entity_id_json, 'EntityId'), scope=scope, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_entity_telemetry'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_entity_telemetry_with_ttl(entity_id_json: str, scope: str, ttl: int, body: Optional[str] = None) -> str:
    """
    Save or update time-series data with TTL (saveEntityTelemetryWithTTL)  # noqa: E501

Creates or updates the entity time-series data based on the Entity Id and request payload.The request payload is a JSON document with three possible formats:  Simple format without timestamp. In such a case, current server time will be used:   ```json {"temperature": 26} ```   Single JSON object with timestamp:   ```json {"ts":1634712287000,"values":{"temperature":26, "humidity":87}} ```   JSON array with timestamps:   ```json [{"ts":1634712287000,"values":{"temperature":26, "humidity":87}}, {"ts":1634712588000,"values":{"temperature":25, "humidity":88}}] ```   The scope parameter is not used in the API call implementation but should be specified whatever value because it is used as a path variable.   The ttl parameter takes affect only in case of Cassandra DB.Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str scope: Value is deprecated, reserved for backward compatibility and not used in the API call implementation. Specify any scope for compatibility (required)
:param str ttl: A long value representing TTL (Time to Live) parameter. (required)
:param str body:
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_entity_telemetry_with_ttl(entity_id=deserialize_param(entity_id_json, 'EntityId'), scope=scope, ttl=ttl, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_entity_telemetry_with_ttl'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def subscribe_to_attributes(device_token: str, timeout: Optional[str] = None) -> str:
    """
    Subscribe to attribute updates (subscribeToAttributes) (Deprecated)  # noqa: E501

Subscribes to client and shared scope attribute updates using http long polling. Deprecated, since long polling is resource and network consuming. Consider using MQTT or CoAP protocol for light-weight real-time updates.   The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str device_token: Your device access token. (required)
:param int timeout: Optional timeout of the long poll. Typically less then 60 seconds, since limited on the server side.
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.subscribe_to_attributes(device_token=device_token, timeout=timeout)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'subscribe_to_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    """Register tools with FastMCP server"""
    mcp.tool()( delete_entity_attributes )
    mcp.tool()( delete_entity_timeseries )
    mcp.tool()( find_all_related_edges_missing_attributes )
    mcp.tool()( find_edge_missing_attributes_get )
    mcp.tool()( find_entity_timeseries_and_attributes_keys_by_query )
    mcp.tool()( get_attribute_keys )
    mcp.tool()( get_attribute_keys_by_scope )
    mcp.tool()( get_attributes )
    mcp.tool()( get_attributes_by_scope )
    mcp.tool()( get_attributes_keys )
    mcp.tool()( get_latest_timeseries )
    mcp.tool()( get_timeseries )
    mcp.tool()( get_timeseries_keys )
    mcp.tool()( get_timeseries_keys_v1 )
    mcp.tool()( post_telemetry )
    mcp.tool()( save_entity_attributes_v1 )
    mcp.tool()( save_entity_attributes_v2 )
    mcp.tool()( save_entity_telemetry )
    mcp.tool()( save_entity_telemetry_with_ttl )
    mcp.tool()( subscribe_to_attributes )
