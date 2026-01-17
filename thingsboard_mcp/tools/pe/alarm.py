import json
import tb_rest_client.models.models_pe as models
from ...shared import get_client, deserialize_param, format_response, ApiException


def ack_alarm(alarm_id_json: str) -> str:
    """
    No description available.
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
    No description available.
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
    No description available.
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

def count_alarms_by_query(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.count_alarms_by_query(body=deserialize_param(body_json, 'AlarmCountQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'count_alarms_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_alarm(alarm_id_json: str) -> str:
    """
    No description available.
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

def delete_alarm_comment(alarm_id_json: str, comment_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.delete_alarm_comment(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'), comment_id=deserialize_param(comment_id_json, 'AlarmCommentId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_alarm_comment'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_alarm_data_by_query(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_alarm_data_by_query(body=deserialize_param(body_json, 'AlarmDataQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_alarm_data_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_alarm_by_id(alarm_id_json: str) -> str:
    """
    No description available.
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

def get_alarm_comments(alarm_id_json: str, page_size: int, page: int, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_alarm_comments(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'), page_size=page_size, page=page, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_alarm_comments'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_alarm_info_by_id(alarm_id_json: str) -> str:
    """
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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

def save_alarm_comment(alarm_id_json: str, body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.save_alarm_comment(alarm_id=deserialize_param(alarm_id_json, 'AlarmId'), body=deserialize_param(body_json, 'AlarmComment'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_alarm_comment'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def unassign_alarm(id_json: str) -> str:
    """
    No description available.
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
