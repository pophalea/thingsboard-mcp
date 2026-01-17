import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_notification_template_by_id(id: str) -> str:
    """
    Delete notification template by id (deleteNotificationTemplateById  # noqa: E501

Deletes notification template by its id.  This template cannot be referenced by existing scheduled notification requests or any notification rules.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_notification_template_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_notification_template_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_notification_template_by_id(id: str) -> str:
    """
    Get notification template by id (getNotificationTemplateById)  # noqa: E501

Fetches notification template by id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_template_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_template_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_notification_templates(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get notification templates (getNotificationTemplates)  # noqa: E501

Returns the page of notification templates owned by sysadmin or tenant.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_templates(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_templates'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def list_slack_conversations(type: str, token: Optional[str] = None) -> str:
    """
    List Slack conversations (listSlackConversations)  # noqa: E501

List available Slack conversations by type.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.list_slack_conversations(type=type, token=token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'list_slack_conversations'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_notification_template(body_json: str) -> str:
    """
    Save notification template (saveNotificationTemplate)  # noqa: E501

Creates or updates notification template.  Here is an example of template to send notification via Web, SMS and Slack: ```json {   "name": "Greetings",   "notificationType": "GENERAL",   "configuration": {     "deliveryMethodsTemplates": {       "WEB": {         "enabled": true,         "subject": "Greetings",         "body": "Hi there, ${recipientTitle}",         "additionalConfig": {           "icon": {             "enabled": true,             "icon": "back_hand",             "color": "#757575"           },           "actionButtonConfig": {             "enabled": false           }         },         "method": "WEB"       },       "SMS": {         "enabled": true,         "body": "Hi there, ${recipientTitle}",         "method": "SMS"       },       "SLACK": {         "enabled": true,         "body": "Hi there, @${recipientTitle}",         "method": "SLACK"       }     }   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_notification_template(body=deserialize_param(body_json, 'NotificationTemplate'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_notification_template'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_notification_template_by_id )
    mcp.tool()( get_notification_template_by_id )
    mcp.tool()( get_notification_templates )
    mcp.tool()( list_slack_conversations )
    mcp.tool()( save_notification_template )
