import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_device_profile(device_profile_id_json: str) -> str:
    """
    Delete device profile (deleteDeviceProfile)  # noqa: E501

Deletes the device profile. Referencing non-existing device profile Id will cause an error. Can't delete the device profile if it is referenced by existing devices.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (DeviceProfileId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.delete_device_profile(device_profile_id=deserialize_param(device_profile_id_json, 'DeviceProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_device_profile'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_attributes_keys(device_profile_id_json: str = None) -> str:
    """
    Get attribute keys (getAttributesKeys)  # noqa: E501

Get a set of unique attribute keys used by devices that belong to specified profile. If profile is not set returns a list of unique keys among all profiles. The call is used for auto-complete in the UI forms. The implementation limits the number of devices that participate in search to 100 as a trade of between accurate results and time-consuming queries.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (DeviceProfileId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_attributes_keys(device_profile_id=deserialize_param(device_profile_id_json, 'DeviceProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_attributes_keys'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_default_device_profile_info() -> str:
    """
    Get Default Device Profile (getDefaultDeviceProfileInfo)  # noqa: E501

Fetch the Default Device Profile Info object. Device Profile Info is a lightweight object that includes main information about Device Profile excluding the heavyweight configuration object.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_default_device_profile_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_default_device_profile_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_device_profile_by_id(device_profile_id_json: str, inline_images: Optional[bool] = None) -> str:
    """
    Get Device Profile (getDeviceProfileById)  # noqa: E501

Fetch the Device Profile object based on the provided Device Profile Id. The server checks that the device profile is owned by the same tenant.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (DeviceProfileId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_device_profile_by_id(device_profile_id=deserialize_param(device_profile_id_json, 'DeviceProfileId'), inline_images=inline_images)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_device_profile_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_device_profile_info_by_id(device_profile_id_json: str) -> str:
    """
    Get Device Profile Info (getDeviceProfileInfoById)  # noqa: E501

Fetch the Device Profile Info object based on the provided Device Profile Id. Device Profile Info is a lightweight object that includes main information about Device Profile excluding the heavyweight configuration object.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (DeviceProfileId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_device_profile_info_by_id(device_profile_id=deserialize_param(device_profile_id_json, 'DeviceProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_device_profile_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_device_profile_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, transport_type: Optional[str] = None) -> str:
    """
    Get Device Profiles for transport type (getDeviceProfileInfos)  # noqa: E501

Returns a page of devices profile info objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. Device Profile Info is a lightweight object that includes main information about Device Profile excluding the heavyweight configuration object.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_device_profile_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, transport_type=transport_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_device_profile_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_device_profile_names(active_only: bool) -> str:
    """
    Get Device Profile names (getDeviceProfileNames)  # noqa: E501

Returns a set of unique device profile names owned by the tenant.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_device_profile_names(active_only=active_only)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_device_profile_names'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_device_profiles(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Device Profiles (getDeviceProfiles)  # noqa: E501

Returns a page of devices profile objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_device_profiles(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_device_profiles'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_device_profiles_by_ids(device_profile_ids_json: str) -> str:
    """
    Get Device Profiles By Ids (getDeviceProfilesByIds)  # noqa: E501

Requested device profiles must be owned by tenant which is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_device_profiles_by_ids(device_profile_ids=json.loads(device_profile_ids_json) if device_profile_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_device_profiles_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_timeseries_keys(device_profile_id_json: str = None) -> str:
    """
    Get time-series keys (getTimeseriesKeys)  # noqa: E501

Get a set of unique time-series keys used by devices that belong to specified profile. If profile is not set returns a list of unique keys among all profiles. The call is used for auto-complete in the UI forms. The implementation limits the number of devices that participate in search to 100 as a trade of between accurate results and time-consuming queries.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (DeviceProfileId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_timeseries_keys(device_profile_id=deserialize_param(device_profile_id_json, 'DeviceProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_timeseries_keys'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_device_profile(body_json: str = None) -> str:
    """
    Create Or Update Device Profile (saveDeviceProfile)  # noqa: E501

Create or update the Device Profile. When creating device profile, platform generates device profile id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created device profile id will be present in the response. Specify existing device profile id to update the device profile. Referencing non-existing device profile Id will cause 'Not Found' error.   Device profile name is unique in the scope of tenant. Only one 'default' device profile may exist in scope of tenant.  # Device profile data definition  Device profile data object contains alarm rules configuration, device provision strategy and transport type configuration for device connectivity. Let's review some examples. First one is the default device profile data configuration and second one - the custom one.   ```json {    "alarms":[    ],    "configuration":{       "type":"DEFAULT"    },    "provisionConfiguration":{       "type":"DISABLED",       "provisionDeviceSecret":null    },    "transportConfiguration":{       "type":"DEFAULT"    } } ```  ```json {    "alarms":[       {          "id":"2492b935-1226-59e9-8615-17d8978a4f93",          "alarmType":"Temperature Alarm",          "clearRule":{             "schedule":null,             "condition":{                "spec":{                   "type":"SIMPLE"                },                "condition":[                   {                      "key":{                         "key":"temperature",                         "type":"TIME_SERIES"                      },                      "value":null,                      "predicate":{                         "type":"NUMERIC",                         "value":{                            "userValue":null,                            "defaultValue":30.0,                            "dynamicValue":null                         },                         "operation":"LESS"                      },                      "valueType":"NUMERIC"                   }                ]             },             "dashboardId":null,             "alarmDetails":null          },          "propagate":false,          "createRules":{             "MAJOR":{                "schedule":{                   "type":"SPECIFIC_TIME",                   "endsOn":64800000,                   "startsOn":43200000,                   "timezone":"Europe/Kiev",                   "daysOfWeek":[                      1,                      3,                      5                   ]                },                "condition":{                   "spec":{                      "type":"DURATION",                      "unit":"MINUTES",                      "predicate":{                         "userValue":null,                         "defaultValue":30,                         "dynamicValue":null                      }                   },                   "condition":[                      {                         "key":{                            "key":"temperature",                            "type":"TIME_SERIES"                         },                         "value":null,                         "predicate":{                            "type":"COMPLEX",                            "operation":"OR",                            "predicates":[                               {                                  "type":"NUMERIC",                                  "value":{                                     "userValue":null,                                     "defaultValue":50.0,                                     "dynamicValue":null                                  },                                  "operation":"LESS_OR_EQUAL"                               },                               {                                  "type":"NUMERIC",                                  "value":{                                     "userValue":null,                                     "defaultValue":30.0,                                     "dynamicValue":null                                  },                                  "operation":"GREATER"                               }                            ]                         },                         "valueType":"NUMERIC"                      }                   ]                },                "dashboardId":null,                "alarmDetails":null             },             "WARNING":{                "schedule":{                   "type":"CUSTOM",                   "items":[                      {                         "endsOn":0,                         "enabled":false,                         "startsOn":0,                         "dayOfWeek":1                      },                      {                         "endsOn":64800000,                         "enabled":true,                         "startsOn":43200000,                         "dayOfWeek":2                      },                      {                         "endsOn":0,                         "enabled":false,                         "startsOn":0,                         "dayOfWeek":3                      },                      {                         "endsOn":57600000,                         "enabled":true,                         "startsOn":36000000,                         "dayOfWeek":4                      },                      {                         "endsOn":0,                         "enabled":false,                         "startsOn":0,                         "dayOfWeek":5                      },                      {                         "endsOn":0,                         "enabled":false,                         "startsOn":0,                         "dayOfWeek":6                      },                      {                         "endsOn":0,                         "enabled":false,                         "startsOn":0,                         "dayOfWeek":7                      }                   ],                   "timezone":"Europe/Kiev"                },                "condition":{                   "spec":{                      "type":"REPEATING",                      "predicate":{                         "userValue":null,                         "defaultValue":5,                         "dynamicValue":null                      }                   },                   "condition":[                      {                         "key":{                            "key":"tempConstant",                            "type":"CONSTANT"                         },                         "value":30,                         "predicate":{                            "type":"NUMERIC",                            "value":{                               "userValue":null,                               "defaultValue":0.0,                               "dynamicValue":{                                  "inherit":false,                                  "sourceType":"CURRENT_DEVICE",                                  "sourceAttribute":"tempThreshold"                               }                            },                            "operation":"EQUAL"                         },                         "valueType":"NUMERIC"                      }                   ]                },                "dashboardId":null,                "alarmDetails":null             },             "CRITICAL":{                "schedule":null,                "condition":{                   "spec":{                      "type":"SIMPLE"                   },                   "condition":[                      {                         "key":{                            "key":"temperature",                            "type":"TIME_SERIES"                         },                         "value":null,                         "predicate":{                            "type":"NUMERIC",                            "value":{                               "userValue":null,                               "defaultValue":50.0,                               "dynamicValue":null                            },                            "operation":"GREATER"                         },                         "valueType":"NUMERIC"                      }                   ]                },                "dashboardId":null,                "alarmDetails":null             }          },          "propagateRelationTypes":null       }    ],    "configuration":{       "type":"DEFAULT"    },    "provisionConfiguration":{       "type":"ALLOW_CREATE_NEW_DEVICES",       "provisionDeviceSecret":"vaxb9hzqdbz3oqukvomg"    },    "transportConfiguration":{       "type":"MQTT",       "deviceTelemetryTopic":"v1/devices/me/telemetry",       "deviceAttributesTopic":"v1/devices/me/attributes",       "transportPayloadTypeConfiguration":{          "transportPayloadType":"PROTOBUF",          "deviceTelemetryProtoSchema":"syntax =\\"proto3\\";\\npackage telemetry;\\n\\nmessage SensorDataReading {\\n\\n  optional double temperature = 1;\\n  optional double humidity = 2;\\n  InnerObject innerObject = 3;\\n\\n  message InnerObject {\\n    optional string key1 = 1;\\n    optional bool key2 = 2;\\n    optional double key3 = 3;\\n    optional int32 key4 = 4;\\n    optional string key5 = 5;\\n  }\\n}",          "deviceAttributesProtoSchema":"syntax =\\"proto3\\";\\npackage attributes;\\n\\nmessage SensorConfiguration {\\n  optional string firmwareVersion = 1;\\n  optional string serialNumber = 2;\\n}",          "deviceRpcRequestProtoSchema":"syntax =\\"proto3\\";\\npackage rpc;\\n\\nmessage RpcRequestMsg {\\n  optional string method = 1;\\n  optional int32 requestId = 2;\\n  optional string params = 3;\\n}",          "deviceRpcResponseProtoSchema":"syntax =\\"proto3\\";\\npackage rpc;\\n\\nmessage RpcResponseMsg {\\n  optional string payload = 1;\\n}"       }    } } ```  Let's review some specific objects examples related to the device profile configuration:  # Alarm Schedule  Alarm Schedule JSON object represents the time interval during which the alarm rule is active. Note,   ```json "schedule": null ```  means alarm rule is active all the time. **'daysOfWeek'** field represents Monday as 1, Tuesday as 2 and so on. **'startsOn'** and **'endsOn'** fields represent hours in millis (e.g. 64800000 = 18:00 or 6pm). **'enabled'** flag specifies if item in a custom rule is active for specific day of the week:  ## Specific Time Schedule  ```json {    "schedule":{       "type":"SPECIFIC_TIME",       "endsOn":64800000,       "startsOn":43200000,       "timezone":"Europe/Kiev",       "daysOfWeek":[          1,          3,          5       ]    } } ```  ## Custom Schedule  ```json {    "schedule":{       "type":"CUSTOM",       "items":[          {             "endsOn":0,             "enabled":false,             "startsOn":0,             "dayOfWeek":1          },          {             "endsOn":64800000,             "enabled":true,             "startsOn":43200000,             "dayOfWeek":2          },          {             "endsOn":0,             "enabled":false,             "startsOn":0,             "dayOfWeek":3          },          {             "endsOn":57600000,             "enabled":true,             "startsOn":36000000,             "dayOfWeek":4          },          {             "endsOn":0,             "enabled":false,             "startsOn":0,             "dayOfWeek":5          },          {             "endsOn":0,             "enabled":false,             "startsOn":0,             "dayOfWeek":6          },          {             "endsOn":0,             "enabled":false,             "startsOn":0,             "dayOfWeek":7          }       ],       "timezone":"Europe/Kiev"    } } ```  # Alarm condition type (**'spec'**)  Alarm condition type can be either simple, duration, or repeating. For example, 5 times in a row or during 5 minutes.  Note, **'userValue'** field is not used and reserved for future usage, **'dynamicValue'** is used for condition appliance by using the value of the **'sourceAttribute'** or else **'defaultValue'** is used (if **'sourceAttribute'** is absent).  **'sourceType'** of the **'sourceAttribute'** can be:   * 'CURRENT_DEVICE';  * 'CURRENT_CUSTOMER';  * 'CURRENT_TENANT'.  **'sourceAttribute'** can be inherited from the owner if **'inherit'** is set to true (for CURRENT_DEVICE and CURRENT_CUSTOMER).  ## Repeating alarm condition  ```json {    "spec":{       "type":"REPEATING",       "predicate":{          "userValue":null,          "defaultValue":5,          "dynamicValue":{             "inherit":true,             "sourceType":"CURRENT_DEVICE",             "sourceAttribute":"tempAttr"          }       }    } } ```  ## Duration alarm condition  ```json {    "spec":{       "type":"DURATION",       "unit":"MINUTES",       "predicate":{          "userValue":null,          "defaultValue":30,          "dynamicValue":null       }    } } ```  **'unit'** can be:   * 'SECONDS';  * 'MINUTES';  * 'HOURS';  * 'DAYS'.  # Key Filters  Key filter objects are created under the **'condition'** array. They allow you to define complex logical expressions over entity field, attribute, latest time-series value or constant. The filter is defined using 'key', 'valueType', 'value' (refers to the value of the 'CONSTANT' alarm filter key type) and 'predicate' objects. Let's review each object:  ## Alarm Filter Key  Filter Key defines either entity field, attribute, telemetry or constant. It is a JSON object that consists the key name and type. The following filter key types are supported:  * 'ATTRIBUTE' - used for attributes values;  * 'TIME_SERIES' - used for time-series values;  * 'ENTITY_FIELD' - used for accessing entity fields like 'name', 'label', etc. The list of available fields depends on the entity type;  * 'CONSTANT' - constant value specified.  Let's review the example:  ```json {   "type": "TIME_SERIES",   "key": "temperature" } ```  ## Value Type and Operations  Provides a hint about the data type of the entity field that is defined in the filter key. The value type impacts the list of possible operations that you may use in the corresponding predicate. For example, you may use 'STARTS_WITH' or 'END_WITH', but you can't use 'GREATER_OR_EQUAL' for string values.The following filter value types and corresponding predicate operations are supported:    * 'STRING' - used to filter any 'String' or 'JSON' values. Operations: EQUAL, NOT_EQUAL, STARTS_WITH, ENDS_WITH, CONTAINS, NOT_CONTAINS;   * 'NUMERIC' - used for 'Long' and 'Double' values. Operations: EQUAL, NOT_EQUAL, GREATER, LESS, GREATER_OR_EQUAL, LESS_OR_EQUAL;   * 'BOOLEAN' - used for boolean values. Operations: EQUAL, NOT_EQUAL;  * 'DATE_TIME' - similar to numeric, transforms value to milliseconds since epoch. Operations: EQUAL, NOT_EQUAL, GREATER, LESS, GREATER_OR_EQUAL, LESS_OR_EQUAL;      ## Filter Predicate  Filter Predicate defines the logical expression to evaluate. The list of available operations depends on the filter value type, see above. Platform supports 4 predicate types: 'STRING', 'NUMERIC', 'BOOLEAN' and 'COMPLEX'. The last one allows to combine multiple operations over one filter key.  Simple predicate example to check 'value < 100':   ```json {   "operation": "LESS",   "value": {     "userValue": null,     "defaultValue": 100,     "dynamicValue": null   },   "type": "NUMERIC" } ```  Complex predicate example, to check 'value < 10 or value > 20':   ```json {   "type": "COMPLEX",   "operation": "OR",   "predicates": [     {       "operation": "LESS",       "value": {         "userValue": null,         "defaultValue": 10,         "dynamicValue": null       },       "type": "NUMERIC"     },     {       "operation": "GREATER",       "value": {         "userValue": null,         "defaultValue": 20,         "dynamicValue": null       },       "type": "NUMERIC"     }   ] } ```  More complex predicate example, to check 'value < 10 or (value > 50 && value < 60)':   ```json {   "type": "COMPLEX",   "operation": "OR",   "predicates": [     {       "operation": "LESS",       "value": {         "userValue": null,         "defaultValue": 10,         "dynamicValue": null       },       "type": "NUMERIC"     },     {       "type": "COMPLEX",       "operation": "AND",       "predicates": [         {           "operation": "GREATER",           "value": {             "userValue": null,             "defaultValue": 50,             "dynamicValue": null           },           "type": "NUMERIC"         },         {           "operation": "LESS",           "value": {             "userValue": null,             "defaultValue": 60,             "dynamicValue": null           },           "type": "NUMERIC"         }       ]     }   ] } ```  You may also want to replace hardcoded values (for example, temperature > 20) with the more dynamic expression (for example, temperature > value of the tenant attribute with key 'temperatureThreshold'). It is possible to use 'dynamicValue' to define attribute of the tenant, customer or device. See example below:  ```json {   "operation": "GREATER",   "value": {     "userValue": null,     "defaultValue": 0,     "dynamicValue": {       "inherit": false,       "sourceType": "CURRENT_TENANT",       "sourceAttribute": "temperatureThreshold"     }   },   "type": "NUMERIC" } ```  Note that you may use 'CURRENT_DEVICE', 'CURRENT_CUSTOMER' and 'CURRENT_TENANT' as a 'sourceType'. The 'defaultValue' is used when the attribute with such a name is not defined for the chosen source. The 'sourceAttribute' can be inherited from the owner of the specified 'sourceType' if 'inherit' is set to true.  # Provision Configuration  There are 3 types of device provision configuration for the device profile:   * 'DISABLED';  * 'ALLOW_CREATE_NEW_DEVICES';  * 'CHECK_PRE_PROVISIONED_DEVICES'.  Please refer to the [docs](https://thingsboard.io/docs/user-guide/device-provisioning/) for more details.  # Transport Configuration  5 transport configuration types are available:  * 'DEFAULT';  * 'MQTT';  * 'LWM2M';  * 'COAP';  * 'SNMP'.  Default type supports basic MQTT, HTTP, CoAP and LwM2M transports. Please refer to the [docs](https://thingsboard.io/docs/user-guide/device-profiles/#transport-configuration) for more details about other types.  See another example of COAP transport configuration below:  ```json {    "type":"COAP",    "clientSettings":{       "edrxCycle":null,       "powerMode":"DRX",       "psmActivityTimer":null,       "pagingTransmissionWindow":null    },    "coapDeviceTypeConfiguration":{       "coapDeviceType":"DEFAULT",       "transportPayloadTypeConfiguration":{          "transportPayloadType":"JSON"       }    } } ```Remove 'id', 'tenantId' from the request body example (below) to create new Device Profile entity.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_device_profile(body=deserialize_param(body_json, 'DeviceProfile'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_device_profile'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def set_default_device_profile(device_profile_id_json: str) -> str:
    """
    Make Device Profile Default (setDefaultDeviceProfile)  # noqa: E501

Marks device profile as default within a tenant scope.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (DeviceProfileId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.set_default_device_profile(device_profile_id=deserialize_param(device_profile_id_json, 'DeviceProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'set_default_device_profile'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_device_profile )
    mcp.tool()( get_attributes_keys )
    mcp.tool()( get_default_device_profile_info )
    mcp.tool()( get_device_profile_by_id )
    mcp.tool()( get_device_profile_info_by_id )
    mcp.tool()( get_device_profile_infos )
    mcp.tool()( get_device_profile_names )
    mcp.tool()( get_device_profiles )
    mcp.tool()( get_device_profiles_by_ids )
    mcp.tool()( get_timeseries_keys )
    mcp.tool()( save_device_profile )
    mcp.tool()( set_default_device_profile )
