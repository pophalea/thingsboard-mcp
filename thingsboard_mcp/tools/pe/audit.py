import json
import tb_rest_client.models.models_pe as models
from ...shared import get_client, deserialize_param, format_response, ApiException


def get_audit_logs(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, action_types: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_audit_logs(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time, action_types=action_types)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_audit_logs'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_audit_logs_by_entity_id(entity_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, action_types: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_audit_logs_by_entity_id(entity_id=deserialize_param(entity_id_json, 'EntityId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time, action_types=action_types)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_audit_logs_by_entity_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def register(mcp):
    mcp.tool()( get_audit_logs )
    mcp.tool()( get_audit_logs_by_entity_id )
