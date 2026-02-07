import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def clear_events_post(entity_id_json: str, body_json: str = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    Clear Events (clearEvents)  # noqa: E501

Clears events by filter for specified entity.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.clear_events_post(entity_id=deserialize_param(entity_id_json, 'EntityId'), body=deserialize_param(body_json, 'EntityIdClearstartTimeendTimeBody'), start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'clear_events_post'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_events_get(entity_id_json: str, tenant_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    Get Events (Deprecated)  # noqa: E501

Returns a page of events for specified entity. Deprecated and will be removed in next minor release. The call was deprecated to improve the performance of the system. Current implementation will return 'Lifecycle' events only. Use 'Get events by type' or 'Get events by filter' instead. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_events_get(entity_id=deserialize_param(entity_id_json, 'EntityId'), tenant_id=deserialize_param(tenant_id_json, 'TenantId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_events_get'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_events_post(tenant_id_json: str, page_size: int, page: int, entity_id_json: str, body_json: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    Get Events by event filter (getEvents)  # noqa: E501

Returns a page of events for the chosen entity by specifying the event filter. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # Event Filter Definition  5 different eventFilter objects could be set for different event types. The eventType field is required. Others are optional. If some of them are set, the filtering will be applied according to them. See the examples below for all the fields used for each event type filtering.   Note,   * 'server' - string value representing the server name, identifier or ip address where the platform is running;  * 'errorStr' - the case insensitive 'contains' filter based on error message.  ## Error Event Filter  ```json {    "eventType":"ERROR",    "server":"ip-172-31-24-152",    "method":"onClusterEventMsg",    "errorStr":"Error Message" } ```   * 'method' - string value representing the method name when the error happened.  ## Lifecycle Event Filter  ```json {    "eventType":"LC_EVENT",    "server":"ip-172-31-24-152",    "event":"STARTED",    "status":"Success",    "errorStr":"Error Message" } ```   * 'event' - string value representing the lifecycle event type;  * 'status' - string value representing status of the lifecycle event.  ## Statistics Event Filter  ```json {    "eventType":"STATS",    "server":"ip-172-31-24-152",    "messagesProcessed":10,    "errorsOccurred":5 } ```   * 'messagesProcessed' - the minimum number of successfully processed messages;  * 'errorsOccurred' - the minimum number of errors occurred during messages processing.  ## Debug Rule Node Event Filter  ```json {    "eventType":"DEBUG_RULE_NODE",    "msgDirectionType":"IN",    "server":"ip-172-31-24-152",    "dataSearch":"humidity",    "metadataSearch":"deviceName",    "entityName":"DEVICE",    "relationType":"Success",    "entityId":"de9d54a0-2b7a-11ec-a3cc-23386423d98f",    "msgType":"POST_TELEMETRY_REQUEST",    "isError":"false",    "errorStr":"Error Message" } ```  ## Debug Rule Chain Event Filter  ```json {    "eventType":"DEBUG_RULE_CHAIN",    "msgDirectionType":"IN",    "server":"ip-172-31-24-152",    "dataSearch":"humidity",    "metadataSearch":"deviceName",    "entityName":"DEVICE",    "relationType":"Success",    "entityId":"de9d54a0-2b7a-11ec-a3cc-23386423d98f",    "msgType":"POST_TELEMETRY_REQUEST",    "isError":"false",    "errorStr":"Error Message" } ```   * 'msgDirectionType' - string value representing msg direction type (incoming to entity or outcoming from entity);  * 'dataSearch' - the case insensitive 'contains' filter based on data (key and value) for the message;  * 'metadataSearch' - the case insensitive 'contains' filter based on metadata (key and value) for the message;  * 'entityName' - string value representing the entity type;  * 'relationType' - string value representing the type of message routing;  * 'entityId' - string value representing the entity id in the event body (originator of the message);  * 'msgType' - string value representing the message type;  * 'isError' - boolean value to filter the errors.    # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    Expected JSON Structure (EventFilter):
    - `not_empty` (bool)
    - `event_type` (str)
    """
    try:
        client = get_client()
        result = client.get_events_post(tenant_id=deserialize_param(tenant_id_json, 'TenantId'), page_size=page_size, page=page, entity_id=deserialize_param(entity_id_json, 'EntityId'), body=deserialize_param(body_json, 'EventFilter'), text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_events_post'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_events_v1_get1(entity_id_json: str, event_type: str, tenant_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    Get Events by type (getEvents)  # noqa: E501

Returns a page of events for specified entity by specifying event type. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_events_v1_get1(entity_id=deserialize_param(entity_id_json, 'EntityId'), event_type=event_type, tenant_id=deserialize_param(tenant_id_json, 'TenantId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_events_v1_get1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( clear_events_post )
    mcp.tool()( get_events_get )
    mcp.tool()( get_events_post )
    mcp.tool()( get_events_v1_get1 )
