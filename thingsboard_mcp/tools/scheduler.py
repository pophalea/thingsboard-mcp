import json
from typing import Optional
from .shared import get_client, deserialize_param, format_response, ApiException


def delete_scheduler_event(scheduler_event_id_json: str) -> str:
    """
    Delete Scheduler Event (deleteSchedulerEvent)  # noqa: E501

Deletes the scheduler event. Referencing non-existing Scheduler Event Id will cause 'Not Found' error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str scheduler_event_id: A string value representing the scheduler id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_scheduler_event(scheduler_event_id=deserialize_param(scheduler_event_id_json, 'SchedulerEventId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_scheduler_event'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def enable_scheduler_event(scheduler_event_id_json: str, enabled_value: bool) -> str:
    """
    Enable or disable Scheduler Event (enableSchedulerEvent)  # noqa: E501

Updates scheduler event with enabled = true/false. Scheduler Event extends Scheduler Event Info object and adds 'configuration' - a JSON structure of scheduler event configuration. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str scheduler_event_id: A string value representing the scheduler id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param bool enabled_value: Enabled or disabled scheduler (required)
:return: SchedulerEvent
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.enable_scheduler_event(scheduler_event_id=deserialize_param(scheduler_event_id_json, 'SchedulerEventId'), enabled_value=enabled_value)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'enable_scheduler_event'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_all_scheduler_events(edge_id_json: str) -> str:
    """
    Get All Edge Scheduler Events (getAllSchedulerEvents)  # noqa: E501

Fetch the list of Scheduler Event Info objects based on the provided Edge entity. Scheduler Event extends Scheduler Event Info object and adds 'configuration' - a JSON structure of scheduler event configuration. See the 'Model' tab of the Response Class for more details. Scheduler Events allows you to schedule various types of events with flexible schedule configuration. Scheduler fires configured scheduler events according to their schedule. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str edge_id: A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: list[SchedulerEventInfo]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_all_scheduler_events(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_all_scheduler_events'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_scheduler_event_by_id(scheduler_event_id_json: str) -> str:
    """
    Get Scheduler Event (getSchedulerEventById)  # noqa: E501

Fetch the SchedulerEvent object based on the provided scheduler event Id. Scheduler Event extends Scheduler Event Info object and adds 'configuration' - a JSON structure of scheduler event configuration. See the 'Model' tab of the Response Class for more details. Referencing non-existing Scheduler Event Id will cause 'Not Found' error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str scheduler_event_id: A string value representing the scheduler id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: SchedulerEvent
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_scheduler_event_by_id(scheduler_event_id=deserialize_param(scheduler_event_id_json, 'SchedulerEventId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_scheduler_event_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_scheduler_event_info_by_id(scheduler_event_id_json: str) -> str:
    """
    Get Scheduler Event With Customer Info (getSchedulerEventInfoById)  # noqa: E501

Fetch the SchedulerEventWithCustomerInfo object based on the provided scheduler event Id. Scheduler Event With Customer Info extends Scheduler Event Info object and adds 'customerTitle' - a String value representing the title of the customer which user created a Scheduler Event and 'customerIsPublic' - a boolean parameter that specifies if customer is public. See the 'Model' tab of the Response Class for more details. Referencing non-existing Scheduler Event Id will cause 'Not Found' error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str scheduler_event_id: A string value representing the scheduler id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: SchedulerEventWithCustomerInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_scheduler_event_info_by_id(scheduler_event_id=deserialize_param(scheduler_event_id_json, 'SchedulerEventId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_scheduler_event_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_scheduler_events(type: Optional[str] = None) -> str:
    """
    Get Scheduler Events By Type (getSchedulerEvents)  # noqa: E501

Requested scheduler events must be owned by tenant or assigned to customer which user is performing the request. Scheduler Event With Customer Info extends Scheduler Event Info object and adds 'customerTitle' - a String value representing the title of the customer which user created a Scheduler Event and 'customerIsPublic' - a boolean parameter that specifies if customer is public. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str type: A string value representing the scheduler type. For example, 'generateReport'
:return: list[SchedulerEventWithCustomerInfo]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_scheduler_events(type=type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_scheduler_events'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_scheduler_events_by_ids(scheduler_event_ids_json: str) -> str:
    """
    Get Scheduler Events By Ids (getSchedulerEventsByIds)  # noqa: E501

Requested scheduler events must be owned by tenant or assigned to customer which user is performing the request. Scheduler Events allows you to schedule various types of events with flexible schedule configuration. Scheduler fires configured scheduler events according to their schedule. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str scheduler_event_ids: A list of scheduler event ids, separated by comma ',' (required)
:return: list[SchedulerEventInfo]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_scheduler_events_by_ids(scheduler_event_ids=json.loads(scheduler_event_ids_json) if scheduler_event_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_scheduler_events_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_scheduler_event(body: Optional[str] = None) -> str:
    """
    Save Scheduler Event (saveSchedulerEvent)  # noqa: E501

Creates or Updates scheduler event. Scheduler Event extends Scheduler Event Info object and adds 'configuration' - a JSON structure of scheduler event configuration. See the 'Model' tab of the Response Class for more details. When creating scheduler event, platform generates scheduler event Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created scheduler event id will be present in the response. Specify existing scheduler event id to update the scheduler event. Referencing non-existing scheduler event Id will cause 'Not Found' error. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Scheduler Event entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param SchedulerEvent body:
:return: SchedulerEvent
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_scheduler_event(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_scheduler_event'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    """Register tools with FastMCP server"""
    mcp.tool()( delete_scheduler_event )
    mcp.tool()( enable_scheduler_event )
    mcp.tool()( get_all_scheduler_events )
    mcp.tool()( get_scheduler_event_by_id )
    mcp.tool()( get_scheduler_event_info_by_id )
    mcp.tool()( get_scheduler_events )
    mcp.tool()( get_scheduler_events_by_ids )
    mcp.tool()( save_scheduler_event )
