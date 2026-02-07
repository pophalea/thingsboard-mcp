import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_calculated_field(calculated_field_id_json: str) -> str:
    """
    Delete Calculated Field (deleteCalculatedField)  # noqa: E501

Deletes the calculated field. Referencing non-existing Calculated Field Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_calculated_field(calculated_field_id=deserialize_param(calculated_field_id_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_calculated_field'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_calculated_field_by_id(calculated_field_id_json: str) -> str:
    """
    Get Calculated Field (getCalculatedFieldById)  # noqa: E501

Fetch the Calculated Field object based on the provided Calculated Field Id.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_calculated_field_by_id(calculated_field_id=deserialize_param(calculated_field_id_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_calculated_field_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_calculated_fields_by_entity_id(entity_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Calculated Fields by Entity Id (getCalculatedFieldsByEntityId)  # noqa: E501

Fetch the Calculated Fields based on the provided Entity Id.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_calculated_fields_by_entity_id(entity_id=deserialize_param(entity_id_json, 'EntityId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_calculated_fields_by_entity_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_latest_calculated_field_debug_event(calculated_field_id_json: str) -> str:
    """
    Get latest calculated field debug event (getLatestCalculatedFieldDebugEvent)  # noqa: E501

Gets latest calculated field debug event for specified calculated field id. Referencing non-existing calculated field id will cause an error.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CalculatedFieldId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_latest_calculated_field_debug_event(calculated_field_id=deserialize_param(calculated_field_id_json, 'CalculatedFieldId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_latest_calculated_field_debug_event'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_calculated_field(body_json: str) -> str:
    """
    Create Or Update Calculated Field (saveCalculatedField)  # noqa: E501

Creates or Updates the Calculated Field. When creating calculated field, platform generates Calculated Field Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Calculated Field Id will be present in the response. Specify existing Calculated Field Id to update the calculated field. Referencing non-existing Calculated Field Id will cause 'Not Found' error. Remove 'id', 'tenantId' from the request body example (below) to create new Calculated Field entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CalculatedField):
    - `id` (CalculatedFieldId)
    - `created_time` (int)
    - `tenant_id` (TenantId)
    - `entity_id` (EntityId)
    - `type` (str)
    - `name` (str)
    - `debug_mode` (bool)
    - `debug_settings` (DebugSettings)
    - `configuration_version` (int)
    - `configuration` (object)
    - `version` (int)
    """
    try:
        client = get_client()
        result = client.save_calculated_field(body=deserialize_param(body_json, 'CalculatedField'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_calculated_field'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_calculated_field )
    mcp.tool()( get_calculated_field_by_id )
    mcp.tool()( get_calculated_fields_by_entity_id )
    mcp.tool()( get_latest_calculated_field_debug_event )
    mcp.tool()( save_calculated_field )
