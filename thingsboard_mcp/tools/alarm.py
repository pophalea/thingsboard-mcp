import json
from typing import Optional
from .shared import get_client, deserialize_param, format_response, ApiException


def ack_alarm(alarm_id_json: str) -> str:
    """
    Acknowledge Alarm (ackAlarm)  # noqa: E501

Acknowledge the Alarm. Once acknowledged, the 'ack_ts' field will be set to current timestamp and special rule chain event 'ALARM_ACK' will be generated. Referencing non-existing Alarm Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: AlarmInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.ack_alarm(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'ack_alarm'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def assign_alarm(alarm_id_json: str, assignee_id: str) -> str:
    """
    Assign/Reassign Alarm (assignAlarm)  # noqa: E501

Assign the Alarm. Once assigned, the 'assign_ts' field will be set to current timestamp and special rule chain event 'ALARM_ASSIGNED' (or ALARM_REASSIGNED in case of assigning already assigned alarm) will be generated. Referencing non-existing Alarm Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str assignee_id: A string value representing the user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: Alarm
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.assign_alarm(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'), assignee_id=assignee_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'assign_alarm'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def clear_alarm(alarm_id_json: str) -> str:
    """
    Clear Alarm (clearAlarm)  # noqa: E501

Clear the Alarm. Once cleared, the 'clear_ts' field will be set to current timestamp and special rule chain event 'ALARM_CLEAR' will be generated. Referencing non-existing Alarm Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: AlarmInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.clear_alarm(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'clear_alarm'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def count_alarms_by_query(body_json: str) -> str:
    """
    Count Alarms by Query (countAlarmsByQuery)  # noqa: E501

Returns the number of alarms that match the query definition.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param AlarmCountQuery body:
:return: int
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.count_alarms_by_query(body=deserialize_param(body_json, 'AlarmCountQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'count_alarms_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_alarm(alarm_id_json: str) -> str:
    """
    Delete Alarm (deleteAlarm)  # noqa: E501

Deletes the Alarm. Referencing non-existing Alarm Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: bool
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_alarm(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_alarm'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_alarm_comment(alarm_id_json: str, comment_id_json: str) -> str:
    """
    Delete Alarm comment (deleteAlarmComment)  # noqa: E501

Deletes the Alarm comment. Referencing non-existing Alarm comment Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str comment_id: A string value representing the alarm comment id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_alarm_comment(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'), comment_id=deserialize_param(comment_id_json, 'AlarmCommentId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_alarm_comment'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_alarm_data_by_query(body: Optional[str] = None) -> str:
    """
    Find Alarms by Query  # noqa: E501

This method description defines how Alarm Data Query extends the Entity Data Query. See method 'Find Entity Data by Query' first to get the info about 'Entity Data Query'.   The platform will first search the entities that match the entity and key filters. Then, the platform will use 'Alarm Page Link' to filter the alarms related to those entities. Finally, platform fetch the properties of alarm that are defined in the **'alarmFields'** and combine them with the other entity, attribute and latest time-series fields to return the result.    See example of the alarm query below. The query will search first 100 active alarms with type 'Temperature Alarm' or 'Fire Alarm' for any device with current temperature > 0. The query will return combination of the entity fields: name of the device, device model and latest temperature reading and alarms fields: createdTime, type, severity and status:   ```json {   "entityFilter": {     "type": "entityType",     "resolveMultiple": true,     "entityType": "DEVICE"   },   "pageLink": {     "page": 0,     "pageSize": 100,     "textSearch": null,     "searchPropagatedAlarms": false,     "statusList": [       "ACTIVE"     ],     "severityList": [       "CRITICAL",       "MAJOR"     ],     "typeList": [       "Temperature Alarm",       "Fire Alarm"     ],     "sortOrder": {       "key": {         "key": "createdTime",         "type": "ALARM_FIELD"       },       "direction": "DESC"     },     "timeWindow": 86400000   },   "keyFilters": [     {       "key": {         "type": "TIME_SERIES",         "key": "temperature"       },       "valueType": "NUMERIC",       "predicate": {         "operation": "GREATER",         "value": {           "defaultValue": 0,           "dynamicValue": null         },         "type": "NUMERIC"       }     }   ],   "alarmFields": [     {       "type": "ALARM_FIELD",       "key": "createdTime"     },     {       "type": "ALARM_FIELD",       "key": "type"     },     {       "type": "ALARM_FIELD",       "key": "severity"     },     {       "type": "ALARM_FIELD",       "key": "status"     }   ],   "entityFields": [     {       "type": "ENTITY_FIELD",       "key": "name"     }   ],   "latestValues": [     {       "type": "ATTRIBUTE",       "key": "model"     },     {       "type": "TIME_SERIES",       "key": "temperature"     }   ] } ```  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param AlarmDataQuery body:
:return: PageDataAlarmData
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.find_alarm_data_by_query(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_alarm_data_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_alarm_by_id(alarm_id_json: str) -> str:
    """
    Get Alarm (getAlarmById)  # noqa: E501

Fetch the Alarm object based on the provided Alarm Id. If the user has the authority of 'Tenant Administrator', the server checks that the originator of alarm is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the originator of alarm belongs to the customer.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: Alarm
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_alarm_by_id(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_alarm_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_alarm_comments(alarm_id_json: str, page_size: int, page: int, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Alarm comments (getAlarmComments)  # noqa: E501

Returns a page of alarm comments for specified alarm. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataAlarmCommentInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_alarm_comments(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'), page_size=page_size, page=page, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_alarm_comments'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_alarm_info_by_id(alarm_id_json: str) -> str:
    """
    Get Alarm Info (getAlarmInfoById)  # noqa: E501

Fetch the Alarm Info object based on the provided Alarm Id. If the user has the authority of 'Tenant Administrator', the server checks that the originator of alarm is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the originator of alarm belongs to the customer. Alarm Info is an extension of the default Alarm object that also contains name of the alarm originator.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: AlarmInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_alarm_info_by_id(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_alarm_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_alarm_types(page_size: int, page: int, text_search: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Alarm Types (getAlarmTypes)  # noqa: E501

Returns a set of unique alarm types based on alarms that are either owned by the tenant or assigned to the customer which user is performing the request.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on of next alarm fields: type, severity or status
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataEntitySubtype
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_alarm_types(page_size=page_size, page=page, text_search=text_search, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_alarm_types'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_alarms(entity_id_json: str, page_size: int, page: int, search_status: Optional[str] = None, status: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[str] = None, end_time: Optional[str] = None, fetch_originator: Optional[str] = None, assignee_id: Optional[str] = None) -> str:
    """
    Get Alarms (getAlarms)  # noqa: E501

Returns a page of alarms for the selected entity. Specifying both parameters 'searchStatus' and 'status' at the same time will cause an error. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str search_status: A string value representing one of the AlarmSearchStatus enumeration value
:param str status: A string value representing one of the AlarmStatus enumeration value
:param str assignee_id: A string value representing the assignee user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
:param str text_search: The case insensitive 'substring' filter based on of next alarm fields: type, severity or status
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:param int start_time: The start timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'.
:param int end_time: The end timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'.
:param bool fetch_originator: A boolean value to specify if the alarm originator name will be filled in the AlarmInfo object  field: 'originatorName' or will returns as null.
:return: PageDataAlarmInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_alarms(entity_id=deserialize_param(entity_id_json, 'EntityId'), page_size=page_size, page=page, search_status=search_status, status=status, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time, fetch_originator=fetch_originator, assignee_id=assignee_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_alarms'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_all_alarms(page_size: int, page: int, search_status: Optional[str] = None, status: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[str] = None, end_time: Optional[str] = None, fetch_originator: Optional[str] = None) -> str:
    """
    Get All Alarms (getAllAlarms)  # noqa: E501

Returns a page of alarms that belongs to the current user owner. If the user has the authority of 'Tenant Administrator', the server returns alarms that belongs to the tenant of current user. If the user has the authority of 'Customer User', the server returns alarms that belongs to the customer of current user. Specifying both parameters 'searchStatus' and 'status' at the same time will cause an error. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str search_status: A string value representing one of the AlarmSearchStatus enumeration value
:param str status: A string value representing one of the AlarmStatus enumeration value
:param str assignee_id: A string value representing the assignee user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
:param str text_search: The case insensitive 'substring' filter based on of next alarm fields: type, severity or status
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:param int start_time: The start timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'.
:param int end_time: The end timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'.
:param bool fetch_originator: A boolean value to specify if the alarm originator name will be filled in the AlarmInfo object  field: 'originatorName' or will returns as null.
:return: PageDataAlarmInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_all_alarms(page_size=page_size, page=page, search_status=search_status, status=status, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time, fetch_originator=fetch_originator)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_all_alarms'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_highest_alarm_severity(entity_id_json: str, search_status: Optional[str] = None, status: Optional[str] = None, assignee_id: Optional[str] = None) -> str:
    """
    Get Highest Alarm Severity (getHighestAlarmSeverity)  # noqa: E501

Search the alarms by originator ('entityType' and entityId') and optional 'status' or 'searchStatus' filters and returns the highest AlarmSeverity(CRITICAL, MAJOR, MINOR, WARNING or INDETERMINATE). Specifying both parameters 'searchStatus' and 'status' at the same time will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str search_status: A string value representing one of the AlarmSearchStatus enumeration value
:param str status: A string value representing one of the AlarmStatus enumeration value
:param str assignee_id: A string value representing the assignee user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_highest_alarm_severity(entity_id=deserialize_param(entity_id_json, 'EntityId'), search_status=search_status, status=status, assignee_id=assignee_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_highest_alarm_severity'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_alarm(body_json: str) -> str:
    """
    Create or Update Alarm (saveAlarm)  # noqa: E501

Creates or Updates the Alarm. When creating alarm, platform generates Alarm Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Alarm id will be present in the response. Specify existing Alarm id to update the alarm. Referencing non-existing Alarm Id will cause 'Not Found' error.   Platform also deduplicate the alarms based on the entity id of originator and alarm 'type'. For example, if the user or system component create the alarm with the type 'HighTemperature' for device 'Device A' the new active alarm is created. If the user tries to create 'HighTemperature' alarm for the same device again, the previous alarm will be updated (the 'end_ts' will be set to current timestamp). If the user clears the alarm (see 'Clear Alarm(clearAlarm)'), than new alarm with the same type and same device may be created. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Alarm entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param Alarm body:
:return: Alarm
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_alarm(body=deserialize_param(body_json, 'Alarm'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_alarm'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_alarm_comment(alarm_id_json: str, body: Optional[str] = None) -> str:
    """
    Create or update Alarm Comment   # noqa: E501

Creates or Updates the Alarm Comment. When creating comment, platform generates Alarm Comment Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Alarm Comment id will be present in the response. Specify existing Alarm Comment id to update the alarm. Referencing non-existing Alarm Comment Id will cause 'Not Found' error.    To create new Alarm comment entity it is enough to specify 'comment' json element with 'text' node, for example: {"comment": { "text": "my comment"}}.    If comment type is not specified the default value 'OTHER' will be saved. If 'alarmId' or 'userId' specified in body it will be ignored.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param AlarmComment body:
:return: AlarmComment
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_alarm_comment(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'), body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_alarm_comment'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def unassign_alarm(id_json: str) -> str:
    """
    Unassign Alarm (unassignAlarm)  # noqa: E501

Unassign the Alarm. Once unassigned, the 'assign_ts' field will be set to current timestamp and special rule chain event 'ALARM_UNASSIGNED' will be generated. Referencing non-existing Alarm Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: Alarm
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.unassign_alarm(id=deserialize_param(id_json, 'AlarmId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'unassign_alarm'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    """Register tools with FastMCP server"""
    mcp.tool()( ack_alarm )
    mcp.tool()( assign_alarm )
    mcp.tool()( clear_alarm )
    mcp.tool()( count_alarms_by_query )
    mcp.tool()( delete_alarm )
    mcp.tool()( delete_alarm_comment )
    mcp.tool()( find_alarm_data_by_query )
    mcp.tool()( get_alarm_by_id )
    mcp.tool()( get_alarm_comments )
    mcp.tool()( get_alarm_info_by_id )
    mcp.tool()( get_alarm_types )
    mcp.tool()( get_alarms )
    mcp.tool()( get_all_alarms )
    mcp.tool()( get_highest_alarm_severity )
    mcp.tool()( save_alarm )
    mcp.tool()( save_alarm_comment )
    mcp.tool()( unassign_alarm )
