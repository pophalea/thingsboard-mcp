import json
import tb_rest_client.models.models_ce as models
from ...shared import get_client, deserialize_param, format_response, ApiException


def activate_instance(license_secret: str, release_date: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.activate_instance(license_secret=license_secret, release_date=release_date)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'activate_instance'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def assign_entity_view_to_edge(edge_id_json: str, entity_view_id_json: str) -> str:
    """
    Assign entity view to edge (assignEntityViewToEdge)  # noqa: E501

Creates assignment of an existing entity view to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment entity view (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once entity view will be delivered to edge service, it's going to be available for usage on remote edge instance.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_entity_view_to_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_entity_view_to_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def auto_commit_settings_exists() -> str:
    """
    Check auto commit settings exists (autoCommitSettingsExists)  # noqa: E501

Check whether the auto commit settings exists.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.auto_commit_settings_exists()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'auto_commit_settings_exists'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def cancel_job(id_json: str) -> str:
    """
    cancelJob  # noqa: E501
    """
    try:
        client = get_client()
        result = client.cancel_job(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'cancel_job'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def change_password(body_json: str) -> str:
    """
    Change password for current User (changePassword)  # noqa: E501

Change the password for the User which credentials are used to perform this REST API call. Be aware that previously generated [JWT](https://jwt.io/) tokens will be still valid until they expire.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.change_password(body=deserialize_param(body_json, 'ChangePasswordRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'change_password'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def check_activate_token(activate_token: str) -> str:
    """
    Check Activate User Token (checkActivateToken)  # noqa: E501

Checks the activation token and forwards user to 'Create Password' page. If token is valid, returns '303 See Other' (redirect) response code with the correct address of 'Create Password' page and same 'activateToken' specified in the URL parameters. If token is not valid, returns '409 Conflict'.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.check_activate_token(activate_token=activate_token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'check_activate_token'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def check_repository_access(body_json: str) -> str:
    """
    Check repository access (checkRepositoryAccess)  # noqa: E501

Attempts to check repository access.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.check_repository_access(body=deserialize_param(body_json, 'RepositorySettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'check_repository_access'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def check_reset_token(reset_token: str) -> str:
    """
    Check password reset token (checkResetToken)  # noqa: E501

Checks the password reset token and forwards user to 'Reset Password' page. If token is valid, returns '303 See Other' (redirect) response code with the correct address of 'Reset Password' page and same 'resetToken' specified in the URL parameters. If token is not valid, returns '409 Conflict'.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.check_reset_token(reset_token=reset_token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'check_reset_token'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def check_updates() -> str:
    """
    Check for new Platform Releases (checkUpdates)  # noqa: E501

Check notifications about new platform releases.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.check_updates()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'check_updates'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def clear_events_post(entity_id_json: str, body_json: str, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    Clear Events (clearEvents)  # noqa: E501

Clears events by filter for specified entity.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.clear_events_post(entity_id=deserialize_param(entity_id_json, 'EntityId'), body=deserialize_param(body_json, 'EntityIdClearstartTimeendTimeBody'), start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'clear_events_post'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def code_processing_url(code: str, state: str) -> str:
    """
    codeProcessingUrl  # noqa: E501
    """
    try:
        client = get_client()
        result = client.code_processing_url(code=code, state=state)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'code_processing_url'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def compare_entity_data_to_version(entity_id_json: str, version_id: str) -> str:
    """
    Compare entity data to version (compareEntityDataToVersion)  # noqa: E501

Returns an object with current entity data and the one at a specific version. Entity data structure is the same as stored in a repository.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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

def count_entities_by_query(body_json: str) -> str:
    """
    Count Entities by Query  # noqa: E501

Allows to run complex queries to search the count of platform entities (devices, assets, customers, etc) based on the combination of main entity filter and multiple key filters. Returns the number of entities that match the query definition.  # Query Definition    Main **entity filter** is mandatory and defines generic search criteria. For example, "find all devices with profile 'Moisture Sensor'" or "Find all devices related to asset 'Building A'"  Optional **key filters** allow to filter results of the entity filter by complex criteria against main entity fields (name, label, type, etc), attributes and telemetry. For example, "temperature > 20 or temperature< 10" or "name starts with 'T', and attribute 'model' is 'T1000', and timeseries field 'batteryLevel' > 40".  Let's review the example:  ```json {   "entityFilter": {     "type": "entityType",     "entityType": "DEVICE"   },   "keyFilters": [     {       "key": {         "type": "ATTRIBUTE",         "key": "active"       },       "valueType": "BOOLEAN",       "predicate": {         "operation": "EQUAL",         "value": {           "defaultValue": true,           "dynamicValue": null         },         "type": "BOOLEAN"       }     }   ] } ```   Example mentioned above search all devices which have attribute 'active' set to 'true'. Now let's review available entity filters and key filters syntax:   # Entity Filters Entity Filter body depends on the 'type' parameter. Let's review available entity filter types. In fact, they do correspond to available dashboard aliases.  ## Single Entity  Allows to filter only one entity based on the id. For example, this entity filter selects certain device:  ```json {   "type": "singleEntity",   "singleEntity": {     "id": "d521edb0-2a7a-11ec-94eb-213c95f54092",     "entityType": "DEVICE"   } } ```  ## Entity List Filter  Allows to filter entities of the same type using their ids. For example, this entity filter selects two devices:  ```json {   "type": "entityList",   "entityType": "DEVICE",   "entityList": [     "e6501f30-2a7a-11ec-94eb-213c95f54092",     "e6657bf0-2a7a-11ec-94eb-213c95f54092"   ] } ```  ## Entity Name Filter  Allows to filter entities of the same type using the **'starts with'** expression over entity name. For example, this entity filter selects all devices which name starts with 'Air Quality':  ```json {   "type": "entityName",   "entityType": "DEVICE",   "entityNameFilter": "Air Quality" } ```  ## Entity Type Filter  Allows to filter entities based on their type (CUSTOMER, USER, DASHBOARD, ASSET, DEVICE, etc)For example, this entity filter selects all tenant customers:  ```json {   "type": "entityType",   "entityType": "CUSTOMER" } ```  ## Asset Type Filter  Allows to filter assets based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'charging station' assets which name starts with 'Tesla':  ```json {   "type": "assetType",   "assetType": "charging station",   "assetNameFilter": "Tesla" } ```  ## Device Type Filter  Allows to filter devices based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Temperature Sensor' devices which name starts with 'ABC':  ```json {   "type": "deviceType",   "deviceType": "Temperature Sensor",   "deviceNameFilter": "ABC" } ```  ## Edge Type Filter  Allows to filter edge instances based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Factory' edge instances which name starts with 'Nevada':  ```json {   "type": "edgeType",   "edgeType": "Factory",   "edgeNameFilter": "Nevada" } ```  ## Entity View Filter  Allows to filter entity views based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Concrete Mixer' entity views which name starts with 'CAT':  ```json {   "type": "entityViewType",   "entityViewType": "Concrete Mixer",   "entityViewNameFilter": "CAT" } ```  ## Api Usage Filter  Allows to query for Api Usage based on optional customer id. If the customer id is not set, returns current tenant API usage.For example, this entity filter selects the 'Api Usage' entity for customer with id 'e6501f30-2a7a-11ec-94eb-213c95f54092':  ```json {   "type": "apiUsageState",   "customerId": {     "id": "d521edb0-2a7a-11ec-94eb-213c95f54092",     "entityType": "CUSTOMER"   } } ```  ## Relations Query Filter  Allows to filter entities that are related to the provided root entity. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'filter' object allows you to define the relation type and set of acceptable entity types to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only those who match the 'filters'.  For example, this entity filter selects all devices and assets which are related to the asset with id 'e51de0c0-2a7a-11ec-94eb-213c95f54092':  ```json {   "type": "relationsQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e51de0c0-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 1,   "fetchLastLevelOnly": false,   "filters": [     {       "relationType": "Contains",       "entityTypes": [         "DEVICE",         "ASSET"       ]     }   ] } ```  ## Asset Search Query  Allows to filter assets that are related to the provided root entity. Filters related assets based on the relation type and set of asset types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'assetTypes' defines the type of the asset to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only assets that match 'relationType' and 'assetTypes' conditions.  For example, this entity filter selects 'charging station' assets which are related to the asset with id 'e51de0c0-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "assetSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e51de0c0-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 1,   "fetchLastLevelOnly": false,   "relationType": "Contains",   "assetTypes": [     "charging station"   ] } ```  ## Device Search Query  Allows to filter devices that are related to the provided root entity. Filters related devices based on the relation type and set of device types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'deviceTypes' defines the type of the device to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only devices that match 'relationType' and 'deviceTypes' conditions.  For example, this entity filter selects 'Charging port' and 'Air Quality Sensor' devices which are related to the asset with id 'e52b0020-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "deviceSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e52b0020-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 2,   "fetchLastLevelOnly": true,   "relationType": "Contains",   "deviceTypes": [     "Air Quality Sensor",     "Charging port"   ] } ```  ## Entity View Query  Allows to filter entity views that are related to the provided root entity. Filters related entity views based on the relation type and set of entity view types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'entityViewTypes' defines the type of the entity view to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only devices that match 'relationType' and 'deviceTypes' conditions.  For example, this entity filter selects 'Concrete mixer' entity views which are related to the asset with id 'e52b0020-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "entityViewSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e52b0020-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 1,   "fetchLastLevelOnly": false,   "relationType": "Contains",   "entityViewTypes": [     "Concrete mixer"   ] } ```  ## Edge Search Query  Allows to filter edge instances that are related to the provided root entity. Filters related edge instances based on the relation type and set of edge types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'deviceTypes' defines the type of the device to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only devices that match 'relationType' and 'deviceTypes' conditions.  For example, this entity filter selects 'Factory' edge instances which are related to the asset with id 'e52b0020-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "deviceSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e52b0020-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 2,   "fetchLastLevelOnly": true,   "relationType": "Contains",   "edgeTypes": [     "Factory"   ] } ```   # Key Filters Key Filter allows you to define complex logical expressions over entity field, attribute or latest time-series value. The filter is defined using 'key', 'valueType' and 'predicate' objects. Single Entity Query may have zero, one or multiple predicates. If multiple filters are defined, they are evaluated using logical 'AND'. The example below checks that temperature of the entity is above 20 degrees:  ```json {   "key": {     "type": "TIME_SERIES",     "key": "temperature"   },   "valueType": "NUMERIC",   "predicate": {     "operation": "GREATER",     "value": {       "defaultValue": 20,       "dynamicValue": null     },     "type": "NUMERIC"   } } ```   Now let's review 'key', 'valueType' and 'predicate' objects in detail.  ## Filter Key  Filter Key defines either entity field, attribute or telemetry. It is a JSON object that consists the key name and type. The following filter key types are supported:    * 'CLIENT_ATTRIBUTE' - used for client attributes;   * 'SHARED_ATTRIBUTE' - used for shared attributes;   * 'SERVER_ATTRIBUTE' - used for server attributes;   * 'ATTRIBUTE' - used for any of the above;   * 'TIME_SERIES' - used for time-series values;   * 'ENTITY_FIELD' - used for accessing entity fields like 'name', 'label', etc. The list of available fields depends on the entity type;   * 'ALARM_FIELD' - similar to entity field, but is used in alarm queries only;     Let's review the example:  ```json {   "type": "TIME_SERIES",   "key": "temperature" } ```  ## Value Type and Operations  Provides a hint about the data type of the entity field that is defined in the filter key. The value type impacts the list of possible operations that you may use in the corresponding predicate. For example, you may use 'STARTS_WITH' or 'END_WITH', but you can't use 'GREATER_OR_EQUAL' for string values.The following filter value types and corresponding predicate operations are supported:    * 'STRING' - used to filter any 'String' or 'JSON' values. Operations: EQUAL, NOT_EQUAL, STARTS_WITH, ENDS_WITH, CONTAINS, NOT_CONTAINS;   * 'NUMERIC' - used for 'Long' and 'Double' values. Operations: EQUAL, NOT_EQUAL, GREATER, LESS, GREATER_OR_EQUAL, LESS_OR_EQUAL;   * 'BOOLEAN' - used for boolean values. Operations: EQUAL, NOT_EQUAL;  * 'DATE_TIME' - similar to numeric, transforms value to milliseconds since epoch. Operations: EQUAL, NOT_EQUAL, GREATER, LESS, GREATER_OR_EQUAL, LESS_OR_EQUAL;    ## Filter Predicate  Filter Predicate defines the logical expression to evaluate. The list of available operations depends on the filter value type, see above. Platform supports 4 predicate types: 'STRING', 'NUMERIC', 'BOOLEAN' and 'COMPLEX'. The last one allows to combine multiple operations over one filter key.  Simple predicate example to check 'value < 100':   ```json {   "operation": "LESS",   "value": {     "defaultValue": 100,     "dynamicValue": null   },   "type": "NUMERIC" } ```  Complex predicate example, to check 'value < 10 or value > 20':   ```json {   "type": "COMPLEX",   "operation": "OR",   "predicates": [     {       "operation": "LESS",       "value": {         "defaultValue": 10,         "dynamicValue": null       },       "type": "NUMERIC"     },     {       "operation": "GREATER",       "value": {         "defaultValue": 20,         "dynamicValue": null       },       "type": "NUMERIC"     }   ] } ```  More complex predicate example, to check 'value < 10 or (value > 50 && value < 60)':   ```json {   "type": "COMPLEX",   "operation": "OR",   "predicates": [     {       "operation": "LESS",       "value": {         "defaultValue": 10,         "dynamicValue": null       },       "type": "NUMERIC"     },     {       "type": "COMPLEX",       "operation": "AND",       "predicates": [         {           "operation": "GREATER",           "value": {             "defaultValue": 50,             "dynamicValue": null           },           "type": "NUMERIC"         },         {           "operation": "LESS",           "value": {             "defaultValue": 60,             "dynamicValue": null           },           "type": "NUMERIC"         }       ]     }   ] } ```   You may also want to replace hardcoded values (for example, temperature > 20) with the more dynamic expression (for example, temperature > 'value of the tenant attribute with key 'temperatureThreshold'). It is possible to use 'dynamicValue' to define attribute of the tenant, customer or user that is performing the API call. See example below:   ```json {   "operation": "GREATER",   "value": {     "defaultValue": 0,     "dynamicValue": {       "sourceType": "CURRENT_USER",       "sourceAttribute": "temperatureThreshold"     }   },   "type": "NUMERIC" } ```   Note that you may use 'CURRENT_USER', 'CURRENT_CUSTOMER' and 'CURRENT_TENANT' as a 'sourceType'. The 'defaultValue' is used when the attribute with such a name is not defined for the chosen source.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.count_entities_by_query(body=deserialize_param(body_json, 'EntityCountQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'count_entities_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def create_notification_request(body_json: str) -> str:
    """
    Create notification request (createNotificationRequest)  # noqa: E501

Processes notification request. Mandatory request properties are `targets` (list of targets ids to send notification to), and either `templateId` (existing notification template id) or `template` (to send notification without saving the template). Optionally, you can set `sendingDelayInSec` inside the `additionalConfig` field to schedule the notification.  For each enabled delivery method in the notification template, there must be a target in the `targets` list that supports this delivery method: if you chose `WEB`, `EMAIL` or `SMS` - there must be at least one target in `targets` of `PLATFORM_USERS` type. For `SLACK` delivery method - you need to chose at least one `SLACK` notification target.  Notification request object with `PROCESSING` status will be returned immediately, and the notification sending itself is done asynchronously. After all notifications are sent, the `status` of the request becomes `SENT`. Use `getNotificationRequestById` to see the notification request processing status and some sending stats.   Here is an example of notification request to one target using saved template: ```json {   "templateId": {     "entityType": "NOTIFICATION_TEMPLATE",     "id": "6dbc3670-e4dd-11ed-9401-dbcc5dff78be"   },   "targets": [     "320e3ed0-d785-11ed-a06c-21dd57dd88ca"   ],   "additionalConfig": {     "sendingDelayInSec": 0   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.create_notification_request(body=deserialize_param(body_json, 'NotificationRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'create_notification_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_ai_model_by_id(ai_model_id_json: str) -> str:
    """
    Delete AI model by ID (deleteAiModelById)  # noqa: E501

Deletes the AI model record by its `id`. If a record with the specified `id` exists, the record is deleted and the endpoint returns `true`. If no such record exists, the endpoint returns `false`.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_ai_model_by_id(ai_model_id=deserialize_param(ai_model_id_json, 'AiModelId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_ai_model_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_auto_commit_settings() -> str:
    """
    Delete auto commit settings (deleteAutoCommitSettings)  # noqa: E501

Deletes the auto commit settings.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_auto_commit_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_auto_commit_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

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

def delete_client_registration_template(client_registration_template_id_json: str) -> str:
    """
    Delete OAuth2 client registration template by id (deleteClientRegistrationTemplate)  Available for users with 'SYS_ADMIN' authority.  # noqa: E501

Client registration template is OAuth2 provider configuration template with default settings for registering new OAuth2 clients  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_client_registration_template(client_registration_template_id=deserialize_param(client_registration_template_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_client_registration_template'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_domain(domain_id_json: str) -> str:
    """
    Delete Domain by ID (deleteDomain)  # noqa: E501

Deletes Domain by ID. Referencing non-existing domain Id will cause an error.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_domain(domain_id=deserialize_param(domain_id_json, 'DomainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_domain'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_edge(edge_id_json: str) -> str:
    """
    Delete edge (deleteEdge)  # noqa: E501

Deletes the edge. Referencing non-existing edge Id will cause an error.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_entity_view(entity_view_id_json: str) -> str:
    """
    Delete entity view (deleteEntityView)  # noqa: E501

Delete the EntityView object based on the provided entity view id.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_entity_view(entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_entity_view'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_image(_type: str, key: str, force: Optional[bool] = None) -> str:
    """
    deleteImage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_image(_type=_type, key=key, force=force)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_image'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_job(id_json: str) -> str:
    """
    deleteJob  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_job(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_job'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_mobile_app(mobile_app_id_json: str) -> str:
    """
    Delete Mobile App by ID (deleteMobileApp)  # noqa: E501

Deletes Mobile App by ID. Referencing non-existing mobile app Id will cause an error.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_mobile_app(mobile_app_id=deserialize_param(mobile_app_id_json, 'MobileAppId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_mobile_app'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_mobile_app_bundle(mobile_app_bundle_id_json: str) -> str:
    """
    Delete Mobile App Bundle by ID (deleteMobileAppBundle)  # noqa: E501

Deletes Mobile App Bundle by ID. Referencing non-existing mobile app bundle Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_mobile_app_bundle(mobile_app_bundle_id=deserialize_param(mobile_app_bundle_id_json, 'MobileAppBundleId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_mobile_app_bundle'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_notification(id: str) -> str:
    """
    Delete notification (deleteNotification)  # noqa: E501

Deletes notification by its id.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_notification(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_notification'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_notification_request(id: str) -> str:
    """
    Delete notification request (deleteNotificationRequest)  # noqa: E501

Deletes notification request by its id.  If the request has status `SENT` - all sent notifications for this request will be deleted. If it is `SCHEDULED`, the request will be cancelled.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_notification_request(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_notification_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_notification_rule(id: str) -> str:
    """
    Delete notification rule (deleteNotificationRule)  # noqa: E501

Deletes notification rule by id. Cancels all related scheduled notification requests (e.g. due to escalation table)  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_notification_rule(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_notification_rule'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_notification_target_by_id(id: str) -> str:
    """
    Delete notification target by id (deleteNotificationTargetById)  # noqa: E501

Deletes notification target by its id.  This target cannot be referenced by existing scheduled notification requests or any notification rules.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_notification_target_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_notification_target_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_notification_template_by_id(id: str) -> str:
    """
    Delete notification template by id (deleteNotificationTemplateById  # noqa: E501

Deletes notification template by its id.  This template cannot be referenced by existing scheduled notification requests or any notification rules.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_notification_template_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_notification_template_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_queue(queue_id_json: str) -> str:
    """
    Delete Queue (deleteQueue)  # noqa: E501

Deletes the Queue.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_queue(queue_id=deserialize_param(queue_id_json, 'QueueId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_queue'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_repository_settings() -> str:
    """
    Delete repository settings (deleteRepositorySettings)  # noqa: E501

Deletes the repository settings.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_repository_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_repository_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_resource(rpc_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.delete_resource(rpc_id=deserialize_param(rpc_id_json, 'RpcId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_resource'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_resource_v1(resource_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.delete_resource_v1(resource_id=deserialize_param(resource_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_resource_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_rpc(rpc_id_json: str) -> str:
    """
    Delete persistent RPC  # noqa: E501

Deletes the persistent RPC request.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_rpc(rpc_id=deserialize_param(rpc_id_json, 'RpcId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_rpc'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_gateway_docker_compose(device_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.download_gateway_docker_compose(device_id=deserialize_param(device_id_json, 'DeviceId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_gateway_docker_compose'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_image(_type: str, key: str, if_none_match: str = "") -> str:
    """
    downloadImage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_image(_type=_type, key=key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_image'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_image_preview(_type: str, key: str, if_none_match: str = "") -> str:
    """
    downloadImagePreview  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_image_preview(_type=_type, key=key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_image_preview'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_jks_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    Download JKS Resource (downloadJksResourceIfChanged)  # noqa: E501

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_jks_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_jks_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_js_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    Download JS Resource (downloadJsResourceIfChanged)  # noqa: E501

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_js_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_js_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_lwm2m_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    Download LWM2M Resource (downloadLwm2mResourceIfChanged)  # noqa: E501

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_lwm2m_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_lwm2m_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_pkcs12_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    Download PKCS_12 Resource (downloadPkcs12ResourceIfChanged)  # noqa: E501

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_pkcs12_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_pkcs12_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_public_image(public_resource_key: str, if_none_match: str = "") -> str:
    """
    downloadPublicImage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_public_image(public_resource_key=public_resource_key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_public_image'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_resource(resource_id_json: str) -> str:
    """
    Download Resource (downloadResource)  # noqa: E501

Download Resource based on the provided Resource Id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_resource(resource_id=deserialize_param(resource_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_resource'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_resource_if_changed(resource_type: str, scope: str, key: str, if_none_match: str = "") -> str:
    """
    Download resource (downloadResource)  # noqa: E501

Download resource with a given type and key for the given scope  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_resource_if_changed(resource_type=resource_type, scope=scope, key=key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_server_certificate(protocol: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.download_server_certificate(protocol=protocol)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_server_certificate'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def export_image(_type: str, key: str) -> str:
    """
    exportImage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.export_image(_type=_type, key=key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'export_image'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_from(from_id_json: str, relation_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    Get List of Relations (findByFrom)  # noqa: E501

Returns list of relation objects for the specified entity by the 'from' direction and relation type.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer.  # noqa: E501
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

def find_by_query(body_json: str) -> str:
    """
    Find related assets (findByQuery)  # noqa: E501

Returns all assets that are related to the specific entity. The entity id, relation type, asset types, depth of the search, and other query parameters defined using complex 'AssetSearchQuery' object. See 'Model' tab of the Parameters for more info.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_by_query(body=deserialize_param(body_json, 'AssetSearchQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_query_v1(body_json: str) -> str:
    """
    Find related devices (findByQuery)  # noqa: E501

Returns all devices that are related to the specific entity. The entity id, relation type, device types, depth of the search, and other query parameters defined using complex 'DeviceSearchQuery' object. See 'Model' tab of the Parameters for more info.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_by_query_v1(body=deserialize_param(body_json, 'DeviceSearchQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_query_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_query_v2(body_json: str) -> str:
    """
    Find related edges (findByQuery)  # noqa: E501

Returns all edges that are related to the specific entity. The entity id, relation type, edge types, depth of the search, and other query parameters defined using complex 'EdgeSearchQuery' object. See 'Model' tab of the Parameters for more info.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_by_query_v2(body=deserialize_param(body_json, 'EdgeSearchQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_query_v2'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_query_v3(body_json: str) -> str:
    """
    Find related entities (findByQuery)  # noqa: E501

Returns all entities that are related to the specific entity. The entity id, relation type, entity types, depth of the search, and other query parameters defined using complex 'EntityRelationsQuery' object. See 'Model' tab of the Parameters for more info.  # noqa: E501
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

def find_by_query_v4(body_json: str) -> str:
    """
    Find related entity views (findByQuery)  # noqa: E501

Returns all entity views that are related to the specific entity. The entity id, relation type, entity view types, depth of the search, and other query parameters defined using complex 'EntityViewSearchQuery' object. See 'Model' tab of the Parameters for more info.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_by_query_v4(body=deserialize_param(body_json, 'EntityViewSearchQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_query_v4'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_to(to_id_json: str, relation_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    Get List of Relations (findByTo)  # noqa: E501

Returns list of relation objects for the specified entity by the 'to' direction and relation type.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer.  # noqa: E501
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

def find_entity_data_by_query(body_json: str) -> str:
    """
    Find Entity Data by Query  # noqa: E501

Allows to run complex queries over platform entities (devices, assets, customers, etc) based on the combination of main entity filter and multiple key filters. Returns the paginated result of the query that contains requested entity fields and latest values of requested attributes and time-series data.  # Query Definition    Main **entity filter** is mandatory and defines generic search criteria. For example, "find all devices with profile 'Moisture Sensor'" or "Find all devices related to asset 'Building A'"  Optional **key filters** allow to filter results of the **entity filter** by complex criteria against main entity fields (name, label, type, etc), attributes and telemetry. For example, "temperature > 20 or temperature< 10" or "name starts with 'T', and attribute 'model' is 'T1000', and timeseries field 'batteryLevel' > 40".  The **entity fields** and **latest values** contains list of entity fields and latest attribute/telemetry fields to fetch for each entity.  The **page link** contains information about the page to fetch and the sort ordering.  Let's review the example:  ```json {   "entityFilter": {     "type": "entityType",     "resolveMultiple": true,     "entityType": "DEVICE"   },   "keyFilters": [     {       "key": {         "type": "TIME_SERIES",         "key": "temperature"       },       "valueType": "NUMERIC",       "predicate": {         "operation": "GREATER",         "value": {           "defaultValue": 0,           "dynamicValue": {             "sourceType": "CURRENT_USER",             "sourceAttribute": "temperatureThreshold",             "inherit": false           }         },         "type": "NUMERIC"       }     }   ],   "entityFields": [     {       "type": "ENTITY_FIELD",       "key": "name"     },     {       "type": "ENTITY_FIELD",       "key": "label"     },     {       "type": "ENTITY_FIELD",       "key": "additionalInfo"     }   ],   "latestValues": [     {       "type": "ATTRIBUTE",       "key": "model"     },     {       "type": "TIME_SERIES",       "key": "temperature"     }   ],   "pageLink": {     "page": 0,     "pageSize": 10,     "sortOrder": {       "key": {         "key": "name",         "type": "ENTITY_FIELD"       },       "direction": "ASC"     }   } } ```   Example mentioned above search all devices which have attribute 'active' set to 'true'. Now let's review available entity filters and key filters syntax:   # Entity Filters Entity Filter body depends on the 'type' parameter. Let's review available entity filter types. In fact, they do correspond to available dashboard aliases.  ## Single Entity  Allows to filter only one entity based on the id. For example, this entity filter selects certain device:  ```json {   "type": "singleEntity",   "singleEntity": {     "id": "d521edb0-2a7a-11ec-94eb-213c95f54092",     "entityType": "DEVICE"   } } ```  ## Entity List Filter  Allows to filter entities of the same type using their ids. For example, this entity filter selects two devices:  ```json {   "type": "entityList",   "entityType": "DEVICE",   "entityList": [     "e6501f30-2a7a-11ec-94eb-213c95f54092",     "e6657bf0-2a7a-11ec-94eb-213c95f54092"   ] } ```  ## Entity Name Filter  Allows to filter entities of the same type using the **'starts with'** expression over entity name. For example, this entity filter selects all devices which name starts with 'Air Quality':  ```json {   "type": "entityName",   "entityType": "DEVICE",   "entityNameFilter": "Air Quality" } ```  ## Entity Type Filter  Allows to filter entities based on their type (CUSTOMER, USER, DASHBOARD, ASSET, DEVICE, etc)For example, this entity filter selects all tenant customers:  ```json {   "type": "entityType",   "entityType": "CUSTOMER" } ```  ## Asset Type Filter  Allows to filter assets based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'charging station' assets which name starts with 'Tesla':  ```json {   "type": "assetType",   "assetType": "charging station",   "assetNameFilter": "Tesla" } ```  ## Device Type Filter  Allows to filter devices based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Temperature Sensor' devices which name starts with 'ABC':  ```json {   "type": "deviceType",   "deviceType": "Temperature Sensor",   "deviceNameFilter": "ABC" } ```  ## Edge Type Filter  Allows to filter edge instances based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Factory' edge instances which name starts with 'Nevada':  ```json {   "type": "edgeType",   "edgeType": "Factory",   "edgeNameFilter": "Nevada" } ```  ## Entity View Filter  Allows to filter entity views based on their type and the **'starts with'** expression over their name. For example, this entity filter selects all 'Concrete Mixer' entity views which name starts with 'CAT':  ```json {   "type": "entityViewType",   "entityViewType": "Concrete Mixer",   "entityViewNameFilter": "CAT" } ```  ## Api Usage Filter  Allows to query for Api Usage based on optional customer id. If the customer id is not set, returns current tenant API usage.For example, this entity filter selects the 'Api Usage' entity for customer with id 'e6501f30-2a7a-11ec-94eb-213c95f54092':  ```json {   "type": "apiUsageState",   "customerId": {     "id": "d521edb0-2a7a-11ec-94eb-213c95f54092",     "entityType": "CUSTOMER"   } } ```  ## Relations Query Filter  Allows to filter entities that are related to the provided root entity. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'filter' object allows you to define the relation type and set of acceptable entity types to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only those who match the 'filters'.  For example, this entity filter selects all devices and assets which are related to the asset with id 'e51de0c0-2a7a-11ec-94eb-213c95f54092':  ```json {   "type": "relationsQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e51de0c0-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 1,   "fetchLastLevelOnly": false,   "filters": [     {       "relationType": "Contains",       "entityTypes": [         "DEVICE",         "ASSET"       ]     }   ] } ```  ## Asset Search Query  Allows to filter assets that are related to the provided root entity. Filters related assets based on the relation type and set of asset types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'assetTypes' defines the type of the asset to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only assets that match 'relationType' and 'assetTypes' conditions.  For example, this entity filter selects 'charging station' assets which are related to the asset with id 'e51de0c0-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "assetSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e51de0c0-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 1,   "fetchLastLevelOnly": false,   "relationType": "Contains",   "assetTypes": [     "charging station"   ] } ```  ## Device Search Query  Allows to filter devices that are related to the provided root entity. Filters related devices based on the relation type and set of device types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'deviceTypes' defines the type of the device to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only devices that match 'relationType' and 'deviceTypes' conditions.  For example, this entity filter selects 'Charging port' and 'Air Quality Sensor' devices which are related to the asset with id 'e52b0020-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "deviceSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e52b0020-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 2,   "fetchLastLevelOnly": true,   "relationType": "Contains",   "deviceTypes": [     "Air Quality Sensor",     "Charging port"   ] } ```  ## Entity View Query  Allows to filter entity views that are related to the provided root entity. Filters related entity views based on the relation type and set of entity view types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'entityViewTypes' defines the type of the entity view to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only devices that match 'relationType' and 'deviceTypes' conditions.  For example, this entity filter selects 'Concrete mixer' entity views which are related to the asset with id 'e52b0020-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "entityViewSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e52b0020-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 1,   "fetchLastLevelOnly": false,   "relationType": "Contains",   "entityViewTypes": [     "Concrete mixer"   ] } ```  ## Edge Search Query  Allows to filter edge instances that are related to the provided root entity. Filters related edge instances based on the relation type and set of edge types. Possible direction values are 'TO' and 'FROM'. The 'maxLevel' defines how many relation levels should the query search 'recursively'. Assuming the 'maxLevel' is > 1, the 'fetchLastLevelOnly' defines either to return all related entities or only entities that are on the last level of relations. The 'relationType' defines the type of the relation to search for. The 'deviceTypes' defines the type of the device to search for. The relation query calculates all related entities, even if they are filtered using different relation types, and then extracts only devices that match 'relationType' and 'deviceTypes' conditions.  For example, this entity filter selects 'Factory' edge instances which are related to the asset with id 'e52b0020-2a7a-11ec-94eb-213c95f54092' using 'Contains' relation:  ```json {   "type": "deviceSearchQuery",   "rootEntity": {     "entityType": "ASSET",     "id": "e52b0020-2a7a-11ec-94eb-213c95f54092"   },   "direction": "FROM",   "maxLevel": 2,   "fetchLastLevelOnly": true,   "relationType": "Contains",   "edgeTypes": [     "Factory"   ] } ```   # Key Filters Key Filter allows you to define complex logical expressions over entity field, attribute or latest time-series value. The filter is defined using 'key', 'valueType' and 'predicate' objects. Single Entity Query may have zero, one or multiple predicates. If multiple filters are defined, they are evaluated using logical 'AND'. The example below checks that temperature of the entity is above 20 degrees:  ```json {   "key": {     "type": "TIME_SERIES",     "key": "temperature"   },   "valueType": "NUMERIC",   "predicate": {     "operation": "GREATER",     "value": {       "defaultValue": 20,       "dynamicValue": null     },     "type": "NUMERIC"   } } ```   Now let's review 'key', 'valueType' and 'predicate' objects in detail.  ## Filter Key  Filter Key defines either entity field, attribute or telemetry. It is a JSON object that consists the key name and type. The following filter key types are supported:    * 'CLIENT_ATTRIBUTE' - used for client attributes;   * 'SHARED_ATTRIBUTE' - used for shared attributes;   * 'SERVER_ATTRIBUTE' - used for server attributes;   * 'ATTRIBUTE' - used for any of the above;   * 'TIME_SERIES' - used for time-series values;   * 'ENTITY_FIELD' - used for accessing entity fields like 'name', 'label', etc. The list of available fields depends on the entity type;   * 'ALARM_FIELD' - similar to entity field, but is used in alarm queries only;     Let's review the example:  ```json {   "type": "TIME_SERIES",   "key": "temperature" } ```  ## Value Type and Operations  Provides a hint about the data type of the entity field that is defined in the filter key. The value type impacts the list of possible operations that you may use in the corresponding predicate. For example, you may use 'STARTS_WITH' or 'END_WITH', but you can't use 'GREATER_OR_EQUAL' for string values.The following filter value types and corresponding predicate operations are supported:    * 'STRING' - used to filter any 'String' or 'JSON' values. Operations: EQUAL, NOT_EQUAL, STARTS_WITH, ENDS_WITH, CONTAINS, NOT_CONTAINS;   * 'NUMERIC' - used for 'Long' and 'Double' values. Operations: EQUAL, NOT_EQUAL, GREATER, LESS, GREATER_OR_EQUAL, LESS_OR_EQUAL;   * 'BOOLEAN' - used for boolean values. Operations: EQUAL, NOT_EQUAL;  * 'DATE_TIME' - similar to numeric, transforms value to milliseconds since epoch. Operations: EQUAL, NOT_EQUAL, GREATER, LESS, GREATER_OR_EQUAL, LESS_OR_EQUAL;    ## Filter Predicate  Filter Predicate defines the logical expression to evaluate. The list of available operations depends on the filter value type, see above. Platform supports 4 predicate types: 'STRING', 'NUMERIC', 'BOOLEAN' and 'COMPLEX'. The last one allows to combine multiple operations over one filter key.  Simple predicate example to check 'value < 100':   ```json {   "operation": "LESS",   "value": {     "defaultValue": 100,     "dynamicValue": null   },   "type": "NUMERIC" } ```  Complex predicate example, to check 'value < 10 or value > 20':   ```json {   "type": "COMPLEX",   "operation": "OR",   "predicates": [     {       "operation": "LESS",       "value": {         "defaultValue": 10,         "dynamicValue": null       },       "type": "NUMERIC"     },     {       "operation": "GREATER",       "value": {         "defaultValue": 20,         "dynamicValue": null       },       "type": "NUMERIC"     }   ] } ```  More complex predicate example, to check 'value < 10 or (value > 50 && value < 60)':   ```json {   "type": "COMPLEX",   "operation": "OR",   "predicates": [     {       "operation": "LESS",       "value": {         "defaultValue": 10,         "dynamicValue": null       },       "type": "NUMERIC"     },     {       "type": "COMPLEX",       "operation": "AND",       "predicates": [         {           "operation": "GREATER",           "value": {             "defaultValue": 50,             "dynamicValue": null           },           "type": "NUMERIC"         },         {           "operation": "LESS",           "value": {             "defaultValue": 60,             "dynamicValue": null           },           "type": "NUMERIC"         }       ]     }   ] } ```   You may also want to replace hardcoded values (for example, temperature > 20) with the more dynamic expression (for example, temperature > 'value of the tenant attribute with key 'temperatureThreshold'). It is possible to use 'dynamicValue' to define attribute of the tenant, customer or user that is performing the API call. See example below:   ```json {   "operation": "GREATER",   "value": {     "defaultValue": 0,     "dynamicValue": {       "sourceType": "CURRENT_USER",       "sourceAttribute": "temperatureThreshold"     }   },   "type": "NUMERIC" } ```   Note that you may use 'CURRENT_USER', 'CURRENT_CUSTOMER' and 'CURRENT_TENANT' as a 'sourceType'. The 'defaultValue' is used when the attribute with such a name is not defined for the chosen source.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_entity_data_by_query(body=deserialize_param(body_json, 'EntityDataQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_entity_data_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_info_by_from(from_id_json: str, relation_type_group: Optional[str] = None) -> str:
    """
    Get List of Relation Infos (findInfoByFrom)  # noqa: E501

Returns list of relation info objects for the specified entity by the 'from' direction.   If the user has the authority of 'System Administrator', the server checks that the entity is owned by the sysadmin. If the user has the authority of 'Tenant Administrator', the server checks that the entity is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the entity is assigned to the same customer. Relation Info is an extension of the default Relation object that contains information about the 'from' and 'to' entity names.   # noqa: E501
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

def getName() -> str:
    """
    Return a string used for identification purposes only.

This method is deprecated, use the name attribute instead.
    """
    try:
        client = get_client()
        result = client.getName()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'getName'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_activation_link(user_id_json: str) -> str:
    """
    Get the activation link (getActivationLink)  # noqa: E501

Get the activation link for the user. The base url for activation link is configurable in the general settings of system administrator.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_activation_link(user_id=deserialize_param(user_id_json, 'UserId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_activation_link'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_activation_link_info(user_id_json: str) -> str:
    """
    Get the activation link (getActivationLink)  # noqa: E501

Get the activation link for the user. The base url for activation link is configurable in the general settings of system administrator.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_activation_link_info(user_id=deserialize_param(user_id_json, 'UserId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_activation_link_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_ai_model_by_id(ai_model_id_json: str) -> str:
    """
    Get AI model by ID (getAiModelById)  # noqa: E501

Fetches an AI model record by its `id`.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_ai_model_by_id(ai_model_id=deserialize_param(ai_model_id_json, 'AiModelId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_ai_model_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_ai_models(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get AI models (getAiModels)  # noqa: E501

Returns a page of AI models. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_ai_models(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_ai_models'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_application_redirect(user_agent: str) -> str:
    """
    getApplicationRedirect  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_application_redirect(user_agent=user_agent)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_application_redirect'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_auto_commit_settings() -> str:
    """
    Get auto commit settings (getAutoCommitSettings)  # noqa: E501

Get the auto commit settings object.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_auto_commit_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_auto_commit_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_available_delivery_methods() -> str:
    """
    Get available delivery methods (getAvailableDeliveryMethods)  # noqa: E501

Returns the list of delivery methods that are properly configured and are allowed to be used for sending notifications.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_available_delivery_methods()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_available_delivery_methods'."
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

def get_client_registration_templates() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_client_registration_templates()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_client_registration_templates'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_client_registration_templates1() -> str:
    """
    Get the list of all OAuth2 client registration templates (getClientRegistrationTemplates)  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501

Client registration template is OAuth2 provider configuration template with default settings for registering new OAuth2 clients  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_client_registration_templates1()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_client_registration_templates1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
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
            return "PERMISSION DENIED: You do not have permission to perform 'get_client_registration_templates_mail'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_component_descriptor_by_clazz(component_descriptor_clazz: str) -> str:
    """
    Get Component Descriptor (getComponentDescriptorByClazz)  # noqa: E501

Gets the Component Descriptor object using class name from the path parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_component_descriptor_by_clazz(component_descriptor_clazz=component_descriptor_clazz)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_component_descriptor_by_clazz'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_component_descriptors_by_type(component_type: str, rule_chain_type: Optional[str] = None) -> str:
    """
    Get Component Descriptors (getComponentDescriptorsByType)  # noqa: E501

Gets the Component Descriptors using rule node type and optional rule chain type request parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_component_descriptors_by_type(component_type=component_type, rule_chain_type=rule_chain_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_component_descriptors_by_type'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_component_descriptors_by_types(component_types: str, rule_chain_type: Optional[str] = None) -> str:
    """
    Get Component Descriptors (getComponentDescriptorsByTypes)  # noqa: E501

Gets the Component Descriptors using coma separated list of rule node types and optional rule chain type request parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_component_descriptors_by_types(component_types=component_types, rule_chain_type=rule_chain_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_component_descriptors_by_types'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_domain_info_by_id(domain_id_json: str) -> str:
    """
    Get Domain info by Id (getDomainInfoById)  # noqa: E501

  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_domain_info_by_id(domain_id=deserialize_param(domain_id_json, 'DomainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_domain_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_domain_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Domain infos (getDomainInfos)  # noqa: E501

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_domain_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_domain_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edge_by_id(edge_id_json: str) -> str:
    """
    Get Edge (getEdgeById)  # noqa: E501

Get the Edge object based on the provided Edge Id. If the user has the authority of 'Tenant Administrator', the server checks that the edge is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the edge is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_by_id(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edge_entity_views(edge_id_json: str, page: int, page_size: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    getEdgeEntityViews  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_entity_views(edge_id=deserialize_param(edge_id_json, 'EdgeId'), page=page, page_size=page_size, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_entity_views'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edge_events(edge_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    Get Edge Events (getEdgeEvents)  # noqa: E501

Returns a page of edge events for the requested edge. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_events(edge_id=deserialize_param(edge_id_json, 'EdgeId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_events'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edge_info_by_id(edge_id_json: str) -> str:
    """
    Get Edge Info (getEdgeInfoById)  # noqa: E501

Get the Edge Info object based on the provided Edge Id. If the user has the authority of 'Tenant Administrator', the server checks that the edge is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the edge is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_info_by_id(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edge_install_instructions(edge_id_json: str, method: str) -> str:
    """
    Get Edge Install Instructions (getEdgeInstallInstructions)  # noqa: E501

Get an install instructions for provided edge id.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_install_instructions(edge_id=deserialize_param(edge_id_json, 'EdgeId'), method=method)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_install_instructions'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edge_types() -> str:
    """
    Get Edge Types (getEdgeTypes)  # noqa: E501

Returns a set of unique edge types based on edges that are either owned by the tenant or assigned to the customer which user is performing the request.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_types()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_types'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edge_upgrade_instructions(edge_version: str, method: str) -> str:
    """
    Get Edge Upgrade Instructions (getEdgeUpgradeInstructions)  # noqa: E501

Get an upgrade instructions for provided edge version.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_upgrade_instructions(edge_version=edge_version, method=method)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_upgrade_instructions'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edges(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Edges (getEdges)  # noqa: E501

Returns a page of edges owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edges(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edges'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edges_by_ids(edge_ids_json: str) -> str:
    """
    Get Edges By Ids (getEdgesByIds)  # noqa: E501

Requested edges must be owned by tenant or assigned to customer which user is performing the request.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edges_by_ids(edge_ids=json.loads(edge_ids_json) if edge_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edges_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edqs_state() -> str:
    """
    getEdqsState  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edqs_state()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edqs_state'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_entity_data_info(version_id: str, entity_id_json: str) -> str:
    """
    Get entity data info (getEntityDataInfo)  # noqa: E501

Retrieves short info about the remote entity by external id at a concrete version.  Returned entity data info contains following properties: `hasRelations` (whether stored entity data contains relations), `hasAttributes` (contains attributes) and `hasCredentials` (whether stored device data has credentials).  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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

def get_entity_view_by_id(entity_view_id_json: str) -> str:
    """
    Get entity view (getEntityViewById)  # noqa: E501

Fetch the EntityView object based on the provided entity view id. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. See the 'Model' tab for more details.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_entity_view_by_id(entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_entity_view_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_entity_view_info_by_id(entity_view_id_json: str) -> str:
    """
    Get Entity View info (getEntityViewInfoById)  # noqa: E501

Fetch the Entity View info object based on the provided Entity View Id. Entity Views Info extends the Entity View with customer title and 'is public' flag. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. See the 'Model' tab for more details.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_entity_view_info_by_id(entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_entity_view_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_entity_view_types() -> str:
    """
    Get Entity View Types (getEntityViewTypes)  # noqa: E501

Returns a set of unique entity view types based on entity views that are either owned by the tenant or assigned to the customer which user is performing the request.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_entity_view_types()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_entity_view_types'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_events_get(entity_id_json: str, tenant_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    Get Events (Deprecated)  # noqa: E501

Returns a page of events for specified entity. Deprecated and will be removed in next minor release. The call was deprecated to improve the performance of the system. Current implementation will return 'Lifecycle' events only. Use 'Get events by type' or 'Get events by filter' instead. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_events_get(entity_id=deserialize_param(entity_id_json, 'EntityId'), tenant_id=deserialize_param(tenant_id_json, 'TenantId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_events_get'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_events_post(tenant_id_json: str, page_size: int, page: int, entity_id_json: str, body_json: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    Get Events by event filter (getEvents)  # noqa: E501

Returns a page of events for the chosen entity by specifying the event filter. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # Event Filter Definition  5 different eventFilter objects could be set for different event types. The eventType field is required. Others are optional. If some of them are set, the filtering will be applied according to them. See the examples below for all the fields used for each event type filtering.   Note,   * 'server' - string value representing the server name, identifier or ip address where the platform is running;  * 'errorStr' - the case insensitive 'contains' filter based on error message.  ## Error Event Filter  ```json {    "eventType":"ERROR",    "server":"ip-172-31-24-152",    "method":"onClusterEventMsg",    "errorStr":"Error Message" } ```   * 'method' - string value representing the method name when the error happened.  ## Lifecycle Event Filter  ```json {    "eventType":"LC_EVENT",    "server":"ip-172-31-24-152",    "event":"STARTED",    "status":"Success",    "errorStr":"Error Message" } ```   * 'event' - string value representing the lifecycle event type;  * 'status' - string value representing status of the lifecycle event.  ## Statistics Event Filter  ```json {    "eventType":"STATS",    "server":"ip-172-31-24-152",    "messagesProcessed":10,    "errorsOccurred":5 } ```   * 'messagesProcessed' - the minimum number of successfully processed messages;  * 'errorsOccurred' - the minimum number of errors occurred during messages processing.  ## Debug Rule Node Event Filter  ```json {    "eventType":"DEBUG_RULE_NODE",    "msgDirectionType":"IN",    "server":"ip-172-31-24-152",    "dataSearch":"humidity",    "metadataSearch":"deviceName",    "entityName":"DEVICE",    "relationType":"Success",    "entityId":"de9d54a0-2b7a-11ec-a3cc-23386423d98f",    "msgType":"POST_TELEMETRY_REQUEST",    "isError":"false",    "errorStr":"Error Message" } ```  ## Debug Rule Chain Event Filter  ```json {    "eventType":"DEBUG_RULE_CHAIN",    "msgDirectionType":"IN",    "server":"ip-172-31-24-152",    "dataSearch":"humidity",    "metadataSearch":"deviceName",    "entityName":"DEVICE",    "relationType":"Success",    "entityId":"de9d54a0-2b7a-11ec-a3cc-23386423d98f",    "msgType":"POST_TELEMETRY_REQUEST",    "isError":"false",    "errorStr":"Error Message" } ```   * 'msgDirectionType' - string value representing msg direction type (incoming to entity or outcoming from entity);  * 'dataSearch' - the case insensitive 'contains' filter based on data (key and value) for the message;  * 'metadataSearch' - the case insensitive 'contains' filter based on metadata (key and value) for the message;  * 'entityName' - string value representing the entity type;  * 'relationType' - string value representing the type of message routing;  * 'entityId' - string value representing the entity id in the event body (originator of the message);  * 'msgType' - string value representing the message type;  * 'isError' - boolean value to filter the errors.    # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_events_post(tenant_id=deserialize_param(tenant_id_json, 'TenantId'), page_size=page_size, page=page, entity_id=deserialize_param(entity_id_json, 'EntityId'), body=deserialize_param(body_json, 'EventFilter'), text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_events_post'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_events_v1_get1(entity_id_json: str, event_type: str, tenant_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    Get Events by type (getEvents)  # noqa: E501

Returns a page of events for specified entity by specifying event type. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_events_v1_get1(entity_id=deserialize_param(entity_id_json, 'EntityId'), event_type=event_type, tenant_id=deserialize_param(tenant_id_json, 'TenantId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_events_v1_get1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_features_info() -> str:
    """
    Get features info (getFeaturesInfo)  # noqa: E501

Get information about enabled/disabled features.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_features_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_features_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_firmware(device_token: str, title: str, version: str, size: Optional[int] = None, chunk: Optional[int] = None) -> str:
    """
    Get Device Firmware (getFirmware)  # noqa: E501

Downloads the current firmware package.When the platform initiates firmware update, it informs the device by updating the 'fw_title', 'fw_version', 'fw_checksum' and 'fw_checksum_algorithm' shared attributes.The 'fw_title' and 'fw_version' parameters must be supplied in this request to double-check that the firmware that device is downloading matches the firmware it expects to download. This is important, since the administrator may change the firmware assignment while device is downloading the firmware.   Optional 'chunk' and 'size' parameters may be used to download the firmware in chunks. For example, device may request first 16 KB of firmware using 'chunk'=0 and 'size'=16384. Next 16KB using 'chunk'=1 and 'size'=16384. The last chunk should have less bytes then requested using 'size' parameter.   The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_firmware(device_token=device_token, title=title, version=version, size=size, chunk=chunk)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_firmware'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
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
            return "PERMISSION DENIED: You do not have permission to perform 'get_help_base_url'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_image_info(_type: str, key: str) -> str:
    """
    getImageInfo  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_image_info(_type=_type, key=key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_image_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_images(page_size: int, page: int, text_search: Optional[str] = None, include_system_images: Optional[bool] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    getImages  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_images(page_size=page_size, page=page, text_search=text_search, include_system_images=include_system_images, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_images'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_job_by_id(id_json: str) -> str:
    """
    getJobById  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_job_by_id(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_job_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_jobs(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    getJobs  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_jobs(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_jobs'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_jwt_setting() -> str:
    """
    Get the JWT Settings object (getJwtSettings)  # noqa: E501

Get the JWT Settings object that contains JWT token policy, etc.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_jwt_setting()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_jwt_setting'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_latest_calculated_field_debug_event(calculated_field_id_json: str) -> str:
    """
    Get latest calculated field debug event (getLatestCalculatedFieldDebugEvent)  # noqa: E501

Gets latest calculated field debug event for specified calculated field id. Referencing non-existing calculated field id will cause an error.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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

def get_latest_rule_node_debug_input(rule_node_id_json: str) -> str:
    """
    Get latest input message (getLatestRuleNodeDebugInput)  # noqa: E501

Gets the input message from the debug events for specified Rule Chain Id. Referencing non-existing rule chain Id will cause an error.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_latest_rule_node_debug_input(rule_node_id=deserialize_param(rule_node_id_json, 'RuleNodeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_latest_rule_node_debug_input'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_login_mobile_info(pkg_name: str, platform: str) -> str:
    """
    Get mobile app login info (getLoginMobileInfo)  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_login_mobile_info(pkg_name=pkg_name, platform=platform)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_login_mobile_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_login_processing_url() -> str:
    """
    Get OAuth2 log in processing URL (getLoginProcessingUrl)  # noqa: E501

Returns the URL enclosed in double quotes. After successful authentication with OAuth2 provider, it makes a redirect to this path so that the platform can do further log in processing. This URL may be configured as 'security.oauth2.loginProcessingUrl' property in yml configuration file, or as 'SECURITY_OAUTH2_LOGIN_PROCESSING_URL' env variable. By default it is '/login/oauth2/code/'  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_login_processing_url()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_login_processing_url'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_lwm2m_bootstrap_security_info(is_bootstrap_server: bool) -> str:
    """
    Get Lwm2m Bootstrap SecurityInfo (getLwm2mBootstrapSecurityInfo)  # noqa: E501

Get the Lwm2m Bootstrap SecurityInfo object (of the current server) based on the provided isBootstrapServer parameter. If isBootstrapServer == true, get the parameters of the current Bootstrap Server. If isBootstrapServer == false, get the parameters of the current Lwm2m Server. Used for client settings when starting the client in Bootstrap mode.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_lwm2m_bootstrap_security_info(is_bootstrap_server=is_bootstrap_server)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_lwm2m_bootstrap_security_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_lwm2m_list_objects(sort_order: str, sort_property: str, object_ids_json: str) -> str:
    """
    Get LwM2M Objects (getLwm2mListObjects)  # noqa: E501

Returns a page of LwM2M objects parsed from Resources with type 'LWM2M_MODEL' owned by tenant or sysadmin. You can specify parameters to filter the results. LwM2M Object is a object that includes information about the LwM2M model which can be used in transport configuration for the LwM2M device profile.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_lwm2m_list_objects(sort_order=sort_order, sort_property=sort_property, object_ids=json.loads(object_ids_json) if object_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_lwm2m_list_objects'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_lwm2m_list_objects_page(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get LwM2M Objects (getLwm2mListObjectsPage)  # noqa: E501

Returns a page of LwM2M objects parsed from Resources with type 'LWM2M_MODEL' owned by tenant or sysadmin. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. LwM2M Object is a object that includes information about the LwM2M model which can be used in transport configuration for the LwM2M device profile.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_lwm2m_list_objects_page(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_lwm2m_list_objects_page'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mail_processing_url() -> str:
    """
    Get OAuth2 log in processing URL (getMailProcessingUrl)  # noqa: E501

Returns the URL enclosed in double quotes. After successful authentication with OAuth2 provider and user consent for requested scope, it makes a redirect to this path so that the platform can do further log in processing and generating access tokens.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mail_processing_url()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mail_processing_url'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_max_datapoints_limit() -> str:
    """
    Get max data points limit (getMaxDatapointsLimit)  # noqa: E501

Get the maximum number of data points that dashboard may request from the server per in a single subscription command. This value impacts the time window behavior. It impacts 'Max values' parameter in case user selects 'None' as 'Data aggregation function'. It also impacts the 'Grouping interval' in case of any other 'Data aggregation function' is selected. The actual value of the limit is configurable in the system configuration file.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_max_datapoints_limit()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_max_datapoints_limit'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_app_bundle_info_by_id(mobile_app_bundle_id_json: str) -> str:
    """
    Get mobile app bundle info by id (getMobileAppBundleInfoById)  # noqa: E501

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_app_bundle_info_by_id(mobile_app_bundle_id=deserialize_param(mobile_app_bundle_id_json, 'MobileAppBundleId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_app_bundle_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_app_by_id(mobile_app_id_json: str) -> str:
    """
    Get mobile info by id (getMobileAppInfoById)  # noqa: E501

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_app_by_id(mobile_app_id=deserialize_param(mobile_app_id_json, 'MobileAppId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_app_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_app_deep_link() -> str:
    """
    Get the deep link to the associated mobile application (getMobileAppDeepLink)  # noqa: E501

Fetch the url that takes user to linked mobile application   Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_app_deep_link()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_app_deep_link'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_app_info_by_id(mobile_app_id_json: str) -> str:
    """
    Get mobile info by id (getMobileAppInfoById)  # noqa: E501

  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_app_info_by_id(mobile_app_id=deserialize_param(mobile_app_id_json, 'MobileAppId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_app_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_app_settings() -> str:
    """
    Get Mobile application settings (getMobileAppSettings)  # noqa: E501

The response payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_app_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_app_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_session(x_mobile_token: str) -> str:
    """
    getMobileSession  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_session(x_mobile_token=x_mobile_token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_session'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_request_by_id(id: str) -> str:
    """
    Get notification request by id (getNotificationRequestById)  # noqa: E501

Fetches notification request info by request id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_request_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_request_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_request_preview(body_json: str, recipients_preview_size: Optional[int] = None) -> str:
    """
    Get notification request preview (getNotificationRequestPreview)  # noqa: E501

Returns preview for notification request.  `processedTemplates` shows how the notifications for each delivery method will look like for the first recipient of the corresponding notification target.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_request_preview(body=deserialize_param(body_json, 'NotificationRequest'), recipients_preview_size=recipients_preview_size)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_request_preview'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_requests(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get notification requests (getNotificationRequests)  # noqa: E501

Returns the page of notification requests submitted by users of this tenant or sysadmins.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_requests(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_requests'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_rule_by_id(id: str) -> str:
    """
    Get notification rule by id (getNotificationRuleById)  # noqa: E501

Fetches notification rule info by rule's id. In addition to regular notification rule fields, there are `templateName` and `deliveryMethods` in the response.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_rule_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_rule_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_rules(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get notification rules (getNotificationRules)  # noqa: E501

Returns the page of notification rules.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_rules(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_rules'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_settings() -> str:
    """
    Get notification settings (getNotificationSettings)  # noqa: E501

Retrieves notification settings for this tenant or sysadmin.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_target_by_id(id: str) -> str:
    """
    Get notification target by id (getNotificationTargetById)  # noqa: E501

Fetches notification target by id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_target_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_target_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_targets(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get notification targets (getNotificationTargets)  # noqa: E501

Returns the page of notification targets owned by sysadmin or tenant.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_targets(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_targets'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_targets_by_ids(ids_json: str) -> str:
    """
    Get notification targets by ids (getNotificationTargetsByIds)  # noqa: E501

Returns the list of notification targets found by provided ids.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_targets_by_ids(ids=json.loads(ids_json) if ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_targets_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_targets_by_supported_notification_type(notification_type: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get notification targets by supported notification type (getNotificationTargetsBySupportedNotificationType)  # noqa: E501

Returns the page of notification targets filtered by notification type that they can be used for.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_targets_by_supported_notification_type(notification_type=notification_type, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_targets_by_supported_notification_type'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_template_by_id(id: str) -> str:
    """
    Get notification template by id (getNotificationTemplateById)  # noqa: E501

Fetches notification template by id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_template_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_template_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_templates(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get notification templates (getNotificationTemplates)  # noqa: E501

Returns the page of notification templates owned by sysadmin or tenant.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notification_templates(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_templates'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notifications(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, delivery_method: Optional[str] = None) -> str:
    """
    Get notifications (getNotifications)  # noqa: E501

Returns the page of notifications for current user.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for any authorized user.   **WebSocket API**:  There are 2 types of subscriptions: one for unread notifications count, another for unread notifications themselves.  The URI for opening WS session for notifications: `/api/ws/plugins/notifications`.  Subscription command for unread notifications count: ``` {   "unreadCountSubCmd": {     "cmdId": 1234   } } ``` To subscribe for latest unread notifications: ``` {   "unreadSubCmd": {     "cmdId": 1234,     "limit": 10   } } ``` To unsubscribe from any subscription: ``` {   "unsubCmd": {     "cmdId": 1234   } } ``` To mark certain notifications as read, use following command: ``` {   "markAsReadCmd": {     "cmdId": 1234,     "notifications": [       "6f860330-7fc2-11ed-b855-7dd3b7d2faa9",       "5b6dfee0-8d0d-11ed-b61f-35a57b03dade"     ]   } }  ``` To mark all notifications as read: ``` {   "markAllAsReadCmd": {     "cmdId": 1234   } } ```   Update structure for unread **notifications count subscription**: ``` {   "cmdId": 1234,   "totalUnreadCount": 55 } ``` For **notifications subscription**: - full update of latest unread notifications: ``` {   "cmdId": 1234,   "notifications": [     {       "id": {         "entityType": "NOTIFICATION",         "id": "6f860330-7fc2-11ed-b855-7dd3b7d2faa9"       },       ...     }   ],   "totalUnreadCount": 1 } ``` - when new notification arrives or shown notification is updated: ``` {   "cmdId": 1234,   "update": {     "id": {       "entityType": "NOTIFICATION",       "id": "6f860330-7fc2-11ed-b855-7dd3b7d2faa9"     },     # updated notification info, text, subject etc.     ...   },   "totalUnreadCount": 2 } ``` - when unread notifications count changes: ``` {   "cmdId": 1234,   "totalUnreadCount": 5 } ```  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_notifications(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, delivery_method=delivery_method)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notifications'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_persisted_rpc(rpc_id_json: str) -> str:
    """
    Get persistent RPC request  # noqa: E501

Get information about the status of the RPC call.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_persisted_rpc(rpc_id=deserialize_param(rpc_id_json, 'RpcId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_persisted_rpc'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_qr_code_settings() -> str:
    """
    Get Mobile application settings (getMobileAppSettings)  # noqa: E501

The response payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_qr_code_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_qr_code_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_queue_by_id(queue_id_json: str) -> str:
    """
    Get Queue (getQueueById)  # noqa: E501

Fetch the Queue object based on the provided Queue Id.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_queue_by_id(queue_id=deserialize_param(queue_id_json, 'QueueId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_queue_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_queue_by_name(queue_name: str) -> str:
    """
    Get Queue (getQueueByName)  # noqa: E501

Fetch the Queue object based on the provided Queue name.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_queue_by_name(queue_name=queue_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_queue_by_name'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_queue_stats_by_id(queue_stats_id_json: str) -> str:
    """
    Get Queue stats entity by id (getQueueStatsById)  # noqa: E501

Fetch the Queue stats object based on the provided Queue stats id.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_queue_stats_by_id(queue_stats_id=deserialize_param(queue_stats_id_json, 'QueueId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_queue_stats_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_queue_stats_by_ids(queue_stats_ids_json: str) -> str:
    """
    Get QueueStats By Ids (getQueueStatsByIds)  # noqa: E501

Fetch the Queue stats objects based on the provided ids.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_queue_stats_by_ids(queue_stats_ids=json.loads(queue_stats_ids_json) if queue_stats_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_queue_stats_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_recipients_for_notification_target_config(page_size: int, page: int) -> str:
    """
    Get recipients for notification target config (getRecipientsForNotificationTargetConfig)  # noqa: E501

Returns the page of recipients for such notification target configuration.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_recipients_for_notification_target_config(page_size=page_size, page=page)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_recipients_for_notification_target_config'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_repository_settings() -> str:
    """
    Get repository settings (getRepositorySettings)  # noqa: E501

Get the repository settings object.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_repository_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_repository_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_repository_settings_info() -> str:
    """
    getRepositorySettingsInfo  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_repository_settings_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_repository_settings_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_resource_by_id(resource_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_resource_by_id(resource_id=deserialize_param(resource_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_resource_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_resource_info_by_id(resource_id_json: str) -> str:
    """
    Get Resource Info (getResourceInfoById)  # noqa: E501

Fetch the Resource Info object based on the provided Resource Id. Resource Info is a lightweight object that includes main information about the Resource excluding the heavyweight data.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_resource_info_by_id(resource_id=deserialize_param(resource_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_resource_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_resources(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Resource Infos (getResources)  # noqa: E501

Returns a page of Resource Info objects owned by tenant or sysadmin. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. Resource Info is a lightweight object that includes main information about the Resource excluding the heavyweight data.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_resources(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_resources'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_security_settings() -> str:
    """
    Get the Security Settings object  # noqa: E501

Get the Security Settings object that contains password policy, etc.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_security_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_security_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_server_time() -> str:
    """
    Get server time (getServerTime)  # noqa: E501

Get the server time (milliseconds since January 1, 1970 UTC). Used to adjust view of the dashboards according to the difference between browser and server time.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_server_time()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_server_time'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_software(device_token: str, title: str, version: str, size: Optional[int] = None, chunk: Optional[int] = None) -> str:
    """
    Get Device Software (getSoftware)  # noqa: E501

Downloads the current software package.When the platform initiates software update, it informs the device by updating the 'sw_title', 'sw_version', 'sw_checksum' and 'sw_checksum_algorithm' shared attributes.The 'sw_title' and 'sw_version' parameters must be supplied in this request to double-check that the software that device is downloading matches the software it expects to download. This is important, since the administrator may change the software assignment while device is downloading the software.   Optional 'chunk' and 'size' parameters may be used to download the software in chunks. For example, device may request first 16 KB of software using 'chunk'=0 and 'size'=16384. Next 16KB using 'chunk'=1 and 'size'=16384. The last chunk should have less bytes then requested using 'size' parameter.   The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_software(device_token=device_token, title=title, version=version, size=size, chunk=chunk)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_software'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_system_info() -> str:
    """
    Get system info (getSystemInfo)  # noqa: E501

Get main information about system.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_system_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_system_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_trendz_settings() -> str:
    """
    Get Trendz Settings (getTrendzSettings)  # noqa: E501

Retrieves Trendz settings for this tenant.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_trendz_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_trendz_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_unread_notifications_count(delivery_method: Optional[str] = None) -> str:
    """
    Get unread notifications count (getUnreadNotificationsCount)  # noqa: E501

Returns unread notifications count for chosen delivery method.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_unread_notifications_count(delivery_method=delivery_method)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_unread_notifications_count'."
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

def handle_rule_engine_request(body_json: str, entity_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.handle_rule_engine_request(body=deserialize_param(body_json, '_empty'), entity_id=deserialize_param(entity_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'handle_rule_engine_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_rule_engine_request1(body_json: str, entity_id_json: str, timeout: int) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.handle_rule_engine_request1(body=deserialize_param(body_json, '_empty'), entity_id=deserialize_param(entity_id_json, 'EntityId'), timeout=timeout)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'handle_rule_engine_request1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_rule_engine_request2(body_json: str, entity_id_json: str, timeout: int, queue_name: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.handle_rule_engine_request2(body=deserialize_param(body_json, '_empty'), entity_id=deserialize_param(entity_id_json, 'EntityId'), timeout=timeout, queue_name=queue_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'handle_rule_engine_request2'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_rule_engine_request3(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.handle_rule_engine_request3(body=deserialize_param(body_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'handle_rule_engine_request3'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def import_image(body_json: str) -> str:
    """
    importImage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.import_image(body=deserialize_param(body_json, 'ImageExportData'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'import_image'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def isDaemon() -> str:
    """
    Return whether this thread is a daemon.

This method is deprecated, use the daemon attribute instead.
    """
    try:
        client = get_client()
        result = client.isDaemon()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'isDaemon'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def is_alive() -> str:
    """
    Return whether the thread is alive.

This method returns True just before the run() method starts until just
after the run() method terminates. See also the module function
enumerate().
    """
    try:
        client = get_client()
        result = client.is_alive()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'is_alive'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def is_edge_upgrade_available(edge_id_json: str) -> str:
    """
    Is edge upgrade enabled (isEdgeUpgradeAvailable)  # noqa: E501

Returns 'true' if upgrade available for connected edge, 'false' - otherwise.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.is_edge_upgrade_available(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'is_edge_upgrade_available'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def is_edges_support_enabled() -> str:
    """
    Is edges support enabled (isEdgesSupportEnabled)  # noqa: E501

Returns 'true' if edges support enabled on server, 'false' - otherwise.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.is_edges_support_enabled()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'is_edges_support_enabled'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def is_edqs_api_enabled() -> str:
    """
    isEdqsApiEnabled  # noqa: E501
    """
    try:
        client = get_client()
        result = client.is_edqs_api_enabled()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'is_edqs_api_enabled'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def is_tbel_enabled() -> str:
    """
    Is TBEL script executor enabled  # noqa: E501

Returns 'True' if the TBEL script execution is enabled  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.is_tbel_enabled()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'is_tbel_enabled'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def join(timeout_json: str) -> str:
    """
    Wait until the thread terminates.

This blocks the calling thread until the thread whose join() method is
called terminates -- either normally or through an unhandled exception
or until the optional timeout occurs.

When the timeout argument is present and not None, it should be a
floating-point number specifying a timeout for the operation in seconds
(or fractions thereof). As join() always returns None, you must call
is_alive() after join() to decide whether a timeout happened -- if the
thread is still alive, the join() call timed out.

When the timeout argument is not present or None, the operation will
block until the thread terminates.

A thread can be join()ed many times.

join() raises a RuntimeError if an attempt is made to join the current
thread as that would cause a deadlock. It is also an error to join() a
thread before it has been started and attempts to do so raises the same
exception.
    """
    try:
        client = get_client()
        result = client.join(timeout=deserialize_param(timeout_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'join'."
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

def list_slack_conversations(type: str, token: Optional[str] = None) -> str:
    """
    List Slack conversations (listSlackConversations)  # noqa: E501

List available Slack conversations by type.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.list_slack_conversations(type=type, token=token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'list_slack_conversations'."
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

def load_entities_version(body_json: str) -> str:
    """
    Load entities version (loadEntitiesVersion)  # noqa: E501

Loads specific version of remote entities (or single entity) by request. Supported entity types: CUSTOMER, ASSET, RULE_CHAIN, DASHBOARD, DEVICE_PROFILE, DEVICE, ENTITY_VIEW, WIDGETS_BUNDLE.  There are multiple types of request. Each of them requires branch name (`branch`) and version id (`versionId`). Request of type `SINGLE_ENTITY` is needed to restore a concrete version of a specific entity. It contains id of a remote entity (`externalEntityId`) and additional configuration (`config`): - `loadRelations` - to update relations list (in case `saveRelations` option was enabled during version creation); - `loadAttributes` - to load entity attributes (if `saveAttributes` config option was enabled); - `loadCredentials` - to update device credentials (if `saveCredentials` option was enabled during version creation).  An example of such request: ```json {   "type": "SINGLE_ENTITY",      "branch": "dev",   "versionId": "b3c28d722d328324c7c15b0b30047b0c40011cf7",      "externalEntityId": {     "entityType": "DEVICE",     "id": "b7944123-d4f4-11ec-847b-0f432358ab48"   },   "config": {     "loadRelations": false,     "loadAttributes": true,     "loadCredentials": true   } } ```  Another request type (`ENTITY_TYPE`) is needed to load specific version of the whole entity types. It contains a structure with entity types to load and configs for each entity type (`entityTypes`). For each specified entity type, the method will load all remote entities of this type that are present at the version. A config for each entity type contains the same options as in `SINGLE_ENTITY` request type, and additionally contains following options: - `removeOtherEntities` - to remove local entities that are not present on the remote - basically to    overwrite local entity type with the remote one; - `findExistingEntityByName` - when you are loading some remote entities that are not yet present at this tenant,    try to find existing entity by name and update it rather than create new.  Here is an example of the request to completely restore version of the whole device entity type: ```json {   "type": "ENTITY_TYPE",    "branch": "dev",   "versionId": "b3c28d722d328324c7c15b0b30047b0c40011cf7",    "entityTypes": {     "DEVICE": {       "removeOtherEntities": true,       "findExistingEntityByName": false,       "loadRelations": true,       "loadAttributes": true,       "loadCredentials": true     }   } } ```  The response will contain generated request UUID that is to be used to check the status of operation via `getVersionLoadRequestStatus`.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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

def mark_all_notifications_as_read() -> str:
    """
    Mark all notifications as read (markAllNotificationsAsRead)  # noqa: E501

Marks all unread notifications as read.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.mark_all_notifications_as_read()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'mark_all_notifications_as_read'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def mark_notification_as_read(id: str) -> str:
    """
    Mark notification as read (markNotificationAsRead)  # noqa: E501

Marks notification as read by its id.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.mark_notification_as_read(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'mark_notification_as_read'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def post_rpc_request(device_token: str, body_json: str = None) -> str:
    """
    Send the RPC command (postRpcRequest)  # noqa: E501

Send the RPC request to server. The request payload is a JSON document that contains 'method' and 'params'. For example:  ```json {"method": "sumOnServer", "params":{"a":2, "b":2}} ```  The response contains arbitrary JSON with the RPC reply. For example:   ```json {"result": 4} ```  The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.post_rpc_request(device_token=device_token, body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'post_rpc_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def process_edges_bulk_import(body_json: str) -> str:
    """
    Import the bulk of edges (processEdgesBulkImport)  # noqa: E501

There's an ability to import the bulk of edges using the only .csv file.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.process_edges_bulk_import(body=deserialize_param(body_json, 'BulkImportRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'process_edges_bulk_import'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def process_system_edqs_request(body_json: str) -> str:
    """
    processSystemEdqsRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.process_system_edqs_request(body=deserialize_param(body_json, 'ToCoreEdqsRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'process_system_edqs_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
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
            return "PERMISSION DENIED: You do not have permission to perform 'refresh'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def remove_mobile_session(x_mobile_token: str) -> str:
    """
    removeMobileSession  # noqa: E501
    """
    try:
        client = get_client()
        result = client.remove_mobile_session(x_mobile_token=x_mobile_token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'remove_mobile_session'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def reply_to_command(device_token: str, request_id: int, body: Optional[str] = None) -> str:
    """
    Reply to RPC commands (replyToCommand)  # noqa: E501

Replies to server originated RPC command identified by 'requestId' parameter. The response is arbitrary JSON.  The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.reply_to_command(device_token=device_token, request_id=request_id, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'reply_to_command'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def repository_settings_exists() -> str:
    """
    Check repository settings exists (repositorySettingsExists)  # noqa: E501

Check whether the repository settings exists.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.repository_settings_exists()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'repository_settings_exists'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def reprocess_job(id_json: str) -> str:
    """
    reprocessJob  # noqa: E501
    """
    try:
        client = get_client()
        result = client.reprocess_job(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'reprocess_job'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def request_reset_password_by_email(body_json: str) -> str:
    """
    Request reset password email (requestResetPasswordByEmail)  # noqa: E501

Request to send the reset password email if the user with specified email address is present in the database. Always return '200 OK' status for security purposes.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.request_reset_password_by_email(body=deserialize_param(body_json, 'ResetPasswordEmailRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'request_reset_password_by_email'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def reset_password(body_json: str) -> str:
    """
    Reset password (resetPassword)  # noqa: E501

Checks the password reset token and updates the password. If token is valid, returns the object that contains [JWT](https://jwt.io/) access and refresh tokens. If token is not valid, returns '404 Bad Request'.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.reset_password(body=deserialize_param(body_json, 'ResetPasswordRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'reset_password'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
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
            return "PERMISSION DENIED: You do not have permission to perform 'run'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_ai_model(body_json: str) -> str:
    """
    Create or update AI model (saveAiModel)  # noqa: E501

Creates or updates an AI model record.  • **Create:** Omit the `id` to create a new record. The platform assigns a UUID to the new record and returns it in the `id` field of the response.  • **Update:** Include an existing `id` to modify that record. If no matching record exists, the API responds with **404 Not Found**.  Tenant ID for the AI model will be taken from the authenticated user making the request, regardless of any value provided in the request body.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_ai_model(body=deserialize_param(body_json, 'AiModel'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_ai_model'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_auto_commit_settings(body_json: str = None) -> str:
    """
    Creates or Updates the auto commit settings (saveAutoCommitSettings)  # noqa: E501

Creates or Updates the auto commit settings object.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_auto_commit_settings(body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_auto_commit_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_calculated_field(body_json: str) -> str:
    """
    Create Or Update Calculated Field (saveCalculatedField)  # noqa: E501

Creates or Updates the Calculated Field. When creating calculated field, platform generates Calculated Field Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Calculated Field Id will be present in the response. Specify existing Calculated Field Id to update the calculated field. Referencing non-existing Calculated Field Id will cause 'Not Found' error. Remove 'id', 'tenantId' from the request body example (below) to create new Calculated Field entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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

def save_client_registration_template(body_json: str) -> str:
    """
    Create or update OAuth2 client registration template (saveClientRegistrationTemplate)  Available for users with 'SYS_ADMIN' authority.  # noqa: E501

Client registration template is OAuth2 provider configuration template with default settings for registering new OAuth2 clients  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_client_registration_template(body=deserialize_param(body_json, 'OAuth2ClientRegistrationTemplate'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_client_registration_template'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_domain(body_json: str, oauth2_client_ids: Optional[str] = None) -> str:
    """
    Save or Update Domain (saveDomain)  # noqa: E501

Create or update the Domain. When creating domain, platform generates Domain Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Domain Id will be present in the response. Specify existing Domain Id to update the domain. Referencing non-existing Domain Id will cause 'Not Found' error.  Domain name is unique for entire platform setup.    Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_domain(body=deserialize_param(body_json, 'Domain'), oauth2_client_ids=oauth2_client_ids)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_domain'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_edge(body_json: str) -> str:
    """
    Create Or Update Edge (saveEdge)  # noqa: E501

Create or update the Edge. When creating edge, platform generates Edge Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created edge id will be present in the response. Specify existing Edge id to update the edge. Referencing non-existing Edge Id will cause 'Not Found' error.  Edge name is unique in the scope of tenant. Use unique identifiers like MAC or IMEI for the edge names and non-unique 'label' field for user-friendly visualization purposes.Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Edge entity.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_edge(body=deserialize_param(body_json, 'Edge'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_entities_version(body_json: str) -> str:
    """
    Save entities version (saveEntitiesVersion)  # noqa: E501

Creates a new version of entities (or a single entity) by request. Supported entity types: CUSTOMER, ASSET, RULE_CHAIN, DASHBOARD, DEVICE_PROFILE, DEVICE, ENTITY_VIEW, WIDGETS_BUNDLE.  There are two available types of request: `SINGLE_ENTITY` and `COMPLEX`. Each of them contains version name (`versionName`) and name of a branch (`branch`) to create version (commit) in. If specified branch does not exists in a remote repo, then new empty branch will be created. Request of the `SINGLE_ENTITY` type has id of an entity (`entityId`) and additional configuration (`config`) which has following options:  - `saveRelations` - whether to add inbound and outbound relations of type COMMON to created entity version; - `saveAttributes` - to save attributes of server scope (and also shared scope for devices); - `saveCredentials` - when saving a version of a device, to add its credentials to the version.  An example of a `SINGLE_ENTITY` version create request: ```json {   "type": "SINGLE_ENTITY",    "versionName": "Version 1.0",   "branch": "dev",    "entityId": {     "entityType": "DEVICE",     "id": "b79448e0-d4f4-11ec-847b-0f432358ab48"   },   "config": {     "saveRelations": true,     "saveAttributes": true,     "saveCredentials": false   } } ```  Second request type (`COMPLEX`), additionally to `branch` and `versionName`, contains following properties: - `entityTypes` - a structure with entity types to export and configuration for each entity type;    this configuration has all the options available for `SINGLE_ENTITY` and additionally has these ones:       - `allEntities` and `entityIds` - if you want to save the version of all entities of the entity type         then set `allEntities` param to true, otherwise set it to false and specify the list of specific entities (`entityIds`);      - `syncStrategy` - synchronization strategy to use for this entity type: when set to `OVERWRITE`         then the list of remote entities of this type will be overwritten by newly added entities. If set to         `MERGE` - existing remote entities of this entity type will not be removed, new entities will just         be added on top (or existing remote entities will be updated). - `syncStrategy` - default synchronization strategy to use when it is not specified for an entity type.  Example for this type of request: ```json {   "type": "COMPLEX",    "versionName": "Devices and profiles: release 2",   "branch": "master",    "syncStrategy": "OVERWRITE",   "entityTypes": {     "DEVICE": {       "syncStrategy": null,       "allEntities": true,       "saveRelations": true,       "saveAttributes": true,       "saveCredentials": true     },     "DEVICE_PROFILE": {       "syncStrategy": "MERGE",       "allEntities": false,       "entityIds": [         "b79448e0-d4f4-11ec-847b-0f432358ab48"       ],       "saveRelations": true     }   } } ```  Response wil contain generated request UUID, that can be then used to retrieve status of operation via `getVersionCreateRequestStatus`.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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

def save_entity_view(body_json: str) -> str:
    """
    Save or update entity view (saveEntityView)  # noqa: E501

Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. See the 'Model' tab for more details.Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Entity View entity.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_entity_view(body=deserialize_param(body_json, 'EntityView'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_entity_view'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_jwt_settings(body_json: str) -> str:
    """
    Update JWT Settings (saveJwtSettings)  # noqa: E501

Updates the JWT Settings object that contains JWT token policy, etc. The tokenSigningKey field is a Base64 encoded string.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_jwt_settings(body=deserialize_param(body_json, 'JwtSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_jwt_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_mobile_app(body_json: str, oauth2_client_ids: Optional[str] = None) -> str:
    """
    Save Or update Mobile app (saveMobileApp)  # noqa: E501

Create or update the Mobile app. When creating mobile app, platform generates Mobile App Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Mobile App Id will be present in the response. Specify existing Mobile App Id to update the mobile app. Referencing non-existing Mobile App Id will cause 'Not Found' error.  Mobile app package name is unique for entire platform setup.    Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_mobile_app(body=deserialize_param(body_json, 'MobileApp'), oauth2_client_ids=oauth2_client_ids)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_mobile_app'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_mobile_app_bundle(body_json: str, oauth2_client_ids_json: str = None) -> str:
    """
    Save Or update Mobile app bundle (saveMobileAppBundle)  # noqa: E501

Create or update the Mobile app bundle that represents tha pair of ANDROID and IOS app and mobile settings like oauth2 clients, self-registration and layout configuration.When creating mobile app bundle, platform generates Mobile App Bundle Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Mobile App Bundle Id will be present in the response. Referencing non-existing Mobile App Bundle Id will cause 'Not Found' error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_mobile_app_bundle(body=deserialize_param(body_json, 'MobileAppBundle'), oauth2_client_ids=json.loads(oauth2_client_ids_json) if oauth2_client_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_mobile_app_bundle'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_mobile_app_settings(body_json: str) -> str:
    """
    Create Or Update the Mobile application settings (saveMobileAppSettings)  # noqa: E501

The request payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_mobile_app_settings(body=deserialize_param(body_json, 'MobileAppSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_mobile_app_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_mobile_session(x_mobile_token: str, body_json: str) -> str:
    """
    saveMobileSession  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_mobile_session(x_mobile_token=x_mobile_token, body=deserialize_param(body_json, 'MobileSessionInfo'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_mobile_session'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_notification_rule(body_json: str) -> str:
    """
    Save notification rule (saveNotificationRule)  # noqa: E501

Creates or updates notification rule.   Mandatory properties are `name`, `templateId` (of a template with `notificationType` matching to rule's `triggerType`), `triggerType`, `triggerConfig` and `recipientConfig`. Additionally, you may specify rule `description` inside of `additionalConfig`.  Trigger type of the rule cannot be changed. Available trigger types for tenant: `ENTITY_ACTION`, `ALARM`, `ALARM_COMMENT`, `ALARM_ASSIGNMENT`, `DEVICE_ACTIVITY`, `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT`. For sysadmin, there are following trigger types available: `ENTITIES_LIMIT`, `API_USAGE_LIMIT`, `NEW_PLATFORM_VERSION`.  Here is an example of notification rule to send notification when a device, asset or customer is created or deleted: ```json {   "name": "Entity action",   "templateId": {     "entityType": "NOTIFICATION_TEMPLATE",     "id": "32117320-d785-11ed-a06c-21dd57dd88ca"   },   "triggerType": "ENTITY_ACTION",   "triggerConfig": {     "entityTypes": [       "CUSTOMER",       "DEVICE",       "ASSET"     ],     "created": true,     "updated": false,     "deleted": true,     "triggerType": "ENTITY_ACTION"   },   "recipientsConfig": {     "targets": [       "320f2930-d785-11ed-a06c-21dd57dd88ca"     ],     "triggerType": "ENTITY_ACTION"   },   "additionalConfig": {     "description": "Send notification to tenant admins or customer users when a device, asset or customer is created"   },   "templateName": "Entity action notification",   "deliveryMethods": [     "WEB"   ] } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_notification_rule(body=deserialize_param(body_json, 'NotificationRule'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_notification_rule'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_notification_settings(body_json: str) -> str:
    """
    Save notification settings (saveNotificationSettings)  # noqa: E501

Saves notification settings for this tenant or sysadmin. `deliveryMethodsConfigs` of the settings must be specified.  Here is an example of the notification settings with Slack configuration: ```json {   "deliveryMethodsConfigs": {     "SLACK": {       "method": "SLACK",       "botToken": "xoxb-...."     }   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_notification_settings(body=deserialize_param(body_json, 'NotificationSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_notification_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_notification_target(body_json: str) -> str:
    """
    Save notification target (saveNotificationTarget)  # noqa: E501

Creates or updates notification target.  Available `configuration` types are `PLATFORM_USERS` and `SLACK`. For `PLATFORM_USERS` the `usersFilter` must be specified. For tenant, there are following users filter types available: `USER_LIST`, `CUSTOMER_USERS`, `TENANT_ADMINISTRATORS`, `ALL_USERS`, `ORIGINATOR_ENTITY_OWNER_USERS`, `AFFECTED_USER`. For sysadmin: `TENANT_ADMINISTRATORS`, `AFFECTED_TENANT_ADMINISTRATORS`, `SYSTEM_ADMINISTRATORS`, `ALL_USERS`.  Here is an example of tenant-level notification target to send notification to customer's users: ```json {   "name": "Users of Customer A",   "configuration": {     "type": "PLATFORM_USERS",     "usersFilter": {       "type": "CUSTOMER_USERS",       "customerId": "32499a20-d785-11ed-a06c-21dd57dd88ca"     },     "description": "Users of Customer A"   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_notification_target(body=deserialize_param(body_json, 'NotificationTarget'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_notification_target'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_notification_template(body_json: str) -> str:
    """
    Save notification template (saveNotificationTemplate)  # noqa: E501

Creates or updates notification template.  Here is an example of template to send notification via Web, SMS and Slack: ```json {   "name": "Greetings",   "notificationType": "GENERAL",   "configuration": {     "deliveryMethodsTemplates": {       "WEB": {         "enabled": true,         "subject": "Greetings",         "body": "Hi there, ${recipientTitle}",         "additionalConfig": {           "icon": {             "enabled": true,             "icon": "back_hand",             "color": "#757575"           },           "actionButtonConfig": {             "enabled": false           }         },         "method": "WEB"       },       "SMS": {         "enabled": true,         "body": "Hi there, ${recipientTitle}",         "method": "SMS"       },       "SLACK": {         "enabled": true,         "body": "Hi there, @${recipientTitle}",         "method": "SLACK"       }     }   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_notification_template(body=deserialize_param(body_json, 'NotificationTemplate'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_notification_template'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_qr_code_settings(body_json: str) -> str:
    """
    Create Or Update the Mobile application settings (saveMobileAppSettings)  # noqa: E501

The request payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_qr_code_settings(body=deserialize_param(body_json, 'QrCodeSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_qr_code_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_queue(service_type: str, body_json: str) -> str:
    """
    Create Or Update Queue (saveQueue)  # noqa: E501

Create or update the Queue. When creating queue, platform generates Queue Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). Specify existing Queue id to update the queue. Referencing non-existing Queue Id will cause 'Not Found' error.  Queue name is unique in the scope of sysadmin. Remove 'id', 'tenantId' from the request body example (below) to create new Queue entity.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_queue(service_type=service_type, body=deserialize_param(body_json, 'Queue'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_queue'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_repository_settings(body_json: str) -> str:
    """
    Creates or Updates the repository settings (saveRepositorySettings)  # noqa: E501

Creates or Updates the repository settings object.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_repository_settings(body=deserialize_param(body_json, 'RepositorySettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_repository_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_resource(body_json: str) -> str:
    """
    Create Or Update Resource (saveResource)  # noqa: E501

Create or update the Resource. When creating the Resource, platform generates Resource id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Resource id will be present in the response. Specify existing Resource id to update the Resource. Referencing non-existing Resource Id will cause 'Not Found' error.   Resource combination of the title with the key is unique in the scope of tenant. Remove 'id', 'tenantId' from the request body example (below) to create new Resource entity.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_resource(body=deserialize_param(body_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_resource'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_security_settings(body_json: str) -> str:
    """
    Update Security Settings (saveSecuritySettings)  # noqa: E501

Updates the Security Settings object that contains password policy, etc.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_security_settings(body=deserialize_param(body_json, 'SecuritySettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_security_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_trendz_settings(body_json: str) -> str:
    """
    Save Trendz settings (saveTrendzSettings)  # noqa: E501

Saves Trendz settings for this tenant.   Here is an example of the Trendz settings: ```json {   "enabled": true,   "baseUrl": "https://some.domain.com:18888/also_necessary_prefix" } ```  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_trendz_settings(body=deserialize_param(body_json, 'TrendzSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_trendz_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def send_activation_email(email: str) -> str:
    """
    Send or re-send the activation email  # noqa: E501

Force send the activation email to the user. Useful to resend the email if user has accidentally deleted it.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.send_activation_email(email=email)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'send_activation_email'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def send_chat_request(body_json: str) -> str:
    """
    Send request to AI chat model (sendChatRequest)  # noqa: E501

Submits a single prompt - made up of an optional system message and a required user message - to the specified AI chat model and returns either the generated answer or an error envelope.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.send_chat_request(body=deserialize_param(body_json, 'TbChatRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'send_chat_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def send_test_mail(body_json: str) -> str:
    """
    Send test email (sendTestMail)  # noqa: E501

Attempts to send test email to the System Administrator User using Mail Settings provided as a parameter. You may change the 'To' email in the user profile of the System Administrator.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.send_test_mail(body=deserialize_param(body_json, 'AdminSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'send_test_mail'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def send_test_sms(body_json: str) -> str:
    """
    Send test sms (sendTestMail)  # noqa: E501

Attempts to send test sms to the System Administrator User using SMS Settings and phone number provided as a parameters of the request.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.send_test_sms(body=deserialize_param(body_json, 'TestSmsRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'send_test_sms'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def setDaemon(daemonic_json: str) -> str:
    """
    Set whether this thread is a daemon.

This method is deprecated, use the .daemon property instead.
    """
    try:
        client = get_client()
        result = client.setDaemon(daemonic=deserialize_param(daemonic_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'setDaemon'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def setName(name_json: str) -> str:
    """
    Set the name string for this thread.

This method is deprecated, use the name attribute instead.
    """
    try:
        client = get_client()
        result = client.setName(name=deserialize_param(name_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'setName'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def start() -> str:
    """
    Start the thread's activity.

It must be called at most once per thread object. It arranges for the
object's run() method to be invoked in a separate thread of control.

This method will raise a RuntimeError if called more than once on the
same thread object.
    """
    try:
        client = get_client()
        result = client.start()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'start'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
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
            return "PERMISSION DENIED: You do not have permission to perform 'stop'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def subscribe_to_commands(device_token: str, timeout: Optional[int] = None) -> str:
    """
    Subscribe to RPC commands (subscribeToCommands) (Deprecated)  # noqa: E501

Subscribes to RPC commands using http long polling. Deprecated, since long polling is resource and network consuming. Consider using MQTT or CoAP protocol for light-weight real-time updates.   The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.subscribe_to_commands(device_token=device_token, timeout=timeout)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'subscribe_to_commands'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sync_edge(edge_id_json: str) -> str:
    """
    Sync edge (syncEdge)  # noqa: E501

Starts synchronization process between edge and cloud.  All entities that are assigned to particular edge are going to be send to remote edge service.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sync_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sync_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def test_script(body_json: str = None) -> str:
    """
    Test Script function  # noqa: E501

Execute the Script function and return the result. The format of request:   ```json {   "script": "Your Function as String",   "scriptType": "One of: update, generate, filter, switch, json, string",   "argNames": ["msg", "metadata", "type"],   "msg": "{\\"temperature\\": 42}",    "metadata": {     "deviceName": "Device A",     "deviceType": "Thermometer"   },   "msgType": "POST_TELEMETRY_REQUEST" } ```   Expected result JSON contains "output" and "error".  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.test_script(body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'test_script'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def unassign_entity_view_from_edge(edge_id_json: str, entity_view_id_json: str) -> str:
    """
    Unassign entity view from edge (unassignEntityViewFromEdge)  # noqa: E501

Clears assignment of the entity view to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove entity view (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove entity view locally.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.unassign_entity_view_from_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unassign_entity_view_from_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_image(_type: str, key: str, file: str) -> str:
    """
    updateImage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_image(_type=_type, key=key, file=file)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_image'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_image_info(_type: str, key: str, body_json: str) -> str:
    """
    updateImageInfo  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_image_info(_type=_type, key=key, body=deserialize_param(body_json, 'TbResourceInfo'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_image_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_image_public_status(_type: str, key: str, is_public: Optional[bool] = None) -> str:
    """
    updateImagePublicStatus  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_image_public_status(_type=_type, key=key, is_public=is_public)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_image_public_status'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def upload_image(title: str, file: str) -> str:
    """
    uploadImage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.upload_image(title=title, file=file)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'upload_image'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def register(mcp):
    mcp.tool()( activate_instance )
    mcp.tool()( assign_entity_view_to_edge )
    mcp.tool()( auto_commit_settings_exists )
    mcp.tool()( cancel_job )
    mcp.tool()( change_password )
    mcp.tool()( check_activate_token )
    mcp.tool()( check_repository_access )
    mcp.tool()( check_reset_token )
    mcp.tool()( check_updates )
    mcp.tool()( clear_events_post )
    mcp.tool()( code_processing_url )
    mcp.tool()( compare_entity_data_to_version )
    mcp.tool()( count_entities_by_query )
    mcp.tool()( create_notification_request )
    mcp.tool()( delete_ai_model_by_id )
    mcp.tool()( delete_auto_commit_settings )
    mcp.tool()( delete_calculated_field )
    mcp.tool()( delete_client_registration_template )
    mcp.tool()( delete_domain )
    mcp.tool()( delete_edge )
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
    mcp.tool()( delete_queue )
    mcp.tool()( delete_repository_settings )
    mcp.tool()( delete_resource )
    mcp.tool()( delete_resource_v1 )
    mcp.tool()( delete_rpc )
    mcp.tool()( download_gateway_docker_compose )
    mcp.tool()( download_image )
    mcp.tool()( download_image_preview )
    mcp.tool()( download_jks_resource_if_changed )
    mcp.tool()( download_js_resource_if_changed )
    mcp.tool()( download_lwm2m_resource_if_changed )
    mcp.tool()( download_pkcs12_resource_if_changed )
    mcp.tool()( download_public_image )
    mcp.tool()( download_resource )
    mcp.tool()( download_resource_if_changed )
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
    mcp.tool()( get_application_redirect )
    mcp.tool()( get_auto_commit_settings )
    mcp.tool()( get_available_delivery_methods )
    mcp.tool()( get_calculated_field_by_id )
    mcp.tool()( get_calculated_fields_by_entity_id )
    mcp.tool()( get_client_registration_templates )
    mcp.tool()( get_client_registration_templates1 )
    mcp.tool()( get_client_registration_templates_mail )
    mcp.tool()( get_component_descriptor_by_clazz )
    mcp.tool()( get_component_descriptors_by_type )
    mcp.tool()( get_component_descriptors_by_types )
    mcp.tool()( get_domain_info_by_id )
    mcp.tool()( get_domain_infos )
    mcp.tool()( get_edge_by_id )
    mcp.tool()( get_edge_entity_views )
    mcp.tool()( get_edge_events )
    mcp.tool()( get_edge_info_by_id )
    mcp.tool()( get_edge_install_instructions )
    mcp.tool()( get_edge_types )
    mcp.tool()( get_edge_upgrade_instructions )
    mcp.tool()( get_edges )
    mcp.tool()( get_edges_by_ids )
    mcp.tool()( get_edqs_state )
    mcp.tool()( get_entity_data_info )
    mcp.tool()( get_entity_view_by_id )
    mcp.tool()( get_entity_view_info_by_id )
    mcp.tool()( get_entity_view_types )
    mcp.tool()( get_events_get )
    mcp.tool()( get_events_post )
    mcp.tool()( get_events_v1_get1 )
    mcp.tool()( get_features_info )
    mcp.tool()( get_firmware )
    mcp.tool()( get_help_base_url )
    mcp.tool()( get_image_info )
    mcp.tool()( get_images )
    mcp.tool()( get_job_by_id )
    mcp.tool()( get_jobs )
    mcp.tool()( get_jwt_setting )
    mcp.tool()( get_latest_calculated_field_debug_event )
    mcp.tool()( get_latest_rule_node_debug_input )
    mcp.tool()( get_login_mobile_info )
    mcp.tool()( get_login_processing_url )
    mcp.tool()( get_lwm2m_bootstrap_security_info )
    mcp.tool()( get_lwm2m_list_objects )
    mcp.tool()( get_lwm2m_list_objects_page )
    mcp.tool()( get_mail_processing_url )
    mcp.tool()( get_max_datapoints_limit )
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
    mcp.tool()( get_persisted_rpc )
    mcp.tool()( get_qr_code_settings )
    mcp.tool()( get_queue_by_id )
    mcp.tool()( get_queue_by_name )
    mcp.tool()( get_queue_stats_by_id )
    mcp.tool()( get_queue_stats_by_ids )
    mcp.tool()( get_recipients_for_notification_target_config )
    mcp.tool()( get_repository_settings )
    mcp.tool()( get_repository_settings_info )
    mcp.tool()( get_resource_by_id )
    mcp.tool()( get_resource_info_by_id )
    mcp.tool()( get_resources )
    mcp.tool()( get_security_settings )
    mcp.tool()( get_server_time )
    mcp.tool()( get_software )
    mcp.tool()( get_system_info )
    mcp.tool()( get_trendz_settings )
    mcp.tool()( get_unread_notifications_count )
    mcp.tool()( get_version_create_request_status )
    mcp.tool()( get_version_load_request_status )
    mcp.tool()( handle_rule_engine_request )
    mcp.tool()( handle_rule_engine_request1 )
    mcp.tool()( handle_rule_engine_request2 )
    mcp.tool()( handle_rule_engine_request3 )
    mcp.tool()( import_image )
    mcp.tool()( isDaemon )
    mcp.tool()( is_alive )
    mcp.tool()( is_edge_upgrade_available )
    mcp.tool()( is_edges_support_enabled )
    mcp.tool()( is_edqs_api_enabled )
    mcp.tool()( is_tbel_enabled )
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
    mcp.tool()( post_rpc_request )
    mcp.tool()( process_edges_bulk_import )
    mcp.tool()( process_system_edqs_request )
    mcp.tool()( refresh )
    mcp.tool()( remove_mobile_session )
    mcp.tool()( reply_to_command )
    mcp.tool()( repository_settings_exists )
    mcp.tool()( reprocess_job )
    mcp.tool()( request_reset_password_by_email )
    mcp.tool()( reset_password )
    mcp.tool()( run )
    mcp.tool()( save_ai_model )
    mcp.tool()( save_auto_commit_settings )
    mcp.tool()( save_calculated_field )
    mcp.tool()( save_client_registration_template )
    mcp.tool()( save_domain )
    mcp.tool()( save_edge )
    mcp.tool()( save_entities_version )
    mcp.tool()( save_entity_view )
    mcp.tool()( save_jwt_settings )
    mcp.tool()( save_mobile_app )
    mcp.tool()( save_mobile_app_bundle )
    mcp.tool()( save_mobile_app_settings )
    mcp.tool()( save_mobile_session )
    mcp.tool()( save_notification_rule )
    mcp.tool()( save_notification_settings )
    mcp.tool()( save_notification_target )
    mcp.tool()( save_notification_template )
    mcp.tool()( save_qr_code_settings )
    mcp.tool()( save_queue )
    mcp.tool()( save_repository_settings )
    mcp.tool()( save_resource )
    mcp.tool()( save_security_settings )
    mcp.tool()( save_trendz_settings )
    mcp.tool()( send_activation_email )
    mcp.tool()( send_chat_request )
    mcp.tool()( send_test_mail )
    mcp.tool()( send_test_sms )
    mcp.tool()( setDaemon )
    mcp.tool()( setName )
    mcp.tool()( start )
    mcp.tool()( stop )
    mcp.tool()( subscribe_to_commands )
    mcp.tool()( sync_edge )
    mcp.tool()( test_script )
    mcp.tool()( unassign_entity_view_from_edge )
    mcp.tool()( update_image )
    mcp.tool()( update_image_info )
    mcp.tool()( update_image_public_status )
    mcp.tool()( upload_image )
