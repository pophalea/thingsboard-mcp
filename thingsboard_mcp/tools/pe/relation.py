import json
import tb_rest_client.models.models_pe as models
from ...shared import get_client, deserialize_param, format_response, ApiException


def delete_relation(from_id_json: str, relation_type: str, to_id_json: str, relation_type_group: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.delete_relation(from_id=deserialize_param(from_id_json, 'EntityId'), relation_type=relation_type, to_id=deserialize_param(to_id_json, 'EntityId'), relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_relation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_relations(entity_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.delete_relations(entity_id=deserialize_param(entity_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_relations'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_relation(from_id_json: str, relation_type: str, to_id_json: str, relation_type_group: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_relation(from_id=deserialize_param(from_id_json, 'EntityId'), relation_type=relation_type, to_id=deserialize_param(to_id_json, 'EntityId'), relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_relation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_relation(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.save_relation(body=deserialize_param(body_json, 'EntityRelation'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_relation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def register(mcp):
    mcp.tool()( delete_relation )
    mcp.tool()( delete_relations )
    mcp.tool()( get_relation )
    mcp.tool()( save_relation )
