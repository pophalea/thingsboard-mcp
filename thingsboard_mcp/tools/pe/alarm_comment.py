import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_alarm_comment(alarm_id_json: str, comment_id_json: str) -> str:
    """
    Delete Alarm comment (deleteAlarmComment)  # noqa: E501

Deletes the Alarm comment. Referencing non-existing Alarm comment Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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


def get_alarm_comments(alarm_id_json: str, page_size: int, page: int, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Alarm comments (getAlarmComments)  # noqa: E501

Returns a page of alarm comments for specified alarm. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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


def save_alarm_comment(alarm_id_json: str, body_json: str = None) -> str:
    """
    Create or update Alarm Comment   # noqa: E501

Creates or Updates the Alarm Comment. When creating comment, platform generates Alarm Comment Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Alarm Comment id will be present in the response. Specify existing Alarm Comment id to update the alarm. Referencing non-existing Alarm Comment Id will cause 'Not Found' error.    To create new Alarm comment entity it is enough to specify 'comment' json element with 'text' node, for example: {"comment": { "text": "my comment"}}.    If comment type is not specified the default value 'OTHER' will be saved. If 'alarmId' or 'userId' specified in body it will be ignored.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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


def register(mcp):
    mcp.tool()( delete_alarm_comment )
    mcp.tool()( get_alarm_comments )
    mcp.tool()( save_alarm_comment )
