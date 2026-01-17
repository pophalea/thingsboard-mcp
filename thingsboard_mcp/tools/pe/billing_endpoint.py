import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def check_tenant_can_update_plan(body_json: str) -> str:
    """
    checkTenantCanUpdatePlan  # noqa: E501
    """
    try:
        client = get_client()
        result = client.check_tenant_can_update_plan(body=deserialize_param(body_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'check_tenant_can_update_plan'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def notify_tenant_plan_changed(body_json: str) -> str:
    """
    notifyTenantPlanChanged  # noqa: E501
    """
    try:
        client = get_client()
        result = client.notify_tenant_plan_changed(body=deserialize_param(body_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'notify_tenant_plan_changed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def notify_tenant_state_changed(body_json: str) -> str:
    """
    notifyTenantStateChanged  # noqa: E501
    """
    try:
        client = get_client()
        result = client.notify_tenant_state_changed(body=deserialize_param(body_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'notify_tenant_state_changed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def send_password_was_reset_email(body_json: str) -> str:
    """
    sendPasswordWasResetEmail  # noqa: E501
    """
    try:
        client = get_client()
        result = client.send_password_was_reset_email(body=deserialize_param(body_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'send_password_was_reset_email'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def send_reset_password_email(body_json: str) -> str:
    """
    sendResetPasswordEmail  # noqa: E501
    """
    try:
        client = get_client()
        result = client.send_reset_password_email(body=deserialize_param(body_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'send_reset_password_email'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def tenant_has_billing_read() -> str:
    """
    tenantHasBillingRead  # noqa: E501
    """
    try:
        client = get_client()
        result = client.tenant_has_billing_read()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'tenant_has_billing_read'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def tenant_has_billing_write() -> str:
    """
    tenantHasBillingWrite  # noqa: E501
    """
    try:
        client = get_client()
        result = client.tenant_has_billing_write()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'tenant_has_billing_write'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( check_tenant_can_update_plan )
    mcp.tool()( notify_tenant_plan_changed )
    mcp.tool()( notify_tenant_state_changed )
    mcp.tool()( send_password_was_reset_email )
    mcp.tool()( send_reset_password_email )
    mcp.tool()( tenant_has_billing_read )
    mcp.tool()( tenant_has_billing_write )
