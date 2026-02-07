import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def change_owner_to_customer(owner_id_json: str, entity_id_json: str, body_json: str = None) -> str:
    """
    Change owner to customer (changeOwnerToCustomer)  # noqa: E501

Tenant/Customer changes Owner to Customer or sub-Customer. Sub-Customer can`t perform this operation!   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (UserId):
    - `id` (str)
    - `entity_type` (str)
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.change_owner_to_customer(owner_id=deserialize_param(owner_id_json, 'UserId'), entity_id=deserialize_param(entity_id_json, 'EntityId'), body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'change_owner_to_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def change_owner_to_tenant(owner_id_json: str, entity_id_json: str, body_json: str = None) -> str:
    """
    Change owner to tenant (changeOwnerToTenant)  # noqa: E501

Tenant changes Owner from Customer or sub-Customer to Tenant.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (UserId):
    - `id` (str)
    - `entity_type` (str)
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.change_owner_to_tenant(owner_id=deserialize_param(owner_id_json, 'UserId'), entity_id=deserialize_param(entity_id_json, 'EntityId'), body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'change_owner_to_tenant'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( change_owner_to_customer )
    mcp.tool()( change_owner_to_tenant )
