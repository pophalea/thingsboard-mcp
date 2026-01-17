import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_device_attributes(device_id_json: str, scope: str, keys: str) -> str:
    """
    Delete device attributes (deleteDeviceAttributes)  # noqa: E501

Delete device attributes using provided Device Id, scope and a list of keys. Referencing a non-existing Device Id will cause an error  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_device_attributes(device_id=deserialize_param(device_id_json, 'DeviceId'), scope=scope, keys=keys)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_device_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_entity_attributes(entity_id_json: str, scope: str, keys: str) -> str:
    """
    Delete entity attributes (deleteEntityAttributes)  # noqa: E501

Delete entity attributes using provided Entity Id, scope and a list of keys. Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_entity_attributes(entity_id=deserialize_param(entity_id_json, 'EntityId'), scope=scope, keys=keys)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_entity_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_entity_timeseries(entity_id_json: str, keys: str, delete_all_data_for_keys: Optional[bool] = None, start_ts: Optional[int] = None, end_ts: Optional[int] = None, delete_latest: Optional[bool] = None, rewrite_latest_if_deleted: Optional[bool] = None) -> str:
    """
    Delete entity time-series data (deleteEntityTimeseries)  # noqa: E501

Delete time-series for selected entity based on entity id, entity type and keys. Use 'deleteAllDataForKeys' to delete all time-series data. Use 'startTs' and 'endTs' to specify time-range instead.  Use 'deleteLatest' to delete latest value (stored in separate table for performance) if the value's timestamp matches the time-range.  Use 'rewriteLatestIfDeleted' to rewrite latest value (stored in separate table for performance) if the value's timestamp matches the time-range and 'deleteLatest' param is true. The replacement value will be fetched from the 'time-series' table, and its timestamp will be the most recent one before the defined time-range.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_entity_timeseries(entity_id=deserialize_param(entity_id_json, 'EntityId'), keys=keys, delete_all_data_for_keys=delete_all_data_for_keys, start_ts=start_ts, end_ts=end_ts, delete_latest=delete_latest, rewrite_latest_if_deleted=rewrite_latest_if_deleted)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_entity_timeseries'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_attribute_keys(entity_id_json: str) -> str:
    """
    Get all attribute keys (getAttributeKeys)  # noqa: E501

Returns a set of unique attribute key names for the selected entity. The response will include merged key names set for all attribute scopes:   * SERVER_SCOPE - supported for all entity types;  * CLIENT_SCOPE - supported for devices;  * SHARED_SCOPE - supported for devices.   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_attribute_keys(entity_id=deserialize_param(entity_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_attribute_keys'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_attribute_keys_by_scope(entity_id_json: str, scope: str) -> str:
    """
    Get all attribute keys by scope (getAttributeKeysByScope)  # noqa: E501

Returns a set of unique attribute key names for the selected entity and attributes scope:    * SERVER_SCOPE - supported for all entity types;  * CLIENT_SCOPE - supported for devices;  * SHARED_SCOPE - supported for devices.   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_attribute_keys_by_scope(entity_id=deserialize_param(entity_id_json, 'EntityId'), scope=scope)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_attribute_keys_by_scope'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_attributes(entity_id_json: str, keys: Optional[str] = None) -> str:
    """
    Get attributes (getAttributes)  # noqa: E501

Returns all attributes that belong to specified entity. Use optional 'keys' parameter to return specific attributes.  Example of the result:   ```json [   {"key": "stringAttributeKey", "value": "value", "lastUpdateTs": 1609459200000},   {"key": "booleanAttributeKey", "value": false, "lastUpdateTs": 1609459200001},   {"key": "doubleAttributeKey", "value": 42.2, "lastUpdateTs": 1609459200002},   {"key": "longKeyExample", "value": 73, "lastUpdateTs": 1609459200003},   {"key": "jsonKeyExample",     "value": {       "someNumber": 42,       "someArray": [1,2,3],       "someNestedObject": {"key": "value"}     },     "lastUpdateTs": 1609459200004   } ] ```   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_attributes(entity_id=deserialize_param(entity_id_json, 'EntityId'), keys=keys)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_attributes_by_scope(entity_id_json: str, scope: str, keys: Optional[str] = None) -> str:
    """
    Get attributes by scope (getAttributesByScope)  # noqa: E501

Returns all attributes of a specified scope that belong to specified entity. List of possible attribute scopes depends on the entity type:    * SERVER_SCOPE - supported for all entity types;  * SHARED_SCOPE - supported for devices;  * CLIENT_SCOPE - supported for devices.   Use optional 'keys' parameter to return specific attributes.  Example of the result:   ```json [   {"key": "stringAttributeKey", "value": "value", "lastUpdateTs": 1609459200000},   {"key": "booleanAttributeKey", "value": false, "lastUpdateTs": 1609459200001},   {"key": "doubleAttributeKey", "value": 42.2, "lastUpdateTs": 1609459200002},   {"key": "longKeyExample", "value": 73, "lastUpdateTs": 1609459200003},   {"key": "jsonKeyExample",     "value": {       "someNumber": 42,       "someArray": [1,2,3],       "someNestedObject": {"key": "value"}     },     "lastUpdateTs": 1609459200004   } ] ```   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_attributes_by_scope(entity_id=deserialize_param(entity_id_json, 'EntityId'), scope=scope, keys=keys)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_attributes_by_scope'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_latest_timeseries(entity_id_json: str, keys: Optional[str] = None, use_strict_data_types: Optional[bool] = None) -> str:
    """
    Get latest time-series value (getLatestTimeseries)  # noqa: E501

Returns all time-series that belong to specified entity. Use optional 'keys' parameter to return specific time-series. The result is a JSON object. The format of the values depends on the 'useStrictDataTypes' parameter. By default, all time-series values are converted to strings:   ```json {   "stringTsKey": [{ "value": "value", "ts": 1609459200000}],   "booleanTsKey": [{ "value": "false", "ts": 1609459200000}],   "doubleTsKey": [{ "value": "42.2", "ts": 1609459200000}],   "longTsKey": [{ "value": "73", "ts": 1609459200000}],   "jsonTsKey": [{ "value": "{\\"someNumber\\": 42,\\"someArray\\": [1,2,3],\\"someNestedObject\\": {\\"key\\": \\"value\\"}}", "ts": 1609459200000}] }  ```   However, it is possible to request the values without conversion ('useStrictDataTypes'=true):   ```json {   "stringTsKey": [{ "value": "value", "ts": 1609459200000}],   "booleanTsKey": [{ "value": false, "ts": 1609459200000}],   "doubleTsKey": [{ "value": 42.2, "ts": 1609459200000}],   "longTsKey": [{ "value": 73, "ts": 1609459200000}],   "jsonTsKey": [{      "value": {       "someNumber": 42,       "someArray": [1,2,3],       "someNestedObject": {"key": "value"}     },      "ts": 1609459200000}] }  ```   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_latest_timeseries(entity_id=deserialize_param(entity_id_json, 'EntityId'), keys=keys, use_strict_data_types=use_strict_data_types)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_latest_timeseries'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_timeseries(entity_id_json: str, keys: str, start_ts: int, end_ts: int, interval_type: Optional[str] = None, interval: Optional[int] = None, time_zone: Optional[str] = None, limit: Optional[int] = None, agg: Optional[str] = None, order_by: Optional[str] = None, use_strict_data_types: Optional[bool] = None) -> str:
    """
    Get time-series data (getTimeseries)  # noqa: E501

Returns a range of time-series values for specified entity. Returns not aggregated data by default. Use aggregation function ('agg') and aggregation interval ('interval') to enable aggregation of the results on the database / server side. The aggregation is generally more efficient then fetching all records.   ```json {   "temperature": [     {       "value": 36.7,       "ts": 1609459200000     },     {       "value": 36.6,       "ts": 1609459201000     }   ] } ```  Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_timeseries(entity_id=deserialize_param(entity_id_json, 'EntityId'), keys=keys, start_ts=start_ts, end_ts=end_ts, interval_type=interval_type, interval=interval, time_zone=time_zone, limit=limit, agg=agg, order_by=order_by, use_strict_data_types=use_strict_data_types)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_timeseries'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_timeseries_keys_v1(entity_id_json: str) -> str:
    """
    Get time-series keys (getTimeseriesKeys)  # noqa: E501

Returns a set of unique time-series key names for the selected entity.   Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_timeseries_keys_v1(entity_id=deserialize_param(entity_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_timeseries_keys_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_device_attributes(device_id_json: str, scope: str, body_json: str = None) -> str:
    """
    Save device attributes (saveDeviceAttributes)  # noqa: E501

Creates or updates the device attributes based on device id and specified attribute scope. The request payload is a JSON object with key-value format of attributes to create or update. For example:  ```json {  "stringKey":"value1",   "booleanKey":true,   "doubleKey":42.0,   "longKey":73,   "jsonKey": {     "someNumber": 42,     "someArray": [1,2,3],     "someNestedObject": {"key": "value"}  } } ```   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_device_attributes(device_id=deserialize_param(device_id_json, 'DeviceId'), scope=scope, body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_device_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_entity_attributes_v1(entity_id_json: str, scope: str, body_json: str = None) -> str:
    """
    Save entity attributes (saveEntityAttributesV1)  # noqa: E501

Creates or updates the entity attributes based on Entity Id and the specified attribute scope.  List of possible attribute scopes depends on the entity type:    * SERVER_SCOPE - supported for all entity types;  * SHARED_SCOPE - supported for devices.  The request payload is a JSON object with key-value format of attributes to create or update. For example:  ```json {  "stringKey":"value1",   "booleanKey":true,   "doubleKey":42.0,   "longKey":73,   "jsonKey": {     "someNumber": 42,     "someArray": [1,2,3],     "someNestedObject": {"key": "value"}  } } ``` Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_entity_attributes_v1(entity_id=deserialize_param(entity_id_json, 'EntityId'), scope=scope, body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_entity_attributes_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_entity_attributes_v2(entity_id_json: str, scope: str, body_json: str = None) -> str:
    """
    Save entity attributes (saveEntityAttributesV2)  # noqa: E501

Creates or updates the entity attributes based on Entity Id and the specified attribute scope.  List of possible attribute scopes depends on the entity type:    * SERVER_SCOPE - supported for all entity types;  * SHARED_SCOPE - supported for devices.  The request payload is a JSON object with key-value format of attributes to create or update. For example:  ```json {  "stringKey":"value1",   "booleanKey":true,   "doubleKey":42.0,   "longKey":73,   "jsonKey": {     "someNumber": 42,     "someArray": [1,2,3],     "someNestedObject": {"key": "value"}  } } ``` Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_entity_attributes_v2(entity_id=deserialize_param(entity_id_json, 'EntityId'), scope=scope, body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_entity_attributes_v2'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_entity_telemetry(entity_id_json: str, scope: str, body_json: str = None) -> str:
    """
    Save or update time-series data (saveEntityTelemetry)  # noqa: E501

Creates or updates the entity time-series data based on the Entity Id and request payload.The request payload is a JSON document with three possible formats:  Simple format without timestamp. In such a case, current server time will be used:   ```json {"temperature": 26} ```   Single JSON object with timestamp:   ```json {"ts":1634712287000,"values":{"temperature":26, "humidity":87}} ```   JSON array with timestamps:   ```json [{"ts":1634712287000,"values":{"temperature":26, "humidity":87}}, {"ts":1634712588000,"values":{"temperature":25, "humidity":88}}] ```   The scope parameter is not used in the API call implementation but should be specified whatever value because it is used as a path variable. Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_entity_telemetry(entity_id=deserialize_param(entity_id_json, 'EntityId'), scope=scope, body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_entity_telemetry'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_entity_telemetry_with_ttl(entity_id_json: str, scope: str, ttl: int, body_json: str = None) -> str:
    """
    Save or update time-series data with TTL (saveEntityTelemetryWithTTL)  # noqa: E501

Creates or updates the entity time-series data based on the Entity Id and request payload.The request payload is a JSON document with three possible formats:  Simple format without timestamp. In such a case, current server time will be used:   ```json {"temperature": 26} ```   Single JSON object with timestamp:   ```json {"ts":1634712287000,"values":{"temperature":26, "humidity":87}} ```   JSON array with timestamps:   ```json [{"ts":1634712287000,"values":{"temperature":26, "humidity":87}}, {"ts":1634712588000,"values":{"temperature":25, "humidity":88}}] ```   The scope parameter is not used in the API call implementation but should be specified whatever value because it is used as a path variable.   The ttl parameter takes affect only in case of Cassandra DB.Referencing a non-existing entity Id or invalid entity type will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_entity_telemetry_with_ttl(entity_id=deserialize_param(entity_id_json, 'EntityId'), scope=scope, ttl=ttl, body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_entity_telemetry_with_ttl'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_device_attributes )
    mcp.tool()( delete_entity_attributes )
    mcp.tool()( delete_entity_timeseries )
    mcp.tool()( get_attribute_keys )
    mcp.tool()( get_attribute_keys_by_scope )
    mcp.tool()( get_attributes )
    mcp.tool()( get_attributes_by_scope )
    mcp.tool()( get_latest_timeseries )
    mcp.tool()( get_timeseries )
    mcp.tool()( get_timeseries_keys_v1 )
    mcp.tool()( save_device_attributes )
    mcp.tool()( save_entity_attributes_v1 )
    mcp.tool()( save_entity_attributes_v2 )
    mcp.tool()( save_entity_telemetry )
    mcp.tool()( save_entity_telemetry_with_ttl )
