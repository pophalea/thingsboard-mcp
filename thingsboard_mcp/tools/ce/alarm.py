import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def ack_alarm(alarm_id_json: str) -> str:
    """
    Acknowledge Alarm (ackAlarm)  # noqa: E501

Acknowledge the Alarm. Once acknowledged, the 'ack_ts' field will be set to current timestamp and special rule chain event 'ALARM_ACK' will be generated. Referencing non-existing Alarm Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.ack_alarm(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'ack_alarm'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def assign_alarm(alarm_id_json: str, assignee_id: str) -> str:
    """
    Assign/Reassign Alarm (assignAlarm)  # noqa: E501

Assign the Alarm. Once assigned, the 'assign_ts' field will be set to current timestamp and special rule chain event 'ALARM_ASSIGNED' (or ALARM_REASSIGNED in case of assigning already assigned alarm) will be generated. Referencing non-existing Alarm Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_alarm(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'), assignee_id=assignee_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_alarm'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def clear_alarm(alarm_id_json: str) -> str:
    """
    Clear Alarm (clearAlarm)  # noqa: E501

Clear the Alarm. Once cleared, the 'clear_ts' field will be set to current timestamp and special rule chain event 'ALARM_CLEAR' will be generated. Referencing non-existing Alarm Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.clear_alarm(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'clear_alarm'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_alarm(alarm_id_json: str) -> str:
    """
    Delete Alarm (deleteAlarm)  # noqa: E501

Deletes the Alarm. Referencing non-existing Alarm Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_alarm(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_alarm'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_alarm_by_id(alarm_id_json: str) -> str:
    """
    Get Alarm (getAlarmById)  # noqa: E501

Fetch the Alarm object based on the provided Alarm Id. If the user has the authority of 'Tenant Administrator', the server checks that the originator of alarm is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the originator of alarm belongs to the customer.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_alarm_by_id(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_alarm_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_alarm_info_by_id(alarm_id_json: str) -> str:
    """
    Get Alarm Info (getAlarmInfoById)  # noqa: E501

Fetch the Alarm Info object based on the provided Alarm Id. If the user has the authority of 'Tenant Administrator', the server checks that the originator of alarm is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the originator of alarm belongs to the customer. Alarm Info is an extension of the default Alarm object that also contains name of the alarm originator.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_alarm_info_by_id(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_alarm_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_alarm_types(page_size: int, page: int, text_search: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Alarm Types (getAlarmTypes)  # noqa: E501

Returns a set of unique alarm types based on alarms that are either owned by the tenant or assigned to the customer which user is performing the request.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_alarm_types(page_size=page_size, page=page, text_search=text_search, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_alarm_types'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_alarms(entity_id_json: str, page_size: int, page: int, search_status: Optional[str] = None, status: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, fetch_originator: Optional[bool] = None, assignee_id: Optional[str] = None) -> str:
    """
    Get Alarms (getAlarms)  # noqa: E501

Returns a page of alarms for the selected entity. Specifying both parameters 'searchStatus' and 'status' at the same time will cause an error. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_alarms(entity_id=deserialize_param(entity_id_json, 'EntityId'), page_size=page_size, page=page, search_status=search_status, status=status, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time, fetch_originator=fetch_originator, assignee_id=assignee_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_alarms'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_all_alarms(page_size: int, page: int, search_status: Optional[str] = None, status: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, fetch_originator: Optional[bool] = None) -> str:
    """
    Get All Alarms (getAllAlarms)  # noqa: E501

Returns a page of alarms that belongs to the current user owner. If the user has the authority of 'Tenant Administrator', the server returns alarms that belongs to the tenant of current user. If the user has the authority of 'Customer User', the server returns alarms that belongs to the customer of current user. Specifying both parameters 'searchStatus' and 'status' at the same time will cause an error. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_all_alarms(page_size=page_size, page=page, search_status=search_status, status=status, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time, fetch_originator=fetch_originator)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_all_alarms'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_highest_alarm_severity(entity_id_json: str, search_status: Optional[str] = None, status: Optional[str] = None, assignee_id: Optional[str] = None) -> str:
    """
    Get Highest Alarm Severity (getHighestAlarmSeverity)  # noqa: E501

Search the alarms by originator ('entityType' and entityId') and optional 'status' or 'searchStatus' filters and returns the highest AlarmSeverity(CRITICAL, MAJOR, MINOR, WARNING or INDETERMINATE). Specifying both parameters 'searchStatus' and 'status' at the same time will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_highest_alarm_severity(entity_id=deserialize_param(entity_id_json, 'EntityId'), search_status=search_status, status=status, assignee_id=assignee_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_highest_alarm_severity'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_alarm(body_json: str) -> str:
    """
    Create or Update Alarm (saveAlarm)  # noqa: E501

Creates or Updates the Alarm. When creating alarm, platform generates Alarm Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Alarm id will be present in the response. Specify existing Alarm id to update the alarm. Referencing non-existing Alarm Id will cause 'Not Found' error.   Platform also deduplicate the alarms based on the entity id of originator and alarm 'type'. For example, if the user or system component create the alarm with the type 'HighTemperature' for device 'Device A' the new active alarm is created. If the user tries to create 'HighTemperature' alarm for the same device again, the previous alarm will be updated (the 'end_ts' will be set to current timestamp). If the user clears the alarm (see 'Clear Alarm(clearAlarm)'), than new alarm with the same type and same device may be created. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Alarm entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_alarm(body=deserialize_param(body_json, 'Alarm'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_alarm'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def unassign_alarm(id_json: str) -> str:
    """
    Unassign Alarm (unassignAlarm)  # noqa: E501

Unassign the Alarm. Once unassigned, the 'assign_ts' field will be set to current timestamp and special rule chain event 'ALARM_UNASSIGNED' will be generated. Referencing non-existing Alarm Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.unassign_alarm(id=deserialize_param(id_json, 'AlarmId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unassign_alarm'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( ack_alarm )
    mcp.tool()( assign_alarm )
    mcp.tool()( clear_alarm )
    mcp.tool()( delete_alarm )
    mcp.tool()( get_alarm_by_id )
    mcp.tool()( get_alarm_info_by_id )
    mcp.tool()( get_alarm_types )
    mcp.tool()( get_alarms )
    mcp.tool()( get_all_alarms )
    mcp.tool()( get_highest_alarm_severity )
    mcp.tool()( save_alarm )
    mcp.tool()( unassign_alarm )
