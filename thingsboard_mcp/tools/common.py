import json
from typing import Optional
from .shared import get_client, deserialize_param, format_response, ApiException


def accept_terms_of_use() -> str:
    """
    Accept Terms of Use (acceptTermsOfUse)  # noqa: E501

Accept Terms of Use by the current user.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: JsonNode
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.accept_terms_of_use()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'accept_terms_of_use'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def activate_email(email_code: str, pkg_name: Optional[str] = None) -> str:
    """
    Activate User using code from Email (activateEmail)  # noqa: E501

Activate the user using code(link) from the activation email. Validates the code an redirects according to the signup flow. Checks that user was not activated yet.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str email_code: Activation token. (required)
:param str pkg_name: Optional package name of the mobile application.
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.activate_email(email_code=email_code, pkg_name=pkg_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'activate_email'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def activate_instance(license_secret: str, release_date: str) -> str:
    """
    Activate edge instance (activateInstance)  # noqa: E501

Activates edge license on license portal.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str license_secret: licenseSecret (required)
:param str release_date: releaseDate (required)
:return: JsonNode
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.activate_instance(license_secret=license_secret, release_date=release_date)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'activate_instance'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def auto_commit_settings_exists() -> str:
    """
    Check auto commit settings exists (autoCommitSettingsExists)  # noqa: E501

Check whether the auto commit settings exists.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: bool
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.auto_commit_settings_exists()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'auto_commit_settings_exists'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def cancel_job(id_json: str) -> str:
    """
    Cancel job (cancelJob)  # noqa: E501

Cancels the job. The status of the job must be QUEUED, PENDING or RUNNING.  For a running job, all the tasks not yet processed will be discarded.  See the example of a cancelled job result in getJobById method description.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.cancel_job(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'cancel_job'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def change_password(body: Optional[str] = None) -> str:
    """
    Change password for current User (changePassword)  # noqa: E501

Change the password for the User which credentials are used to perform this REST API call. Be aware that previously generated [JWT](https://jwt.io/) tokens will be still valid until they expire.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param ChangePasswordRequest body:
:return: ObjectNode
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.change_password(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'change_password'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def check_activate_token(activate_token: str) -> str:
    """
    Check Activate User Token (checkActivateToken)  # noqa: E501

Checks the activation token and forwards user to 'Create Password' page. If token is valid, returns '303 See Other' (redirect) response code with the correct address of 'Create Password' page and same 'activateToken' specified in the URL parameters. If token is not valid, returns '409 Conflict'.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str activate_token: The activate token string. (required)
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.check_activate_token(activate_token=activate_token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'check_activate_token'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def check_instance(body_json: str = None) -> str:
    """
    Check edge license (checkInstance)  # noqa: E501

Checks license request from edge service by forwarding request to license portal.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param JsonNode body:
:return: JsonNode
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.check_instance(body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'check_instance'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def check_repository_access(body: Optional[str] = None) -> str:
    """
    Check repository access (checkRepositoryAccess)  # noqa: E501

Attempts to check repository access.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param RepositorySettings body:
:return: DeferredResultVoid
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.check_repository_access(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'check_repository_access'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def check_reset_token(reset_token: str) -> str:
    """
    Check password reset token (checkResetToken)  # noqa: E501

Checks the password reset token and forwards user to 'Reset Password' page. If token is valid, returns '303 See Other' (redirect) response code with the correct address of 'Reset Password' page and same 'resetToken' specified in the URL parameters. If token is not valid, returns '409 Conflict'.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str reset_token: The reset token string. (required)
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.check_reset_token(reset_token=reset_token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'check_reset_token'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def check_updates() -> str:
    """
    Check for new Platform Releases (checkUpdates)  # noqa: E501

Check notifications about new platform releases.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: UpdateMessage
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.check_updates()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'check_updates'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def chirp_stack_process_request_delete(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_delete(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'chirp_stack_process_request_delete'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def chirp_stack_process_request_get(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_get(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'chirp_stack_process_request_get'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def chirp_stack_process_request_head(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_head(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'chirp_stack_process_request_head'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def chirp_stack_process_request_options(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_options(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'chirp_stack_process_request_options'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def chirp_stack_process_request_patch(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_patch(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'chirp_stack_process_request_patch'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def chirp_stack_process_request_post(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_post(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'chirp_stack_process_request_post'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def chirp_stack_process_request_put(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_put(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'chirp_stack_process_request_put'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def clear_events_post(entity_id_json: str, body: Optional[str] = None, start_time: Optional[str] = None, end_time: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.clear_events_post(entity_id=deserialize_param(entity_id_json, 'EntityId'), body=body, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'clear_events_post'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def code_processing_url(code: str, state: str) -> str:
    """
    codeProcessingUrl  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str code: code (required)
:param str state: state (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.code_processing_url(code=code, state=state)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'code_processing_url'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def compare_entity_data_to_version(entity_id_json: str, version_id: str) -> str:
    """
    Compare entity data to version (compareEntityDataToVersion)  # noqa: E501

Returns an object with current entity data and the one at a specific version. Entity data structure is the same as stored in a repository.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str internal_entity_uuid: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str version_id: Version id, for example fd82625bdd7d6131cf8027b44ee967012ecaf990. Represents commit hash. (required)
:return: DeferredResultEntityDataDiff
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.compare_entity_data_to_version(entity_id=deserialize_param(entity_id_json, 'EntityId'), version_id=version_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'compare_entity_data_to_version'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def count_entities_by_query(body: Optional[str] = None) -> str:
    """
    Count Entities by Query  # noqa: E501

Allows to run complex queries to search the count of platform entities (devices, assets, customers, etc) based on the combination of main entity filter and multiple key filters. Returns the number of entities that match the query definition.  # Query Definition    Main **entity filter** is mandatory and defines generic search criteria. For example, "find all devices with profile 'Moisture Sensor'" or "Find all devices related to asset 'Building A'"  Optional **key filters** allow to filter results of the entity filter by complex criteria against main entity fields (name, label, type, etc), attributes and telemetry. For example, "temperature > 20 or temperature< 10" or "name starts with 'T', and attribute 'model' is 'T1000', and timeseries field 'batteryLevel' > 40".  Let's review the example:  ```json {   "entityFilter": {     "type": "entityType",     "entityType": "DEVICE"   },   "keyFilters": [     {       "key": {         "type": "ATTRIBUTE",         "key": "active"       },       "valueType": "BOOLEAN",       "predicate": {         "operation": "EQUAL",         "value": {           "defaultValue": true,           "dynamicValue": null         },         "type": "BOOLEAN"       }     }   ] } ```   Example mentioned above search all devices which have attribute 'active' set to 'true'. Now let's review available entity filters and key filters syntax:   # Entity Filters Entity Filter body depends on the 'type' parameter. Let's review available entity filter types. In fact, they do correspond to available dashboard aliases.  ## Single Entity  Allows to filter only one entity based on the id. For example, this entity filter selects certain device:  ```json {   "type": "singleEntity",   "singleEntity": {     "id": "d521edb0-2a7a-11ec-94eb-213c95f54092",     "entityType": "DEVICE"   } } ```  ## Entity List Filter  Allows to filter entities of the same type using their ids. For example, this entity filter selects two devices:  ```json {   "type": "entityList",   "entityType": "DEVICE",   "entityList": [     "e6501f30-2a7a-11ec-94eb-213c95f54092",     "e6657bf0-2a7a-11ec-94eb-213c95f54092"   ] } ```  ## Entity Name Filter  Allows to filter entities of the same type using the **'starts with'** expression over entity name. For example, this entity filter selects all devices which name starts with 'Air Quality':  ```json {   "type": "entityName",   "entityType": "DEVICE",   "entityNameFilter": "Air Quality" } ```  ## Entity Type Filter  Allows to filter entities based on their type (CUSTOMER, USER, DASHBOARD, ASSET, DEVICE, etc)For example, this entity filter selects all tenant customers:  ```json {   "type": "entityType",   "entityType": "CUSTOMER" } ```  ## Asset Type Filter  Allows to filter assets based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'charging station' assets which name starts with 'Tesla':  ```json {   "type": "assetType",   "assetType": "charging station",   "assetNameFilter": "Tesla" } ```  ## Device Type Filter  Allows to filter devices based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Temperature Sensor' devices which name starts with 'ABC':  ```json {   "type": "deviceType",   "deviceType": "Temperature Sensor",   "deviceNameFilter": "ABC" } ```  ## Edge Type Filter  Allows to filter edge instances based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Factory' edge instances which name starts with 'Nevada':  ```json {   "type": "edgeType",   "edgeType": "Factory",   "edgeNameFilter": "Nevada" } ```  ## Entity View Filter  Allows to filter entity views based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Concrete Mixer' entity views which name starts with 'CAT':  ```json {   "type": "entityViewType",   "entityViewType": "Concrete Mixer",   "entityViewNameFilter": "CAT" } ```  ## Api Usage Filter  Allows to query for Api Usage based on optional customer id. If the customer id is not set, returns current tenant API usage.For example, this entity filter selects the 'Api Usage' entity for customer with id 'e6501f30-2a7a-11ec-94eb-213c95f54092':  ```json {   "type": "apiUsageState",   "customerId": {     "id": "d521edb0-2a7a-11ec-94eb-213c95f54092",     "entityType": "CUSTOMER"   } } ```  ## Relations Query Filter  Allows to filter entities that are related to the provided root entity. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'filter' object allows you to define the relation type and set of acceptable entity types to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only those who match the 'filters'.  For example, this entity filter selects all devices and assets which are related to the asset with id 'e51de0c0-2a7a-11ec-94eb-213c95f54092':  ```json {   "type": "relationsQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e51de0c0-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 1,   "fetchLastLevelOnly": false,   "filters": [     {       "relationType": "Contains",       "entityTypes": [         "DEVICE",         "ASSET"       ]     }   ] } ```  ## Asset Search Query  Allows to filter assets that are related to the provided root entity. Filters related assets based on the relation type and set of asset types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'assetTypes' defines the type of the asset to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only assets that match 'relationType' and 'assetTypes' conditions.  For example, this entity filter selects 'charging station' assets which are related to the asset with id 'e51de0c0-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "assetSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e51de0c0-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 1,   "fetchLastLevelOnly": false,   "relationType": "Contains",   "assetTypes": [     "charging station"   ] } ```  ## Device Search Query  Allows to filter devices that are related to the provided root entity. Filters related devices based on the relation type and set of device types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'deviceTypes' defines the type of the device to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only devices that match 'relationType' and 'deviceTypes' conditions.  For example, this entity filter selects 'Charging port' and 'Air Quality Sensor' devices which are related to the asset with id 'e52b0020-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "deviceSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e52b0020-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 2,   "fetchLastLevelOnly": true,   "relationType": "Contains",   "deviceTypes": [     "Air Quality Sensor",     "Charging port"   ] } ```  ## Entity View Query  Allows to filter entity views that are related to the provided root entity. Filters related entity views based on the relation type and set of entity view types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'entityViewTypes' defines the type of the entity view to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only devices that match 'relationType' and 'deviceTypes' conditions.  For example, this entity filter selects 'Concrete mixer' entity views which are related to the asset with id 'e52b0020-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "entityViewSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e52b0020-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 1,   "fetchLastLevelOnly": false,   "relationType": "Contains",   "entityViewTypes": [     "Concrete mixer"   ] } ```  ## Edge Search Query  Allows to filter edge instances that are related to the provided root entity. Filters related edge instances based on the relation type and set of edge types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'deviceTypes' defines the type of the device to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only devices that match 'relationType' and 'deviceTypes' conditions.  For example, this entity filter selects 'Factory' edge instances which are related to the asset with id 'e52b0020-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "deviceSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e52b0020-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 2,   "fetchLastLevelOnly": true,   "relationType": "Contains",   "edgeTypes": [     "Factory"   ] } ```   # Key Filters Key Filter allows you to define complex logical expressions over entity field, attribute or latest time-series value. The filter is defined using 'key', 'valueType' and 'predicate' objects. Single Entity Query may have zero, one or multiple predicates. If multiple filters are defined, they are evaluated using logical 'AND'. The example below checks that temperature of the entity is above 20 degrees:  ```json {   "key": {     "type": "TIME_SERIES",     "key": "temperature"   },   "valueType": "NUMERIC",   "predicate": {     "operation": "GREATER",     "value": {       "defaultValue": 20,       "dynamicValue": null     },     "type": "NUMERIC"   } } ```   Now let's review 'key', 'valueType' and 'predicate' objects in detail.  ## Filter Key  Filter Key defines either entity field, attribute or telemetry. It is a JSON object that consists the key name and type. The following filter key types are supported:    * 'CLIENT_ATTRIBUTE' - used for client attributes;   * 'SHARED_ATTRIBUTE' - used for shared attributes;   * 'SERVER_ATTRIBUTE' - used for server attributes;   * 'ATTRIBUTE' - used for any of the above;   * 'TIME_SERIES' - used for time-series values;   * 'ENTITY_FIELD' - used for accessing entity fields like 'name', 'label', etc. The list of available fields depends on the entity type;   * 'ALARM_FIELD' - similar to entity field, but is used in alarm queries only;     Let's review the example:  ```json {   "type": "TIME_SERIES",   "key": "temperature" } ```  ## Value Type and Operations  Provides a hint about the data type of the entity field that is defined in the filter key. The value type impacts the list of possible operations that you may use in the corresponding predicate. For example, you may use 'STARTS_WITH' or 'END_WITH', but you can't use 'GREATER_OR_EQUAL' for string values.The following filter value types and corresponding predicate operations are supported:    * 'STRING' - used to filter any 'String' or 'JSON' values. Operations: EQUAL, NOT_EQUAL, STARTS_WITH, ENDS_WITH, CONTAINS, NOT_CONTAINS;   * 'NUMERIC' - used for 'Long' and 'Double' values. Operations: EQUAL, NOT_EQUAL, GREATER, LESS, GREATER_OR_EQUAL, LESS_OR_EQUAL;   * 'BOOLEAN' - used for boolean values. Operations: EQUAL, NOT_EQUAL;  * 'DATE_TIME' - similar to numeric, transforms value to milliseconds since epoch. Operations: EQUAL, NOT_EQUAL, GREATER, LESS, GREATER_OR_EQUAL, LESS_OR_EQUAL;    ## Filter Predicate  Filter Predicate defines the logical expression to evaluate. The list of available operations depends on the filter value type, see above. Platform supports 4 predicate types: 'STRING', 'NUMERIC', 'BOOLEAN' and 'COMPLEX'. The last one allows to combine multiple operations over one filter key.  Simple predicate example to check 'value < 100':   ```json {   "operation": "LESS",   "value": {     "defaultValue": 100,     "dynamicValue": null   },   "type": "NUMERIC" } ```  Complex predicate example, to check 'value < 10 or value > 20':   ```json {   "type": "COMPLEX",   "operation": "OR",   "predicates": [     {       "operation": "LESS",       "value": {         "defaultValue": 10,         "dynamicValue": null       },       "type": "NUMERIC"     },     {       "operation": "GREATER",       "value": {         "defaultValue": 20,         "dynamicValue": null       },       "type": "NUMERIC"     }   ] } ```  More complex predicate example, to check 'value < 10 or (value > 50 && value < 60)':   ```json {   "type": "COMPLEX",   "operation": "OR",   "predicates": [     {       "operation": "LESS",       "value": {         "defaultValue": 10,         "dynamicValue": null       },       "type": "NUMERIC"     },     {       "type": "COMPLEX",       "operation": "AND",       "predicates": [         {           "operation": "GREATER",           "value": {             "defaultValue": 50,             "dynamicValue": null           },           "type": "NUMERIC"         },         {           "operation": "LESS",           "value": {             "defaultValue": 60,             "dynamicValue": null           },           "type": "NUMERIC"         }       ]     }   ] } ```   You may also want to replace hardcoded values (for example, temperature > 20) with the more dynamic expression (for example, temperature > 'value of the tenant attribute with key 'temperatureThreshold'). It is possible to use 'dynamicValue' to define attribute of the tenant, customer or user that is performing the API call. See example below:   ```json {   "operation": "GREATER",   "value": {     "defaultValue": 0,     "dynamicValue": {       "sourceType": "CURRENT_USER",       "sourceAttribute": "temperatureThreshold"     }   },   "type": "NUMERIC" } ```   Note that you may use 'CURRENT_USER', 'CURRENT_CUSTOMER' and 'CURRENT_TENANT' as a 'sourceType'. The 'defaultValue' is used when the attribute with such a name is not defined for the chosen source.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param EntityCountQuery body:
:return: int
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.count_entities_by_query(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'count_entities_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def create_custom_menu(body: Optional[str] = None, assign_to_list_json: str = None, force: Optional[str] = None) -> str:
    """
    Create Custom Menu (createCustomMenu)  # noqa: E501

The api is designed to create Custom Menu without configuration. Is not applicable for update.  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param CustomMenuInfo body: (required)
:param list[object] assign_to_list: A list of entity ids, separated by comma ','
:param bool force: Use force if you want to create default menu that conflicts with the existing one (old one will be update NO_ASSIGN assignee type)
:return: CustomMenu
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.create_custom_menu(body=body, assign_to_list=json.loads(assign_to_list_json) if assign_to_list_json else None, force=force)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'create_custom_menu'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def create_notification_request(body_json: str) -> str:
    """
    Create notification request (createNotificationRequest)  # noqa: E501

Processes notification request. Mandatory request properties are `targets` (list of targets ids to send notification to), and either `templateId` (existing notification template id) or `template` (to send notification without saving the template). Optionally, you can set `sendingDelayInSec` inside the `additionalConfig` field to schedule the notification.  For each enabled delivery method in the notification template, there must be a target in the `targets` list that supports this delivery method: if you chose `WEB`, `EMAIL` or `SMS` - there must be at least one target in `targets` of `PLATFORM_USERS` type. For `SLACK` delivery method - you need to chose at least one `SLACK` notification target.  Notification request object with `PROCESSING` status will be returned immediately, and the notification sending itself is done asynchronously. After all notifications are sent, the `status` of the request becomes `SENT`. Use `getNotificationRequestById` to see the notification request processing status and some sending stats.   Here is an example of notification request to one target using saved template: ```json {   "templateId": {     "entityType": "NOTIFICATION_TEMPLATE",     "id": "6dbc3670-e4dd-11ed-9401-dbcc5dff78be"   },   "targets": [     "320e3ed0-d785-11ed-a06c-21dd57dd88ca"   ],   "additionalConfig": {     "sendingDelayInSec": 0   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param NotificationRequest body:
:return: NotificationRequest
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.create_notification_request(body=deserialize_param(body_json, 'NotificationRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'create_notification_request'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_ai_model_by_id(ai_model_id_json: str) -> str:
    """
    Delete AI model by ID (deleteAiModelById)  # noqa: E501

Deletes the AI model record by its `id`. If a record with the specified `id` exists, the record is deleted and the endpoint returns `true`. If no such record exists, the endpoint returns `false`.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str model_uuid: ID of the AI model record (required)
:return: object
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_ai_model_by_id(ai_model_id=deserialize_param(ai_model_id_json, 'AiModelId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_ai_model_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_auto_commit_settings() -> str:
    """
    Delete auto commit settings (deleteAutoCommitSettings)  # noqa: E501

Deletes the auto commit settings.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_auto_commit_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_auto_commit_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_blob_entity(blob_entity_id_json: str) -> str:
    """
    Delete Blob Entity (deleteBlobEntity)  # noqa: E501

Delete Blob entity based on the provided Blob entity Id. Referencing non-existing Blob entity Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str blob_entity_id: A string value representing the blob entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_blob_entity(blob_entity_id=deserialize_param(blob_entity_id_json, 'BlobEntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_blob_entity'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_calculated_field(calculated_field_id: str) -> str:
    """
    Delete Calculated Field (deleteCalculatedField)  # noqa: E501

Deletes the calculated field. Referencing non-existing Calculated Field Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param object calculated_field_id: (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_calculated_field(calculated_field_id=calculated_field_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_calculated_field'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_client_registration_template(client_registration_template_id_json: str) -> str:
    """
    Delete OAuth2 client registration template by id (deleteClientRegistrationTemplate)  Available for users with 'SYS_ADMIN' authority.  # noqa: E501

Client registration template is OAuth2 provider configuration template with default settings for registering new OAuth2 clients  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str client_registration_template_id: String representation of client registration template id to delete (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_client_registration_template(client_registration_template_id=deserialize_param(client_registration_template_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_client_registration_template'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_current_login_white_label_params(customer_id_json: str) -> str:
    """
    Delete Login White Labeling configuration (deleteCurrentLoginWhiteLabelParams)  # noqa: E501

Delete the Login White Labeling configuration that corresponds to the authority of the user.   Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param object customer_id: A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_current_login_white_label_params(customer_id=deserialize_param(customer_id_json, 'CustomerId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_current_login_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_current_white_label_params(customer_id_json: str) -> str:
    """
    Delete General White Labeling configuration (deleteCurrentWhiteLabelParams)  # noqa: E501

Delete the White Labeling configuration that corresponds to the authority of the user.   Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param object customer_id: A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_current_white_label_params(customer_id=deserialize_param(customer_id_json, 'CustomerId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_current_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_custom_menu(custom_menu_id_json: str, force: Optional[str] = None) -> str:
    """
    Delete custom menu (deleteCustomMenu)  # noqa: E501

Deletes the custom menu based on the provided Custom Menu Id. Referencing non-existing custom menu Id will cause an error. If the custom menu is assigned to the list of users or customers bad request is returned.To delete a custom menu that has assignee list set 'force' request param to true   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str custom_menu_id: A string value representing the custom menu id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param bool force: Force set to true will unassign menu before deletion
:return: CustomMenuDeleteResult
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_custom_menu(custom_menu_id=deserialize_param(custom_menu_id_json, 'CustomMenuId'), force=force)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_custom_menu'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_custom_translation(locale_code: str) -> str:
    """
    Delete Custom Translation for specified locale (deleteCustomTranslation)  # noqa: E501

Delete entire custom translation settings for end-user  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str locale_code: Locale code (e.g. 'en_US'). (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_custom_translation(locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_custom_translation_key(locale_code: str, key_path: str) -> str:
    """
    Delete specified key of Custom Translation (deleteCustomTranslationKey)   # noqa: E501

The API call is designed to delete specified key of the custom translation and return as a result parent translation.(e.g. if tenant translation for key is 'value1' and customer translation is 'value2' then by deletinf key onn customer level you will get 'value1' in response)   Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str locale_code: Locale code (e.g. 'en_US'). (required)
:param str key_path: A string value representing key of the custom translation (e.g. 'notification.active'). (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_custom_translation_key(locale_code=locale_code, key_path=key_path)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_custom_translation_key'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_domain(domain_id_json: str) -> str:
    """
    Delete Domain by ID (deleteDomain)  # noqa: E501

Deletes Domain by ID. Referencing non-existing domain Id will cause an error.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_domain(domain_id=deserialize_param(domain_id_json, 'DomainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_domain'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_entity_view(entity_view_id_json: str) -> str:
    """
    Delete entity view (deleteEntityView)  # noqa: E501

Delete the EntityView object based on the provided entity view id.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_view_id: A string value representing the entity view id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_entity_view(entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_entity_view'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_image(_type: str, key: str, force: Optional[str] = None) -> str:
    """
    deleteImage  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str type: Type of the image: tenant or system (required)
:param str key: Image resource key, for example thermostats_dashboard_background.jpeg (required)
:param bool force: force
:return: TbImageDeleteResult
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_image(_type=_type, key=key, force=force)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_image'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_job(id_json: str) -> str:
    """
    deleteJob  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_job(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_job'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_mobile_app(mobile_app_id_json: str) -> str:
    """
    Delete Mobile App by ID (deleteMobileApp)  # noqa: E501

Deletes Mobile App by ID. Referencing non-existing mobile app Id will cause an error.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_mobile_app(mobile_app_id=deserialize_param(mobile_app_id_json, 'MobileAppId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_mobile_app'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_mobile_app_bundle(mobile_app_bundle_id_json: str) -> str:
    """
    Delete Mobile App Bundle by ID (deleteMobileAppBundle)  # noqa: E501

Deletes Mobile App Bundle by ID. Referencing non-existing mobile app bundle Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_mobile_app_bundle(mobile_app_bundle_id=deserialize_param(mobile_app_bundle_id_json, 'MobileAppBundleId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_mobile_app_bundle'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_notification(id: str) -> str:
    """
    Delete notification (deleteNotification)  # noqa: E501

Deletes notification by its id.  Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: id (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_notification(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_notification'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_notification_request(id: str) -> str:
    """
    Delete notification request (deleteNotificationRequest)  # noqa: E501

Deletes notification request by its id.  If the request has status `SENT` - all sent notifications for this request will be deleted. If it is `SCHEDULED`, the request will be cancelled.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: id (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_notification_request(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_notification_request'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_notification_rule(id: str) -> str:
    """
    Delete notification rule (deleteNotificationRule)  # noqa: E501

Deletes notification rule by id. Cancels all related scheduled notification requests (e.g. due to escalation table)  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: id (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_notification_rule(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_notification_rule'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_notification_target_by_id(id: str) -> str:
    """
    Delete notification target by id (deleteNotificationTargetById)  # noqa: E501

Deletes notification target by its id.  This target cannot be referenced by existing scheduled notification requests or any notification rules.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: id (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_notification_target_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_notification_target_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_notification_template_by_id(id: str) -> str:
    """
    Delete notification template by id (deleteNotificationTemplateById  # noqa: E501

Deletes notification template by its id.  This template cannot be referenced by existing scheduled notification requests or any notification rules.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: id (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_notification_template_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_notification_template_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_repository_settings() -> str:
    """
    Delete repository settings (deleteRepositorySettings)  # noqa: E501

Deletes the repository settings.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: DeferredResultVoid
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_repository_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_repository_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_rpc(rpc_id_json: str) -> str:
    """
    Delete persistent RPC  # noqa: E501

Deletes the persistent RPC request.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str rpc_id: A string value representing the rpc id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_rpc(rpc_id=deserialize_param(rpc_id_json, 'RpcId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_rpc'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_secret(secret_id_json: str) -> str:
    """
    Delete secret by ID (deleteSecret)  # noqa: E501

Deletes the secret. Referencing non-existing Secret Id will cause an error.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:return: TbSecretDeleteResult
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_secret(secret_id=deserialize_param(secret_id_json, 'SecretId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_secret'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_self_registration_params(domain_name: str) -> str:
    """
    deleteSelfRegistrationParams  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str domain_name: domainName (required)
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_self_registration_params(domain_name=domain_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_self_registration_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_web_self_registration_params() -> str:
    """
    deleteWebSelfRegistrationParams  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_web_self_registration_params()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_web_self_registration_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_blob_entity(blob_entity_id_json: str) -> str:
    """
    Download Blob Entity By Id (downloadBlobEntity)  # noqa: E501

Download report file based on the provided Blob entity Id. Referencing non-existing Blob entity Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str blob_entity_id: A string value representing the blob entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: Resource
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.download_blob_entity(blob_entity_id=deserialize_param(blob_entity_id_json, 'BlobEntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'download_blob_entity'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_full_translation(locale_code: str) -> str:
    """
    Download end-user all-to-one translation (downloadFullTranslation)  # noqa: E501

Fetch the end-user translation for the specified locale. The result is a json file with merged user custom translation, system language translation and default locale translation.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str locale_code: Locale code (e.g. 'en_US'). (required)
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.download_full_translation(locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'download_full_translation'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_gateway_docker_compose(device_id_json: str) -> str:
    """
    Download generated docker-compose.yml file for gateway (downloadGatewayDockerCompose)  # noqa: E501

Download generated docker-compose.yml for gateway.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str device_id: A string value representing the device id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: Resource
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.download_gateway_docker_compose(device_id=deserialize_param(device_id_json, 'DeviceId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'download_gateway_docker_compose'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_image(_type: str, key: str, if_none_match: str = "") -> str:
    """
    downloadImage  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str type: Type of the image: tenant or system (required)
:param str key: Image resource key, for example thermostats_dashboard_background.jpeg (required)
:param str if_none_match: If-None-Match
:return: ByteArrayResource
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.download_image(_type=_type, key=key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'download_image'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_image_preview(_type: str, key: str, if_none_match: str = "") -> str:
    """
    downloadImagePreview  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str type: Type of the image: tenant or system (required)
:param str key: Image resource key, for example thermostats_dashboard_background.jpeg (required)
:param str if_none_match: If-None-Match
:return: ByteArrayResource
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.download_image_preview(_type=_type, key=key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'download_image_preview'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_login_favicon(type: str, key: str, if_none_match: str) -> str:
    """
    downloadLoginFavicon  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str type: Type of the image: tenant or system (required)
:param str key: Image resource key, for example thermostats_dashboard_background.jpeg (required)
:param str if_none_match: If-None-Match
:return: ByteArrayResource
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.download_login_favicon(type=type, key=key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'download_login_favicon'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_login_logo(type: str, key: str, if_none_match: str) -> str:
    """
    downloadLoginLogo  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str type: Type of the image: tenant or system (required)
:param str key: Image resource key, for example thermostats_dashboard_background.jpeg (required)
:param str if_none_match: If-None-Match
:return: ByteArrayResource
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.download_login_logo(type=type, key=key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'download_login_logo'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_public_image(public_resource_key: str, if_none_match: str = "") -> str:
    """
    downloadPublicImage  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str public_resource_key: publicResourceKey (required)
:param str if_none_match: If-None-Match
:return: ByteArrayResource
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.download_public_image(public_resource_key=public_resource_key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'download_public_image'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_server_certificate(protocol: str) -> str:
    """
    Download server certificate using file path defined in device.connectivity properties (downloadServerCertificate)  # noqa: E501

Download server certificate.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str protocol: A string value representing the device connectivity protocol. Possible values: 'mqtt', 'mqtts', 'http', 'https', 'coap', 'coaps' (required)
:return: Resource
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.download_server_certificate(protocol=protocol)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'download_server_certificate'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def export_image(_type: str, key: str) -> str:
    """
    exportImage  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str type: Type of the image: tenant or system (required)
:param str key: Image resource key, for example thermostats_dashboard_background.jpeg (required)
:return: ImageExportData
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.export_image(_type=_type, key=key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'export_image'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_from(from_id_json: str, relation_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    Get List of Relations (findByFrom)  # noqa: E501

Returns list of relation objects for the specified entity by the 'from' direction and relation type.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str from_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str from_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str relation_type: A string value representing relation type between entities. For example, 'Contains', 'Manages'. It can be any string value. (required)
:param str relation_type_group: A string value representing relation type group. For example, 'COMMON'
:return: list[EntityRelation]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.find_by_from(from_id=deserialize_param(from_id_json, 'EntityId'), relation_type=relation_type, relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_by_from'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_from_v1(from_id_json: str, from_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_by_from_v1(from_id=deserialize_param(from_id_json, 'EntityId'), from_type=from_type, relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_by_from_v1'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_query(body: Optional[str] = None) -> str:
    """
    Find related assets (findByQuery)  # noqa: E501

Returns all assets that are related to the specific entity. The entity id, relation type, asset types, depth of the search, and other query parameters defined using complex 'AssetSearchQuery' object. See 'Model' tab of the Parameters for more info.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param AssetSearchQuery body:
:return: list[Asset]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.find_by_query(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_query_v1(body: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_by_query_v1(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_by_query_v1'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_query_v2(body: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_by_query_v2(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_by_query_v2'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_query_v3(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_by_query_v3(body=deserialize_param(body_json, 'EntityRelationsQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_by_query_v3'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_query_v4(body: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_by_query_v4(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_by_query_v4'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_to(to_id_json: str, relation_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    Get List of Relations (findByTo)  # noqa: E501

Returns list of relation objects for the specified entity by the 'to' direction and relation type.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str to_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str to_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str relation_type: A string value representing relation type between entities. For example, 'Contains', 'Manages'. It can be any string value. (required)
:param str relation_type_group: A string value representing relation type group. For example, 'COMMON'
:return: list[EntityRelation]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.find_by_to(to_id=deserialize_param(to_id_json, 'EntityId'), relation_type=relation_type, relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_by_to'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_to_v1(to_id_json: str, to_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_by_to_v1(to_id=deserialize_param(to_id_json, 'EntityId'), to_type=to_type, relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_by_to_v1'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_entity_data_by_query(body: Optional[str] = None) -> str:
    """
    Find Entity Data by Query  # noqa: E501

Allows to run complex queries over platform entities (devices, assets, customers, etc) based on the combination of main entity filter and multiple key filters. Returns the paginated result of the query that contains requested entity fields and latest values of requested attributes and time-series data.  # Query Definition    Main **entity filter** is mandatory and defines generic search criteria. For example, "find all devices with profile 'Moisture Sensor'" or "Find all devices related to asset 'Building A'"  Optional **key filters** allow to filter results of the **entity filter** by complex criteria against main entity fields (name, label, type, etc), attributes and telemetry. For example, "temperature > 20 or temperature< 10" or "name starts with 'T', and attribute 'model' is 'T1000', and timeseries field 'batteryLevel' > 40".  The **entity fields** and **latest values** contains list of entity fields and latest attribute/telemetry fields to fetch for each entity.  The **page link** contains information about the page to fetch and the sort ordering.  Let's review the example:  ```json {   "entityFilter": {     "type": "entityType",     "resolveMultiple": true,     "entityType": "DEVICE"   },   "keyFilters": [     {       "key": {         "type": "TIME_SERIES",         "key": "temperature"       },       "valueType": "NUMERIC",       "predicate": {         "operation": "GREATER",         "value": {           "defaultValue": 0,           "dynamicValue": {             "sourceType": "CURRENT_USER",             "sourceAttribute": "temperatureThreshold",             "inherit": false           }         },         "type": "NUMERIC"       }     }   ],   "entityFields": [     {       "type": "ENTITY_FIELD",       "key": "name"     },     {       "type": "ENTITY_FIELD",       "key": "label"     },     {       "type": "ENTITY_FIELD",       "key": "additionalInfo"     }   ],   "latestValues": [     {       "type": "ATTRIBUTE",       "key": "model"     },     {       "type": "TIME_SERIES",       "key": "temperature"     }   ],   "pageLink": {     "page": 0,     "pageSize": 10,     "sortOrder": {       "key": {         "key": "name",         "type": "ENTITY_FIELD"       },       "direction": "ASC"     }   } } ```   Example mentioned above search all devices which have attribute 'active' set to 'true'. Now let's review available entity filters and key filters syntax:   # Entity Filters Entity Filter body depends on the 'type' parameter. Let's review available entity filter types. In fact, they do correspond to available dashboard aliases.  ## Single Entity  Allows to filter only one entity based on the id. For example, this entity filter selects certain device:  ```json {   "type": "singleEntity",   "singleEntity": {     "id": "d521edb0-2a7a-11ec-94eb-213c95f54092",     "entityType": "DEVICE"   } } ```  ## Entity List Filter  Allows to filter entities of the same type using their ids. For example, this entity filter selects two devices:  ```json {   "type": "entityList",   "entityType": "DEVICE",   "entityList": [     "e6501f30-2a7a-11ec-94eb-213c95f54092",     "e6657bf0-2a7a-11ec-94eb-213c95f54092"   ] } ```  ## Entity Name Filter  Allows to filter entities of the same type using the **'starts with'** expression over entity name. For example, this entity filter selects all devices which name starts with 'Air Quality':  ```json {   "type": "entityName",   "entityType": "DEVICE",   "entityNameFilter": "Air Quality" } ```  ## Entity Type Filter  Allows to filter entities based on their type (CUSTOMER, USER, DASHBOARD, ASSET, DEVICE, etc)For example, this entity filter selects all tenant customers:  ```json {   "type": "entityType",   "entityType": "CUSTOMER" } ```  ## Asset Type Filter  Allows to filter assets based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'charging station' assets which name starts with 'Tesla':  ```json {   "type": "assetType",   "assetType": "charging station",   "assetNameFilter": "Tesla" } ```  ## Device Type Filter  Allows to filter devices based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Temperature Sensor' devices which name starts with 'ABC':  ```json {   "type": "deviceType",   "deviceType": "Temperature Sensor",   "deviceNameFilter": "ABC" } ```  ## Edge Type Filter  Allows to filter edge instances based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Factory' edge instances which name starts with 'Nevada':  ```json {   "type": "edgeType",   "edgeType": "Factory",   "edgeNameFilter": "Nevada" } ```  ## Entity View Filter  Allows to filter entity views based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Concrete Mixer' entity views which name starts with 'CAT':  ```json {   "type": "entityViewType",   "entityViewType": "Concrete Mixer",   "entityViewNameFilter": "CAT" } ```  ## Api Usage Filter  Allows to query for Api Usage based on optional customer id. If the customer id is not set, returns current tenant API usage.For example, this entity filter selects the 'Api Usage' entity for customer with id 'e6501f30-2a7a-11ec-94eb-213c95f54092':  ```json {   "type": "apiUsageState",   "customerId": {     "id": "d521edb0-2a7a-11ec-94eb-213c95f54092",     "entityType": "CUSTOMER"   } } ```  ## Relations Query Filter  Allows to filter entities that are related to the provided root entity. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'filter' object allows you to define the relation type and set of acceptable entity types to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only those who match the 'filters'.  For example, this entity filter selects all devices and assets which are related to the asset with id 'e51de0c0-2a7a-11ec-94eb-213c95f54092':  ```json {   "type": "relationsQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e51de0c0-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 1,   "fetchLastLevelOnly": false,   "filters": [     {       "relationType": "Contains",       "entityTypes": [         "DEVICE",         "ASSET"       ]     }   ] } ```  ## Asset Search Query  Allows to filter assets that are related to the provided root entity. Filters related assets based on the relation type and set of asset types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'assetTypes' defines the type of the asset to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only assets that match 'relationType' and 'assetTypes' conditions.  For example, this entity filter selects 'charging station' assets which are related to the asset with id 'e51de0c0-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "assetSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e51de0c0-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 1,   "fetchLastLevelOnly": false,   "relationType": "Contains",   "assetTypes": [     "charging station"   ] } ```  ## Device Search Query  Allows to filter devices that are related to the provided root entity. Filters related devices based on the relation type and set of device types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'deviceTypes' defines the type of the device to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only devices that match 'relationType' and 'deviceTypes' conditions.  For example, this entity filter selects 'Charging port' and 'Air Quality Sensor' devices which are related to the asset with id 'e52b0020-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "deviceSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e52b0020-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 2,   "fetchLastLevelOnly": true,   "relationType": "Contains",   "deviceTypes": [     "Air Quality Sensor",     "Charging port"   ] } ```  ## Entity View Query  Allows to filter entity views that are related to the provided root entity. Filters related entity views based on the relation type and set of entity view types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'entityViewTypes' defines the type of the entity view to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only devices that match 'relationType' and 'deviceTypes' conditions.  For example, this entity filter selects 'Concrete mixer' entity views which are related to the asset with id 'e52b0020-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "entityViewSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e52b0020-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 1,   "fetchLastLevelOnly": false,   "relationType": "Contains",   "entityViewTypes": [     "Concrete mixer"   ] } ```  ## Edge Search Query  Allows to filter edge instances that are related to the provided root entity. Filters related edge instances based on the relation type and set of edge types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'deviceTypes' defines the type of the device to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only devices that match 'relationType' and 'deviceTypes' conditions.  For example, this entity filter selects 'Factory' edge instances which are related to the asset with id 'e52b0020-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "deviceSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e52b0020-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 2,   "fetchLastLevelOnly": true,   "relationType": "Contains",   "edgeTypes": [     "Factory"   ] } ```   # Key Filters Key Filter allows you to define complex logical expressions over entity field, attribute or latest time-series value. The filter is defined using 'key', 'valueType' and 'predicate' objects. Single Entity Query may have zero, one or multiple predicates. If multiple filters are defined, they are evaluated using logical 'AND'. The example below checks that temperature of the entity is above 20 degrees:  ```json {   "key": {     "type": "TIME_SERIES",     "key": "temperature"   },   "valueType": "NUMERIC",   "predicate": {     "operation": "GREATER",     "value": {       "defaultValue": 20,       "dynamicValue": null     },     "type": "NUMERIC"   } } ```   Now let's review 'key', 'valueType' and 'predicate' objects in detail.  ## Filter Key  Filter Key defines either entity field, attribute or telemetry. It is a JSON object that consists the key name and type. The following filter key types are supported:    * 'CLIENT_ATTRIBUTE' - used for client attributes;   * 'SHARED_ATTRIBUTE' - used for shared attributes;   * 'SERVER_ATTRIBUTE' - used for server attributes;   * 'ATTRIBUTE' - used for any of the above;   * 'TIME_SERIES' - used for time-series values;   * 'ENTITY_FIELD' - used for accessing entity fields like 'name', 'label', etc. The list of available fields depends on the entity type;   * 'ALARM_FIELD' - similar to entity field, but is used in alarm queries only;     Let's review the example:  ```json {   "type": "TIME_SERIES",   "key": "temperature" } ```  ## Value Type and Operations  Provides a hint about the data type of the entity field that is defined in the filter key. The value type impacts the list of possible operations that you may use in the corresponding predicate. For example, you may use 'STARTS_WITH' or 'END_WITH', but you can't use 'GREATER_OR_EQUAL' for string values.The following filter value types and corresponding predicate operations are supported:    * 'STRING' - used to filter any 'String' or 'JSON' values. Operations: EQUAL, NOT_EQUAL, STARTS_WITH, ENDS_WITH, CONTAINS, NOT_CONTAINS;   * 'NUMERIC' - used for 'Long' and 'Double' values. Operations: EQUAL, NOT_EQUAL, GREATER, LESS, GREATER_OR_EQUAL, LESS_OR_EQUAL;   * 'BOOLEAN' - used for boolean values. Operations: EQUAL, NOT_EQUAL;  * 'DATE_TIME' - similar to numeric, transforms value to milliseconds since epoch. Operations: EQUAL, NOT_EQUAL, GREATER, LESS, GREATER_OR_EQUAL, LESS_OR_EQUAL;    ## Filter Predicate  Filter Predicate defines the logical expression to evaluate. The list of available operations depends on the filter value type, see above. Platform supports 4 predicate types: 'STRING', 'NUMERIC', 'BOOLEAN' and 'COMPLEX'. The last one allows to combine multiple operations over one filter key.  Simple predicate example to check 'value < 100':   ```json {   "operation": "LESS",   "value": {     "defaultValue": 100,     "dynamicValue": null   },   "type": "NUMERIC" } ```  Complex predicate example, to check 'value < 10 or value > 20':   ```json {   "type": "COMPLEX",   "operation": "OR",   "predicates": [     {       "operation": "LESS",       "value": {         "defaultValue": 10,         "dynamicValue": null       },       "type": "NUMERIC"     },     {       "operation": "GREATER",       "value": {         "defaultValue": 20,         "dynamicValue": null       },       "type": "NUMERIC"     }   ] } ```  More complex predicate example, to check 'value < 10 or (value > 50 && value < 60)':   ```json {   "type": "COMPLEX",   "operation": "OR",   "predicates": [     {       "operation": "LESS",       "value": {         "defaultValue": 10,         "dynamicValue": null       },       "type": "NUMERIC"     },     {       "type": "COMPLEX",       "operation": "AND",       "predicates": [         {           "operation": "GREATER",           "value": {             "defaultValue": 50,             "dynamicValue": null           },           "type": "NUMERIC"         },         {           "operation": "LESS",           "value": {             "defaultValue": 60,             "dynamicValue": null           },           "type": "NUMERIC"         }       ]     }   ] } ```   You may also want to replace hardcoded values (for example, temperature > 20) with the more dynamic expression (for example, temperature > 'value of the tenant attribute with key 'temperatureThreshold'). It is possible to use 'dynamicValue' to define attribute of the tenant, customer or user that is performing the API call. See example below:   ```json {   "operation": "GREATER",   "value": {     "defaultValue": 0,     "dynamicValue": {       "sourceType": "CURRENT_USER",       "sourceAttribute": "temperatureThreshold"     }   },   "type": "NUMERIC" } ```   Note that you may use 'CURRENT_USER', 'CURRENT_CUSTOMER' and 'CURRENT_TENANT' as a 'sourceType'. The 'defaultValue' is used when the attribute with such a name is not defined for the chosen source.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param EntityDataQuery body:
:return: PageDataEntityData
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.find_entity_data_by_query(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_entity_data_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_info_by_from(from_id_json: str, relation_type_group: Optional[str] = None) -> str:
    """
    Get List of Relation Infos (findInfoByFrom)  # noqa: E501

Returns list of relation info objects for the specified entity by the 'from' direction.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer. Relation Info is an extension of the default Relation object that contains information about the 'from' and 'to' entity names.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str from_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str from_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str relation_type_group: A string value representing relation type group. For example, 'COMMON'
:return: list[EntityRelationInfo]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.find_info_by_from(from_id=deserialize_param(from_id_json, 'EntityId'), relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_info_by_from'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_info_by_query(body_json: str) -> str:
    """
    Find related entity infos (findInfoByQuery)  # noqa: E501

Returns all entity infos that are related to the specific entity. The entity id, relation type, entity types, depth of the search, and other query parameters defined using complex 'EntityRelationsQuery' object. See 'Model' tab of the Parameters for more info. Relation Info is an extension of the default Relation object that contains information about the 'from' and 'to' entity names.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param EntityRelationsQuery body:
:return: list[EntityRelationInfo]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.find_info_by_query(body=deserialize_param(body_json, 'EntityRelationsQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_info_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_info_by_to(to_id_json: str, to_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    Get List of Relation Infos (findInfoByTo)  # noqa: E501

Returns list of relation info objects for the specified entity by the 'to' direction.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer. Relation Info is an extension of the default Relation object that contains information about the 'from' and 'to' entity names.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str to_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param str to_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str relation_type_group: A string value representing relation type group. For example, 'COMMON'
:return: list[EntityRelationInfo]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.find_info_by_to(to_id=deserialize_param(to_id_json, 'EntityId'), to_type=to_type, relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'find_info_by_to'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def getName() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.getName()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'getName'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_activation_link(user_id_json: str) -> str:
    """
    Get the activation link (getActivationLink)  # noqa: E501

Get the activation link for the user. The base url for activation link is configurable in the general settings of system administrator.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str user_id: A string value representing the user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_activation_link(user_id=deserialize_param(user_id_json, 'UserId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_activation_link'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_activation_link_info(user_id_json: str) -> str:
    """
    Get activation link info (getActivationLinkInfo)  # noqa: E501

Get the activation link info for the user. The base url for activation link is configurable in the general settings of system administrator.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str user_id: A string value representing the user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: UserActivationLink
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_activation_link_info(user_id=deserialize_param(user_id_json, 'UserId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_activation_link_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_ai_model_by_id(ai_model_id_json: str) -> str:
    """
    Get AI model by ID (getAiModelById)  # noqa: E501

Fetches an AI model record by its `id`.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str model_uuid: ID of the AI model record (required)
:return: AiModel
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_ai_model_by_id(ai_model_id=deserialize_param(ai_model_id_json, 'AiModelId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_ai_model_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_ai_models(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get AI models (getAiModels)  # noqa: E501

Returns a page of AI models. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on the AI model name, provider and model ID.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataAiModel
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_ai_models(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_ai_models'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_all_entity_view_infos(page_size: int, page: int, include_customers: Optional[str] = None, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get All Entity View Infos for current user (getAllEntityViewInfos)  # noqa: E501

Returns a page of entity view info objects owned by the tenant or the customer of a current user. Entity Views Info extends the Entity View with owner name. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param bool include_customers: Include customer or sub-customer entities
:param str type:   ## Entity View Filter  Allows to filter entity views based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Concrete Mixer' entity views which name starts with 'CAT':  ```json {   "type": "entityViewType",   "entityViewType": "Concrete Mixer",   "entityViewNameFilter": "CAT" } ```
:param str text_search: The case insensitive 'substring' filter based on the entity view name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataEntityViewInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_all_entity_view_infos(page_size=page_size, page=page, include_customers=include_customers, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_all_entity_view_infos'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_application_redirect(user_agent: str) -> str:
    """
    getApplicationRedirect  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param object user_agent: (required)
:return: object
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_application_redirect(user_agent=user_agent)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_application_redirect'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_auto_commit_settings() -> str:
    """
    Get auto commit settings (getAutoCommitSettings)  # noqa: E501

Get the auto commit settings object.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: dict(str, AutoVersionCreateConfig)
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_auto_commit_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_auto_commit_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_available_delivery_methods() -> str:
    """
    Get available delivery methods (getAvailableDeliveryMethods)  # noqa: E501

Returns the list of delivery methods that are properly configured and are allowed to be used for sending notifications.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: list[str]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_available_delivery_methods()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_available_delivery_methods'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_available_java_locales() -> str:
    """
    Get list of available java locales (getAvailableJavaLocales)  # noqa: E501

The result is map where key is locale code and value is locale language and country  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: JsonNode
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_available_java_locales()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_available_java_locales'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_available_locales() -> str:
    """
    Get list of available locales (getAvailableLocales)  # noqa: E501

Fetch the list of customized locales from all levels  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: JsonNode
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_available_locales()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_available_locales'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_blob_entities(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[str] = None, end_time: Optional[str] = None) -> str:
    """
    Get Blob Entities (getBlobEntities)  # noqa: E501

Returns a page of BlobEntityWithCustomerInfo object that are available for the current user. The platform uses Blob(binary large object) entities in the reporting feature, in order to store Dashboard states snapshots of different content types in base64 format. BlobEntityWithCustomerInfo represents an object that contains base info about the blob entity(name, type, contentType, etc.) and info about the customer(customerTitle, customerIsPublic) of the user that scheduled generation of the dashboard report. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str type: A string value representing the blob entity type. For example, 'report'
:param str text_search: The case insensitive 'startsWith' filter based on the blob entity name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:param int start_time: The start timestamp in milliseconds of the search time range over the BlobEntityWithCustomerInfo class field: 'createdTime'.
:param int end_time: The end timestamp in milliseconds of the search time range over the BlobEntityWithCustomerInfo class field: 'createdTime'.
:return: PageDataBlobEntityWithCustomerInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_blob_entities(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_blob_entities'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_blob_entities_by_ids(blob_entity_ids_json: str) -> str:
    """
    Get Blob Entities By Ids (getBlobEntitiesByIds)  # noqa: E501

Requested blob entities must be owned by tenant or assigned to customer which user is performing the request. The platform uses Blob(binary large object) entities in the reporting feature, in order to store Dashboard states snapshots of different content types in base64 format. BlobEntityInfo represents an object that contains base info about the blob entity(name, type, contentType, etc.). See the 'Model' tab of the Response Class for more details.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str blob_entity_ids: A list of blob entity ids, separated by comma ',' (required)
:return: list[BlobEntityInfo]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_blob_entities_by_ids(blob_entity_ids=json.loads(blob_entity_ids_json) if blob_entity_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_blob_entities_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_blob_entity_info_by_id(blob_entity_id_json: str) -> str:
    """
    Get Blob Entity With Customer Info (getBlobEntityInfoById)  # noqa: E501

Fetch the BlobEntityWithCustomerInfo object based on the provided Blob entity Id. The platform uses Blob(binary large object) entities in the reporting feature, in order to store Dashboard states snapshots of different content types in base64 format. BlobEntityWithCustomerInfo represents an object that contains base info about the blob entity(name, type, contentType, etc.) and info about the customer(customerTitle, customerIsPublic) of the user that scheduled generation of the dashboard report. Referencing non-existing Blob entity Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str blob_entity_id: A string value representing the blob entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: BlobEntityWithCustomerInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_blob_entity_info_by_id(blob_entity_id=deserialize_param(blob_entity_id_json, 'BlobEntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_blob_entity_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_calculated_field_by_id(calculated_field_id: str) -> str:
    """
    Get Calculated Field (getCalculatedFieldById)  # noqa: E501

Fetch the Calculated Field object based on the provided Calculated Field Id.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param object calculated_field_id: (required)
:return: CalculatedField
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_calculated_field_by_id(calculated_field_id=calculated_field_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_calculated_field_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_calculated_fields_by_entity_id(entity_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Calculated Fields by Entity Id (getCalculatedFieldsByEntityId)  # noqa: E501

Fetch the Calculated Fields based on the provided Entity Id.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param object entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param object entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param object page_size: Maximum amount of entities in a one page (required)
:param object page: Sequence number of page starting from 0 (required)
:param object text_search: The case insensitive 'substring' filter based on the calculated field name.
:param object sort_property: Property of entity to sort by
:param object sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataCalculatedField
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_calculated_fields_by_entity_id(entity_id=deserialize_param(entity_id_json, 'EntityId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_calculated_fields_by_entity_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_client_registration_templates() -> str:
    """
    Get the list of all OAuth2 client registration templates (getClientRegistrationTemplates)  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501

Mail configuration template is set of default smtp settings for mail server that specific provider supports  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: JsonNode
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_client_registration_templates()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_client_registration_templates'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_client_registration_templates1() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_client_registration_templates1()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_client_registration_templates1'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_client_registration_templates_mail() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_client_registration_templates_mail()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_client_registration_templates_mail'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_component_descriptor_by_clazz(component_descriptor_clazz: str) -> str:
    """
    Get Component Descriptor (getComponentDescriptorByClazz)  # noqa: E501

Gets the Component Descriptor object using class name from the path parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str component_descriptor_clazz: Component Descriptor class name (required)
:return: ComponentDescriptor
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_component_descriptor_by_clazz(component_descriptor_clazz=component_descriptor_clazz)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_component_descriptor_by_clazz'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_component_descriptors_by_type(component_type: str, rule_chain_type: Optional[str] = None) -> str:
    """
    Get Component Descriptors (getComponentDescriptorsByType)  # noqa: E501

Gets the Component Descriptors using rule node type and optional rule chain type request parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str component_type: Type of the Rule Node (required)
:param str rule_chain_type: Type of the Rule Chain
:return: list[ComponentDescriptor]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_component_descriptors_by_type(component_type=component_type, rule_chain_type=rule_chain_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_component_descriptors_by_type'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_component_descriptors_by_types(component_types: str, rule_chain_type: Optional[str] = None) -> str:
    """
    Get Component Descriptors (getComponentDescriptorsByTypes)  # noqa: E501

Gets the Component Descriptors using coma separated list of rule node types and optional rule chain type request parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str component_types: List of types of the Rule Nodes, (ENRICHMENT, FILTER, TRANSFORMATION, ACTION or EXTERNAL) (required)
:param str rule_chain_type: Type of the Rule Chain
:return: list[ComponentDescriptor]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_component_descriptors_by_types(component_types=component_types, rule_chain_type=rule_chain_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_component_descriptors_by_types'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_current_login_white_label_params() -> str:
    """
    Get Login White Labeling configuration (getCurrentWhiteLabelParams)  # noqa: E501

Fetch the Login  White Labeling configuration that corresponds to the authority of the user. The API call is designed to load the Login White Labeling configuration for edition. So, the result is NOT merged with the parent level White Labeling configuration. Let's assume there is a custom White Labeling  configured on a system level. And there is no custom White Labeling  items configured on a tenant level. In such a case, the API call will return default object for the tenant administrator.   Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str customer_id: A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
:return: LoginWhiteLabelingParams
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_current_login_white_label_params()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_current_login_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_current_white_label_params() -> str:
    """
    Get White Labeling configuration (getCurrentWhiteLabelParams)  # noqa: E501

Fetch the White Labeling configuration that corresponds to the authority of the user. The API call is designed to load the White Labeling configuration for edition. So, the result is NOT merged with the parent level White Labeling configuration. Let's assume there is a custom White Labeling  configured on a system level. And there is no custom White Labeling  items configured on a tenant level. In such a case, the API call will return default object for the tenant administrator.   Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str customer_id: A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
:return: WhiteLabelingParams
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_current_white_label_params()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_current_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_custom_menu() -> str:
    """
    Get end-user Custom Menu configuration (getCustomMenu)  # noqa: E501

Fetch the Custom Menu object for the end user. The custom menu is configured in the white labeling parameters. If custom menu configuration on the tenant level is present, it overrides the menu configuration of the system level. Similar, if the custom menu configuration on the customer level is present, it overrides the menu configuration of the tenant level.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: CustomMenu
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_custom_menu()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_custom_menu'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_custom_menu_assignee_list(custom_menu_id_json: str) -> str:
    """
    Get Custom Menu assignee list (getCustomMenuAssigneeList)  # noqa: E501

Fetch the list of Entity Info objects that represents users or customers, or empty list if custom menu is not assigned or has NO_ASSIGN/ALL assignee type.  Security check is performed to verify that the user has 'READ' permission for the custom menu with specified id.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str custom_menu_id: A string value representing the custom menu id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: list[EntityInfo]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_custom_menu_assignee_list(custom_menu_id=deserialize_param(custom_menu_id_json, 'CustomMenuId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_custom_menu_assignee_list'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_custom_menu_config(custom_menu_id_json: str) -> str:
    """
    Get Custom Menu configuration by id (getCustomMenuConfig)  # noqa: E501

Fetch the Custom Menu configuration based on the provided Custom Menu Id.   Security check is performed to verify that the user has 'READ' permission for the custom menu with specified id.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str custom_menu_id: A string value representing the custom menu id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: CustomMenuConfig
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_custom_menu_config(custom_menu_id=deserialize_param(custom_menu_id_json, 'CustomMenuId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_custom_menu_config'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_custom_menu_info_by_id(custom_menu_id_json: str) -> str:
    """
    Get Custom Menu Info (getCustomMenuInfoById)  # noqa: E501

Fetch the Custom Menu Info object based on the provided Custom Menu Id.   Security check is performed to verify that the user has 'READ' permission for the custom menu with specified id.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str custom_menu_id: A string value representing the custom menu id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: CustomMenuInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_custom_menu_info_by_id(custom_menu_id=deserialize_param(custom_menu_id_json, 'CustomMenuId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_custom_menu_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_custom_menu_infos(page_size: int, page: int, scope: Optional[str] = None, assignee_type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get all custom menus configured at user level (getCustomMenuInfos)  # noqa: E501

Returns a page of custom menu info objects owned by the tenant or the customer of a current user, scope and assigneeType request parameters can be used to filter the result.  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str scope: Custom menu scope.
:param str assignee_type: Custom menu assignee type.
:param str text_search: The case insensitive 'substring' filter based on the custom menu name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataCustomMenuInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_custom_menu_infos(page_size=page_size, page=page, scope=scope, assignee_type=assignee_type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_custom_menu_infos'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_custom_translation(locale_code: str) -> str:
    """
    Get end-user Custom Translation configuration (getCustomTranslation)  # noqa: E501

Fetch the Custom Translation map for the end user. The custom translation is configured in the white labeling parameters. If custom translation translation is defined on the tenant level, it overrides the custom translation of the system level. Similar, if the custom translation is defined on the customer level, it overrides the translation configuration of the tenant level.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str locale_code: Locale code (e.g. 'en_US'). (required)
:return: CustomTranslation
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_custom_translation(locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_domain_info_by_id(domain_id_json: str) -> str:
    """
    Get Domain info by Id (getDomainInfoById)  # noqa: E501

  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:return: DomainInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_domain_info_by_id(domain_id=deserialize_param(domain_id_json, 'DomainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_domain_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_domain_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Domain infos (getDomainInfos)  # noqa: E501

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param object page_size: Maximum amount of entities in a one page (required)
:param object page: Sequence number of page starting from 0 (required)
:param object text_search: Case-insensitive 'substring' filter based on domain's name
:param object sort_property: Property of entity to sort by
:param object sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataDomainInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_domain_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_domain_infos'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_downlink_payload(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get downlink payload (getDownlinkPayload)  # noqa: E501

Returns payload example for the downlink converter for the vendor, integration type and model  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str integration_type: (required)
:param str vendor_name: (required)
:param str model: (required)
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_downlink_payload(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_downlink_payload'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edqs_state() -> str:
    """
    getEdqsState  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: EdqsState
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_edqs_state()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_edqs_state'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_entities(entity_group_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Group Entities (getEntities)  # noqa: E501

Returns a page of Short Entity View objects that belongs to specified Entity Group Id. Short Entity View object contains the entity id and number of fields (attributes, telemetry, etc). List of those fields is configurable and defined in the group configuration.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_group_id: A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'startsWith' filter based on the entity group name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataShortEntityView
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_entities(entity_group_id=deserialize_param(entity_group_id_json, 'EntityGroupId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_entities'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_entity_data_info(version_id: str, entity_id_json: str) -> str:
    """
    Get entity data info (getEntityDataInfo)  # noqa: E501

Retrieves short info about the remote entity by external id at a concrete version.  Returned entity data info contains following properties: `hasRelations` (whether stored entity data contains relations), `hasAttributes` (contains attributes) and `hasCredentials` (whether stored device data has credentials).  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str version_id: Version id, for example fd82625bdd7d6131cf8027b44ee967012ecaf990. Represents commit hash. (required)
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str external_entity_uuid: A string value representing external entity id (required)
:return: DeferredResultEntityDataInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_entity_data_info(version_id=version_id, entity_id=deserialize_param(entity_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_entity_data_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_entity_view_by_id(entity_view_id_json: str) -> str:
    """
    Get entity view (getEntityViewById)  # noqa: E501

Fetch the EntityView object based on the provided entity view id. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. See the 'Model' tab for more details.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_view_id: A string value representing the entity view id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: EntityView
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_entity_view_by_id(entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_entity_view_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_entity_view_info_by_id(entity_view_id_json: str) -> str:
    """
    Get entity view info (getEntityViewInfoById)  # noqa: E501

Fetch the Entity View info object based on the provided entity view id. Entity Views Info extends the Entity View with owner name. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. See the 'Model' tab for more details.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_view_id: A string value representing the entity view id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: EntityViewInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_entity_view_info_by_id(entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_entity_view_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_entity_view_types() -> str:
    """
    Get Entity View Types (getEntityViewTypes)  # noqa: E501

Returns a set of unique entity view types based on entity views that are either owned by the tenant or assigned to the customer which user is performing the request.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: list[EntitySubtype]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_entity_view_types()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_entity_view_types'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_entity_views_by_ids(entity_view_ids_json: str) -> str:
    """
    Get Entity Views By Ids (getEntityViewsByIds)  # noqa: E501

Requested entity views must be owned by tenant or assigned to customer which user is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_view_ids: A list of entity view ids, separated by comma ',' (required)
:return: list[EntityView]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_entity_views_by_ids(entity_view_ids=json.loads(entity_view_ids_json) if entity_view_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_entity_views_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_events_get(entity_id_json: str, tenant_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[str] = None, end_time: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_events_get(entity_id=deserialize_param(entity_id_json, 'EntityId'), tenant_id=deserialize_param(tenant_id_json, 'TenantId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_events_get'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_events_post(tenant_id_json: str, page_size: int, page: int, entity_id_json: str, body: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[str] = None, end_time: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_events_post(tenant_id=deserialize_param(tenant_id_json, 'TenantId'), page_size=page_size, page=page, entity_id=deserialize_param(entity_id_json, 'EntityId'), body=body, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_events_post'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_events_v1_get1(entity_id_json: str, event_type: str, tenant_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[str] = None, end_time: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_events_v1_get1(entity_id=deserialize_param(entity_id_json, 'EntityId'), event_type=event_type, tenant_id=deserialize_param(tenant_id_json, 'TenantId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_events_v1_get1'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_features_info() -> str:
    """
    Get features info (getFeaturesInfo)  # noqa: E501

Get information about enabled/disabled features.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: FeaturesInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_features_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_features_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_firmware(device_token: str, title: str, version: str, size: Optional[str] = None, chunk: Optional[str] = None) -> str:
    """
    Get Device Firmware (getFirmware)  # noqa: E501

Downloads the current firmware package.When the platform initiates firmware update, it informs the device by updating the 'fw_title', 'fw_version', 'fw_checksum' and 'fw_checksum_algorithm' shared attributes.The 'fw_title' and 'fw_version' parameters must be supplied in this request to double-check that the firmware that device is downloading matches the firmware it expects to download. This is important, since the administrator may change the firmware assignment while device is downloading the firmware.   Optional 'chunk' and 'size' parameters may be used to download the firmware in chunks. For example, device may request first 16 KB of firmware using 'chunk'=0 and 'size'=16384. Next 16KB using 'chunk'=1 and 'size'=16384. The last chunk should have less bytes then requested using 'size' parameter.   The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str device_token: Your device access token. (required)
:param str title: Title of the firmware, corresponds to the value of 'fw_title' attribute. (required)
:param str version: Version of the firmware, corresponds to the value of 'fw_version' attribute. (required)
:param int size: Size of the chunk. Optional. Omit to download the entire file without chunks.
:param int chunk: Index of the chunk. Optional. Omit to download the entire file without chunks.
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_firmware(device_token=device_token, title=title, version=version, size=size, chunk=chunk)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_firmware'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_firmware_by_id(group_id_json: str, firmware_type: str) -> str:
    """
    getFirmwareById  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str group_id: groupId (required)
:param str firmware_type: firmwareType (required)
:return: DeviceGroupOtaPackage
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_firmware_by_id(group_id=deserialize_param(group_id_json, 'EntityGroupId'), firmware_type=firmware_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_firmware_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_full_translation(locale_code: str, if_none_match: Optional[str] = None, accept_encoding: Optional[str] = None) -> str:
    """
    Get end-user all-to-one translation (getFullTranslation)  # noqa: E501

Fetch the end-user translation for specified locale. The result is the merge of user custom translation, system language translation and default locale translation.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str locale_code: Locale code (e.g. 'en_US'). (required)
:param str if_none_match:
:param str accept_encoding:
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_full_translation(locale_code=locale_code, if_none_match=if_none_match, accept_encoding=accept_encoding)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_full_translation'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_help_base_url() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_help_base_url()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_help_base_url'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_image_info(_type: str, key: str) -> str:
    """
    getImageInfo  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str type: Type of the image: tenant or system (required)
:param str key: Image resource key, for example thermostats_dashboard_background.jpeg (required)
:return: TbResourceInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_image_info(_type=_type, key=key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_image_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_images(page_size: int, page: int, text_search: Optional[str] = None, include_system_images: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    getImages  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param bool include_system_images: Use 'true' to include system images. Disabled by default. Ignored for requests by users with system administrator authority.
:param str text_search: The case insensitive 'substring' filter based on the resource title.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataTbResourceInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_images(page_size=page_size, page=page, text_search=text_search, include_system_images=include_system_images, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_images'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_job_by_id(id_json: str) -> str:
    """
    Get job by id (getJobById)  # noqa: E501

Fetches job info by id.  Example of a RUNNING CF_REPROCESSING job response: ```json {   "id": {     "entityType": "JOB",     "id": "475e94e0-2f2d-11f0-8240-91e99922a704"   },   "createdTime": 1747053196590,   "tenantId": {     "entityType": "TENANT",     "id": "46859a00-2f2d-11f0-8240-91e99922a704"   },   "type": "CF_REPROCESSING",   "key": "474e4130-2f2d-11f0-8240-91e99922a704",   "entityId": {     "entityType": "DEVICE_PROFILE",     "id": "9fd41f20-31a1-11f0-933e-27998d6db02e"    },   "status": "RUNNING",   "configuration": {     "type": "CF_REPROCESSING",     "calculatedFieldId": {       "entityType": "CALCULATED_FIELD",       "id": "474e4130-2f2d-11f0-8240-91e99922a704"     },     "startTs": 1747051995760,     "endTs": 1747052895760,     "tasksKey": "c3cdbd42-799e-4d3a-9aad-9310f767aa36",     "toReprocess": null   },   "result": {     "jobType": "CF_REPROCESSING",     "successfulCount": 1,     "failedCount": 0,     "discardedCount": 0,     "totalCount": 2,     "results": [],     "generalError": null,     "startTs": 1747323069445,     "finishTs": 1747323070585,     "cancellationTs": 0   } }  ```  Example of a CF_REPROCESSING job with failures: ```json {   ...,   "status": "FAILED",   ...,   "result": {     "jobType": "CF_REPROCESSING",     "successfulCount": 0,     "failedCount": 2,     "discardedCount": 0,     "totalCount": 2,     "results": [       {         "jobType": "CF_REPROCESSING",         "key": "c3cdbd42-799e-4d3a-9aad-9310f767aa36",         "success": false,         "discarded": false,         "failure": {           "error": "Failed to fetch temperature: Failed to fetch timeseries data",           "entityInfo": {             "id": {               "entityType": "DEVICE",               "id": "9fd41f20-31a1-11f0-933e-27998d6db02e"             },             "name": "Test device 1"           }         }       },       {         "jobType": "CF_REPROCESSING",         "key": "c3cdbd42-799e-4d3a-9aad-9310f767aa36",         "success": false,         "discarded": false,         "failure": {           "error": "Failed to fetch temperature: Failed to fetch timeseries data",           "entityInfo": {             "id": {               "entityType": "DEVICE",               "id": "9ffc4090-31a1-11f0-933e-27998d6db02e"             },             "name": "Test device 2"           }         }       }     ],     "generalError": null,     "startTs": 1747323069445,     "finishTs": 1747323070585,     "cancellationTs": 0   } }  ```  Example of a FAILED job result with general error: ```json {   ...,   "status": "FAILED",   ...,   "result": {     "jobType": "CF_REPROCESSING",     "successfulCount": 1,     "failedCount": 0,     "discardedCount": 0,     "totalCount": null,     "results": [],     "generalError": "Timeout to find devices by profile",     "cancellationTs": 0   } }  ```  Example of a CANCELLED job result: ```json {   ...,   "status": "CANCELLED",   ...,   "result": {     "jobType": "CF_REPROCESSING",     "successfulCount": 15,     "failedCount": 0,     "discardedCount": 85,     "totalCount": 100,     "results": [],     "generalError": null,     "cancellationTs": 1747065908414   } }  ```  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:return: Job
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_job_by_id(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_job_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_jobs(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[str] = None, end_time: Optional[str] = None) -> str:
    """
    Get jobs (getJobs)  # noqa: E501

Returns the page of jobs.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: Case-insensitive 'substring' filter based on job's description
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:param str types: Comma-separated list of job types to include. If empty - all job types are included.
:param str statuses: Comma-separated list of job statuses to include. If empty - all job statuses are included.
:param str entities: Comma-separated list of entity ids. If empty - jobs for all entities are included.
:param int start_time: To only include jobs created after this timestamp.
:param int end_time: To only include jobs created before this timestamp.
:return: PageDataJob
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_jobs(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_jobs'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_jwt_setting() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_jwt_setting()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_jwt_setting'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_last_calculated_field_reprocessing_job(id_json: str) -> str:
    """
    getLastCalculatedFieldReprocessingJob  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str calculated_field_id: (required)
:return: Job
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_last_calculated_field_reprocessing_job(id=deserialize_param(id_json, 'CalculatedFieldId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_last_calculated_field_reprocessing_job'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_latest_calculated_field_debug_event(calculated_field_id_json: str) -> str:
    """
    Get latest calculated field debug event (getLatestCalculatedFieldDebugEvent)  # noqa: E501

Gets latest calculated field debug event for specified calculated field id. Referencing non-existing calculated field id will cause an error.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param object calculated_field_id: (required)
:return: JsonNode
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_latest_calculated_field_debug_event(calculated_field_id=deserialize_param(calculated_field_id_json, 'CalculatedFieldId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_latest_calculated_field_debug_event'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_latest_rule_node_debug_input(rule_node_id_json: str) -> str:
    """
    Get latest input message (getLatestRuleNodeDebugInput)  # noqa: E501

Gets the input message from the debug events for specified Rule Chain Id. Referencing non-existing rule chain Id will cause an error.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str rule_node_id: A string value representing the rule node id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: JsonNode
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_latest_rule_node_debug_input(rule_node_id=deserialize_param(rule_node_id_json, 'RuleNodeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_latest_rule_node_debug_input'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_license_usage_info() -> str:
    """
    Get license usage info (getLicenseUsageInfo)  # noqa: E501

Get license usage info.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: LicenseUsageInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_license_usage_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_license_usage_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_login_mobile_info(pkg_name: str, platform: str) -> str:
    """
    Get mobile app login info (getLoginMobileInfo)  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str pkg_name: Mobile application package name (required)
:param str platform: Platform type (required)
:return: LoginMobileInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_login_mobile_info(pkg_name=pkg_name, platform=platform)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_login_mobile_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_login_page_translation(locale_code: str, if_none_match: Optional[str] = None, accept_encoding: Optional[str] = None) -> str:
    """
    Get system translation for login page  # noqa: E501

Fetch the end-user translation for specified locale.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str locale_code: Locale code (e.g. 'en_US'). (required)
:param str if_none_match:
:param str accept_encoding:
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_login_page_translation(locale_code=locale_code, if_none_match=if_none_match, accept_encoding=accept_encoding)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_login_page_translation'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_login_processing_url() -> str:
    """
    Get OAuth2 log in processing URL (getLoginProcessingUrl)  # noqa: E501

Returns the URL enclosed in double quotes. After successful authentication with OAuth2 provider, it makes a redirect to this path so that the platform can do further log in processing. This URL may be configured as 'security.oauth2.loginProcessingUrl' property in yml configuration file, or as 'SECURITY_OAUTH2_LOGIN_PROCESSING_URL' env variable. By default it is '/login/oauth2/code/'  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_login_processing_url()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_login_processing_url'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_login_white_label_params(logo_image_checksum: str, favicon_checksum: str) -> str:
    """
    Get Login White Labeling parameters  # noqa: E501

Returns login white-labeling parameters based on the hostname from request.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: LoginWhiteLabelingParams
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_login_white_label_params(logo_image_checksum=logo_image_checksum, favicon_checksum=favicon_checksum)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_login_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_lwm2m_bootstrap_security_info(is_bootstrap_server: bool) -> str:
    """
    Get Lwm2m Bootstrap SecurityInfo (getLwm2mBootstrapSecurityInfo)  # noqa: E501

Get the Lwm2m Bootstrap SecurityInfo object (of the current server) based on the provided isBootstrapServer parameter. If isBootstrapServer == true, get the parameters of the current Bootstrap Server. If isBootstrapServer == false, get the parameters of the current Lwm2m Server. Used for client settings when starting the client in Bootstrap mode.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param bool is_bootstrap_server: A Boolean value representing the Server SecurityInfo for future Bootstrap client mode settings. Values: 'true' for Bootstrap Server; 'false' for Lwm2m Server.  (required)
:return: LwM2MServerSecurityConfigDefault
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_lwm2m_bootstrap_security_info(is_bootstrap_server=is_bootstrap_server)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_lwm2m_bootstrap_security_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_lwm2m_list_objects(sort_order: str, sort_property: str, object_ids_json: str) -> str:
    """
    Get LwM2M Objects (getLwm2mListObjects)  # noqa: E501

Returns a page of LwM2M objects parsed from Resources with type 'LWM2M_MODEL' owned by tenant or sysadmin. You can specify parameters to filter the results. LwM2M Object is a object that includes information about the LwM2M model which can be used in transport configuration for the LwM2M device profile.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING) (required)
:param str sort_property: Property of entity to sort by (required)
:param str object_ids: LwM2M Object ids. (required)
:return: list[LwM2mObject]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_lwm2m_list_objects(sort_order=sort_order, sort_property=sort_property, object_ids=json.loads(object_ids_json) if object_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_lwm2m_list_objects'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_lwm2m_list_objects_page(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get LwM2M Objects (getLwm2mListObjectsPage)  # noqa: E501

Returns a page of LwM2M objects parsed from Resources with type 'LWM2M_MODEL' owned by tenant or sysadmin. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. LwM2M Object is a object that includes information about the LwM2M model which can be used in transport configuration for the LwM2M device profile.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on the resource title.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: list[LwM2mObject]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_lwm2m_list_objects_page(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_lwm2m_list_objects_page'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mail_processing_url() -> str:
    """
    Get OAuth2 log in processing URL (getMailProcessingUrl)  # noqa: E501

Returns the URL enclosed in double quotes. After successful authentication with OAuth2 provider and user consent for requested scope, it makes a redirect to this path so that the platform can do further log in processing and generating access tokens.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_mail_processing_url()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_mail_processing_url'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_max_datapoints_limit() -> str:
    """
    Get max data points limit (getMaxDatapointsLimit)  # noqa: E501

Get the maximum number of data points that dashboard may request from the server per in a single subscription command. This value impacts the time window behavior. It impacts 'Max values' parameter in case user selects 'None' as 'Data aggregation function'. It also impacts the 'Grouping interval' in case of any other 'Data aggregation function' is selected. The actual value of the limit is configurable in the system configuration file.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: int
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_max_datapoints_limit()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_max_datapoints_limit'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_merged_custom_translation(locale_code: str) -> str:
    """
    Get end-user Custom Translation configuration (getMergedCustomTranslation)  # noqa: E501

Fetch end-user Custom Translation for specified locale. The custom translation is configured in the white labeling parameters. If custom translation translation is defined on the tenant level, it overrides the custom translation of the system level. Similar, if the custom translation is defined on the customer level, it overrides the translation configuration of the tenant level.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str locale_code: Locale code (e.g. 'en_US'). (required)
:return: CustomTranslation
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_merged_custom_translation(locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_merged_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_merged_mobile_app_settings() -> str:
    """
    Get QR code configuration for home page (getMobileAppQrCodeConfig)  # noqa: E501

The response payload contains ui configuration of qr code  Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: QrCodeSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_merged_mobile_app_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_merged_mobile_app_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_app_bundle_info_by_id(mobile_app_bundle_id_json: str) -> str:
    """
    Get mobile app bundle info by id (getMobileAppBundleInfoById)  # noqa: E501

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:return: MobileAppBundleInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_mobile_app_bundle_info_by_id(mobile_app_bundle_id=deserialize_param(mobile_app_bundle_id_json, 'MobileAppBundleId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_mobile_app_bundle_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_app_by_id(mobile_app_id_json: str) -> str:
    """
    Get mobile info by id (getMobileAppInfoById)  # noqa: E501

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:return: MobileApp
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_mobile_app_by_id(mobile_app_id=deserialize_param(mobile_app_id_json, 'MobileAppId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_mobile_app_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_app_deep_link() -> str:
    """
    Get the deep link to the associated mobile application (getMobileAppDeepLink)  # noqa: E501

Fetch the url that takes user to linked mobile application   Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: object
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_mobile_app_deep_link()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_mobile_app_deep_link'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_app_info_by_id(mobile_app_id_json: str) -> str:
    """
    Get mobile info by id (getMobileAppInfoById)  # noqa: E501

  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:return: MobileAppInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_mobile_app_info_by_id(mobile_app_id=deserialize_param(mobile_app_id_json, 'MobileAppId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_mobile_app_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_app_settings() -> str:
    """
    Get Mobile application settings (getMobileAppSettings)  # noqa: E501

The response payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: MobileAppSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_mobile_app_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_mobile_app_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_session(x_mobile_token: str) -> str:
    """
    getMobileSession  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str x_mobile_token: X-Mobile-Token (required)
:return: MobileSessionInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_mobile_session(x_mobile_token=x_mobile_token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_mobile_session'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_request_by_id(id: str) -> str:
    """
    Get notification request by id (getNotificationRequestById)  # noqa: E501

Fetches notification request info by request id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: id (required)
:return: NotificationRequestInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_notification_request_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_notification_request_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_request_preview(body_json: str, recipients_preview_size: Optional[str] = None) -> str:
    """
    Get notification request preview (getNotificationRequestPreview)  # noqa: E501

Returns preview for notification request.  `processedTemplates` shows how the notifications for each delivery method will look like for the first recipient of the corresponding notification target.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param NotificationRequest body:
:param int recipients_preview_size: Amount of the recipients to show in preview
:return: NotificationRequestPreview
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_notification_request_preview(body=deserialize_param(body_json, 'NotificationRequest'), recipients_preview_size=recipients_preview_size)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_notification_request_preview'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_requests(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get notification requests (getNotificationRequests)  # noqa: E501

Returns the page of notification requests submitted by users of this tenant or sysadmins.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: Case-insensitive 'substring' filed based on the used template name
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataNotificationRequestInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_notification_requests(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_notification_requests'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_rule_by_id(id: str) -> str:
    """
    Get notification rule by id (getNotificationRuleById)  # noqa: E501

Fetches notification rule info by rule's id. In addition to regular notification rule fields, there are `templateName` and `deliveryMethods` in the response.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: id (required)
:return: NotificationRuleInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_notification_rule_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_notification_rule_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_rules(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get notification rules (getNotificationRules)  # noqa: E501

Returns the page of notification rules.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: Case-insensitive 'substring' filter based on rule's name
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataNotificationRuleInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_notification_rules(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_notification_rules'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_settings() -> str:
    """
    Get notification settings (getNotificationSettings)  # noqa: E501

Retrieves notification settings for this tenant or sysadmin.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: NotificationSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_notification_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_notification_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_target_by_id(id: str) -> str:
    """
    Get notification target by id (getNotificationTargetById)  # noqa: E501

Fetches notification target by id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: id (required)
:return: NotificationTarget
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_notification_target_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_notification_target_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_targets(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get notification targets (getNotificationTargets)  # noqa: E501

Returns the page of notification targets owned by sysadmin or tenant.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: Case-insensitive 'substring' filed based on the target's name
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataNotificationTarget
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_notification_targets(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_notification_targets'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_targets_by_ids(ids_json: str) -> str:
    """
    Get notification targets by ids (getNotificationTargetsByIds)  # noqa: E501

Returns the list of notification targets found by provided ids.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str ids: Comma-separated list of uuids representing targets ids (required)
:return: list[NotificationTarget]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_notification_targets_by_ids(ids=json.loads(ids_json) if ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_notification_targets_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_targets_by_supported_notification_type(notification_type: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get notification targets by supported notification type (getNotificationTargetsBySupportedNotificationType)  # noqa: E501

Returns the page of notification targets filtered by notification type that they can be used for.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str notification_type: notificationType (required)
:param int page_size: pageSize (required)
:param int page: page (required)
:param str text_search: textSearch
:param str sort_property: sortProperty
:param str sort_order: sortOrder
:return: PageDataNotificationTarget
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_notification_targets_by_supported_notification_type(notification_type=notification_type, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_notification_targets_by_supported_notification_type'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_template_by_id(id: str) -> str:
    """
    Get notification template by id (getNotificationTemplateById)  # noqa: E501

Fetches notification template by id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: id (required)
:return: NotificationTemplate
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_notification_template_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_notification_template_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_templates(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get notification templates (getNotificationTemplates)  # noqa: E501

Returns the page of notification templates owned by sysadmin or tenant.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: Case-insensitive 'substring' filter based on template's name and notification type
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:param str notification_types: Comma-separated list of notification types to filter the templates
:return: PageDataNotificationTemplate
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_notification_templates(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_notification_templates'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notifications(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, delivery_method: Optional[str] = None) -> str:
    """
    Get notifications (getNotifications)  # noqa: E501

Returns the page of notifications for current user.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for any authorized user.   **WebSocket API**:  There are 2 types of subscriptions: one for unread notifications count, another for unread notifications themselves.  The URI for opening WS session for notifications: `/api/ws/plugins/notifications`.  Subscription command for unread notifications count: ``` {   "unreadCountSubCmd": {     "cmdId": 1234   } } ``` To subscribe for latest unread notifications: ``` {   "unreadSubCmd": {     "cmdId": 1234,     "limit": 10   } } ``` To unsubscribe from any subscription: ``` {   "unsubCmd": {     "cmdId": 1234   } } ``` To mark certain notifications as read, use following command: ``` {   "markAsReadCmd": {     "cmdId": 1234,     "notifications": [       "6f860330-7fc2-11ed-b855-7dd3b7d2faa9",       "5b6dfee0-8d0d-11ed-b61f-35a57b03dade"     ]   } }  ``` To mark all notifications as read: ``` {   "markAllAsReadCmd": {     "cmdId": 1234   } } ```   Update structure for unread **notifications count subscription**: ``` {   "cmdId": 1234,   "totalUnreadCount": 55 } ``` For **notifications subscription**: - full update of latest unread notifications: ``` {   "cmdId": 1234,   "notifications": [     {       "id": {         "entityType": "NOTIFICATION",         "id": "6f860330-7fc2-11ed-b855-7dd3b7d2faa9"       },       ...     }   ],   "totalUnreadCount": 1 } ``` - when new notification arrives or shown notification is updated: ``` {   "cmdId": 1234,   "update": {     "id": {       "entityType": "NOTIFICATION",       "id": "6f860330-7fc2-11ed-b855-7dd3b7d2faa9"     },     # updated notification info, text, subject etc.     ...   },   "totalUnreadCount": 2 } ``` - when unread notifications count changes: ``` {   "cmdId": 1234,   "totalUnreadCount": 5 } ```  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: Case-insensitive 'substring' filter based on notification subject or text
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:param bool unread_only: To search for unread notifications only
:param str delivery_method: Delivery method
:return: PageDataNotification
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_notifications(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, delivery_method=delivery_method)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_notifications'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_owner_info(owner_type: str, owner_id: str) -> str:
    """
    Get Owner Info (getOwnerInfo)  # noqa: E501

Fetch the owner info (tenant or customer) presented as Entity Info object based on the provided owner Id.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str owner_type: Tenant or Customer (required)
:param str owner_id: A string value representing the Tenant or Customer id (required)
:return: EntityInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_owner_info(owner_type=owner_type, owner_id=owner_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_owner_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_owner_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Owner Infos (getOwnerInfos)  # noqa: E501

Provides a rage view of Customers that the current user has READ access to. If the current user is Tenant administrator, the result set also contains the tenant. The call is designed for the UI auto-complete component to show tenant and all possible Customers that the user may select to change the owner of the particular entity or entity group.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'startsWith' filter based on the entity group name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataEntityInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_owner_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_owner_infos'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_owners(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Owners (getOwners)  # noqa: E501

Provides a rage view of Customers that the current user has READ access to. If the current user is Tenant administrator, the result set also contains the tenant. The call is designed for the UI auto-complete component to show tenant and all possible Customers that the user may select to change the owner of the particular entity or entity group.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'startsWith' filter based on the entity group name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataContactBasedobject
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_owners(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_owners'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_persisted_rpc(rpc_id_json: str) -> str:
    """
    Get persistent RPC request  # noqa: E501

Get information about the status of the RPC call.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str rpc_id: A string value representing the rpc id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: Rpc
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_persisted_rpc(rpc_id=deserialize_param(rpc_id_json, 'RpcId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_persisted_rpc'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_privacy_policy() -> str:
    """
    Get Privacy Policy for Self Registration form (getPrivacyPolicy)  # noqa: E501

Fetch the Privacy Policy based on the domain name from the request. Available for non-authorized users.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_privacy_policy()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_privacy_policy'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_qr_code_settings() -> str:
    """
    Get Mobile application settings (getMobileAppSettings)  # noqa: E501

The response payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: QrCodeSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_qr_code_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_qr_code_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_recipients_for_notification_target_config(page_size: int, page: int) -> str:
    """
    Get recipients for notification target config (getRecipientsForNotificationTargetConfig)  # noqa: E501

Returns the page of recipients for such notification target configuration.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param NotificationTarget body:
:return: PageDataUser
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_recipients_for_notification_target_config(page_size=page_size, page=page)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_recipients_for_notification_target_config'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_repository_settings() -> str:
    """
    Get repository settings (getRepositorySettings)  # noqa: E501

Get the repository settings object.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: RepositorySettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_repository_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_repository_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_repository_settings_info() -> str:
    """
    getRepositorySettingsInfo  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: RepositorySettingsInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_repository_settings_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_repository_settings_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_secret_info_by_id(secret_id_json: str) -> str:
    """
    Get Secret info by Id (getSecretInfoById)  # noqa: E501

  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:return: SecretInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_secret_info_by_id(secret_id=deserialize_param(secret_id_json, 'SecretId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_secret_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_secret_info_by_name(name: str) -> str:
    """
    Get Secret info by name (getSecretInfoByName)  # noqa: E501

  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str name: (required)
:return: SecretInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_secret_info_by_name(name=name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_secret_info_by_name'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_secret_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Secret infos (getSecretInfos)  # noqa: E501

Returns a page of secret infos owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on the secret name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: PageDataSecretInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_secret_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_secret_infos'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_secret_names() -> str:
    """
    Get Tenant Secret names (getSecretNames)  # noqa: E501

Returns a page of secret names owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: list[str]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_secret_names()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_secret_names'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_security_settings() -> str:
    """
    Get the Security Settings object  # noqa: E501

Get the Security Settings object that contains password policy, etc.  Available for users with 'SYS_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: SecuritySettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_security_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_security_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_self_registration_params() -> str:
    """
    Get Self Registration parameters (getSelfRegistrationParams)  # noqa: E501

Fetch the Self Registration parameters object for the tenant of the current user.   Available for users with 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: SelfRegistrationParams
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_self_registration_params()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_self_registration_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_server_time() -> str:
    """
    Get server time (getServerTime)  # noqa: E501

Get the server time (milliseconds since January 1, 1970 UTC). Used to adjust view of the dashboards according to the difference between browser and server time.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: int
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_server_time()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_server_time'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_sign_up_self_registration_params(pkg_name: Optional[str] = None) -> str:
    """
    Get Self Registration form parameters without authentication (getSignUpSelfRegistrationParams)  # noqa: E501

Fetch the Self Registration parameters based on the domain name from the request. Available for non-authorized users. Contains the information to customize the sign-up form.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str pkg_name: pkgName
:return: SignUpSelfRegistrationParams
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_sign_up_self_registration_params(pkg_name=pkg_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_sign_up_self_registration_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_software(device_token: str, title: str, version: str, size: Optional[str] = None, chunk: Optional[str] = None) -> str:
    """
    Get Device Software (getSoftware)  # noqa: E501

Downloads the current software package.When the platform initiates software update, it informs the device by updating the 'sw_title', 'sw_version', 'sw_checksum' and 'sw_checksum_algorithm' shared attributes.The 'sw_title' and 'sw_version' parameters must be supplied in this request to double-check that the software that device is downloading matches the software it expects to download. This is important, since the administrator may change the software assignment while device is downloading the software.   Optional 'chunk' and 'size' parameters may be used to download the software in chunks. For example, device may request first 16 KB of software using 'chunk'=0 and 'size'=16384. Next 16KB using 'chunk'=1 and 'size'=16384. The last chunk should have less bytes then requested using 'size' parameter.   The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str device_token: Your device access token. (required)
:param str title: Title of the software, corresponds to the value of 'sw_title' attribute. (required)
:param str version: Version of the software, corresponds to the value of 'sw_version' attribute. (required)
:param int size: Size of the chunk. Optional. Omit to download the entire file without using  chunks.
:param int chunk: Index of the chunk. Optional. Omit to download the entire file without using chunks.
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_software(device_token=device_token, title=title, version=version, size=size, chunk=chunk)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_software'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_solution_template_details(solution_template_id: str) -> str:
    """
    Get Solution template details (getSolutionTemplateDetails)  # noqa: E501

Get a solution template details based on the provided id   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str solution_template_id: A string value representing the solution template id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: TenantSolutionTemplateDetails
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_solution_template_details(solution_template_id=solution_template_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_solution_template_details'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_solution_template_infos() -> str:
    """
    Get Solution templates (getSolutionTemplateInfos)  # noqa: E501

Get a list of solution template descriptors   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: list[TenantSolutionTemplateInfo]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_solution_template_infos()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_solution_template_infos'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_solution_template_instructions(solution_template_id: str) -> str:
    """
    Get Solution Template Instructions (getSolutionTemplateInstructions)  # noqa: E501

Get a solution template instructions based on the provided id   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str solution_template_id: A string value representing the solution template id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: TenantSolutionTemplateInstructions
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_solution_template_instructions(solution_template_id=solution_template_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_solution_template_instructions'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_system_info() -> str:
    """
    Get system info (getSystemInfo)  # noqa: E501

Get main information about system.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: SystemInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_system_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_system_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_terms_of_use() -> str:
    """
    Get Terms of Use for Self Registration form (getTermsOfUse)  # noqa: E501

Fetch the Terms of Use based on the domain name from the request. Available for non-authorized users.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_terms_of_use()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_terms_of_use'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_translation_for_basic_edit(locale_code: str) -> str:
    """
    Get end-user multi-translation for basic edit (getTranslationForBasicEdit)  # noqa: E501

Fetch the translation info map where value is info object containing key translation, origin translation, translation of parent level, translation status.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str locale_code: (required)
:return: JsonNode
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_translation_for_basic_edit(locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_translation_for_basic_edit'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_translation_infos() -> str:
    """
    Get Translation info (getTranslationInfos)  # noqa: E501

Fetch the list of customized locales and corresponding details such as language display name, country display name and translation progress percentage.   Response example:   ```json [   {     "localeCode": "uk_UA",     "language": "Ukrainian (українська)",     "country": "Україна",     "progress": 32   },   {     "localeCode": "es_ES",     "language": "Spanish (español)",     "country": "España",     "progress": 79   }] ```  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: list[TranslationInfo]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_translation_infos()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_translation_infos'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_trendz_settings() -> str:
    """
    Get Trendz Settings (getTrendzSettings)  # noqa: E501

Retrieves Trendz settings for this tenant.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: TrendzSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_trendz_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_trendz_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_unread_notifications_count(delivery_method: Optional[str] = None) -> str:
    """
    Get unread notifications count (getUnreadNotificationsCount)  # noqa: E501

Returns unread notifications count for chosen delivery method.  Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str delivery_method: Delivery method
:return: int
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_unread_notifications_count(delivery_method=delivery_method)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_unread_notifications_count'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_uplink_payload(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get uplink payload (getUplinkPayload)  # noqa: E501

Returns payload example for the uplink converter for the vendor, integration type and model  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str integration_type: (required)
:param str vendor_name: (required)
:param str model: (required)
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_uplink_payload(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_uplink_payload'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_vendor_models(integration_type: str, vendor_name: str, converter_type: str) -> str:
    """
    Get vendor models (getVendorModels)  # noqa: E501

Returns a list of models for the vendor, integration type and converter type  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str integration_type: (required)
:param str vendor_name: (required)
:param str converter_type:
:return: list[Model]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_vendor_models(integration_type=integration_type, vendor_name=vendor_name, converter_type=converter_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_vendor_models'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_vendors(integration_type: str) -> str:
    """
    Get vendors (getVendors)  # noqa: E501

Returns a list of vendors for the integration type  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str integration_type: (required)
:return: list[Vendor]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_vendors(integration_type=integration_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_vendors'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_version_create_request_status(request_id: str) -> str:
    """
    Get version create request status (getVersionCreateRequestStatus)  # noqa: E501

Returns the status of previously made version create request.   This status contains following properties: - `done` - whether request processing is finished; - `version` - created version info: timestamp, version id (commit hash), commit name and commit author; - `added` - count of items that were created in the remote repo; - `modified` - modified items count; - `removed` - removed items count; - `error` - error message, if an error occurred while handling the request.  An example of successful status: ```json {   "done": true,   "added": 10,   "modified": 2,   "removed": 5,   "version": {     "timestamp": 1655198528000,     "id":"8a834dd389ed80e0759ba8ee338b3f1fd160a114",     "name": "My devices v2.0",     "author": "John Doe"   },   "error": null } ```  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str request_id: A string value representing the version control request id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: VersionCreationResult
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_version_create_request_status(request_id=request_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_version_create_request_status'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_version_load_request_status(request_id: str) -> str:
    """
    Get version load request status (getVersionLoadRequestStatus)  # noqa: E501

Returns the status of previously made version load request. The structure contains following parameters: - `done` - if the request was successfully processed; - `result` - a list of load results for each entity type:      - `created` - created entities count;      - `updated` - updated entities count;      - `deleted` - removed entities count. - `error` - if an error occurred during processing, error info:      - `type` - error type;      - `source` - an external id of remote entity;      - `target` - if failed to find referenced entity by external id - this external id;      - `message` - error message.  An example of successfully processed request status: ```json {   "done": true,   "result": [     {       "entityType": "DEVICE",       "created": 10,       "updated": 5,       "deleted": 5     },      {       "entityType": "ASSET",       "created": 4,       "updated": 0,       "deleted": 8     }   ] } ```  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str request_id: A string value representing the version control request id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: VersionLoadResult
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_version_load_request_status(request_id=request_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_version_load_request_status'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_web_self_registration_params() -> str:
    """
    Get Self Registration parameters (getSelfRegistrationParams)  # noqa: E501

Fetch the Self Registration parameters object for the tenant of the current user.   Available for users with 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: list[str]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_web_self_registration_params()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_web_self_registration_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_white_label_params(logo_image_checksum: str, favicon_checksum: str) -> str:
    """
    Get White Labeling parameters  # noqa: E501

Returns white-labeling parameters for the current user.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: WhiteLabelingParams
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_white_label_params(logo_image_checksum=logo_image_checksum, favicon_checksum=favicon_checksum)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_rule_engine_request(entity_id_json: str, timeout: int, body: Optional[str] = None) -> str:
    """
    Push entity message to the rule engine (handleRuleEngineRequest)  # noqa: E501

Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses specified Entity Id as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. The default timeout of the request processing is 10 seconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param object body: (required)
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: object
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.handle_rule_engine_request(entity_id=deserialize_param(entity_id_json, 'EntityId'), timeout=timeout, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'handle_rule_engine_request'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_rule_engine_request_v1(entity_id_json: str, body: Optional[str] = None, queue_name: Optional[str] = None, timeout: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.handle_rule_engine_request_v1(entity_id=deserialize_param(entity_id_json, 'EntityId'), body=body, queue_name=queue_name, timeout=timeout)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'handle_rule_engine_request_v1'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_rule_engine_request_v2(entity_id_json: str, body: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.handle_rule_engine_request_v2(entity_id=deserialize_param(entity_id_json, 'EntityId'), body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'handle_rule_engine_request_v2'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def http_check_status_get(routing_key: str, request_params: str, request_headers: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.http_check_status_get(routing_key=routing_key, request_params=request_params, request_headers=request_headers)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'http_check_status_get'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def http_process_request_v1_post1(routing_key: str, suffix: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.http_process_request_v1_post1(routing_key=routing_key, suffix=suffix)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'http_process_request_v1_post1'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def http_process_request_v2_post2(routing_key: str, suffix: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.http_process_request_v2_post2(routing_key=routing_key, suffix=suffix)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'http_process_request_v2_post2'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def import_image(body_json: str) -> str:
    """
    importImage  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param ImageExportData body:
:return: TbResourceInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.import_image(body=deserialize_param(body_json, 'ImageExportData'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'import_image'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def install_solution_template(solution_template_id: str) -> str:
    """
    Install Solution Template (installSolutionTemplate)  # noqa: E501

Install solution template based on the provided id   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str solution_template_id: A string value representing the solution template id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: SolutionInstallResponse
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.install_solution_template(solution_template_id=solution_template_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'install_solution_template'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def isDaemon() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.isDaemon()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'isDaemon'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def is_alive() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.is_alive()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'is_alive'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def is_edqs_api_enabled() -> str:
    """
    isEdqsApiEnabled  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: object
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.is_edqs_api_enabled()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'is_edqs_api_enabled'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def is_tbel_enabled() -> str:
    """
    Is TBEL script executor enabled  # noqa: E501

Returns 'True' if the TBEL script execution is enabled  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: bool
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.is_tbel_enabled()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'is_tbel_enabled'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def is_white_labeling_allowed() -> str:
    """
    Check White Labeling Allowed  # noqa: E501

Check if the White Labeling is enabled for the current user owner (tenant or customer)  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: bool
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.is_white_labeling_allowed()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'is_white_labeling_allowed'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def join(timeout: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.join(timeout=timeout)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'join'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def list_all_entities_at_version(version_id: str) -> str:
    """
    List all entities at version (listAllEntitiesAtVersion)  # noqa: E501

Returns a list of all remote entities available in a specific version. Response type is the same as for listAllEntitiesAtVersion API method.  Returned entities order will be the same as in the repository.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str version_id: Version id, for example fd82625bdd7d6131cf8027b44ee967012ecaf990. Represents commit hash. (required)
:return: DeferredResultListVersionedEntityInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.list_all_entities_at_version(version_id=version_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'list_all_entities_at_version'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def list_branches() -> str:
    """
    List branches (listBranches)  # noqa: E501

Lists branches available in the remote repository.   Response example:  ```json [   {     "name": "master",     "default": true   },   {     "name": "dev",     "default": false   },   {     "name": "dev-2",     "default": false   } ] ```  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: DeferredResultListBranchInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.list_branches()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'list_branches'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def list_entities_at_version(entity_type: str, version_id: str) -> str:
    """
    List entities at version (listEntitiesAtVersion)  # noqa: E501

Returns a list of remote entities of a specific entity type that are available at a concrete version.  Each entity item in the result has `externalId` property. Entities order will be the same as in the repository.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str version_id: Version id, for example fd82625bdd7d6131cf8027b44ee967012ecaf990. Represents commit hash. (required)
:return: DeferredResultListVersionedEntityInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.list_entities_at_version(entity_type=entity_type, version_id=version_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'list_entities_at_version'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def list_entity_type_versions(entity_type: str, branch: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    List entity type versions (listEntityTypeVersions)  # noqa: E501

Returns list of versions of an entity type in a branch. This is a collected list of versions that were created for entities of this type in a remote branch.  If specified branch does not exist - empty page data will be returned. The response structure is the same as for `listEntityVersions` API method.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str branch: The name of the working branch, for example 'master' (required)
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on the entity version name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: DeferredResultPageDataEntityVersion
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.list_entity_type_versions(entity_type=entity_type, branch=branch, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'list_entity_type_versions'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def list_entity_versions(entity_type: str, external_entity_uuid: str, branch: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    List entity versions (listEntityVersions)  # noqa: E501

Returns list of versions for a specific entity in a concrete branch.  You need to specify external id of an entity to list versions for. This is `externalId` property of an entity, or otherwise if not set - simply id of this entity.  If specified branch does not exist - empty page data will be returned.   Each version info item has timestamp, id, name and author. Version id can then be used to restore the version. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Response example:  ```json {   "data": [     {       "timestamp": 1655198593000,       "id": "fd82625bdd7d6131cf8027b44ee967012ecaf990",       "name": "Devices and assets - v2.0",       "author": "John Doe <johndoe@gmail.com>"     },     {       "timestamp": 1655198528000,       "id": "682adcffa9c8a2f863af6f00c4850323acbd4219",       "name": "Update my device",       "author": "John Doe <johndoe@gmail.com>"     },     {       "timestamp": 1655198280000,       "id": "d2a6087c2b30e18cc55e7cdda345a8d0dfb959a4",       "name": "Devices and assets - v1.0",       "author": "John Doe <johndoe@gmail.com>"     }   ],   "totalPages": 1,   "totalElements": 3,   "hasNext": false } ```  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
:param str external_entity_uuid: A string value representing external entity id. This is `externalId` property of an entity, or otherwise if not set - simply id of this entity. (required)
:param str branch: The name of the working branch, for example 'master' (required)
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on the entity version name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: DeferredResultPageDataEntityVersion
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.list_entity_versions(entity_type=entity_type, external_entity_uuid=external_entity_uuid, branch=branch, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'list_entity_versions'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def list_slack_conversations(type: str, token: Optional[str] = None) -> str:
    """
    List Slack conversations (listSlackConversations)  # noqa: E501

List available Slack conversations by type.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str type: type (required)
:param str token: Slack bot token. If absent - system Slack settings will be used
:return: list[SlackConversation]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.list_slack_conversations(type=type, token=token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'list_slack_conversations'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def list_versions(branch: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    List all versions (listVersions)  # noqa: E501

Lists all available versions in a branch for all entity types.  If specified branch does not exist - empty page data will be returned. The response format is the same as for `listEntityVersions` API method.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str branch: The name of the working branch, for example 'master' (required)
:param int page_size: Maximum amount of entities in a one page (required)
:param int page: Sequence number of page starting from 0 (required)
:param str text_search: The case insensitive 'substring' filter based on the entity version name.
:param str sort_property: Property of entity to sort by
:param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
:return: DeferredResultPageDataEntityVersion
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.list_versions(branch=branch, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'list_versions'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def load_entities_version(body: Optional[str] = None) -> str:
    """
    Load entities version (loadEntitiesVersion)  # noqa: E501

Loads specific version of remote entities (or single entity) by request. Supported entity types: CUSTOMER, ASSET, RULE_CHAIN, DASHBOARD, DEVICE_PROFILE, DEVICE, ENTITY_VIEW, WIDGETS_BUNDLE.  There are multiple types of request. Each of them requires branch name (`branch`) and version id (`versionId`). Request of type `SINGLE_ENTITY` is needed to restore a concrete version of a specific entity. It contains id of a remote entity (`externalEntityId`) and additional configuration (`config`): - `loadRelations` - to update relations list (in case `saveRelations` option was enabled during version creation); - `loadAttributes` - to load entity attributes (if `saveAttributes` config option was enabled); - `loadCredentials` - to update device credentials (if `saveCredentials` option was enabled during version creation).  An example of such request: ```json {   "type": "SINGLE_ENTITY",      "branch": "dev",   "versionId": "b3c28d722d328324c7c15b0b30047b0c40011cf7",      "externalEntityId": {     "entityType": "DEVICE",     "id": "b7944123-d4f4-11ec-847b-0f432358ab48"   },   "config": {     "loadRelations": false,     "loadAttributes": true,     "loadCredentials": true   } } ```  Another request type (`ENTITY_TYPE`) is needed to load specific version of the whole entity types. It contains a structure with entity types to load and configs for each entity type (`entityTypes`). For each specified entity type, the method will load all remote entities of this type that are present at the version. A config for each entity type contains the same options as in `SINGLE_ENTITY` request type, and additionally contains following options: - `removeOtherEntities` - to remove local entities that are not present on the remote - basically to    overwrite local entity type with the remote one; - `findExistingEntityByName` - when you are loading some remote entities that are not yet present at this tenant,    try to find existing entity by name and update it rather than create new.  Here is an example of the request to completely restore version of the whole device entity type: ```json {   "type": "ENTITY_TYPE",    "branch": "dev",   "versionId": "b3c28d722d328324c7c15b0b30047b0c40011cf7",    "entityTypes": {     "DEVICE": {       "removeOtherEntities": true,       "findExistingEntityByName": false,       "loadRelations": true,       "loadAttributes": true,       "loadCredentials": true     }   } } ```  The response will contain generated request UUID that is to be used to check the status of operation via `getVersionLoadRequestStatus`.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param VersionLoadRequest body:
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.load_entities_version(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'load_entities_version'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def mark_all_notifications_as_read() -> str:
    """
    Mark all notifications as read (markAllNotificationsAsRead)  # noqa: E501

Marks all unread notifications as read.  Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str delivery_method: Delivery method
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.mark_all_notifications_as_read()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'mark_all_notifications_as_read'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def mark_notification_as_read(id: str) -> str:
    """
    Mark notification as read (markNotificationAsRead)  # noqa: E501

Marks notification as read by its id.  Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: id (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.mark_notification_as_read(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'mark_notification_as_read'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def mobile_login(pkg_name: str) -> str:
    """
    Mobile Login redirect (mobileLogin)  # noqa: E501

This method generates redirect to the special link that is handled by mobile application. Useful for email verification flow on mobile app.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str pkg_name: Mobile app package name. Used to identify the application and build the redirect link. (required)
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.mobile_login(pkg_name=pkg_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'mobile_login'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def patch_custom_translation(body_json: str, locale_code: str) -> str:
    """
    Update Custom Translation for specified translation keys only (patchCustomTranslation)  # noqa: E501

The API call is designed to update the custom translation for specified key only.    Request example:   ```json {"notification.active":"active"} ```  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param object body: (required)
:param str locale_code: Locale code (e.g. 'en_US'). (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.patch_custom_translation(body=deserialize_param(body_json, 'CustomTranslation'), locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'patch_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def post_rpc_request(device_token: str, body: Optional[str] = None) -> str:
    """
    Send the RPC command (postRpcRequest)  # noqa: E501

Send the RPC request to server. The request payload is a JSON document that contains 'method' and 'params'. For example:  ```json {"method": "sumOnServer", "params":{"a":2, "b":2}} ```  The response contains arbitrary JSON with the RPC reply. For example:   ```json {"result": 4} ```  The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str device_token: Your device access token. (required)
:param str body:
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.post_rpc_request(device_token=device_token, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'post_rpc_request'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def preview_white_label_params(body: Optional[str] = None) -> str:
    """
    Preview Login White Labeling configuration (saveWhiteLabelParams)  # noqa: E501

Merge the White Labeling configuration with the parent configuration and return the result.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param WhiteLabelingParams body:
:return: WhiteLabelingParams
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.preview_white_label_params(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'preview_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def privacy_policy_accepted() -> str:
    """
    Check privacy policy (privacyPolicyAccepted)  # noqa: E501

Checks that current user accepted the privacy policy.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: bool
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.privacy_policy_accepted()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'privacy_policy_accepted'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def process_system_edqs_request(body_json: str) -> str:
    """
    processSystemEdqsRequest  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param ToCoreEdqsRequest body: (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.process_system_edqs_request(body=deserialize_param(body_json, 'ToCoreEdqsRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'process_system_edqs_request'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def refresh() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.refresh()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'refresh'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def remove_mobile_session(x_mobile_token: str) -> str:
    """
    removeMobileSession  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str x_mobile_token: X-Mobile-Token (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.remove_mobile_session(x_mobile_token=x_mobile_token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'remove_mobile_session'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def reply_to_command(device_token: str, request_id: int, body: Optional[str] = None) -> str:
    """
    Reply to RPC commands (replyToCommand)  # noqa: E501

Replies to server originated RPC command identified by 'requestId' parameter. The response is arbitrary JSON.  The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str device_token: Your device access token. (required)
:param int request_id: RPC request id from the incoming RPC request (required)
:param str body:
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.reply_to_command(device_token=device_token, request_id=request_id, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'reply_to_command'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def repository_settings_exists() -> str:
    """
    Check repository settings exists (repositorySettingsExists)  # noqa: E501

Check whether the repository settings exists.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: bool
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.repository_settings_exists()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'repository_settings_exists'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def reprocess_calculated_field(id_json: str, start_ts: int, end_ts: int) -> str:
    """
    Reprocess Calculated Field (reprocessCalculatedField)  # noqa: E501

Reprocesses the calculated field.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str calculated_field_id: (required)
:param int start_ts: (required)
:param int end_ts: (required)
:return: Job
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.reprocess_calculated_field(id=deserialize_param(id_json, 'CalculatedFieldId'), start_ts=start_ts, end_ts=end_ts)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'reprocess_calculated_field'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def reprocess_job(id_json: str) -> str:
    """
    Reprocess job (reprocessJob)  # noqa: E501

Reprocesses the job. Failures are located at job.result.results list. Platform iterates over this list and submits new tasks for them. Doesn't create new job entity but updates the existing one. Successfully reprocessed job will look the same as completed one.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.reprocess_job(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'reprocess_job'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def request_reset_password_by_email(body: Optional[str] = None) -> str:
    """
    Request reset password email (requestResetPasswordByEmail)  # noqa: E501

Request to send the reset password email if the user with specified email address is present in the database. Always return '200 OK' status for security purposes.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param ResetPasswordEmailRequest body:
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.request_reset_password_by_email(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'request_reset_password_by_email'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def resend_email_activation(email: str, pkg_name: Optional[str] = None) -> str:
    """
    Resend Activation Email (resendEmailActivation)  # noqa: E501

Request to resend the activation email for the user. Checks that user was not activated yet.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str email: Email of the user. (required)
:param str pkg_name: Optional package name of the mobile application.
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.resend_email_activation(email=email, pkg_name=pkg_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'resend_email_activation'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def reset_password(body: Optional[str] = None) -> str:
    """
    Reset password (resetPassword)  # noqa: E501

Checks the password reset token and updates the password. If token is valid, returns the object that contains [JWT](https://jwt.io/) access and refresh tokens. If token is not valid, returns '404 Bad Request'.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param ResetPasswordRequest body:
:return: JwtPair
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.reset_password(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'reset_password'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def rpc_v2_get_persisted_rpc(rpc_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.rpc_v2_get_persisted_rpc(rpc_id=deserialize_param(rpc_id_json, 'RpcId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'rpc_v2_get_persisted_rpc'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def run() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.run()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'run'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_ai_model(body_json: str) -> str:
    """
    Create or update AI model (saveAiModel)  # noqa: E501

Creates or updates an AI model record.  • **Create:** Omit the `id` to create a new record. The platform assigns a UUID to the new record and returns it in the `id` field of the response.  • **Update:** Include an existing `id` to modify that record. If no matching record exists, the API responds with **404 Not Found**.  Tenant ID for the AI model will be taken from the authenticated user making the request, regardless of any value provided in the request body.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param AiModel body: (required)
:return: AiModel
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_ai_model(body=deserialize_param(body_json, 'AiModel'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_ai_model'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_auto_commit_settings(body: Optional[str] = None) -> str:
    """
    Creates or Updates the auto commit settings (saveAutoCommitSettings)  # noqa: E501

Creates or Updates the auto commit settings object.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param dict(str, AutoVersionCreateConfig) body:
:return: AutoCommitSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_auto_commit_settings(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_auto_commit_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_calculated_field(body_json: str) -> str:
    """
    Create Or Update Calculated Field (saveCalculatedField)  # noqa: E501

Creates or Updates the Calculated Field. When creating calculated field, platform generates Calculated Field Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Calculated Field Id will be present in the response. Specify existing Calculated Field Id to update the calculated field. Referencing non-existing Calculated Field Id will cause 'Not Found' error. Remove 'id', 'tenantId' from the request body example (below) to create new Calculated Field entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param CalculatedField body: A JSON value representing the calculated field. (required)
:return: CalculatedField
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_calculated_field(body=deserialize_param(body_json, 'CalculatedField'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_calculated_field'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_client_registration_template(body: Optional[str] = None) -> str:
    """
    Create or update OAuth2 client registration template (saveClientRegistrationTemplate)  Available for users with 'SYS_ADMIN' authority.  # noqa: E501

Client registration template is OAuth2 provider configuration template with default settings for registering new OAuth2 clients  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param OAuth2ClientRegistrationTemplate body:
:return: OAuth2ClientRegistrationTemplate
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_client_registration_template(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_client_registration_template'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_custom_translation(locale_code: str, body_json: str) -> str:
    """
    Create Or Update Custom Translation (saveCustomTranslation)  # noqa: E501

Creates or Updates the Custom Translation map.   Request example:   ```json {"translationMap":{"es_ES":"{\\"home\\":\\"MyHome\\"}"}} ```  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param CustomTranslation body:
:param str locale_code: Locale code (e.g. 'en_US'). (required)
:return: CustomTranslation
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_custom_translation(locale_code=locale_code, body=deserialize_param(body_json, 'CustomTranslation'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_domain(body_json: str, oauth2_client_ids: Optional[str] = None) -> str:
    """
    Save or Update Domain (saveDomain)  # noqa: E501

Create or update the Domain. When creating domain, platform generates Domain Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Domain Id will be present in the response. Specify existing Domain Id to update the domain. Referencing non-existing Domain Id will cause 'Not Found' error.  Domain name is unique for entire platform setup.    Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param Domain body: (required)
:param list[object] oauth2_client_ids: A list of oauth2 client registration ids, separated by comma ','
:return: Domain
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_domain(body=deserialize_param(body_json, 'Domain'), oauth2_client_ids=oauth2_client_ids)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_domain'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_entities_version(body: Optional[str] = None) -> str:
    """
    Save entities version (saveEntitiesVersion)  # noqa: E501

Creates a new version of entities (or a single entity) by request. Supported entity types: CUSTOMER, ASSET, RULE_CHAIN, DASHBOARD, DEVICE_PROFILE, DEVICE, ENTITY_VIEW, WIDGETS_BUNDLE.  There are two available types of request: `SINGLE_ENTITY` and `COMPLEX`. Each of them contains version name (`versionName`) and name of a branch (`branch`) to create version (commit) in. If specified branch does not exists in a remote repo, then new empty branch will be created. Request of the `SINGLE_ENTITY` type has id of an entity (`entityId`) and additional configuration (`config`) which has following options:  - `saveRelations` - whether to add inbound and outbound relations of type COMMON to created entity version; - `saveAttributes` - to save attributes of server scope (and also shared scope for devices); - `saveCredentials` - when saving a version of a device, to add its credentials to the version.  An example of a `SINGLE_ENTITY` version create request: ```json {   "type": "SINGLE_ENTITY",    "versionName": "Version 1.0",   "branch": "dev",    "entityId": {     "entityType": "DEVICE",     "id": "b79448e0-d4f4-11ec-847b-0f432358ab48"   },   "config": {     "saveRelations": true,     "saveAttributes": true,     "saveCredentials": false   } } ```  Second request type (`COMPLEX`), additionally to `branch` and `versionName`, contains following properties: - `entityTypes` - a structure with entity types to export and configuration for each entity type;    this configuration has all the options available for `SINGLE_ENTITY` and additionally has these ones:       - `allEntities` and `entityIds` - if you want to save the version of all entities of the entity type         then set `allEntities` param to true, otherwise set it to false and specify the list of specific entities (`entityIds`);      - `syncStrategy` - synchronization strategy to use for this entity type: when set to `OVERWRITE`         then the list of remote entities of this type will be overwritten by newly added entities. If set to         `MERGE` - existing remote entities of this entity type will not be removed, new entities will just         be added on top (or existing remote entities will be updated). - `syncStrategy` - default synchronization strategy to use when it is not specified for an entity type.  Example for this type of request: ```json {   "type": "COMPLEX",    "versionName": "Devices and profiles: release 2",   "branch": "master",    "syncStrategy": "OVERWRITE",   "entityTypes": {     "DEVICE": {       "syncStrategy": null,       "allEntities": true,       "saveRelations": true,       "saveAttributes": true,       "saveCredentials": true     },     "DEVICE_PROFILE": {       "syncStrategy": "MERGE",       "allEntities": false,       "entityIds": [         "b79448e0-d4f4-11ec-847b-0f432358ab48"       ],       "saveRelations": true     }   } } ```  Response wil contain generated request UUID, that can be then used to retrieve status of operation via `getVersionCreateRequestStatus`.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param VersionCreateRequest body:
:return: DeferredResultuuid
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_entities_version(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_entities_version'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_entity_view(body: Optional[str] = None, entity_group_id: Optional[str] = None, entity_group_ids_json: str = None) -> str:
    """
    Save or update entity view (saveEntityView)  # noqa: E501

Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. See the 'Model' tab for more details.Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Entity View entity.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param EntityView body:
:param str entity_group_id: entityGroupId
:param str entity_group_ids: entityGroupIds
:return: EntityView
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_entity_view(body=body, entity_group_id=entity_group_id, entity_group_ids=json.loads(entity_group_ids_json) if entity_group_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_entity_view'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_jwt_settings(body: Optional[str] = None) -> str:
    """
    Update JWT Settings (saveJwtSettings)  # noqa: E501

Updates the JWT Settings object that contains JWT token policy, etc. The tokenSigningKey field is a Base64 encoded string.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param JwtSettings body:
:return: JwtPair
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_jwt_settings(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_jwt_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_login_white_label_params(body: Optional[str] = None) -> str:
    """
    Create Or Update Login White Labeling configuration (saveWhiteLabelParams)  # noqa: E501

Creates or Updates the White Labeling configuration.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param LoginWhiteLabelingParams body:
:param str customer_id: A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
:return: LoginWhiteLabelingParams
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_login_white_label_params(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_login_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_mobile_app(body_json: str, oauth2_client_ids: Optional[str] = None) -> str:
    """
    Save Or update Mobile app (saveMobileApp)  # noqa: E501

Create or update the Mobile app. When creating mobile app, platform generates Mobile App Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Mobile App Id will be present in the response. Specify existing Mobile App Id to update the mobile app. Referencing non-existing Mobile App Id will cause 'Not Found' error.  Mobile app package name is unique for entire platform setup.    Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param MobileApp body: (required)
:param list[object] oauth2_client_ids: A list of entity oauth2 client ids, separated by comma ','
:return: MobileApp
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_mobile_app(body=deserialize_param(body_json, 'MobileApp'), oauth2_client_ids=oauth2_client_ids)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_mobile_app'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_mobile_app_bundle(body_json: str, oauth2_client_ids_json: str = None) -> str:
    """
    Save Or update Mobile app bundle (saveMobileAppBundle)  # noqa: E501

Create or update the Mobile app bundle that represents tha pair of ANDROID and IOS app and mobile settings like oauth2 clients, self-registration and layout configuration.When creating mobile app bundle, platform generates Mobile App Bundle Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Mobile App Bundle Id will be present in the response. Referencing non-existing Mobile App Bundle Id will cause 'Not Found' error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param MobileAppBundle body: (required)
:param str oauth2_client_ids: A list of oauth2 client ids, separated by comma ','
:return: MobileAppBundle
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_mobile_app_bundle(body=deserialize_param(body_json, 'MobileAppBundle'), oauth2_client_ids=json.loads(oauth2_client_ids_json) if oauth2_client_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_mobile_app_bundle'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_mobile_app_settings(body_json: str) -> str:
    """
    Create Or Update the Mobile application settings (saveMobileAppSettings)  # noqa: E501

The request payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param MobileAppSettings body: (required)
:return: MobileAppSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_mobile_app_settings(body=deserialize_param(body_json, 'MobileAppSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_mobile_app_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_mobile_session(x_mobile_token: str, body_json: str) -> str:
    """
    saveMobileSession  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str x_mobile_token: X-Mobile-Token (required)
:param MobileSessionInfo body:
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_mobile_session(x_mobile_token=x_mobile_token, body=deserialize_param(body_json, 'MobileSessionInfo'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_mobile_session'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_notification_rule(body_json: str) -> str:
    """
    Save notification rule (saveNotificationRule)  # noqa: E501

Creates or updates notification rule.   Mandatory properties are `name`, `templateId` (of a template with `notificationType` matching to rule's `triggerType`), `triggerType`, `triggerConfig` and `recipientConfig`. Additionally, you may specify rule `description` inside of `additionalConfig`.  Trigger type of the rule cannot be changed. Available trigger types for tenant: `ENTITY_ACTION`, `ALARM`, `ALARM_COMMENT`, `ALARM_ASSIGNMENT`, `DEVICE_ACTIVITY`, `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT`. For sysadmin, there are following trigger types available: `ENTITIES_LIMIT`, `API_USAGE_LIMIT`, `NEW_PLATFORM_VERSION`.  Here is an example of notification rule to send notification when a device, asset or customer is created or deleted: ```json {   "name": "Entity action",   "templateId": {     "entityType": "NOTIFICATION_TEMPLATE",     "id": "32117320-d785-11ed-a06c-21dd57dd88ca"   },   "triggerType": "ENTITY_ACTION",   "triggerConfig": {     "entityTypes": [       "CUSTOMER",       "DEVICE",       "ASSET"     ],     "created": true,     "updated": false,     "deleted": true,     "triggerType": "ENTITY_ACTION"   },   "recipientsConfig": {     "targets": [       "320f2930-d785-11ed-a06c-21dd57dd88ca"     ],     "triggerType": "ENTITY_ACTION"   },   "additionalConfig": {     "description": "Send notification to tenant admins or customer users when a device, asset or customer is created"   },   "templateName": "Entity action notification",   "deliveryMethods": [     "WEB"   ] } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param NotificationRule body:
:return: NotificationRule
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_notification_rule(body=deserialize_param(body_json, 'NotificationRule'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_notification_rule'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_notification_settings(body_json: str) -> str:
    """
    Save notification settings (saveNotificationSettings)  # noqa: E501

Saves notification settings for this tenant or sysadmin. `deliveryMethodsConfigs` of the settings must be specified.  Here is an example of the notification settings with Slack configuration: ```json {   "deliveryMethodsConfigs": {     "SLACK": {       "method": "SLACK",       "botToken": "xoxb-...."     }   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param NotificationSettings body:
:return: NotificationSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_notification_settings(body=deserialize_param(body_json, 'NotificationSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_notification_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_notification_target(body_json: str) -> str:
    """
    Save notification target (saveNotificationTarget)  # noqa: E501

Creates or updates notification target.  Available `configuration` types are `PLATFORM_USERS` and `SLACK`. For `PLATFORM_USERS` the `usersFilter` must be specified. For tenant, there are following users filter types available: `USER_LIST`, `CUSTOMER_USERS`, `TENANT_ADMINISTRATORS`, `ALL_USERS`, `ORIGINATOR_ENTITY_OWNER_USERS`, `AFFECTED_USER`. For sysadmin: `TENANT_ADMINISTRATORS`, `AFFECTED_TENANT_ADMINISTRATORS`, `SYSTEM_ADMINISTRATORS`, `ALL_USERS`.  Here is an example of tenant-level notification target to send notification to customer's users: ```json {   "name": "Users of Customer A",   "configuration": {     "type": "PLATFORM_USERS",     "usersFilter": {       "type": "CUSTOMER_USERS",       "customerId": "32499a20-d785-11ed-a06c-21dd57dd88ca"     },     "description": "Users of Customer A"   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param NotificationTarget body:
:return: NotificationTarget
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_notification_target(body=deserialize_param(body_json, 'NotificationTarget'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_notification_target'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_notification_template(body_json: str) -> str:
    """
    Save notification template (saveNotificationTemplate)  # noqa: E501

Creates or updates notification template.  Here is an example of template to send notification via Web, SMS and Slack: ```json {   "name": "Greetings",   "notificationType": "GENERAL",   "configuration": {     "deliveryMethodsTemplates": {       "WEB": {         "enabled": true,         "subject": "Greetings",         "body": "Hi there, ${recipientTitle}",         "additionalConfig": {           "icon": {             "enabled": true,             "icon": "back_hand",             "color": "#757575"           },           "actionButtonConfig": {             "enabled": false           }         },         "method": "WEB"       },       "SMS": {         "enabled": true,         "body": "Hi there, ${recipientTitle}",         "method": "SMS"       },       "SLACK": {         "enabled": true,         "body": "Hi there, @${recipientTitle}",         "method": "SLACK"       }     }   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param NotificationTemplate body:
:return: NotificationTemplate
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_notification_template(body=deserialize_param(body_json, 'NotificationTemplate'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_notification_template'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_qr_code_settings(body_json: str) -> str:
    """
    Create Or Update the Mobile application settings (saveMobileAppSettings)  # noqa: E501

The request payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param QrCodeSettings body: (required)
:return: QrCodeSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_qr_code_settings(body=deserialize_param(body_json, 'QrCodeSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_qr_code_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_repository_settings(body: Optional[str] = None) -> str:
    """
    Creates or Updates the repository settings (saveRepositorySettings)  # noqa: E501

Creates or Updates the repository settings object.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param RepositorySettings body:
:return: DeferredResultRepositorySettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_repository_settings(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_repository_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_secret(body_json: str) -> str:
    """
    Save or Update Secret (saveSecret)  # noqa: E501

Create or update the Secret. When creating secret, platform generates Secret Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Secret Id will be present in the response. Specify existing Secret Id to update the secret. Secret name is not updatable, only value could be changed. Referencing non-existing Secret Id will cause 'Not Found' error.  Secret name is unique in the scope of tenant.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param Secret body: (required)
:return: SecretInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_secret(body=deserialize_param(body_json, 'Secret'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_secret'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_security_settings(body: Optional[str] = None) -> str:
    """
    Update Security Settings (saveSecuritySettings)  # noqa: E501

Updates the Security Settings object that contains password policy, etc.  Available for users with 'SYS_ADMIN' authority.  Security check is performed to verify that the user has 'WRITE' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param SecuritySettings body:
:return: SecuritySettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_security_settings(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_security_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_self_registration_params(body: Optional[str] = None) -> str:
    """
    Create Or Update Self Registration parameters (saveSelfRegistrationParams)  # noqa: E501

Creates or Updates the Self Registration parameters. When creating, platform generates Admin Settings Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Admin Settings Id will be present in the response. Specify existing Admin Settings Id to update the Self Registration parameters. Referencing non-existing Admin Settings Id will cause 'Not Found' error.  Self Registration allows users to signup for using the platform and automatically create a Customer account for them. You may configure default dashboard and user roles that will be assigned for this Customer. This allows you to build out-of-the-box solutions for customers. Ability to white-label the login and main pages helps to brand the platform.  Available for users with 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param SelfRegistrationParams body:
:return: SelfRegistrationParams
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_self_registration_params(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_self_registration_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_trendz_settings(body_json: str) -> str:
    """
    Save Trendz settings (saveTrendzSettings)  # noqa: E501

Saves Trendz settings for this tenant.   Here is an example of the Trendz settings: ```json {   "enabled": true,   "baseUrl": "https://some.domain.com:18888/also_necessary_prefix" } ```  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param TrendzSettings body: (required)
:return: TrendzSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_trendz_settings(body=deserialize_param(body_json, 'TrendzSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_trendz_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_web_self_registration_params(body: str) -> str:
    """
    Create Or Update Self Registration parameters (saveSelfRegistrationParams)  # noqa: E501

Creates or Updates the Self Registration parameters. When creating, platform generates Admin Settings Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Admin Settings Id will be present in the response. Specify existing Admin Settings Id to update the Self Registration parameters. Referencing non-existing Admin Settings Id will cause 'Not Found' error.  Self Registration allows users to signup for using the platform and automatically create a Customer account for them. You may configure default dashboard and user roles that will be assigned for this Customer. This allows you to build out-of-the-box solutions for customers. Ability to white-label the login and main pages helps to brand the platform.  Available for users with 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param object body: (required)
:return: WebSelfRegistrationParams
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_web_self_registration_params(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_web_self_registration_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_white_label_params(body: Optional[str] = None) -> str:
    """
    Create Or Update White Labeling configuration (saveWhiteLabelParams)  # noqa: E501

Creates or Updates the White Labeling configuration.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param WhiteLabelingParams body:
:param str customer_id: A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'
:return: WhiteLabelingParams
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_white_label_params(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def send_activation_email(email: str) -> str:
    """
    Send or re-send the activation email  # noqa: E501

Force send the activation email to the user. Useful to resend the email if user has accidentally deleted it.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str email: Email of the user (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.send_activation_email(email=email)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'send_activation_email'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def send_chat_request(body_json: str) -> str:
    """
    Send request to AI chat model (sendChatRequest)  # noqa: E501

Submits a single prompt - made up of an optional system message and a required user message - to the specified AI chat model and returns either the generated answer or an error envelope.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param TbChatRequest body: (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.send_chat_request(body=deserialize_param(body_json, 'TbChatRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'send_chat_request'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def send_password_was_reset_email(body: str) -> str:
    """
    sendPasswordWasResetEmail  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str body: sendPassowordWasResetEmailRequest (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.send_password_was_reset_email(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'send_password_was_reset_email'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def send_reset_password_email(body: str) -> str:
    """
    sendResetPasswordEmail  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str body: sendResetPasswordEmailRequest (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.send_reset_password_email(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'send_reset_password_email'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def send_test_mail(body: Optional[str] = None) -> str:
    """
    Send test email (sendTestMail)  # noqa: E501

Attempts to send test email using Mail Settings provided as a parameter. Email is sent to the address specified in the profile of user who is performing the requestYou may change the 'To' email in the user profile of the System/Tenant Administrator.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param AdminSettings body:
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.send_test_mail(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'send_test_mail'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def send_test_sms(body: Optional[str] = None) -> str:
    """
    Send test sms (sendTestMail)  # noqa: E501

Attempts to send test sms to the System Administrator User using SMS Settings and phone number provided as a parameters of the request.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param TestSmsRequest body:
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.send_test_sms(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'send_test_sms'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def setDaemon(daemonic: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.setDaemon(daemonic=daemonic)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'setDaemon'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def setName(name: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.setName(name=name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'setName'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sig_fox_process_request_v11_post11(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v11_post11(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'sig_fox_process_request_v11_post11'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sig_fox_process_request_v3_delete3(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_delete3(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'sig_fox_process_request_v3_delete3'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sig_fox_process_request_v3_get3(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_get3(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'sig_fox_process_request_v3_get3'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sig_fox_process_request_v3_head3(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_head3(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'sig_fox_process_request_v3_head3'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sig_fox_process_request_v3_options3(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_options3(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'sig_fox_process_request_v3_options3'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sig_fox_process_request_v3_patch3(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_patch3(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'sig_fox_process_request_v3_patch3'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sig_fox_process_request_v3_put3(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_put3(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'sig_fox_process_request_v3_put3'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sign_up(body: Optional[str] = None) -> str:
    """
    User Sign Up (signUp)  # noqa: E501

Process user sign up request. Creates the Customer and corresponding User based on self Registration parameters for the domain. See [Self Registration Controller](/swagger-ui.html#/self-registration-controller) for more details.  The result is either 'SUCCESS' or 'INACTIVE_USER_EXISTS'. If Success, the user will receive an email with instruction to activate the account. The content of the email is customizable via the mail templates.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param SignUpRequest body:
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.sign_up(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'sign_up'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def start() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.start()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'start'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def stop() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.stop()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'stop'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def subscribe_to_commands(device_token: str, timeout: Optional[str] = None) -> str:
    """
    Subscribe to RPC commands (subscribeToCommands) (Deprecated)  # noqa: E501

Subscribes to RPC commands using http long polling. Deprecated, since long polling is resource and network consuming. Consider using MQTT or CoAP protocol for light-weight real-time updates.   The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str device_token: Your device access token. (required)
:param int timeout: Optional timeout of the long poll. Typically less then 60 seconds, since limited on the server side.
:return: DeferredResultResponseEntity
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.subscribe_to_commands(device_token=device_token, timeout=timeout)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'subscribe_to_commands'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def t_mobile_iot_cdp_process_request_v12_post12(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v12_post12(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 't_mobile_iot_cdp_process_request_v12_post12'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def t_mobile_iot_cdp_process_request_v4_delete4(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_delete4(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 't_mobile_iot_cdp_process_request_v4_delete4'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def t_mobile_iot_cdp_process_request_v4_get4(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_get4(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 't_mobile_iot_cdp_process_request_v4_get4'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def t_mobile_iot_cdp_process_request_v4_head4(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_head4(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 't_mobile_iot_cdp_process_request_v4_head4'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def t_mobile_iot_cdp_process_request_v4_options4(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_options4(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 't_mobile_iot_cdp_process_request_v4_options4'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def t_mobile_iot_cdp_process_request_v4_patch4(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_patch4(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 't_mobile_iot_cdp_process_request_v4_patch4'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def t_mobile_iot_cdp_process_request_v4_put4(body: str, request_headers: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_put4(body=body, request_headers=request_headers, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 't_mobile_iot_cdp_process_request_v4_put4'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def terms_of_use_accepted() -> str:
    """
    Check Terms Of User (termsOfUseAccepted)  # noqa: E501

Checks that current user accepted the privacy policy.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: bool
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.terms_of_use_accepted()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'terms_of_use_accepted'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def test_script(body: str) -> str:
    """
    Test Script function  # noqa: E501

Execute the Script function and return the result. The format of request:   ```json {   "script": "Your Function as String",   "scriptType": "One of: update, generate, filter, switch, json, string",   "argNames": ["msg", "metadata", "type"],   "msg": "{\\"temperature\\": 42}",    "metadata": {     "deviceName": "Device A",     "deviceType": "Thermometer"   },   "msgType": "POST_TELEMETRY_REQUEST" } ```   Expected result JSON contains "output" and "error".  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param JsonNode body:
:param str script_lang: Script language: JS or TBEL
:return: JsonNode
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.test_script(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'test_script'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_tpe_delete(body: str, request_headers: str, all_request_params: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_delete(body=body, request_headers=request_headers, all_request_params=all_request_params, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'thing_park_process_request_tpe_delete'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_tpe_get(body: str, request_headers: str, all_request_params: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_get(body=body, request_headers=request_headers, all_request_params=all_request_params, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'thing_park_process_request_tpe_get'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_tpe_head(body: str, request_headers: str, all_request_params: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_head(body=body, request_headers=request_headers, all_request_params=all_request_params, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'thing_park_process_request_tpe_head'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_tpe_options(body: str, request_headers: str, all_request_params: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_options(body=body, request_headers=request_headers, all_request_params=all_request_params, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'thing_park_process_request_tpe_options'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_tpe_patch(body: str, request_headers: str, all_request_params: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_patch(body=body, request_headers=request_headers, all_request_params=all_request_params, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'thing_park_process_request_tpe_patch'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_tpe_post(body: str, request_headers: str, all_request_params: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_post(body=body, request_headers=request_headers, all_request_params=all_request_params, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'thing_park_process_request_tpe_post'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_tpe_put(body: str, request_headers: str, all_request_params: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_put(body=body, request_headers=request_headers, all_request_params=all_request_params, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'thing_park_process_request_tpe_put'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_v13_post13(body: str, request_headers: str, all_request_params: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v13_post13(body=body, request_headers=request_headers, all_request_params=all_request_params, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'thing_park_process_request_v13_post13'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_v5_delete5(body: str, request_headers: str, all_request_params: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_delete5(body=body, request_headers=request_headers, all_request_params=all_request_params, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'thing_park_process_request_v5_delete5'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_v5_get5(body: str, request_headers: str, all_request_params: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_get5(body=body, request_headers=request_headers, all_request_params=all_request_params, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'thing_park_process_request_v5_get5'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_v5_head5(body: str, request_headers: str, all_request_params: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_head5(body=body, request_headers=request_headers, all_request_params=all_request_params, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'thing_park_process_request_v5_head5'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_v5_options5(body: str, request_headers: str, all_request_params: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_options5(body=body, request_headers=request_headers, all_request_params=all_request_params, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'thing_park_process_request_v5_options5'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_v5_patch5(body: str, request_headers: str, all_request_params: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_patch5(body=body, request_headers=request_headers, all_request_params=all_request_params, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'thing_park_process_request_v5_patch5'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_v5_put5(body: str, request_headers: str, all_request_params: str, routing_key: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_put5(body=body, request_headers=request_headers, all_request_params=all_request_params, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'thing_park_process_request_v5_put5'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def uninstall_solution_template(solution_template_id: str) -> str:
    """
    Uninstall Solution Template (uninstallSolutionTemplate)  # noqa: E501

Uninstall solution template based on the provided id   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str solution_template_id: A string value representing the solution template id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.uninstall_solution_template(solution_template_id=solution_template_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'uninstall_solution_template'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_custom_menu_assignee_list(id_json: str, assignee_type: str, body_json: str, force: Optional[str] = None) -> str:
    """
    Update custom menu assignee list (updateCustomMenuAssigneeList)  # noqa: E501

The api designed to update the list of assignees or assignee type based on the provided Custom Menu Id. To change assignee type, put new assignee type in path parameter.  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:param str assignee_type: (required)
:param list[str] body:
:param bool force: Use force if you want to override default menu
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.update_custom_menu_assignee_list(id=deserialize_param(id_json, 'CustomMenuId'), assignee_type=assignee_type, body=json.loads(body_json) if body_json else None, force=force)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'update_custom_menu_assignee_list'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_custom_menu_config(id_json: str, body_json: str) -> str:
    """
    Update Custom Menu configuration based on the provided Custom Menu Id (updateCustomMenuConfig)  # noqa: E501

  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param CustomMenuConfig body: (required)
:param str custom_menu_id: A string value representing the custom menu id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: CustomMenu
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.update_custom_menu_config(id=deserialize_param(id_json, 'CustomMenuId'), body=deserialize_param(body_json, 'CustomMenuConfig'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'update_custom_menu_config'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_custom_menu_name(id_json: str, body: str) -> str:
    """
    Update Custom Menu name based on the provided Custom Menu Id (updateCustomMenuName)  # noqa: E501

  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str body: (required)
:param str custom_menu_id: A string value representing the custom menu id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.update_custom_menu_name(id=deserialize_param(id_json, 'CustomMenuId'), body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'update_custom_menu_name'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_image(_type: str, key: str, file: str) -> str:
    """
    updateImage  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str type: Type of the image: tenant or system (required)
:param str key: Image resource key, for example thermostats_dashboard_background.jpeg (required)
:param str file:
:return: TbResourceInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.update_image(_type=_type, key=key, file=file)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'update_image'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_image_info(_type: str, key: str, body_json: str) -> str:
    """
    updateImageInfo  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str type: Type of the image: tenant or system (required)
:param str key: Image resource key, for example thermostats_dashboard_background.jpeg (required)
:param TbResourceInfo body:
:return: TbResourceInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.update_image_info(_type=_type, key=key, body=deserialize_param(body_json, 'TbResourceInfo'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'update_image_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_image_public_status(_type: str, key: str, is_public: Optional[str] = None) -> str:
    """
    updateImagePublicStatus  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str type: Type of the image: tenant or system (required)
:param str key: Image resource key, for example thermostats_dashboard_background.jpeg (required)
:param bool is_public: isPublic (required)
:return: TbResourceInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.update_image_public_status(_type=_type, key=key, is_public=is_public)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'update_image_public_status'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_secret_description(id_json: str, description: str) -> str:
    """
    Update Secret Description  # noqa: E501

Updates the description of the existing Secret by secretId. Only the description can be updated. Referencing a non-existing Secret Id will cause a 'Not Found' error.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: Unique identifier of the Secret to update (required)
:param object body:
:return: SecretInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.update_secret_description(id=deserialize_param(id_json, 'SecretId'), description=description)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'update_secret_description'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_secret_value(id_json: str, value: str) -> str:
    """
    Update Secret value  # noqa: E501

Updates the value of the existing Secret by secretId. Referencing a non-existing Secret Id will cause a 'Not Found' error.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param object body: (required)
:param str id: Unique identifier of the Secret to update (required)
:return: SecretInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.update_secret_value(id=deserialize_param(id_json, 'SecretId'), value=value)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'update_secret_value'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def upload_custom_translation(locale_code: str, file: str) -> str:
    """
    Upload Custom Translation (uploadCustomTranslation)  # noqa: E501

Upload the Custom Translation for specified locale.   Request example:   ```json {"home":"MyHome"} ```  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str locale_code: Locale code (e.g. 'en_US'). (required)
:param str file:
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.upload_custom_translation(locale_code=locale_code, file=file)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'upload_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def upload_image(title: str, file: str) -> str:
    """
    uploadImage  # noqa: E501

This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str file:
:param str title:
:return: TbResourceInfo
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.upload_image(title=title, file=file)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'upload_image'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def validate_calculated_field_reprocessing(id_json: str) -> str:
    """
    Validate reprocessing capability of a calculated field (validateCalculatedFieldReprocessing)  # noqa: E501

Checks whether the specified calculated field can be reprocessed. Returns a validation result indicating if reprocessing is allowed and, if not, provides a reason.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str calculated_field_id: (required)
:return: CfReprocessingValidationResult
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.validate_calculated_field_reprocessing(id=deserialize_param(id_json, 'CalculatedFieldId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'validate_calculated_field_reprocessing'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    """Register tools with FastMCP server"""
    mcp.tool()( accept_terms_of_use )
    mcp.tool()( activate_email )
    mcp.tool()( activate_instance )
    mcp.tool()( auto_commit_settings_exists )
    mcp.tool()( cancel_job )
    mcp.tool()( change_password )
    mcp.tool()( check_activate_token )
    mcp.tool()( check_instance )
    mcp.tool()( check_repository_access )
    mcp.tool()( check_reset_token )
    mcp.tool()( check_updates )
    mcp.tool()( chirp_stack_process_request_delete )
    mcp.tool()( chirp_stack_process_request_get )
    mcp.tool()( chirp_stack_process_request_head )
    mcp.tool()( chirp_stack_process_request_options )
    mcp.tool()( chirp_stack_process_request_patch )
    mcp.tool()( chirp_stack_process_request_post )
    mcp.tool()( chirp_stack_process_request_put )
    mcp.tool()( clear_events_post )
    mcp.tool()( code_processing_url )
    mcp.tool()( compare_entity_data_to_version )
    mcp.tool()( count_entities_by_query )
    mcp.tool()( create_custom_menu )
    mcp.tool()( create_notification_request )
    mcp.tool()( delete_ai_model_by_id )
    mcp.tool()( delete_auto_commit_settings )
    mcp.tool()( delete_blob_entity )
    mcp.tool()( delete_calculated_field )
    mcp.tool()( delete_client_registration_template )
    mcp.tool()( delete_current_login_white_label_params )
    mcp.tool()( delete_current_white_label_params )
    mcp.tool()( delete_custom_menu )
    mcp.tool()( delete_custom_translation )
    mcp.tool()( delete_custom_translation_key )
    mcp.tool()( delete_domain )
    mcp.tool()( delete_entity_view )
    mcp.tool()( delete_image )
    mcp.tool()( delete_job )
    mcp.tool()( delete_mobile_app )
    mcp.tool()( delete_mobile_app_bundle )
    mcp.tool()( delete_notification )
    mcp.tool()( delete_notification_request )
    mcp.tool()( delete_notification_rule )
    mcp.tool()( delete_notification_target_by_id )
    mcp.tool()( delete_notification_template_by_id )
    mcp.tool()( delete_repository_settings )
    mcp.tool()( delete_rpc )
    mcp.tool()( delete_secret )
    mcp.tool()( delete_self_registration_params )
    mcp.tool()( delete_web_self_registration_params )
    mcp.tool()( download_blob_entity )
    mcp.tool()( download_full_translation )
    mcp.tool()( download_gateway_docker_compose )
    mcp.tool()( download_image )
    mcp.tool()( download_image_preview )
    mcp.tool()( download_login_favicon )
    mcp.tool()( download_login_logo )
    mcp.tool()( download_public_image )
    mcp.tool()( download_server_certificate )
    mcp.tool()( export_image )
    mcp.tool()( find_by_from )
    mcp.tool()( find_by_from_v1 )
    mcp.tool()( find_by_query )
    mcp.tool()( find_by_query_v1 )
    mcp.tool()( find_by_query_v2 )
    mcp.tool()( find_by_query_v3 )
    mcp.tool()( find_by_query_v4 )
    mcp.tool()( find_by_to )
    mcp.tool()( find_by_to_v1 )
    mcp.tool()( find_entity_data_by_query )
    mcp.tool()( find_info_by_from )
    mcp.tool()( find_info_by_query )
    mcp.tool()( find_info_by_to )
    mcp.tool()( getName )
    mcp.tool()( get_activation_link )
    mcp.tool()( get_activation_link_info )
    mcp.tool()( get_ai_model_by_id )
    mcp.tool()( get_ai_models )
    mcp.tool()( get_all_entity_view_infos )
    mcp.tool()( get_application_redirect )
    mcp.tool()( get_auto_commit_settings )
    mcp.tool()( get_available_delivery_methods )
    mcp.tool()( get_available_java_locales )
    mcp.tool()( get_available_locales )
    mcp.tool()( get_blob_entities )
    mcp.tool()( get_blob_entities_by_ids )
    mcp.tool()( get_blob_entity_info_by_id )
    mcp.tool()( get_calculated_field_by_id )
    mcp.tool()( get_calculated_fields_by_entity_id )
    mcp.tool()( get_client_registration_templates )
    mcp.tool()( get_client_registration_templates1 )
    mcp.tool()( get_client_registration_templates_mail )
    mcp.tool()( get_component_descriptor_by_clazz )
    mcp.tool()( get_component_descriptors_by_type )
    mcp.tool()( get_component_descriptors_by_types )
    mcp.tool()( get_current_login_white_label_params )
    mcp.tool()( get_current_white_label_params )
    mcp.tool()( get_custom_menu )
    mcp.tool()( get_custom_menu_assignee_list )
    mcp.tool()( get_custom_menu_config )
    mcp.tool()( get_custom_menu_info_by_id )
    mcp.tool()( get_custom_menu_infos )
    mcp.tool()( get_custom_translation )
    mcp.tool()( get_domain_info_by_id )
    mcp.tool()( get_domain_infos )
    mcp.tool()( get_downlink_payload )
    mcp.tool()( get_edqs_state )
    mcp.tool()( get_entities )
    mcp.tool()( get_entity_data_info )
    mcp.tool()( get_entity_view_by_id )
    mcp.tool()( get_entity_view_info_by_id )
    mcp.tool()( get_entity_view_types )
    mcp.tool()( get_entity_views_by_ids )
    mcp.tool()( get_events_get )
    mcp.tool()( get_events_post )
    mcp.tool()( get_events_v1_get1 )
    mcp.tool()( get_features_info )
    mcp.tool()( get_firmware )
    mcp.tool()( get_firmware_by_id )
    mcp.tool()( get_full_translation )
    mcp.tool()( get_help_base_url )
    mcp.tool()( get_image_info )
    mcp.tool()( get_images )
    mcp.tool()( get_job_by_id )
    mcp.tool()( get_jobs )
    mcp.tool()( get_jwt_setting )
    mcp.tool()( get_last_calculated_field_reprocessing_job )
    mcp.tool()( get_latest_calculated_field_debug_event )
    mcp.tool()( get_latest_rule_node_debug_input )
    mcp.tool()( get_license_usage_info )
    mcp.tool()( get_login_mobile_info )
    mcp.tool()( get_login_page_translation )
    mcp.tool()( get_login_processing_url )
    mcp.tool()( get_login_white_label_params )
    mcp.tool()( get_lwm2m_bootstrap_security_info )
    mcp.tool()( get_lwm2m_list_objects )
    mcp.tool()( get_lwm2m_list_objects_page )
    mcp.tool()( get_mail_processing_url )
    mcp.tool()( get_max_datapoints_limit )
    mcp.tool()( get_merged_custom_translation )
    mcp.tool()( get_merged_mobile_app_settings )
    mcp.tool()( get_mobile_app_bundle_info_by_id )
    mcp.tool()( get_mobile_app_by_id )
    mcp.tool()( get_mobile_app_deep_link )
    mcp.tool()( get_mobile_app_info_by_id )
    mcp.tool()( get_mobile_app_settings )
    mcp.tool()( get_mobile_session )
    mcp.tool()( get_notification_request_by_id )
    mcp.tool()( get_notification_request_preview )
    mcp.tool()( get_notification_requests )
    mcp.tool()( get_notification_rule_by_id )
    mcp.tool()( get_notification_rules )
    mcp.tool()( get_notification_settings )
    mcp.tool()( get_notification_target_by_id )
    mcp.tool()( get_notification_targets )
    mcp.tool()( get_notification_targets_by_ids )
    mcp.tool()( get_notification_targets_by_supported_notification_type )
    mcp.tool()( get_notification_template_by_id )
    mcp.tool()( get_notification_templates )
    mcp.tool()( get_notifications )
    mcp.tool()( get_owner_info )
    mcp.tool()( get_owner_infos )
    mcp.tool()( get_owners )
    mcp.tool()( get_persisted_rpc )
    mcp.tool()( get_privacy_policy )
    mcp.tool()( get_qr_code_settings )
    mcp.tool()( get_recipients_for_notification_target_config )
    mcp.tool()( get_repository_settings )
    mcp.tool()( get_repository_settings_info )
    mcp.tool()( get_secret_info_by_id )
    mcp.tool()( get_secret_info_by_name )
    mcp.tool()( get_secret_infos )
    mcp.tool()( get_secret_names )
    mcp.tool()( get_security_settings )
    mcp.tool()( get_self_registration_params )
    mcp.tool()( get_server_time )
    mcp.tool()( get_sign_up_self_registration_params )
    mcp.tool()( get_software )
    mcp.tool()( get_solution_template_details )
    mcp.tool()( get_solution_template_infos )
    mcp.tool()( get_solution_template_instructions )
    mcp.tool()( get_system_info )
    mcp.tool()( get_terms_of_use )
    mcp.tool()( get_translation_for_basic_edit )
    mcp.tool()( get_translation_infos )
    mcp.tool()( get_trendz_settings )
    mcp.tool()( get_unread_notifications_count )
    mcp.tool()( get_uplink_payload )
    mcp.tool()( get_vendor_models )
    mcp.tool()( get_vendors )
    mcp.tool()( get_version_create_request_status )
    mcp.tool()( get_version_load_request_status )
    mcp.tool()( get_web_self_registration_params )
    mcp.tool()( get_white_label_params )
    mcp.tool()( handle_rule_engine_request )
    mcp.tool()( handle_rule_engine_request_v1 )
    mcp.tool()( handle_rule_engine_request_v2 )
    mcp.tool()( http_check_status_get )
    mcp.tool()( http_process_request_v1_post1 )
    mcp.tool()( http_process_request_v2_post2 )
    mcp.tool()( import_image )
    mcp.tool()( install_solution_template )
    mcp.tool()( isDaemon )
    mcp.tool()( is_alive )
    mcp.tool()( is_edqs_api_enabled )
    mcp.tool()( is_tbel_enabled )
    mcp.tool()( is_white_labeling_allowed )
    mcp.tool()( join )
    mcp.tool()( list_all_entities_at_version )
    mcp.tool()( list_branches )
    mcp.tool()( list_entities_at_version )
    mcp.tool()( list_entity_type_versions )
    mcp.tool()( list_entity_versions )
    mcp.tool()( list_slack_conversations )
    mcp.tool()( list_versions )
    mcp.tool()( load_entities_version )
    mcp.tool()( mark_all_notifications_as_read )
    mcp.tool()( mark_notification_as_read )
    mcp.tool()( mobile_login )
    mcp.tool()( patch_custom_translation )
    mcp.tool()( post_rpc_request )
    mcp.tool()( preview_white_label_params )
    mcp.tool()( privacy_policy_accepted )
    mcp.tool()( process_system_edqs_request )
    mcp.tool()( refresh )
    mcp.tool()( remove_mobile_session )
    mcp.tool()( reply_to_command )
    mcp.tool()( repository_settings_exists )
    mcp.tool()( reprocess_calculated_field )
    mcp.tool()( reprocess_job )
    mcp.tool()( request_reset_password_by_email )
    mcp.tool()( resend_email_activation )
    mcp.tool()( reset_password )
    mcp.tool()( rpc_v2_get_persisted_rpc )
    mcp.tool()( run )
    mcp.tool()( save_ai_model )
    mcp.tool()( save_auto_commit_settings )
    mcp.tool()( save_calculated_field )
    mcp.tool()( save_client_registration_template )
    mcp.tool()( save_custom_translation )
    mcp.tool()( save_domain )
    mcp.tool()( save_entities_version )
    mcp.tool()( save_entity_view )
    mcp.tool()( save_jwt_settings )
    mcp.tool()( save_login_white_label_params )
    mcp.tool()( save_mobile_app )
    mcp.tool()( save_mobile_app_bundle )
    mcp.tool()( save_mobile_app_settings )
    mcp.tool()( save_mobile_session )
    mcp.tool()( save_notification_rule )
    mcp.tool()( save_notification_settings )
    mcp.tool()( save_notification_target )
    mcp.tool()( save_notification_template )
    mcp.tool()( save_qr_code_settings )
    mcp.tool()( save_repository_settings )
    mcp.tool()( save_secret )
    mcp.tool()( save_security_settings )
    mcp.tool()( save_self_registration_params )
    mcp.tool()( save_trendz_settings )
    mcp.tool()( save_web_self_registration_params )
    mcp.tool()( save_white_label_params )
    mcp.tool()( send_activation_email )
    mcp.tool()( send_chat_request )
    mcp.tool()( send_password_was_reset_email )
    mcp.tool()( send_reset_password_email )
    mcp.tool()( send_test_mail )
    mcp.tool()( send_test_sms )
    mcp.tool()( setDaemon )
    mcp.tool()( setName )
    mcp.tool()( sig_fox_process_request_v11_post11 )
    mcp.tool()( sig_fox_process_request_v3_delete3 )
    mcp.tool()( sig_fox_process_request_v3_get3 )
    mcp.tool()( sig_fox_process_request_v3_head3 )
    mcp.tool()( sig_fox_process_request_v3_options3 )
    mcp.tool()( sig_fox_process_request_v3_patch3 )
    mcp.tool()( sig_fox_process_request_v3_put3 )
    mcp.tool()( sign_up )
    mcp.tool()( start )
    mcp.tool()( stop )
    mcp.tool()( subscribe_to_commands )
    mcp.tool()( t_mobile_iot_cdp_process_request_v12_post12 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_delete4 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_get4 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_head4 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_options4 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_patch4 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_put4 )
    mcp.tool()( terms_of_use_accepted )
    mcp.tool()( test_script )
    mcp.tool()( thing_park_process_request_tpe_delete )
    mcp.tool()( thing_park_process_request_tpe_get )
    mcp.tool()( thing_park_process_request_tpe_head )
    mcp.tool()( thing_park_process_request_tpe_options )
    mcp.tool()( thing_park_process_request_tpe_patch )
    mcp.tool()( thing_park_process_request_tpe_post )
    mcp.tool()( thing_park_process_request_tpe_put )
    mcp.tool()( thing_park_process_request_v13_post13 )
    mcp.tool()( thing_park_process_request_v5_delete5 )
    mcp.tool()( thing_park_process_request_v5_get5 )
    mcp.tool()( thing_park_process_request_v5_head5 )
    mcp.tool()( thing_park_process_request_v5_options5 )
    mcp.tool()( thing_park_process_request_v5_patch5 )
    mcp.tool()( thing_park_process_request_v5_put5 )
    mcp.tool()( uninstall_solution_template )
    mcp.tool()( update_custom_menu_assignee_list )
    mcp.tool()( update_custom_menu_config )
    mcp.tool()( update_custom_menu_name )
    mcp.tool()( update_image )
    mcp.tool()( update_image_info )
    mcp.tool()( update_image_public_status )
    mcp.tool()( update_secret_description )
    mcp.tool()( update_secret_value )
    mcp.tool()( upload_custom_translation )
    mcp.tool()( upload_image )
    mcp.tool()( validate_calculated_field_reprocessing )
