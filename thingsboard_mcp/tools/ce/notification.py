import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def create_notification_request(body_json: str) -> str:
    """
    Create notification request (createNotificationRequest)  # noqa: E501

Processes notification request. Mandatory request properties are `targets` (list of targets ids to send notification to), and either `templateId` (existing notification template id) or `template` (to send notification without saving the template). Optionally, you can set `sendingDelayInSec` inside the `additionalConfig` field to schedule the notification.  For each enabled delivery method in the notification template, there must be a target in the `targets` list that supports this delivery method: if you chose `WEB`, `EMAIL` or `SMS` - there must be at least one target in `targets` of `PLATFORM_USERS` type. For `SLACK` delivery method - you need to chose at least one `SLACK` notification target.  Notification request object with `PROCESSING` status will be returned immediately, and the notification sending itself is done asynchronously. After all notifications are sent, the `status` of the request becomes `SENT`. Use `getNotificationRequestById` to see the notification request processing status and some sending stats.   Here is an example of notification request to one target using saved template: ```json {   "templateId": {     "entityType": "NOTIFICATION_TEMPLATE",     "id": "6dbc3670-e4dd-11ed-9401-dbcc5dff78be"   },   "targets": [     "320e3ed0-d785-11ed-a06c-21dd57dd88ca"   ],   "additionalConfig": {     "sendingDelayInSec": 0   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (NotificationRequest):
    - `tenant_id` (TenantId)
    - `targets` (list[str])
    - `template_id` (NotificationTemplateId)
    - `template` (NotificationTemplate)
    - `info` (NotificationInfo)
    - `additional_config` (NotificationRequestConfig)
    - `originator_entity_id` (EntityId)
    - `rule_id` (NotificationRuleId)
    - `status` (str)
    - `stats` (NotificationRequestStats)
    - `id` (NotificationRequestId)
    - `created_time` (int)
    """
    try:
        client = get_client()
        result = client.create_notification_request(body=deserialize_param(body_json, 'NotificationRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'create_notification_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_notification(id: str) -> str:
    """
    Delete notification (deleteNotification)  # noqa: E501

Deletes notification by its id.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_notification(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_notification'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_notification_request(id: str) -> str:
    """
    Delete notification request (deleteNotificationRequest)  # noqa: E501

Deletes notification request by its id.  If the request has status `SENT` - all sent notifications for this request will be deleted. If it is `SCHEDULED`, the request will be cancelled.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_notification_request(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_notification_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_available_delivery_methods() -> str:
    """
    Get available delivery methods (getAvailableDeliveryMethods)  # noqa: E501

Returns the list of delivery methods that are properly configured and are allowed to be used for sending notifications.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_available_delivery_methods()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_available_delivery_methods'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_notification_request_by_id(id: str) -> str:
    """
    Get notification request by id (getNotificationRequestById)  # noqa: E501

Fetches notification request info by request id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_request_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_request_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_notification_request_preview(body_json: str, recipients_preview_size: Optional[int] = None) -> str:
    """
    Get notification request preview (getNotificationRequestPreview)  # noqa: E501

Returns preview for notification request.  `processedTemplates` shows how the notifications for each delivery method will look like for the first recipient of the corresponding notification target.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (NotificationRequest):
    - `tenant_id` (TenantId)
    - `targets` (list[str])
    - `template_id` (NotificationTemplateId)
    - `template` (NotificationTemplate)
    - `info` (NotificationInfo)
    - `additional_config` (NotificationRequestConfig)
    - `originator_entity_id` (EntityId)
    - `rule_id` (NotificationRuleId)
    - `status` (str)
    - `stats` (NotificationRequestStats)
    - `id` (NotificationRequestId)
    - `created_time` (int)
    """
    try:
        client = get_client()
        result = client.get_notification_request_preview(body=deserialize_param(body_json, 'NotificationRequest'), recipients_preview_size=recipients_preview_size)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_request_preview'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_notification_requests(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get notification requests (getNotificationRequests)  # noqa: E501

Returns the page of notification requests submitted by users of this tenant or sysadmins.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_requests(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_requests'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_notification_settings() -> str:
    """
    Get notification settings (getNotificationSettings)  # noqa: E501

Retrieves notification settings for this tenant or sysadmin.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_notifications(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, delivery_method: Optional[str] = None) -> str:
    """
    Get notifications (getNotifications)  # noqa: E501

Returns the page of notifications for current user.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for any authorized user.   **WebSocket API**:  There are 2 types of subscriptions: one for unread notifications count, another for unread notifications themselves.  The URI for opening WS session for notifications: `/api/ws/plugins/notifications`.  Subscription command for unread notifications count: ``` {   "unreadCountSubCmd": {     "cmdId": 1234   } } ``` To subscribe for latest unread notifications: ``` {   "unreadSubCmd": {     "cmdId": 1234,     "limit": 10   } } ``` To unsubscribe from any subscription: ``` {   "unsubCmd": {     "cmdId": 1234   } } ``` To mark certain notifications as read, use following command: ``` {   "markAsReadCmd": {     "cmdId": 1234,     "notifications": [       "6f860330-7fc2-11ed-b855-7dd3b7d2faa9",       "5b6dfee0-8d0d-11ed-b61f-35a57b03dade"     ]   } }  ``` To mark all notifications as read: ``` {   "markAllAsReadCmd": {     "cmdId": 1234   } } ```   Update structure for unread **notifications count subscription**: ``` {   "cmdId": 1234,   "totalUnreadCount": 55 } ``` For **notifications subscription**: - full update of latest unread notifications: ``` {   "cmdId": 1234,   "notifications": [     {       "id": {         "entityType": "NOTIFICATION",         "id": "6f860330-7fc2-11ed-b855-7dd3b7d2faa9"       },       ...     }   ],   "totalUnreadCount": 1 } ``` - when new notification arrives or shown notification is updated: ``` {   "cmdId": 1234,   "update": {     "id": {       "entityType": "NOTIFICATION",       "id": "6f860330-7fc2-11ed-b855-7dd3b7d2faa9"     },     # updated notification info, text, subject etc.     ...   },   "totalUnreadCount": 2 } ``` - when unread notifications count changes: ``` {   "cmdId": 1234,   "totalUnreadCount": 5 } ```  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notifications(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, delivery_method=delivery_method)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notifications'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_unread_notifications_count(delivery_method: Optional[str] = None) -> str:
    """
    Get unread notifications count (getUnreadNotificationsCount)  # noqa: E501

Returns unread notifications count for chosen delivery method.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_unread_notifications_count(delivery_method=delivery_method)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_unread_notifications_count'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_user_notification_settings() -> str:
    """
    getUserNotificationSettings  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_user_notification_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_user_notification_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def mark_all_notifications_as_read() -> str:
    """
    Mark all notifications as read (markAllNotificationsAsRead)  # noqa: E501

Marks all unread notifications as read.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.mark_all_notifications_as_read()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'mark_all_notifications_as_read'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def mark_notification_as_read(id: str) -> str:
    """
    Mark notification as read (markNotificationAsRead)  # noqa: E501

Marks notification as read by its id.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.mark_notification_as_read(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'mark_notification_as_read'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_notification_settings(body_json: str) -> str:
    """
    Save notification settings (saveNotificationSettings)  # noqa: E501

Saves notification settings for this tenant or sysadmin. `deliveryMethodsConfigs` of the settings must be specified.  Here is an example of the notification settings with Slack configuration: ```json {   "deliveryMethodsConfigs": {     "SLACK": {       "method": "SLACK",       "botToken": "xoxb-...."     }   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (NotificationSettings):
    - `delivery_methods_configs` (dict(str, object))
    """
    try:
        client = get_client()
        result = client.save_notification_settings(body=deserialize_param(body_json, 'NotificationSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_notification_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_user_notification_settings(body_json: str) -> str:
    """
    saveUserNotificationSettings  # noqa: E501

    ---------------------------
    Expected JSON Structure (UserNotificationSettings):
    - `prefs` (dict(str, NotificationPref))
    """
    try:
        client = get_client()
        result = client.save_user_notification_settings(body=deserialize_param(body_json, 'UserNotificationSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_user_notification_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( create_notification_request )
    mcp.tool()( delete_notification )
    mcp.tool()( delete_notification_request )
    mcp.tool()( get_available_delivery_methods )
    mcp.tool()( get_notification_request_by_id )
    mcp.tool()( get_notification_request_preview )
    mcp.tool()( get_notification_requests )
    mcp.tool()( get_notification_settings )
    mcp.tool()( get_notifications )
    mcp.tool()( get_unread_notifications_count )
    mcp.tool()( get_user_notification_settings )
    mcp.tool()( mark_all_notifications_as_read )
    mcp.tool()( mark_notification_as_read )
    mcp.tool()( save_notification_settings )
    mcp.tool()( save_user_notification_settings )
