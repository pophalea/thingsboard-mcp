import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def assign_device_to_tenant(tenant_id_json: str, device_id_json: str) -> str:
    """
    Assign device to tenant (assignDeviceToTenant)  # noqa: E501

Creates assignment of the device to tenant. Thereafter tenant will be able to reassign the device to a customer.  Available for users with 'TENANT_ADMIN' authority. Security check is performed to verify that the user has 'ASSIGN_TO_TENANT' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (DeviceId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.assign_device_to_tenant(tenant_id=deserialize_param(tenant_id_json, 'TenantId'), device_id=deserialize_param(device_id_json, 'DeviceId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_device_to_tenant'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def count_by_device_group_and_empty_ota_package(ota_package_type: str, ota_package_id_json: str, entity_group_id_json: str) -> str:
    """
    Count devices by device profile  (countByDeviceProfileAndEmptyOtaPackage)  # noqa: E501

The platform gives an ability to load OTA (over-the-air) packages to devices. It can be done in two different ways: device scope or device profile scope.In the response you will find the number of devices with specified device profile, but without previously defined device scope OTA package. It can be useful when you want to define number of devices that will be affected with future OTA package  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (OtaPackageId):
    - `id` (str)
    - `entity_type` (str)
    Expected JSON Structure (EntityGroupId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.count_by_device_group_and_empty_ota_package(ota_package_type=ota_package_type, ota_package_id=deserialize_param(ota_package_id_json, 'OtaPackageId'), entity_group_id=deserialize_param(entity_group_id_json, 'EntityGroupId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'count_by_device_group_and_empty_ota_package'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def count_by_device_profile_and_empty_ota_package(ota_package_type: str, device_profile_id_json: str) -> str:
    """
    Count devices by device profile  (countByDeviceProfileAndEmptyOtaPackage)  # noqa: E501

The platform gives an ability to load OTA (over-the-air) packages to devices. It can be done in two different ways: device scope or device profile scope.In the response you will find the number of devices with specified device profile, but without previously defined device scope OTA package. It can be useful when you want to define number of devices that will be affected with future OTA package  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (DeviceProfileId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.count_by_device_profile_and_empty_ota_package(ota_package_type=ota_package_type, device_profile_id=deserialize_param(device_profile_id_json, 'DeviceProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'count_by_device_profile_and_empty_ota_package'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_device(device_id_json: str) -> str:
    """
    Delete device (deleteDevice)  # noqa: E501

Deletes the device, it's credentials and all the relations (from and to the device). Referencing non-existing device Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (DeviceId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.delete_device(device_id=deserialize_param(device_id_json, 'DeviceId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_device'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def find_by_query_v1(body_json: str = None) -> str:
    """
    Find related devices (findByQuery)  # noqa: E501

Returns all devices that are related to the specific entity. The entity id, relation type, device types, depth of the search, and other query parameters defined using complex 'DeviceSearchQuery' object. See 'Model' tab of the Parameters for more info.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (DeviceSearchQuery):
    - `parameters` (RelationsSearchParameters)
    - `relation_type` (str)
    - `device_types` (list[str])
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


def get_all_device_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, include_customers: Optional[bool] = None, device_profile_id_json: str = None) -> str:
    """
    Get All Device Infos for current user (getAllDeviceInfos)  # noqa: E501

Returns a page of device info objects owned by the tenant or the customer of a current user. Device Info is an extension of the default Device object that contains information about the owner name.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (DeviceProfileId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_all_device_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, include_customers=include_customers, device_profile_id=deserialize_param(device_profile_id_json, 'DeviceProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_all_device_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_customer_device_infos(customer_id_json: str, page_size: int, page: int, type: Optional[str] = None, device_profile_id_json: str = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, active: Optional[bool] = None, include_customers: Optional[bool] = None) -> str:
    """
    Get Customer Device Infos (getCustomerDeviceInfos)  # noqa: E501

Returns a page of device info objects owned by the specified customer. Device Info is an extension of the default Device object that contains information about the owner name.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomerId):
    - `id` (str)
    - `entity_type` (str)
    Expected JSON Structure (DeviceProfileId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_customer_device_infos(customer_id=deserialize_param(customer_id_json, 'CustomerId'), page_size=page_size, page=page, type=type, device_profile_id=deserialize_param(device_profile_id_json, 'DeviceProfileId'), text_search=text_search, sort_property=sort_property, sort_order=sort_order, active=active, include_customers=include_customers)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_customer_device_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_customer_devices(customer_id_json: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Customer Devices (getCustomerDevices)  # noqa: E501

Returns a page of devices objects assigned to customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomerId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_customer_devices(customer_id=deserialize_param(customer_id_json, 'CustomerId'), page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_customer_devices'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_device_by_id(device_id_json: str) -> str:
    """
    Get Device (getDeviceById)  # noqa: E501

Fetch the Device object based on the provided Device Id.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (DeviceId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_device_by_id(device_id=deserialize_param(device_id_json, 'DeviceId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_device_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_device_credentials_by_device_id(device_id_json: str) -> str:
    """
    Get Device Credentials (getDeviceCredentialsByDeviceId)  # noqa: E501

If during device creation there wasn't specified any credentials, platform generates random 'ACCESS_TOKEN' credentials.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ_CREDENTIALS' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (DeviceId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_device_credentials_by_device_id(device_id=deserialize_param(device_id_json, 'DeviceId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_device_credentials_by_device_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_device_info_by_id(device_id_json: str) -> str:
    """
    Get Device (getDeviceInfoById)  # noqa: E501

Fetch the Device info object based on the provided Device Id. Device Info is an extension of the default Device object that contains information about the owner name.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (DeviceId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_device_info_by_id(device_id=deserialize_param(device_id_json, 'DeviceId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_device_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_device_types() -> str:
    """
    Get Device Types (getDeviceTypes)  # noqa: E501

Deprecated. See 'getDeviceProfileNames' API from Device Profile Controller instead.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_device_types()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_device_types'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_devices_by_entity_group_id(entity_group_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get devices by Entity Group Id (getDevicesByEntityGroupId)  # noqa: E501

Returns a page of Device objects that belongs to specified Entity Group Id. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.  # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityGroupId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_devices_by_entity_group_id(entity_group_id=deserialize_param(entity_group_id_json, 'EntityGroupId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_devices_by_entity_group_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_devices_by_ids(device_ids_json: str) -> str:
    """
    Get Devices By Ids (getDevicesByIds)  # noqa: E501

Requested devices must be owned by tenant or assigned to customer which user is performing the request.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_devices_by_ids(device_ids=json.loads(device_ids_json) if device_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_devices_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_device(device_name: str) -> str:
    """
    Get Tenant Device (getTenantDevice)  # noqa: E501

Requested device must be owned by tenant that the user belongs to. Device name is an unique property of device. So it can be used to identify the device.  Available for users with 'TENANT_ADMIN' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_device(device_name=device_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_device'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_devices(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Devices (getTenantDevices)  # noqa: E501

Returns a page of devices owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_devices(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_devices'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_user_devices(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Devices (getUserDevices)  # noqa: E501

Returns a page of devices that are available for the current user. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_user_devices(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_user_devices'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def process_devices_bulk_import(body_json: str = None) -> str:
    """
    Import the bulk of devices (processDevicesBulkImport)  # noqa: E501

There's an ability to import the bulk of devices using the only .csv file. Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (BulkImportRequest):
    - `file` (str)
    - `mapping` (Mapping)
    - `customer_id` (CustomerId)
    - `entity_group_id` (str)
    """
    try:
        client = get_client()
        result = client.process_devices_bulk_import(body=deserialize_param(body_json, 'BulkImportRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'process_devices_bulk_import'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def re_claim_device(device_name: str) -> str:
    """
    Reclaim device (reClaimDevice)  # noqa: E501

Reclaiming means the device will be unassigned from the customer and the device will be available for claiming again.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'CLAIM_DEVICES' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.re_claim_device(device_name=device_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 're_claim_device'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_device(body_json: str, access_token: Optional[str] = None) -> str:
    """
    Create Or Update Device (saveDevice)  # noqa: E501

Create or update the Device. When creating device, platform generates Device Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). Device credentials are also generated if not provided in the 'accessToken' request parameter. The newly created device id will be present in the response. Specify existing Device id to update the device. Referencing non-existing device Id will cause 'Not Found' error.  Device name is unique in the scope of tenant. Use unique identifiers like MAC or IMEI for the device names and non-unique 'label' field for user-friendly visualization purposes.Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Device entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_device(body=deserialize_param(body_json, 'Device'), access_token=access_token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_device'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_device_with_credentials(body_json: str = None, entity_group_id: Optional[str] = None, entity_group_ids: Optional[str] = None) -> str:
    """
    Create Device (saveDevice) with credentials   # noqa: E501

Create or update the Device. When creating device, platform generates Device Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). Requires to provide the Device Credentials object as well as an existing device profile ID or use "default". You may find the example of device with different type of credentials below:   - Credentials type: <b>"Access token"</b> with <b>device profile ID</b> below:   ```json {   "device": {     "name":"Name_DeviceWithCredantial_AccessToken",     "label":"Label_DeviceWithCredantial_AccessToken",     "deviceProfileId":{       "id":"5636aba0-1022-11ee-9631-51fb57f69174",       "entityType":"DEVICE_PROFILE"      }    },   "credentials": {     "credentialsType": "ACCESS_TOKEN",     "credentialsId": "6hmxew8pmmzng4e3une2"    } } ```  - Credentials type: <b>"Access token"</b> with  <b>device profile default</b> below:   ```json {   "device": {     "name":"Name_DeviceWithCredantial_AccessToken_Default",     "label":"Label_DeviceWithCredantial_AccessToken_Default",     "type": "default"    },   "credentials": {     "credentialsType": "ACCESS_TOKEN",     "credentialsId": "6hmxew8pmmzng4e3une3"    } } ```  - Credentials type: <b>"X509"</b> with <b>device profile ID</b> below:   Note: <b>credentialsId</b> -  format <b>Sha3Hash</b>, <b>certificateValue</b> - format <b>PEM</b> (with "--BEGIN CERTIFICATE----" and  -"----END CERTIFICATE-").  ```json {   "device": {     "name":"Name_DeviceWithCredantial_X509_Certificate",     "label":"Label_DeviceWithCredantial_X509_Certificate",     "deviceProfileId":{       "id":"9d9588c0-06c9-11ee-b618-19be30fdeb60",       "entityType":"DEVICE_PROFILE"      }    },   "credentials": {     "credentialsType": "X509_CERTIFICATE",     "credentialsId": "84f5911765abba1f96bf4165604e9e90338fc6214081a8e623b6ff9669aedb27",     "credentialsValue": "-----BEGIN CERTIFICATE----- MIICMTCCAdegAwIBAgIUI9dBuwN6pTtK6uZ03rkiCwV4wEYwCgYIKoZIzj0EAwIwbjELMAkGA1UEBhMCVVMxETAPBgNVBAgMCE5ldyBZb3JrMRowGAYDVQQKDBFUaGluZ3NCb2FyZCwgSW5jLjEwMC4GA1UEAwwnZGV2aWNlQ2VydGlmaWNhdGVAWDUwOVByb3Zpc2lvblN0cmF0ZWd5MB4XDTIzMDMyOTE0NTYxN1oXDTI0MDMyODE0NTYxN1owbjELMAkGA1UEBhMCVVMxETAPBgNVBAgMCE5ldyBZb3JrMRowGAYDVQQKDBFUaGluZ3NCb2FyZCwgSW5jLjEwMC4GA1UEAwwnZGV2aWNlQ2VydGlmaWNhdGVAWDUwOVByb3Zpc2lvblN0cmF0ZWd5MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9Zo791qKQiGNBm11r4ZGxh+w+ossZL3xc46ufq5QckQHP7zkD2XDAcmP5GvdkM1sBFN9AWaCkQfNnWmfERsOOKNTMFEwHQYDVR0OBBYEFFFc5uyCyglQoZiKhzXzMcQ3BKORMB8GA1UdIwQYMBaAFFFc5uyCyglQoZiKhzXzMcQ3BKORMA8GA1UdEwEB/wQFMAMBAf8wCgYIKoZIzj0EAwIDSAAwRQIhANbA9CuhoOifZMMmqkpuld+65CR+ItKdXeRAhLMZuccuAiB0FSQB34zMutXrZj1g8Gl5OkE7YryFHbei1z0SveHR8g== -----END CERTIFICATE-----"    } } ```  - Credentials type: <b>"MQTT_BASIC"</b> with <b>device profile ID</b> below:   ```json {   "device": {     "name":"Name_DeviceWithCredantial_MQTT_Basic",     "label":"Label_DeviceWithCredantial_MQTT_Basic",     "deviceProfileId":{       "id":"9d9588c0-06c9-11ee-b618-19be30fdeb60",       "entityType":"DEVICE_PROFILE"      }    },   "credentials": {     "credentialsType": "MQTT_BASIC",     "credentialsValue": "{\\"clientId\\":\\"5euh5nzm34bjjh1efmlt\\",\\"userName\\":\\"onasd1lgwasmjl7v2v7h\\",\\"password\\":\\"b9xtm4ny8kt9zewaga5o\\"}"    } } ```  - You may find the example of <b>LwM2M</b> device and <b>RPK</b> credentials below:   Note: LwM2M device - only existing device profile ID (Transport configuration -> Transport type: "LWM2M".  ```json {   "device": {     "name":"Name_LwRpk00000000",     "label":"Label_LwRpk00000000",     "deviceProfileId":{       "id":"a660bd50-10ef-11ee-8737-b5634e73c779",       "entityType":"DEVICE_PROFILE"      }    },   "credentials": {     "credentialsType": "LWM2M_CREDENTIALS",     "credentialsId": "LwRpk00000000",     "credentialsValue":        "{\\"client\\":{ \\"endpoint\\":\\"LwRpk00000000\\", \\"securityConfigClientMode\\":\\"RPK\\", \\"key\\":\\"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEUEBxNl/RcYJNm8mk91CyVXoIJiROYDlXcSSqK6e5bDHwOW4ZiN2lNnXalyF0Jxw8MbAytnDMERXyAja5VEMeVQ==\\"   }, \\"bootstrap\\":{ \\"bootstrapServer\\":{ \\"securityMode\\":\\"RPK\\", \\"clientPublicKeyOrId\\":\\"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEUEBxNl/RcYJNm8mk91CyVXoIJiROYDlXcSSqK6e5bDHwOW4ZiN2lNnXalyF0Jxw8MbAytnDMERXyAja5VEMeVQ==\\", \\"clientSecretKey\\":\\"MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgd9GAx7yZW37autew5KZykn4IgRpge/tZSjnudnZJnMahRANCAARQQHE2X9Fxgk2byaT3ULJVeggmJE5gOVdxJKorp7lsMfA5bhmI3aU2ddqXIXQnHDwxsDK2cMwRFfICNrlUQx5V\\"}, \\"lwm2mServer\\":{ \\"securityMode\\":\\"RPK\\", \\"clientPublicKeyOrId\\":\\"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEUEBxNl/RcYJNm8mk91CyVXoIJiROYDlXcSSqK6e5bDHwOW4ZiN2lNnXalyF0Jxw8MbAytnDMERXyAja5VEMeVQ==\\", \\"clientSecretKey\\":\\"MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgd9GAx7yZW37autew5KZykn4IgRpge/tZSjnudnZJnMahRANCAARQQHE2X9Fxgk2byaT3ULJVeggmJE5gOVdxJKorp7lsMfA5bhmI3aU2ddqXIXQnHDwxsDK2cMwRFfICNrlUQx5V\\"}} }"    } } ```  Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Device entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (SaveDeviceWithCredentialsRequest):
    - `device` (Device)
    - `credentials` (DeviceCredentials)
    """
    try:
        client = get_client()
        result = client.save_device_with_credentials(body=deserialize_param(body_json, 'SaveDeviceWithCredentialsRequest'), entity_group_id=entity_group_id, entity_group_ids=entity_group_ids)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_device_with_credentials'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def update_device_credentials(body_json: str = None) -> str:
    """
    Update device credentials (updateDeviceCredentials)  # noqa: E501

During device creation, platform generates random 'ACCESS_TOKEN' credentials. Use this method to update the device credentials. First use 'getDeviceCredentialsByDeviceId' to get the credentials id and value. Then use current method to update the credentials type and value. It is not possible to create multiple device credentials for the same device. The structure of device credentials id and value is simple for the 'ACCESS_TOKEN' but is much more complex for the 'MQTT_BASIC' or 'LWM2M_CREDENTIALS'. You may find the example of device with different type of credentials below:   - Credentials type: <b>"Access token"</b> with <b>device ID</b> and with <b>device ID</b> below:   ```json {   "id": {     "id":"c886a090-168d-11ee-87c9-6f157dbc816a"    },   "deviceId": {     "id":"c5fb3ac0-168d-11ee-87c9-6f157dbc816a",     "entityType":"DEVICE"    },   "credentialsType": "ACCESS_TOKEN",   "credentialsId": "6hmxew8pmmzng4e3une4" } ```  - Credentials type: <b>"X509"</b> with <b>device profile ID</b> below:   Note: <b>credentialsId</b> -  format <b>Sha3Hash</b>, <b>certificateValue</b> - format <b>PEM</b> (with "--BEGIN CERTIFICATE----" and  -"----END CERTIFICATE-").  ```json {   "id": {     "id":"309bd9c0-14f4-11ee-9fc9-d9b7463abb63"    },   "deviceId": {     "id":"3092b200-14f4-11ee-9fc9-d9b7463abb63",     "entityType":"DEVICE"    },   "credentialsType": "X509_CERTIFICATE",   "credentialsId": "6b8adb49015500e51a527acd332b51684ab9b49b4ade03a9582a44c455e2e9b6",   "credentialsValue": "-----BEGIN CERTIFICATE----- MIICMTCCAdegAwIBAgIUUEKxS9hTz4l+oLUMF0LV6TC/gCIwCgYIKoZIzj0EAwIwbjELMAkGA1UEBhMCVVMxETAPBgNVBAgMCE5ldyBZb3JrMRowGAYDVQQKDBFUaGluZ3NCb2FyZCwgSW5jLjEwMC4GA1UEAwwnZGV2aWNlUHJvZmlsZUNlcnRAWDUwOVByb3Zpc2lvblN0cmF0ZWd5MB4XDTIzMDMyOTE0NTczNloXDTI0MDMyODE0NTczNlowbjELMAkGA1UEBhMCVVMxETAPBgNVBAgMCE5ldyBZb3JrMRowGAYDVQQKDBFUaGluZ3NCb2FyZCwgSW5jLjEwMC4GA1UEAwwnZGV2aWNlUHJvZmlsZUNlcnRAWDUwOVByb3Zpc2lvblN0cmF0ZWd5MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAECMlWO72krDoUL9FQjUmSCetkhaEGJUfQkdSfkLSNa0GyAEIMbfmzI4zITeapunu4rGet3EMyLydQzuQanBicp6NTMFEwHQYDVR0OBBYEFHpZ78tPnztNii4Da/yCw6mhEIL3MB8GA1UdIwQYMBaAFHpZ78tPnztNii4Da/yCw6mhEIL3MA8GA1UdEwEB/wQFMAMBAf8wCgYIKoZIzj0EAwIDSAAwRQIgJ7qyMFqNcwSYkH6o+UlQXzLWfwZbNjVk+aR7foAZNGsCIQDsd7v3WQIGHiArfZeDs1DLEDuV/2h6L+ZNoGNhEKL+1A== -----END CERTIFICATE-----" } ```  - Credentials type: <b>"MQTT_BASIC"</b> with <b>device profile ID</b> below:   ```json {   "id": {     "id":"d877ffb0-14f5-11ee-9fc9-d9b7463abb63"    },   "deviceId": {     "id":"d875dcd0-14f5-11ee-9fc9-d9b7463abb63",     "entityType":"DEVICE"    },   "credentialsType": "MQTT_BASIC",   "credentialsValue": "{\\"clientId\\":\\"juy03yv4owqxcmqhqtvk\\",\\"userName\\":\\"ov19fxca0cyjn7lm7w7u\\",\\"password\\":\\"twy94he114dfi9usyk1o\\"}" } ```  - You may find the example of <b>LwM2M</b> device and <b>RPK</b> credentials below:   Note: LwM2M device - only existing device profile ID (Transport configuration -> Transport type: "LWM2M".  ```json {   "id": {     "id":"e238d4d0-1689-11ee-98c6-1713c1be5a8e"    },   "deviceId": {     "id":"e232e160-1689-11ee-98c6-1713c1be5a8e",     "entityType":"DEVICE"    },   "credentialsType": "LWM2M_CREDENTIALS",   "credentialsId": "LwRpk00000000",   "credentialsValue":        "{\\"client\\":{ \\"endpoint\\":\\"LwRpk00000000\\", \\"securityConfigClientMode\\":\\"RPK\\", \\"key\\":\\"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEdvBZZ2vQRK9wgDhctj6B1c7bxR3Z0wYg1+YdoYFnVUKWb+rIfTTyYK9tmQJx5Vlb5fxdLnVv1RJOPiwsLIQbAA==\\"   }, \\"bootstrap\\":{ \\"bootstrapServer\\":{ \\"securityMode\\":\\"RPK\\", \\"clientPublicKeyOrId\\":\\"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEUEBxNl/RcYJNm8mk91CyVXoIJiROYDlXcSSqK6e5bDHwOW4ZiN2lNnXalyF0Jxw8MbAytnDMERXyAja5VEMeVQ==\\", \\"clientSecretKey\\":\\"MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgd9GAx7yZW37autew5KZykn4IgRpge/tZSjnudnZJnMahRANCAARQQHE2X9Fxgk2byaT3ULJVeggmJE5gOVdxJKorp7lsMfA5bhmI3aU2ddqXIXQnHDwxsDK2cMwRFfICNrlUQx5V\\"}, \\"lwm2mServer\\":{ \\"securityMode\\":\\"RPK\\", \\"clientPublicKeyOrId\\":\\"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEUEBxNl/RcYJNm8mk91CyVXoIJiROYDlXcSSqK6e5bDHwOW4ZiN2lNnXalyF0Jxw8MbAytnDMERXyAja5VEMeVQ==\\", \\"clientSecretKey\\":\\"MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgd9GAx7yZW37autew5KZykn4IgRpge/tZSjnudnZJnMahRANCAARQQHE2X9Fxgk2byaT3ULJVeggmJE5gOVdxJKorp7lsMfA5bhmI3aU2ddqXIXQnHDwxsDK2cMwRFfICNrlUQx5V\\"}} }" } ```  Update to real value:  - 'id' (this is id of Device Credentials ->  "Get Device Credentials (getDeviceCredentialsByDeviceId)",  - 'deviceId.id' (this is id of Device). Remove 'tenantId' and optionally 'customerId' from the request body example (below) to create new Device entity.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_device_credentials(body=deserialize_param(body_json, 'DeviceCredentials'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_device_credentials'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( assign_device_to_tenant )
    mcp.tool()( count_by_device_group_and_empty_ota_package )
    mcp.tool()( count_by_device_profile_and_empty_ota_package )
    mcp.tool()( delete_device )
    mcp.tool()( find_by_query_v1 )
    mcp.tool()( get_all_device_infos )
    mcp.tool()( get_customer_device_infos )
    mcp.tool()( get_customer_devices )
    mcp.tool()( get_device_by_id )
    mcp.tool()( get_device_credentials_by_device_id )
    mcp.tool()( get_device_info_by_id )
    mcp.tool()( get_device_types )
    mcp.tool()( get_devices_by_entity_group_id )
    mcp.tool()( get_devices_by_ids )
    mcp.tool()( get_tenant_device )
    mcp.tool()( get_tenant_devices )
    mcp.tool()( get_user_devices )
    mcp.tool()( process_devices_bulk_import )
    mcp.tool()( re_claim_device )
    mcp.tool()( save_device )
    mcp.tool()( save_device_with_credentials )
    mcp.tool()( update_device_credentials )
