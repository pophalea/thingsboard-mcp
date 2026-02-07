import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_notification_rule(id: str) -> str:
    """
    Delete notification rule (deleteNotificationRule)  # noqa: E501

Deletes notification rule by id. Cancels all related scheduled notification requests (e.g. due to escalation table)  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_notification_rule(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_notification_rule'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_notification_rule_by_id(id: str) -> str:
    """
    Get notification rule by id (getNotificationRuleById)  # noqa: E501

Fetches notification rule info by rule's id. In addition to regular notification rule fields, there are `templateName` and `deliveryMethods` in the response.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_rule_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_rule_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_notification_rules(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get notification rules (getNotificationRules)  # noqa: E501

Returns the page of notification rules.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_rules(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_rules'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_notification_rule(body_json: str) -> str:
    """
    Save notification rule (saveNotificationRule)  # noqa: E501

Creates or updates notification rule.   Mandatory properties are `name`, `templateId` (of a template with `notificationType` matching to rule's `triggerType`), `triggerType`, `triggerConfig` and `recipientConfig`. Additionally, you may specify rule `description` inside of `additionalConfig`.  Trigger type of the rule cannot be changed. Available trigger types for tenant: `ENTITY_ACTION`, `ALARM`, `ALARM_COMMENT`, `ALARM_ASSIGNMENT`, `DEVICE_ACTIVITY`, `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT`. For sysadmin, there are following trigger types available: `ENTITIES_LIMIT`, `API_USAGE_LIMIT`, `NEW_PLATFORM_VERSION`.  Here is an example of notification rule to send notification when a device, asset or customer is created or deleted: ```json {   "name": "Entity action",   "templateId": {     "entityType": "NOTIFICATION_TEMPLATE",     "id": "32117320-d785-11ed-a06c-21dd57dd88ca"   },   "triggerType": "ENTITY_ACTION",   "triggerConfig": {     "entityTypes": [       "CUSTOMER",       "DEVICE",       "ASSET"     ],     "created": true,     "updated": false,     "deleted": true,     "triggerType": "ENTITY_ACTION"   },   "recipientsConfig": {     "targets": [       "320f2930-d785-11ed-a06c-21dd57dd88ca"     ],     "triggerType": "ENTITY_ACTION"   },   "additionalConfig": {     "description": "Send notification to tenant admins or customer users when a device, asset or customer is created"   },   "templateName": "Entity action notification",   "deliveryMethods": [     "WEB"   ] } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (NotificationRule):
    - `id` (NotificationRuleId)
    - `created_time` (int)
    - `tenant_id` (TenantId)
    - `name` (str)
    - `enabled` (bool)
    - `template_id` (NotificationTemplateId)
    - `trigger_type` (str)
    - `trigger_config` (OneOfNotificationRuleTriggerConfig)
    - `recipients_config` (OneOfNotificationRuleRecipientsConfig)
    - `additional_config` (NotificationRuleConfig)
    """
    try:
        client = get_client()
        result = client.save_notification_rule(body=deserialize_param(body_json, 'NotificationRule'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_notification_rule'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_notification_rule )
    mcp.tool()( get_notification_rule_by_id )
    mcp.tool()( get_notification_rules )
    mcp.tool()( save_notification_rule )
