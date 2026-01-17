import json
import tb_rest_client.models.models_pe as models
from ...shared import get_client, deserialize_param, format_response, ApiException


def delete_entity_attributes(entity_id_json: str, scope: str, keys: str) -> str:
    """
    No description available.
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
    No description available.
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

def find_all_related_edges_missing_attributes(integration_id_json: str) -> str:
    """
    Find missing attributes for all related edges (findAllRelatedEdgesMissingAttributes)  # noqa: E501

Returns list of attribute names of all related edges that are missing in the integration configuration.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_all_related_edges_missing_attributes(integration_id=deserialize_param(integration_id_json, 'IntegrationId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_all_related_edges_missing_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_edge_missing_attributes_get(edge_id_json: str, integration_ids: str) -> str:
    """
    Find edge missing attributes for assigned integrations (findEdgeMissingAttributes)  # noqa: E501

Returns list of edge attribute names that are missing in assigned integrations.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_edge_missing_attributes_get(edge_id=deserialize_param(edge_id_json, 'EdgeId'), integration_ids=integration_ids)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_edge_missing_attributes_get'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_entity_timeseries_and_attributes_keys_by_query(timeseries: bool, attributes: bool, body_json: str, scope: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_entity_timeseries_and_attributes_keys_by_query(timeseries=timeseries, attributes=attributes, body=deserialize_param(body_json, 'EntityDataQuery'), scope=scope)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_entity_timeseries_and_attributes_keys_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_attribute_keys(entity_id_json: str) -> str:
    """
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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

def get_attributes_keys(device_profile_id_json: str) -> str:
    """
    Get attribute keys (getAttributesKeys)  # noqa: E501

Get a set of unique attribute keys used by devices that belong to specified profile. If profile is not set returns a list of unique keys among all profiles. The call is used for auto-complete in the UI forms. The implementation limits the number of devices that participate in search to 100 as a trade of between accurate results and time-consuming queries.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_attributes_keys(device_profile_id=deserialize_param(device_profile_id_json, 'DeviceProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_attributes_keys'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_latest_timeseries(entity_id_json: str, keys: Optional[str] = None, use_strict_data_types: Optional[bool] = None) -> str:
    """
    No description available.
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
    No description available.
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

def get_timeseries_keys(device_profile_id_json: str) -> str:
    """
    Get time-series keys (getTimeseriesKeys)  # noqa: E501

Get a set of unique time-series keys used by devices that belong to specified profile. If profile is not set returns a list of unique keys among all profiles. The call is used for auto-complete in the UI forms. The implementation limits the number of devices that participate in search to 100 as a trade of between accurate results and time-consuming queries.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_timeseries_keys(device_profile_id=deserialize_param(device_profile_id_json, 'DeviceProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_timeseries_keys'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
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
            return "PERMISSION DENIED: You do not have permission to perform 'get_timeseries_keys_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def post_telemetry(device_token: str, body: Optional[str] = None) -> str:
    """
    No description available.
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

def save_entity_attributes_v1(entity_id_json: str, scope: str, body_json: str = None) -> str:
    """
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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

def subscribe_to_attributes(device_token: str, timeout: Optional[int] = None) -> str:
    """
    No description available.
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

def register(mcp):
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
