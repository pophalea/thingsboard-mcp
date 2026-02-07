import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def get_tenant_profile_data() -> str:
    """
    getTenantProfileData  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_profile_data()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_profile_data'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_profile_data_by_id(tenant_profile_id_json: str) -> str:
    """
    getTenantProfileDataById  # noqa: E501

    ---------------------------
    Expected JSON Structure (TenantProfileId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_tenant_profile_data_by_id(tenant_profile_id=deserialize_param(tenant_profile_id_json, 'TenantProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_profile_data_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_subscription_usage() -> str:
    """
    getTenantSubscriptionUsage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_subscription_usage()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_subscription_usage'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( get_tenant_profile_data )
    mcp.tool()( get_tenant_profile_data_by_id )
    mcp.tool()( get_tenant_subscription_usage )
