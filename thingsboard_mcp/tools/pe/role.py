import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_role(role_id_json: str) -> str:
    """
    Delete role (deleteRole)  # noqa: E501

Deletes the role. Referencing non-existing role Id will cause an error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (RoleId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.delete_role(role_id=deserialize_param(role_id_json, 'RoleId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_role'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_role_by_id(role_id_json: str) -> str:
    """
    Get Role by Id (getRoleById)  # noqa: E501

Fetch the Role object based on the provided Role Id. Role Contains a set of permissions. Role has two types. Generic Role may be assigned to the user group and will provide permissions for all entities of a certain type. Group Role may be assigned to both user and entity group and will provides permissions only for the entities that belong to specified entity group. The assignment of the Role to the User Group is done using [Group Permission Controller](/swagger-ui.html#/group-permission-controller). Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (RoleId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_role_by_id(role_id=deserialize_param(role_id_json, 'RoleId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_role_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_roles(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Roles (getRoles)  # noqa: E501

Returns a page of roles that are available for the current user. Role Contains a set of permissions. Role has two types. Generic Role may be assigned to the user group and will provide permissions for all entities of a certain type. Group Role may be assigned to both user and entity group and will provides permissions only for the entities that belong to specified entity group. The assignment of the Role to the User Group is done using [Group Permission Controller](/swagger-ui.html#/group-permission-controller).You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_roles(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_roles'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_roles_by_ids(role_ids_json: str) -> str:
    """
    Get Roles By Ids (getRolesByIds)  # noqa: E501

Returns the list of rows based on their ids.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_roles_by_ids(role_ids=json.loads(role_ids_json) if role_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_roles_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_role(body_json: str = None) -> str:
    """
    Create Or Update Role (saveRole)  # noqa: E501

Creates or Updates the Role. When creating Role, platform generates Role Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Role id will be present in the response. Specify existing Role id to update the permission. Referencing non-existing Group Permission Id will cause 'Not Found' error.  Role Contains a set of permissions. Role has two types. Generic Role may be assigned to the user group and will provide permissions for all entities of a certain type. Group Role may be assigned to both user and entity group and will provides permissions only for the entities that belong to specified entity group. The assignment of the Role to the User Group is done using [Group Permission Controller](/swagger-ui.html#/group-permission-controller).  Example of Generic Role with read-only permissions for any resource and all permissions for the 'DEVICE' and 'PROFILE' resources is listed below:   ```json {   "name": "Read-Only User",   "type": "GENERIC",   "permissions": {     "ALL": [       "READ",       "RPC_CALL",       "READ_CREDENTIALS",       "READ_ATTRIBUTES",       "READ_TELEMETRY"     ],     "DEVICE": [       "ALL"     ]     "PROFILE": [       "ALL"     ]   },   "additionalInfo": {     "description": "Read-only permissions for everything, Write permissions for devices and own profile."   } } ```  Example of Group Role with read-only permissions. Note that the group role has no association with the resources. The type of the resource is taken from the entity group that this role is assigned to:   ```json {   "name": "Entity Group Read-only User",   "type": "GROUP",   "permissions": [     "READ",     "RPC_CALL",     "READ_CREDENTIALS",     "READ_ATTRIBUTES",     "READ_TELEMETRY"   ],   "additionalInfo": {     "description": "Read-only permissions."   } } ```   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (Role):
    - `tenant_id` (TenantId)
    - `customer_id` (CustomerId)
    - `name` (str)
    - `type` (str)
    - `permissions` (JsonNode)
    - `version` (int)
    - `id` (RoleId)
    - `created_time` (int)
    - `additional_info` (JsonNode)
    - `owner_id` (EntityId)
    """
    try:
        client = get_client()
        result = client.save_role(body=deserialize_param(body_json, 'Role'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_role'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_role )
    mcp.tool()( get_role_by_id )
    mcp.tool()( get_roles )
    mcp.tool()( get_roles_by_ids )
    mcp.tool()( save_role )
