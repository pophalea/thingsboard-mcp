import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def assign_scheduler_event_to_edge(edge_id_json: str, scheduler_event_id_json: str) -> str:
    """
    Assign scheduler event to edge (assignSchedulerEventToEdge)  # noqa: E501

Creates assignment of an existing scheduler event to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment scheduler event (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once scheduler event will be delivered to edge service, it is going to be available for usage on remote edge instance.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (EdgeId):
    - `id` (str)
    - `entity_type` (str)
    Expected JSON Structure (SchedulerEventId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.assign_scheduler_event_to_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), scheduler_event_id=deserialize_param(scheduler_event_id_json, 'SchedulerEventId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_scheduler_event_to_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_scheduler_event(scheduler_event_id_json: str) -> str:
    """
    Delete Scheduler Event (deleteSchedulerEvent)  # noqa: E501

Deletes the scheduler event. Referencing non-existing Scheduler Event Id will cause 'Not Found' error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (SchedulerEventId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.delete_scheduler_event(scheduler_event_id=deserialize_param(scheduler_event_id_json, 'SchedulerEventId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_scheduler_event'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def enable_scheduler_event(scheduler_event_id_json: str, enabled_value: bool) -> str:
    """
    Enable or disable Scheduler Event (enableSchedulerEvent)  # noqa: E501

Updates scheduler event with enabled = true/false. Scheduler Event extends Scheduler Event Info object and adds 'configuration' - a JSON structure of scheduler event configuration. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (SchedulerEventId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.enable_scheduler_event(scheduler_event_id=deserialize_param(scheduler_event_id_json, 'SchedulerEventId'), enabled_value=enabled_value)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'enable_scheduler_event'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_all_scheduler_events(edge_id_json: str) -> str:
    """
    Get All Edge Scheduler Events (getAllSchedulerEvents)  # noqa: E501

Fetch the list of Scheduler Event Info objects based on the provided Edge entity. Scheduler Event extends Scheduler Event Info object and adds 'configuration' - a JSON structure of scheduler event configuration. See the 'Model' tab of the Response Class for more details. Scheduler Events allows you to schedule various types of events with flexible schedule configuration. Scheduler fires configured scheduler events according to their schedule. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (EdgeId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_all_scheduler_events(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_all_scheduler_events'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_edge_scheduler_events(edge_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Edge Scheduler Events (getEdgeSchedulerEvents)  # noqa: E501

Returns a page of  Scheduler Events Info objects based on the provided Edge entity. Scheduler Event extends Scheduler Event Info object and adds 'configuration' - a JSON structure of scheduler event configuration. See the 'Model' tab of the Response Class for more details. Scheduler Events allows you to schedule various types of events with flexible schedule configuration. Scheduler fires configured scheduler events according to their schedule. See the 'Model' tab of the Response Class for more details. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (EdgeId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_edge_scheduler_events(edge_id=deserialize_param(edge_id_json, 'EdgeId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_scheduler_events'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_scheduler_event_by_id(scheduler_event_id_json: str) -> str:
    """
    Get Scheduler Event (getSchedulerEventById)  # noqa: E501

Fetch the SchedulerEvent object based on the provided scheduler event Id. Scheduler Event extends Scheduler Event Info object and adds 'configuration' - a JSON structure of scheduler event configuration. See the 'Model' tab of the Response Class for more details. Referencing non-existing Scheduler Event Id will cause 'Not Found' error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (SchedulerEventId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_scheduler_event_by_id(scheduler_event_id=deserialize_param(scheduler_event_id_json, 'SchedulerEventId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_scheduler_event_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_scheduler_event_info_by_id(scheduler_event_id_json: str) -> str:
    """
    Get Scheduler Event With Customer Info (getSchedulerEventInfoById)  # noqa: E501

Fetch the SchedulerEventWithCustomerInfo object based on the provided scheduler event Id. Scheduler Event With Customer Info extends Scheduler Event Info object and adds 'customerTitle' - a String value representing the title of the customer which user created a Scheduler Event and 'customerIsPublic' - a boolean parameter that specifies if customer is public. See the 'Model' tab of the Response Class for more details. Referencing non-existing Scheduler Event Id will cause 'Not Found' error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (SchedulerEventId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_scheduler_event_info_by_id(scheduler_event_id=deserialize_param(scheduler_event_id_json, 'SchedulerEventId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_scheduler_event_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_scheduler_events(type: Optional[str] = None) -> str:
    """
    Get Scheduler Events By Type (getSchedulerEvents)  # noqa: E501

Requested scheduler events must be owned by tenant or assigned to customer which user is performing the request. Scheduler Event With Customer Info extends Scheduler Event Info object and adds 'customerTitle' - a String value representing the title of the customer which user created a Scheduler Event and 'customerIsPublic' - a boolean parameter that specifies if customer is public. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_scheduler_events(type=type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_scheduler_events'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_scheduler_events_by_ids(scheduler_event_ids_json: str) -> str:
    """
    Get Scheduler Events By Ids (getSchedulerEventsByIds)  # noqa: E501

Requested scheduler events must be owned by tenant or assigned to customer which user is performing the request. Scheduler Events allows you to schedule various types of events with flexible schedule configuration. Scheduler fires configured scheduler events according to their schedule. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_scheduler_events_by_ids(scheduler_event_ids=json.loads(scheduler_event_ids_json) if scheduler_event_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_scheduler_events_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_scheduler_event(body_json: str = None) -> str:
    """
    Save Scheduler Event (saveSchedulerEvent)  # noqa: E501

Creates or Updates scheduler event. Scheduler Event extends Scheduler Event Info object and adds 'configuration' - a JSON structure of scheduler event configuration. See the 'Model' tab of the Response Class for more details. When creating scheduler event, platform generates scheduler event Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created scheduler event id will be present in the response. Specify existing scheduler event id to update the scheduler event. Referencing non-existing scheduler event Id will cause 'Not Found' error. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Scheduler Event entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (SchedulerEvent):
    - `id` (SchedulerEventId)
    - `created_time` (int)
    - `tenant_id` (TenantId)
    - `customer_id` (CustomerId)
    - `originator_id` (EntityId)
    - `name` (str)
    - `type` (str)
    - `enabled` (bool)
    - `version` (int)
    - `configuration` (JsonNode)
    - `additional_info` (JsonNode)
    - `owner_id` (EntityId)
    - `schedule` (JsonNode)
    """
    try:
        client = get_client()
        result = client.save_scheduler_event(body=deserialize_param(body_json, 'SchedulerEvent'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_scheduler_event'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def unassign_scheduler_event_from_edge(edge_id_json: str, scheduler_event_id_json: str) -> str:
    """
    Unassign scheduler event from edge (unassignSchedulerEventFromEdge)  # noqa: E501

Clears assignment of the scheduler event to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove entity group (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove entity group and entities inside this group locally.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (EdgeId):
    - `id` (str)
    - `entity_type` (str)
    Expected JSON Structure (SchedulerEventId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.unassign_scheduler_event_from_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), scheduler_event_id=deserialize_param(scheduler_event_id_json, 'SchedulerEventId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unassign_scheduler_event_from_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( assign_scheduler_event_to_edge )
    mcp.tool()( delete_scheduler_event )
    mcp.tool()( enable_scheduler_event )
    mcp.tool()( get_all_scheduler_events )
    mcp.tool()( get_edge_scheduler_events )
    mcp.tool()( get_scheduler_event_by_id )
    mcp.tool()( get_scheduler_event_info_by_id )
    mcp.tool()( get_scheduler_events )
    mcp.tool()( get_scheduler_events_by_ids )
    mcp.tool()( save_scheduler_event )
    mcp.tool()( unassign_scheduler_event_from_edge )
