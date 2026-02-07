import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_relation(from_id_json: str, relation_type: str, to_id_json: str, relation_type_group: Optional[str] = None) -> str:
    """
    Delete Relation (deleteRelation)  # noqa: E501

Deletes a relation between two entities in the platform.   If the user has the authority of 'System Administrator', the server checks that 'from' and 'to' entities are owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that 'from' and 'to' entities are owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the 'from' and 'to' entities are assigned to the same customer.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
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
    Delete common relations (deleteCommonRelations)  # noqa: E501

Deletes all the relations ('from' and 'to' direction) for the specified entity and relation type group: 'COMMON'.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
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


def find_by_from(from_id_json: str, relation_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    Get List of Relations (findByFrom)  # noqa: E501

Returns list of relation objects for the specified entity by the 'from' direction and relation type.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.find_by_from(from_id=deserialize_param(from_id_json, 'EntityId'), relation_type=relation_type, relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_from'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def find_by_from_v1(from_id_json: str, from_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    Get List of Relations (findByFrom)  # noqa: E501

Returns list of relation objects for the specified entity by the 'from' direction.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.find_by_from_v1(from_id=deserialize_param(from_id_json, 'EntityId'), from_type=from_type, relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_from_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def find_by_query_v3(body_json: str) -> str:
    """
    Find related entities (findByQuery)  # noqa: E501

Returns all entities that are related to the specific entity. The entity id, relation type, entity types, depth of the search, and other query parameters defined using complex 'EntityRelationsQuery' object. See 'Model' tab of the Parameters for more info.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityRelationsQuery):
    - `parameters` (RelationsSearchParameters)
    - `filters` (list[RelationEntityTypeFilter])
    """
    try:
        client = get_client()
        result = client.find_by_query_v3(body=deserialize_param(body_json, 'EntityRelationsQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_query_v3'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def find_by_to(to_id_json: str, relation_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    Get List of Relations (findByTo)  # noqa: E501

Returns list of relation objects for the specified entity by the 'to' direction and relation type.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.find_by_to(to_id=deserialize_param(to_id_json, 'EntityId'), relation_type=relation_type, relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_to'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def find_by_to_v1(to_id_json: str, to_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    Get List of Relations (findByTo)  # noqa: E501

Returns list of relation objects for the specified entity by the 'to' direction.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.find_by_to_v1(to_id=deserialize_param(to_id_json, 'EntityId'), to_type=to_type, relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_to_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def find_info_by_from(from_id_json: str, relation_type_group: Optional[str] = None) -> str:
    """
    Get List of Relation Infos (findInfoByFrom)  # noqa: E501

Returns list of relation info objects for the specified entity by the 'from' direction.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer. Relation Info is an extension of the default Relation object that contains information about the 'from' and 'to' entity names.   # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.find_info_by_from(from_id=deserialize_param(from_id_json, 'EntityId'), relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_info_by_from'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def find_info_by_query(body_json: str) -> str:
    """
    Find related entity infos (findInfoByQuery)  # noqa: E501

Returns all entity infos that are related to the specific entity. The entity id, relation type, entity types, depth of the search, and other query parameters defined using complex 'EntityRelationsQuery' object. See 'Model' tab of the Parameters for more info. Relation Info is an extension of the default Relation object that contains information about the 'from' and 'to' entity names.   # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityRelationsQuery):
    - `parameters` (RelationsSearchParameters)
    - `filters` (list[RelationEntityTypeFilter])
    """
    try:
        client = get_client()
        result = client.find_info_by_query(body=deserialize_param(body_json, 'EntityRelationsQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_info_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def find_info_by_to(to_id_json: str, to_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    Get List of Relation Infos (findInfoByTo)  # noqa: E501

Returns list of relation info objects for the specified entity by the 'to' direction.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer. Relation Info is an extension of the default Relation object that contains information about the 'from' and 'to' entity names.   # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.find_info_by_to(to_id=deserialize_param(to_id_json, 'EntityId'), to_type=to_type, relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_info_by_to'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_relation(from_id_json: str, relation_type: str, to_id_json: str, relation_type_group: Optional[str] = None) -> str:
    """
    Get Relation (getRelation)  # noqa: E501

Returns relation object between two specified entities if present. Otherwise throws exception.   If the user has the authority of 'System Administrator', the server checks that 'from' and 'to' entities are owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that 'from' and 'to' entities are owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the 'from' and 'to' entities are assigned to the same customer.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
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


def save_relation(body_json: str = None) -> str:
    """
    Create Relation (saveRelation)  # noqa: E501

Creates or updates a relation between two entities in the platform. Relations unique key is a combination of from/to entity id and relation type group and relation type.   If the user has the authority of 'System Administrator', the server checks that 'from' and 'to' entities are owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that 'from' and 'to' entities are owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the 'from' and 'to' entities are assigned to the same customer.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityRelation):
    - `_from` (EntityId)
    - `to` (EntityId)
    - `type` (str)
    - `type_group` (str)
    - `version` (int)
    - `additional_info` (JsonNode)
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
    mcp.tool()( find_by_from )
    mcp.tool()( find_by_from_v1 )
    mcp.tool()( find_by_query_v3 )
    mcp.tool()( find_by_to )
    mcp.tool()( find_by_to_v1 )
    mcp.tool()( find_info_by_from )
    mcp.tool()( find_info_by_query )
    mcp.tool()( find_info_by_to )
    mcp.tool()( get_relation )
    mcp.tool()( save_relation )
