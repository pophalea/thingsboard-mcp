import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def compare_entity_data_to_version(entity_id_json: str, version_id: str) -> str:
    """
    Compare entity data to version (compareEntityDataToVersion)  # noqa: E501

Returns an object with current entity data and the one at a specific version. Entity data structure is the same as stored in a repository.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.compare_entity_data_to_version(entity_id=deserialize_param(entity_id_json, 'EntityId'), version_id=version_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'compare_entity_data_to_version'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_entity_data_info(version_id: str, entity_id_json: str) -> str:
    """
    Get entity data info (getEntityDataInfo)  # noqa: E501

Retrieves short info about the remote entity by external id at a concrete version.  Returned entity data info contains following properties: `hasRelations` (whether stored entity data contains relations), `hasAttributes` (contains attributes) and `hasCredentials` (whether stored device data has credentials).  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_entity_data_info(version_id=version_id, entity_id=deserialize_param(entity_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_entity_data_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_version_create_request_status(request_id: str) -> str:
    """
    Get version create request status (getVersionCreateRequestStatus)  # noqa: E501

Returns the status of previously made version create request.   This status contains following properties: - `done` - whether request processing is finished; - `version` - created version info: timestamp, version id (commit hash), commit name and commit author; - `added` - count of items that were created in the remote repo; - `modified` - modified items count; - `removed` - removed items count; - `error` - error message, if an error occurred while handling the request.  An example of successful status: ```json {   "done": true,   "added": 10,   "modified": 2,   "removed": 5,   "version": {     "timestamp": 1655198528000,     "id":"8a834dd389ed80e0759ba8ee338b3f1fd160a114",     "name": "My devices v2.0",     "author": "John Doe"   },   "error": null } ```  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_version_create_request_status(request_id=request_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_version_create_request_status'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_version_load_request_status(request_id: str) -> str:
    """
    Get version load request status (getVersionLoadRequestStatus)  # noqa: E501

Returns the status of previously made version load request. The structure contains following parameters: - `done` - if the request was successfully processed; - `result` - a list of load results for each entity type:      - `created` - created entities count;      - `updated` - updated entities count;      - `deleted` - removed entities count. - `error` - if an error occurred during processing, error info:      - `type` - error type;      - `source` - an external id of remote entity;      - `target` - if failed to find referenced entity by external id - this external id;      - `message` - error message.  An example of successfully processed request status: ```json {   "done": true,   "result": [     {       "entityType": "DEVICE",       "created": 10,       "updated": 5,       "deleted": 5     },      {       "entityType": "ASSET",       "created": 4,       "updated": 0,       "deleted": 8     }   ] } ```  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_version_load_request_status(request_id=request_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_version_load_request_status'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def list_all_entities_at_version(version_id: str) -> str:
    """
    List all entities at version (listAllEntitiesAtVersion)  # noqa: E501

Returns a list of all remote entities available in a specific version. Response type is the same as for listAllEntitiesAtVersion API method.  Returned entities order will be the same as in the repository.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.list_all_entities_at_version(version_id=version_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'list_all_entities_at_version'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def list_branches() -> str:
    """
    List branches (listBranches)  # noqa: E501

Lists branches available in the remote repository.   Response example:  ```json [   {     "name": "master",     "default": true   },   {     "name": "dev",     "default": false   },   {     "name": "dev-2",     "default": false   } ] ```  # noqa: E501
    """
    try:
        client = get_client()
        result = client.list_branches()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'list_branches'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def list_entities_at_version(entity_type: str, version_id: str) -> str:
    """
    List entities at version (listEntitiesAtVersion)  # noqa: E501

Returns a list of remote entities of a specific entity type that are available at a concrete version.  Each entity item in the result has `externalId` property. Entities order will be the same as in the repository.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.list_entities_at_version(entity_type=entity_type, version_id=version_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'list_entities_at_version'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def list_entity_type_versions(entity_type: str, branch: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    List entity type versions (listEntityTypeVersions)  # noqa: E501

Returns list of versions of an entity type in a branch. This is a collected list of versions that were created for entities of this type in a remote branch.  If specified branch does not exist - empty page data will be returned. The response structure is the same as for `listEntityVersions` API method.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.list_entity_type_versions(entity_type=entity_type, branch=branch, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'list_entity_type_versions'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def list_entity_versions(entity_type: str, external_entity_uuid: str, branch: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    List entity versions (listEntityVersions)  # noqa: E501

Returns list of versions for a specific entity in a concrete branch.  You need to specify external id of an entity to list versions for. This is `externalId` property of an entity, or otherwise if not set - simply id of this entity.  If specified branch does not exist - empty page data will be returned.   Each version info item has timestamp, id, name and author. Version id can then be used to restore the version. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Response example:  ```json {   "data": [     {       "timestamp": 1655198593000,       "id": "fd82625bdd7d6131cf8027b44ee967012ecaf990",       "name": "Devices and assets - v2.0",       "author": "John Doe <johndoe@gmail.com>"     },     {       "timestamp": 1655198528000,       "id": "682adcffa9c8a2f863af6f00c4850323acbd4219",       "name": "Update my device",       "author": "John Doe <johndoe@gmail.com>"     },     {       "timestamp": 1655198280000,       "id": "d2a6087c2b30e18cc55e7cdda345a8d0dfb959a4",       "name": "Devices and assets - v1.0",       "author": "John Doe <johndoe@gmail.com>"     }   ],   "totalPages": 1,   "totalElements": 3,   "hasNext": false } ```  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.list_entity_versions(entity_type=entity_type, external_entity_uuid=external_entity_uuid, branch=branch, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'list_entity_versions'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def list_versions(branch: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    List all versions (listVersions)  # noqa: E501

Lists all available versions in a branch for all entity types.  If specified branch does not exist - empty page data will be returned. The response format is the same as for `listEntityVersions` API method.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.list_versions(branch=branch, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'list_versions'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def load_entities_version(body_json: str = None) -> str:
    """
    Load entities version (loadEntitiesVersion)  # noqa: E501

Loads specific version of remote entities (or single entity) by request. Supported entity types: CUSTOMER, ASSET, RULE_CHAIN, DASHBOARD, DEVICE_PROFILE, DEVICE, ENTITY_VIEW, WIDGETS_BUNDLE.  There are multiple types of request. Each of them requires branch name (`branch`) and version id (`versionId`). Request of type `SINGLE_ENTITY` is needed to restore a concrete version of a specific entity. It contains id of a remote entity (`externalEntityId`) and additional configuration (`config`): - `loadRelations` - to update relations list (in case `saveRelations` option was enabled during version creation); - `loadAttributes` - to load entity attributes (if `saveAttributes` config option was enabled); - `loadCredentials` - to update device credentials (if `saveCredentials` option was enabled during version creation).  An example of such request: ```json {   "type": "SINGLE_ENTITY",      "branch": "dev",   "versionId": "b3c28d722d328324c7c15b0b30047b0c40011cf7",      "externalEntityId": {     "entityType": "DEVICE",     "id": "b7944123-d4f4-11ec-847b-0f432358ab48"   },   "config": {     "loadRelations": false,     "loadAttributes": true,     "loadCredentials": true   } } ```  Another request type (`ENTITY_TYPE`) is needed to load specific version of the whole entity types. It contains a structure with entity types to load and configs for each entity type (`entityTypes`). For each specified entity type, the method will load all remote entities of this type that are present at the version. A config for each entity type contains the same options as in `SINGLE_ENTITY` request type, and additionally contains following options: - `removeOtherEntities` - to remove local entities that are not present on the remote - basically to    overwrite local entity type with the remote one; - `findExistingEntityByName` - when you are loading some remote entities that are not yet present at this tenant,    try to find existing entity by name and update it rather than create new.  Here is an example of the request to completely restore version of the whole device entity type: ```json {   "type": "ENTITY_TYPE",    "branch": "dev",   "versionId": "b3c28d722d328324c7c15b0b30047b0c40011cf7",    "entityTypes": {     "DEVICE": {       "removeOtherEntities": true,       "findExistingEntityByName": false,       "loadRelations": true,       "loadAttributes": true,       "loadCredentials": true     }   } } ```  The response will contain generated request UUID that is to be used to check the status of operation via `getVersionLoadRequestStatus`.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (VersionLoadRequest):
    - `version_id` (str)
    - `type` (str)
    """
    try:
        client = get_client()
        result = client.load_entities_version(body=deserialize_param(body_json, 'VersionLoadRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'load_entities_version'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_entities_version(body_json: str = None) -> str:
    """
    Save entities version (saveEntitiesVersion)  # noqa: E501

Creates a new version of entities (or a single entity) by request. Supported entity types: CUSTOMER, ASSET, RULE_CHAIN, DASHBOARD, DEVICE_PROFILE, DEVICE, ENTITY_VIEW, WIDGETS_BUNDLE.  There are two available types of request: `SINGLE_ENTITY` and `COMPLEX`. Each of them contains version name (`versionName`) and name of a branch (`branch`) to create version (commit) in. If specified branch does not exists in a remote repo, then new empty branch will be created. Request of the `SINGLE_ENTITY` type has id of an entity (`entityId`) and additional configuration (`config`) which has following options:  - `saveRelations` - whether to add inbound and outbound relations of type COMMON to created entity version; - `saveAttributes` - to save attributes of server scope (and also shared scope for devices); - `saveCredentials` - when saving a version of a device, to add its credentials to the version.  An example of a `SINGLE_ENTITY` version create request: ```json {   "type": "SINGLE_ENTITY",    "versionName": "Version 1.0",   "branch": "dev",    "entityId": {     "entityType": "DEVICE",     "id": "b79448e0-d4f4-11ec-847b-0f432358ab48"   },   "config": {     "saveRelations": true,     "saveAttributes": true,     "saveCredentials": false   } } ```  Second request type (`COMPLEX`), additionally to `branch` and `versionName`, contains following properties: - `entityTypes` - a structure with entity types to export and configuration for each entity type;    this configuration has all the options available for `SINGLE_ENTITY` and additionally has these ones:       - `allEntities` and `entityIds` - if you want to save the version of all entities of the entity type         then set `allEntities` param to true, otherwise set it to false and specify the list of specific entities (`entityIds`);      - `syncStrategy` - synchronization strategy to use for this entity type: when set to `OVERWRITE`         then the list of remote entities of this type will be overwritten by newly added entities. If set to         `MERGE` - existing remote entities of this entity type will not be removed, new entities will just         be added on top (or existing remote entities will be updated). - `syncStrategy` - default synchronization strategy to use when it is not specified for an entity type.  Example for this type of request: ```json {   "type": "COMPLEX",    "versionName": "Devices and profiles: release 2",   "branch": "master",    "syncStrategy": "OVERWRITE",   "entityTypes": {     "DEVICE": {       "syncStrategy": null,       "allEntities": true,       "saveRelations": true,       "saveAttributes": true,       "saveCredentials": true     },     "DEVICE_PROFILE": {       "syncStrategy": "MERGE",       "allEntities": false,       "entityIds": [         "b79448e0-d4f4-11ec-847b-0f432358ab48"       ],       "saveRelations": true     }   } } ```  Response wil contain generated request UUID, that can be then used to retrieve status of operation via `getVersionCreateRequestStatus`.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (VersionCreateRequest):
    - `version_name` (str)
    - `branch` (str)
    - `type` (str)
    """
    try:
        client = get_client()
        result = client.save_entities_version(body=deserialize_param(body_json, 'VersionCreateRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_entities_version'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( compare_entity_data_to_version )
    mcp.tool()( get_entity_data_info )
    mcp.tool()( get_version_create_request_status )
    mcp.tool()( get_version_load_request_status )
    mcp.tool()( list_all_entities_at_version )
    mcp.tool()( list_branches )
    mcp.tool()( list_entities_at_version )
    mcp.tool()( list_entity_type_versions )
    mcp.tool()( list_entity_versions )
    mcp.tool()( list_versions )
    mcp.tool()( load_entities_version )
    mcp.tool()( save_entities_version )
