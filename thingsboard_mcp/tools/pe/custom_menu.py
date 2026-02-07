import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def create_custom_menu(body_json: str = None, assign_to_list_json: str = None, force: Optional[bool] = None) -> str:
    """
    Create Custom Menu (createCustomMenu)  # noqa: E501

The api is designed to create Custom Menu without configuration. Is not applicable for update.  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomMenuInfo):
    - `id` (CustomMenuId)
    - `created_time` (int)
    - `tenant_id` (TenantId)
    - `customer_id` (CustomerId)
    - `name` (str)
    - `scope` (str)
    - `assignee_type` (str)
    """
    try:
        client = get_client()
        result = client.create_custom_menu(body=deserialize_param(body_json, 'CustomMenuInfo'), assign_to_list=json.loads(assign_to_list_json) if assign_to_list_json else None, force=force)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'create_custom_menu'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_custom_menu(custom_menu_id_json: str, force: Optional[bool] = None) -> str:
    """
    Delete custom menu (deleteCustomMenu)  # noqa: E501

Deletes the custom menu based on the provided Custom Menu Id. Referencing non-existing custom menu Id will cause an error. If the custom menu is assigned to the list of users or customers bad request is returned.To delete a custom menu that has assignee list set 'force' request param to true   # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomMenuId):
    - `id` (str)
    """
    try:
        client = get_client()
        result = client.delete_custom_menu(custom_menu_id=deserialize_param(custom_menu_id_json, 'CustomMenuId'), force=force)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_custom_menu'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_custom_menu() -> str:
    """
    Get end-user Custom Menu configuration (getCustomMenu)  # noqa: E501

Fetch the Custom Menu object for the end user. The custom menu is configured in the white labeling parameters. If custom menu configuration on the tenant level is present, it overrides the menu configuration of the system level. Similar, if the custom menu configuration on the customer level is present, it overrides the menu configuration of the tenant level.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_custom_menu()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_custom_menu'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_custom_menu_assignee_list(custom_menu_id_json: str) -> str:
    """
    Get Custom Menu assignee list (getCustomMenuAssigneeList)  # noqa: E501

Fetch the list of Entity Info objects that represents users or customers, or empty list if custom menu is not assigned or has NO_ASSIGN/ALL assignee type.  Security check is performed to verify that the user has 'READ' permission for the custom menu with specified id.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomMenuId):
    - `id` (str)
    """
    try:
        client = get_client()
        result = client.get_custom_menu_assignee_list(custom_menu_id=deserialize_param(custom_menu_id_json, 'CustomMenuId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_custom_menu_assignee_list'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_custom_menu_config(custom_menu_id_json: str) -> str:
    """
    Get Custom Menu configuration by id (getCustomMenuConfig)  # noqa: E501

Fetch the Custom Menu configuration based on the provided Custom Menu Id.   Security check is performed to verify that the user has 'READ' permission for the custom menu with specified id.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomMenuId):
    - `id` (str)
    """
    try:
        client = get_client()
        result = client.get_custom_menu_config(custom_menu_id=deserialize_param(custom_menu_id_json, 'CustomMenuId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_custom_menu_config'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_custom_menu_info_by_id(custom_menu_id_json: str) -> str:
    """
    Get Custom Menu Info (getCustomMenuInfoById)  # noqa: E501

Fetch the Custom Menu Info object based on the provided Custom Menu Id.   Security check is performed to verify that the user has 'READ' permission for the custom menu with specified id.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomMenuId):
    - `id` (str)
    """
    try:
        client = get_client()
        result = client.get_custom_menu_info_by_id(custom_menu_id=deserialize_param(custom_menu_id_json, 'CustomMenuId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_custom_menu_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_custom_menu_infos(page_size: int, page: int, scope: Optional[str] = None, assignee_type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get all custom menus configured at user level (getCustomMenuInfos)  # noqa: E501

Returns a page of custom menu info objects owned by the tenant or the customer of a current user, scope and assigneeType request parameters can be used to filter the result.  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_custom_menu_infos(page_size=page_size, page=page, scope=scope, assignee_type=assignee_type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_custom_menu_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def update_custom_menu_assignee_list(id_json: str, assignee_type: str, body_json: str, force: Optional[bool] = None) -> str:
    """
    Update custom menu assignee list (updateCustomMenuAssigneeList)  # noqa: E501

The api designed to update the list of assignees or assignee type based on the provided Custom Menu Id. To change assignee type, put new assignee type in path parameter.  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomMenuId):
    - `id` (str)
    """
    try:
        client = get_client()
        result = client.update_custom_menu_assignee_list(id=deserialize_param(id_json, 'CustomMenuId'), assignee_type=assignee_type, body=json.loads(body_json) if body_json else None, force=force)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_custom_menu_assignee_list'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def update_custom_menu_config(id_json: str, body_json: str) -> str:
    """
    Update Custom Menu configuration based on the provided Custom Menu Id (updateCustomMenuConfig)  # noqa: E501

  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomMenuId):
    - `id` (str)
    Expected JSON Structure (CustomMenuConfig):
    - `items` (list[OneOfCustomMenuConfigItemsItems])
    """
    try:
        client = get_client()
        result = client.update_custom_menu_config(id=deserialize_param(id_json, 'CustomMenuId'), body=deserialize_param(body_json, 'CustomMenuConfig'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_custom_menu_config'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def update_custom_menu_name(id_json: str, body: str) -> str:
    """
    Update Custom Menu name based on the provided Custom Menu Id (updateCustomMenuName)  # noqa: E501

  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomMenuId):
    - `id` (str)
    """
    try:
        client = get_client()
        result = client.update_custom_menu_name(id=deserialize_param(id_json, 'CustomMenuId'), body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_custom_menu_name'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( create_custom_menu )
    mcp.tool()( delete_custom_menu )
    mcp.tool()( get_custom_menu )
    mcp.tool()( get_custom_menu_assignee_list )
    mcp.tool()( get_custom_menu_config )
    mcp.tool()( get_custom_menu_info_by_id )
    mcp.tool()( get_custom_menu_infos )
    mcp.tool()( update_custom_menu_assignee_list )
    mcp.tool()( update_custom_menu_config )
    mcp.tool()( update_custom_menu_name )
