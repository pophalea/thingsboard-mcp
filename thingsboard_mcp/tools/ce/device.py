import json
import tb_rest_client.models.models_ce as models
from ...shared import get_client, deserialize_param, format_response, ApiException


def assign_device_to_customer(customer_id_json: str, device_id_json: str) -> str:
    """
    Assign device to customer (assignDeviceToCustomer)  # noqa: E501

Creates assignment of the device to customer. Customer will be able to query device afterwards.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_device_to_customer(customer_id=deserialize_param(customer_id_json, 'CustomerId'), device_id=deserialize_param(device_id_json, 'DeviceId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_device_to_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def assign_device_to_edge(edge_id_json: str, device_id_json: str) -> str:
    """
    Assign device to edge (assignDeviceToEdge)  # noqa: E501

Creates assignment of an existing device to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment device (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once device will be delivered to edge service, it's going to be available for usage on remote edge instance.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_device_to_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), device_id=deserialize_param(device_id_json, 'DeviceId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_device_to_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def assign_device_to_public_customer(device_id_json: str) -> str:
    """
    Make device publicly available (assignDeviceToPublicCustomer)  # noqa: E501

Device will be available for non-authorized (not logged-in) users. This is useful to create dashboards that you plan to share/embed on a publicly available website. However, users that are logged-in and belong to different tenant will not be able to access the device.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_device_to_public_customer(device_id=deserialize_param(device_id_json, 'DeviceId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_device_to_public_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def assign_device_to_tenant(tenant_id_json: str, device_id_json: str) -> str:
    """
    Assign device to tenant (assignDeviceToTenant)  # noqa: E501

Creates assignment of the device to tenant. Thereafter tenant will be able to reassign the device to a customer.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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

def claim_device(device_token: str, body: Optional[str] = None) -> str:
    """
    Save claiming information (claimDevice)  # noqa: E501

Saves the information required for user to claim the device. See more info about claiming in the corresponding 'Claiming devices' platform documentation.  Example of the request payload:   ```json {"secretKey":"value", "durationMs":60000} ```  Note: both 'secretKey' and 'durationMs' is optional parameters. In case the secretKey is not specified, the empty string as a default value is used. In case the durationMs is not specified, the system parameter device.claim.duration is used.  The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.claim_device(device_token=device_token, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'claim_device'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def count_by_device_profile_and_empty_ota_package(ota_package_type: str, device_profile_id_json: str) -> str:
    """
    Count devices by device profile  (countByDeviceProfileAndEmptyOtaPackage)  # noqa: E501

The platform gives an ability to load OTA (over-the-air) packages to devices. It can be done in two different ways: device scope or device profile scope.In the response you will find the number of devices with specified device profile, but without previously defined device scope OTA package. It can be useful when you want to define number of devices that will be affected with future OTA package  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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

Deletes the device, it's credentials and all the relations (from and to the device). Referencing non-existing device Id will cause an error.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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

def delete_device_attributes(device_id_json: str, scope: str, keys: str) -> str:
    """
    Delete device attributes (deleteDeviceAttributes)  # noqa: E501

Delete device attributes using provided Device Id, scope and a list of keys. Referencing a non-existing Device Id will cause an error  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_device_attributes(device_id=deserialize_param(device_id_json, 'DeviceId'), scope=scope, keys=keys)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_device_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_device_profile(device_profile_id_json: str) -> str:
    """
    Delete device profile (deleteDeviceProfile)  # noqa: E501

Deletes the device profile. Referencing non-existing device profile Id will cause an error. Can't delete the device profile if it is referenced by existing devices.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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

def get_customer_device_infos(customer_id_json: str, page_size: int, page: int, type: Optional[str] = None, device_profile_id_json: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, active: Optional[bool] = None) -> str:
    """
    Get Customer Device Infos (getCustomerDeviceInfos)  # noqa: E501

Returns a page of devices info objects assigned to customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. Device Info is an extension of the default Device object that contains information about the assigned customer name and device profile name.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_customer_device_infos(customer_id=deserialize_param(customer_id_json, 'CustomerId'), page_size=page_size, page=page, type=type, device_profile_id=deserialize_param(device_profile_id_json, 'DeviceProfileId'), text_search=text_search, sort_property=sort_property, sort_order=sort_order, active=active)
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

Returns a page of devices objects assigned to customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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

def get_device_attributes(device_token: str, client_keys: str, shared_keys: str) -> str:
    """
    Get attributes (getDeviceAttributes)  # noqa: E501

Returns all attributes that belong to device. Use optional 'clientKeys' and/or 'sharedKeys' parameter to return specific attributes.   Example of the result:   ```json {  "stringKey":"value1",   "booleanKey":true,   "doubleKey":42.0,   "longKey":73,   "jsonKey": {     "someNumber": 42,     "someArray": [1,2,3],     "someNestedObject": {"key": "value"}  } } ```  The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_device_attributes(device_token=device_token, client_keys=client_keys, shared_keys=shared_keys)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_device_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_device_by_id(device_id_json: str) -> str:
    """
    Get Device (getDeviceById)  # noqa: E501

Fetch the Device object based on the provided Device Id. If the user has the authority of 'TENANT_ADMIN', the server checks that the device is owned by the same tenant. If the user has the authority of 'CUSTOMER_USER', the server checks that the device is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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

If during device creation there wasn't specified any credentials, platform generates random 'ACCESS_TOKEN' credentials.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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
    Get Device Info (getDeviceInfoById)  # noqa: E501

Fetch the Device Info object based on the provided Device Id. If the user has the authority of 'Tenant Administrator', the server checks that the device is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the device is assigned to the same customer. Device Info is an extension of the default Device object that contains information about the assigned customer name and device profile name.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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

def get_device_profile_by_id(device_profile_id_json: str, inline_images: Optional[bool] = None) -> str:
    """
    Get Device Profile (getDeviceProfileById)  # noqa: E501

Fetch the Device Profile object based on the provided Device Profile Id. The server checks that the device profile is owned by the same tenant.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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

def get_device_publish_telemetry_commands(device_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_device_publish_telemetry_commands(device_id=deserialize_param(device_id_json, 'DeviceId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_device_publish_telemetry_commands'."
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

def get_devices_by_ids(device_ids_json: str) -> str:
    """
    Get Devices By Ids (getDevicesByIds)  # noqa: E501

Requested devices must be owned by tenant or assigned to customer which user is performing the request.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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

def get_edge_devices(edge_id_json: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, device_profile_id_json: str, active: Optional[bool] = None) -> str:
    """
    Get devices assigned to edge (getEdgeDevices)  # noqa: E501

Returns a page of devices assigned to edge. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_devices(edge_id=deserialize_param(edge_id_json, 'EdgeId'), page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time, device_profile_id=deserialize_param(device_profile_id_json, 'DeviceProfileId'), active=active)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_devices'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_persisted_rpc_by_device(device_id_json: str, page_size: int, page: int, rpc_status: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get persistent RPC requests  # noqa: E501

Allows to query RPC calls for specific device using pagination.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_persisted_rpc_by_device(device_id=deserialize_param(device_id_json, 'DeviceId'), page_size=page_size, page=page, rpc_status=rpc_status, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_persisted_rpc_by_device'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_device(device_name: str) -> str:
    """
    Get Tenant Device (getTenantDevice)  # noqa: E501

Requested device must be owned by tenant that the user belongs to. Device name is an unique property of device. So it can be used to identify the device.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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

def get_tenant_device_infos(page_size: int, page: int, type: Optional[str] = None, device_profile_id_json: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, active: Optional[bool] = None) -> str:
    """
    Get Tenant Device Infos (getTenantDeviceInfos)  # noqa: E501

Returns a page of devices info objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. Device Info is an extension of the default Device object that contains information about the assigned customer name and device profile name.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_device_infos(page_size=page_size, page=page, type=type, device_profile_id=deserialize_param(device_profile_id_json, 'DeviceProfileId'), text_search=text_search, sort_property=sort_property, sort_order=sort_order, active=active)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_device_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_tenant_devices(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Devices (getTenantDevices)  # noqa: E501

Returns a page of devices owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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

def handle_one_way_device_rpc_request(device_id_json: str, body: Optional[str] = None) -> str:
    """
    Send one-way RPC request (handleOneWayDeviceRPCRequest)  # noqa: E501

Deprecated. See 'Rpc V 2 Controller' instead.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.handle_one_way_device_rpc_request(device_id=deserialize_param(device_id_json, 'DeviceId'), body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'handle_one_way_device_rpc_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_one_way_device_rpc_request_v1(device_id_json: str, body: Optional[str] = None) -> str:
    """
    Send one-way RPC request  # noqa: E501

Sends the one-way remote-procedure call (RPC) request to device. Sends the one-way remote-procedure call (RPC) request to device. The RPC call is A JSON that contains the method name ('method'), parameters ('params') and multiple optional fields. See example below. We will review the properties of the RPC call one-by-one below.   ```json {   "method": "setGpio",   "params": {     "pin": 7,     "value": 1   },   "persistent": false,   "timeout": 5000 } ```  ### Server-side RPC structure  The body of server-side RPC request consists of multiple fields:  * **method** - mandatory, name of the method to distinct the RPC calls.   For example, "getCurrentTime" or "getWeatherForecast". The value of the parameter is a string. * **params** - mandatory, parameters used for processing of the request. The value is a JSON. Leave empty JSON "{}" if no parameters needed. * **timeout** - optional, value of the processing timeout in milliseconds. The default value is 10000 (10 seconds). The minimum value is 5000 (5 seconds). * **expirationTime** - optional, value of the epoch time (in milliseconds, UTC timezone). Overrides **timeout** if present. * **persistent** - optional, indicates persistent RPC. The default value is "false". * **retries** - optional, defines how many times persistent RPC will be re-sent in case of failures on the network and/or device side. * **additionalInfo** - optional, defines metadata for the persistent RPC that will be added to the persistent RPC events.  ### RPC Result In case of persistent RPC, the result of this call is 'rpcId' UUID. In case of lightweight RPC, the result of this call is either 200 OK if the message was sent to device, or 504 Gateway Timeout if device is offline.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.handle_one_way_device_rpc_request_v1(device_id=deserialize_param(device_id_json, 'DeviceId'), body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'handle_one_way_device_rpc_request_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_two_way_device_rpc_request(device_id_json: str, body_json: str = None) -> str:
    """
    Send two-way RPC request (handleTwoWayDeviceRPCRequest)  # noqa: E501

Deprecated. See 'Rpc V 2 Controller' instead.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.handle_two_way_device_rpc_request(device_id=deserialize_param(device_id_json, 'DeviceId'), body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'handle_two_way_device_rpc_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_two_way_device_rpc_request_v1(device_id_json: str, body: Optional[str] = None) -> str:
    """
    Send two-way RPC request  # noqa: E501

Sends the two-way remote-procedure call (RPC) request to device. Sends the one-way remote-procedure call (RPC) request to device. The RPC call is A JSON that contains the method name ('method'), parameters ('params') and multiple optional fields. See example below. We will review the properties of the RPC call one-by-one below.   ```json {   "method": "setGpio",   "params": {     "pin": 7,     "value": 1   },   "persistent": false,   "timeout": 5000 } ```  ### Server-side RPC structure  The body of server-side RPC request consists of multiple fields:  * **method** - mandatory, name of the method to distinct the RPC calls.   For example, "getCurrentTime" or "getWeatherForecast". The value of the parameter is a string. * **params** - mandatory, parameters used for processing of the request. The value is a JSON. Leave empty JSON "{}" if no parameters needed. * **timeout** - optional, value of the processing timeout in milliseconds. The default value is 10000 (10 seconds). The minimum value is 5000 (5 seconds). * **expirationTime** - optional, value of the epoch time (in milliseconds, UTC timezone). Overrides **timeout** if present. * **persistent** - optional, indicates persistent RPC. The default value is "false". * **retries** - optional, defines how many times persistent RPC will be re-sent in case of failures on the network and/or device side. * **additionalInfo** - optional, defines metadata for the persistent RPC that will be added to the persistent RPC events.  ### RPC Result In case of persistent RPC, the result of this call is 'rpcId' UUID. In case of lightweight RPC, the result of this call is the response from device, or 504 Gateway Timeout if device is offline.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.handle_two_way_device_rpc_request_v1(device_id=deserialize_param(device_id_json, 'DeviceId'), body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'handle_two_way_device_rpc_request_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def post_device_attributes(device_token: str, body: Optional[str] = None) -> str:
    """
    Post attributes (postDeviceAttributes)  # noqa: E501

Post client attribute updates on behalf of device.   Example of the request:   ```json {  "stringKey":"value1",   "booleanKey":true,   "doubleKey":42.0,   "longKey":73,   "jsonKey": {     "someNumber": 42,     "someArray": [1,2,3],     "someNestedObject": {"key": "value"}  } } ```  The API call is designed to be used by device firmware and requires device access token ('deviceToken'). It is not recommended to use this API call by third-party scripts, rule-engine or platform widgets (use 'Telemetry Controller' instead).   # noqa: E501
    """
    try:
        client = get_client()
        result = client.post_device_attributes(device_token=device_token, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'post_device_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def process_devices_bulk_import(body_json: str) -> str:
    """
    Import the bulk of devices (processDevicesBulkImport)  # noqa: E501

There's an ability to import the bulk of devices using the only .csv file.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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

def provision_device(body: Optional[str] = None) -> str:
    """
    Provision new device (provisionDevice)  # noqa: E501

Exchange the provision request to the device credentials. See more info about provisioning in the corresponding 'Device provisioning' platform documentation.Requires valid JSON request with the following format:   ```json {   "deviceName": "NEW_DEVICE_NAME",   "provisionDeviceKey": "u7piawkboq8v32dmcmpp",   "provisionDeviceSecret": "jpmwdn8ptlswmf4m29bw" } ```  Where 'deviceName' is the name of enw or existing device which depends on the provisioning strategy. The 'provisionDeviceKey' and 'provisionDeviceSecret' matches info configured in one of the existing device profiles. The result of the successful call is the JSON object that contains new credentials:  ```json {   "credentialsType":"ACCESS_TOKEN",   "credentialsValue":"DEVICE_ACCESS_TOKEN",   "status":"SUCCESS" } ```    # noqa: E501
    """
    try:
        client = get_client()
        result = client.provision_device(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'provision_device'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def re_claim_device(device_name: str) -> str:
    """
    Reclaim device (reClaimDevice)  # noqa: E501

Reclaiming means the device will be unassigned from the customer and the device will be available for claiming again.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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

Create or update the Device. When creating device, platform generates Device Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). Device credentials are also generated if not provided in the 'accessToken' request parameter. The newly created device id will be present in the response. Specify existing Device id to update the device. Referencing non-existing device Id will cause 'Not Found' error.  Device name is unique in the scope of tenant. Use unique identifiers like MAC or IMEI for the device names and non-unique 'label' field for user-friendly visualization purposes.Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Device entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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

def save_device_attributes(device_id_json: str, scope: str, body_json: str = None) -> str:
    """
    Save device attributes (saveDeviceAttributes)  # noqa: E501

Creates or updates the device attributes based on device id and specified attribute scope. The request payload is a JSON object with key-value format of attributes to create or update. For example:  ```json {  "stringKey":"value1",   "booleanKey":true,   "doubleKey":42.0,   "longKey":73,   "jsonKey": {     "someNumber": 42,     "someArray": [1,2,3],     "someNestedObject": {"key": "value"}  } } ```   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_device_attributes(device_id=deserialize_param(device_id_json, 'DeviceId'), scope=scope, body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_device_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_device_profile(body_json: str) -> str:
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

def save_device_with_credentials(body_json: str) -> str:
    """
    Create Device (saveDevice) with credentials   # noqa: E501

Create or update the Device. When creating device, platform generates Device Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). Requires to provide the Device Credentials object as well as an existing device profile ID or use "default". You may find the example of device with different type of credentials below:   - Credentials type: <b>"Access token"</b> with <b>device profile ID</b> below:   ```json {   "device": {     "name":"Name_DeviceWithCredantial_AccessToken",     "label":"Label_DeviceWithCredantial_AccessToken",     "deviceProfileId":{       "id":"9d9588c0-06c9-11ee-b618-19be30fdeb60",       "entityType":"DEVICE_PROFILE"      }    },   "credentials": {     "credentialsType": "ACCESS_TOKEN",     "credentialsId": "6hmxew8pmmzng4e3une2"    } } ```  - Credentials type: <b>"Access token"</b> with  <b>device profile default</b> below:   ```json {   "device": {     "name":"Name_DeviceWithCredantial_AccessToken_Default",     "label":"Label_DeviceWithCredantial_AccessToken_Default",     "type": "default"    },   "credentials": {     "credentialsType": "ACCESS_TOKEN",     "credentialsId": "6hmxew8pmmzng4e3une3"    } } ```  - Credentials type: <b>"X509"</b> with <b>device profile ID</b> below:   Note: <b>credentialsId</b> -  format <b>Sha3Hash</b>, <b>certificateValue</b> - format <b>PEM</b> (with "--BEGIN CERTIFICATE----" and  -"----END CERTIFICATE-").  ```json {   "device": {     "name":"Name_DeviceWithCredantial_X509_Certificate",     "label":"Label_DeviceWithCredantial_X509_Certificate",     "deviceProfileId":{       "id":"9d9588c0-06c9-11ee-b618-19be30fdeb60",       "entityType":"DEVICE_PROFILE"      }    },   "credentials": {     "credentialsType": "X509_CERTIFICATE",     "credentialsId": "84f5911765abba1f96bf4165604e9e90338fc6214081a8e623b6ff9669aedb27",     "credentialsValue": "-----BEGIN CERTIFICATE----- MIICMTCCAdegAwIBAgIUI9dBuwN6pTtK6uZ03rkiCwV4wEYwCgYIKoZIzj0EAwIwbjELMAkGA1UEBhMCVVMxETAPBgNVBAgMCE5ldyBZb3JrMRowGAYDVQQKDBFUaGluZ3NCb2FyZCwgSW5jLjEwMC4GA1UEAwwnZGV2aWNlQ2VydGlmaWNhdGVAWDUwOVByb3Zpc2lvblN0cmF0ZWd5MB4XDTIzMDMyOTE0NTYxN1oXDTI0MDMyODE0NTYxN1owbjELMAkGA1UEBhMCVVMxETAPBgNVBAgMCE5ldyBZb3JrMRowGAYDVQQKDBFUaGluZ3NCb2FyZCwgSW5jLjEwMC4GA1UEAwwnZGV2aWNlQ2VydGlmaWNhdGVAWDUwOVByb3Zpc2lvblN0cmF0ZWd5MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9Zo791qKQiGNBm11r4ZGxh+w+ossZL3xc46ufq5QckQHP7zkD2XDAcmP5GvdkM1sBFN9AWaCkQfNnWmfERsOOKNTMFEwHQYDVR0OBBYEFFFc5uyCyglQoZiKhzXzMcQ3BKORMB8GA1UdIwQYMBaAFFFc5uyCyglQoZiKhzXzMcQ3BKORMA8GA1UdEwEB/wQFMAMBAf8wCgYIKoZIzj0EAwIDSAAwRQIhANbA9CuhoOifZMMmqkpuld+65CR+ItKdXeRAhLMZuccuAiB0FSQB34zMutXrZj1g8Gl5OkE7YryFHbei1z0SveHR8g== -----END CERTIFICATE-----"    } } ```  - Credentials type: <b>"MQTT_BASIC"</b> with <b>device profile ID</b> below:   ```json {   "device": {     "name":"Name_DeviceWithCredantial_MQTT_Basic",     "label":"Label_DeviceWithCredantial_MQTT_Basic",     "deviceProfileId":{       "id":"9d9588c0-06c9-11ee-b618-19be30fdeb60",       "entityType":"DEVICE_PROFILE"      }    },   "credentials": {     "credentialsType": "MQTT_BASIC",     "credentialsValue": "{\\"clientId\\":\\"5euh5nzm34bjjh1efmlt\\",\\"userName\\":\\"onasd1lgwasmjl7v2v7h\\",\\"password\\":\\"b9xtm4ny8kt9zewaga5o\\"}"    } } ```  - You may find the example of <b>LwM2M</b> device and <b>RPK</b> credentials below:   Note: LwM2M device - only existing device profile ID (Transport configuration -> Transport type: "LWM2M".  ```json {   "device": {     "name":"Name_LwRpk00000000",     "label":"Label_LwRpk00000000",     "deviceProfileId":{       "id":"a660bd50-10ef-11ee-8737-b5634e73c779",       "entityType":"DEVICE_PROFILE"      }    },   "credentials": {     "credentialsType": "LWM2M_CREDENTIALS",     "credentialsId": "LwRpk00000000",     "credentialsValue":        "{\\"client\\":{ \\"endpoint\\":\\"LwRpk00000000\\", \\"securityConfigClientMode\\":\\"RPK\\", \\"key\\":\\"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEUEBxNl/RcYJNm8mk91CyVXoIJiROYDlXcSSqK6e5bDHwOW4ZiN2lNnXalyF0Jxw8MbAytnDMERXyAja5VEMeVQ==\\"   }, \\"bootstrap\\":{ \\"bootstrapServer\\":{ \\"securityMode\\":\\"RPK\\", \\"clientPublicKeyOrId\\":\\"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEUEBxNl/RcYJNm8mk91CyVXoIJiROYDlXcSSqK6e5bDHwOW4ZiN2lNnXalyF0Jxw8MbAytnDMERXyAja5VEMeVQ==\\", \\"clientSecretKey\\":\\"MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgd9GAx7yZW37autew5KZykn4IgRpge/tZSjnudnZJnMahRANCAARQQHE2X9Fxgk2byaT3ULJVeggmJE5gOVdxJKorp7lsMfA5bhmI3aU2ddqXIXQnHDwxsDK2cMwRFfICNrlUQx5V\\"}, \\"lwm2mServer\\":{ \\"securityMode\\":\\"RPK\\", \\"clientPublicKeyOrId\\":\\"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEUEBxNl/RcYJNm8mk91CyVXoIJiROYDlXcSSqK6e5bDHwOW4ZiN2lNnXalyF0Jxw8MbAytnDMERXyAja5VEMeVQ==\\", \\"clientSecretKey\\":\\"MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgd9GAx7yZW37autew5KZykn4IgRpge/tZSjnudnZJnMahRANCAARQQHE2X9Fxgk2byaT3ULJVeggmJE5gOVdxJKorp7lsMfA5bhmI3aU2ddqXIXQnHDwxsDK2cMwRFfICNrlUQx5V\\"}} }"    } } ```  Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Device entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_device_with_credentials(body=deserialize_param(body_json, 'SaveDeviceWithCredentialsRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_device_with_credentials'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def set_default_device_profile(device_profile_id_json: str) -> str:
    """
    Make Device Profile Default (setDefaultDeviceProfile)  # noqa: E501

Marks device profile as default within a tenant scope.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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

def unassign_device_from_customer(device_id_json: str) -> str:
    """
    Unassign device from customer (unassignDeviceFromCustomer)  # noqa: E501

Clears assignment of the device to customer. Customer will not be able to query device afterwards.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.unassign_device_from_customer(device_id=deserialize_param(device_id_json, 'DeviceId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unassign_device_from_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def unassign_device_from_edge(edge_id_json: str, device_id_json: str) -> str:
    """
    Unassign device from edge (unassignDeviceFromEdge)  # noqa: E501

Clears assignment of the device to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove device (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove device locally.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.unassign_device_from_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), device_id=deserialize_param(device_id_json, 'DeviceId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unassign_device_from_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_device_credentials(body_json: str) -> str:
    """
    Update device credentials (updateDeviceCredentials)  # noqa: E501

During device creation, platform generates random 'ACCESS_TOKEN' credentials. " + Use this method to update the device credentials. First use 'getDeviceCredentialsByDeviceId' to get the credentials id and value. Then use current method to update the credentials type and value. It is not possible to create multiple device credentials for the same device. The structure of device credentials id and value is simple for the 'ACCESS_TOKEN' but is much more complex for the 'MQTT_BASIC' or 'LWM2M_CREDENTIALS'. You may find the example of device with different type of credentials below:   - Credentials type: <b>"Access token"</b> with <b>device ID</b> and with <b>device ID</b> below:   ```json {   "id": {     "id":"c886a090-168d-11ee-87c9-6f157dbc816a"    },   "deviceId": {     "id":"c5fb3ac0-168d-11ee-87c9-6f157dbc816a",     "entityType":"DEVICE"    },   "credentialsType": "ACCESS_TOKEN",   "credentialsId": "6hmxew8pmmzng4e3une4" } ```  - Credentials type: <b>"X509"</b> with <b>device profile ID</b> below:   Note: <b>credentialsId</b> -  format <b>Sha3Hash</b>, <b>certificateValue</b> - format <b>PEM</b> (with "--BEGIN CERTIFICATE----" and  -"----END CERTIFICATE-").  ```json {   "id": {     "id":"309bd9c0-14f4-11ee-9fc9-d9b7463abb63"    },   "deviceId": {     "id":"3092b200-14f4-11ee-9fc9-d9b7463abb63",     "entityType":"DEVICE"    },   "credentialsType": "X509_CERTIFICATE",   "credentialsId": "6b8adb49015500e51a527acd332b51684ab9b49b4ade03a9582a44c455e2e9b6",   "credentialsValue": "-----BEGIN CERTIFICATE----- MIICMTCCAdegAwIBAgIUUEKxS9hTz4l+oLUMF0LV6TC/gCIwCgYIKoZIzj0EAwIwbjELMAkGA1UEBhMCVVMxETAPBgNVBAgMCE5ldyBZb3JrMRowGAYDVQQKDBFUaGluZ3NCb2FyZCwgSW5jLjEwMC4GA1UEAwwnZGV2aWNlUHJvZmlsZUNlcnRAWDUwOVByb3Zpc2lvblN0cmF0ZWd5MB4XDTIzMDMyOTE0NTczNloXDTI0MDMyODE0NTczNlowbjELMAkGA1UEBhMCVVMxETAPBgNVBAgMCE5ldyBZb3JrMRowGAYDVQQKDBFUaGluZ3NCb2FyZCwgSW5jLjEwMC4GA1UEAwwnZGV2aWNlUHJvZmlsZUNlcnRAWDUwOVByb3Zpc2lvblN0cmF0ZWd5MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAECMlWO72krDoUL9FQjUmSCetkhaEGJUfQkdSfkLSNa0GyAEIMbfmzI4zITeapunu4rGet3EMyLydQzuQanBicp6NTMFEwHQYDVR0OBBYEFHpZ78tPnztNii4Da/yCw6mhEIL3MB8GA1UdIwQYMBaAFHpZ78tPnztNii4Da/yCw6mhEIL3MA8GA1UdEwEB/wQFMAMBAf8wCgYIKoZIzj0EAwIDSAAwRQIgJ7qyMFqNcwSYkH6o+UlQXzLWfwZbNjVk+aR7foAZNGsCIQDsd7v3WQIGHiArfZeDs1DLEDuV/2h6L+ZNoGNhEKL+1A== -----END CERTIFICATE-----" } ```  - Credentials type: <b>"MQTT_BASIC"</b> with <b>device profile ID</b> below:   ```json {   "id": {     "id":"d877ffb0-14f5-11ee-9fc9-d9b7463abb63"    },   "deviceId": {     "id":"d875dcd0-14f5-11ee-9fc9-d9b7463abb63",     "entityType":"DEVICE"    },   "credentialsType": "MQTT_BASIC",   "credentialsValue": "{\\"clientId\\":\\"juy03yv4owqxcmqhqtvk\\",\\"userName\\":\\"ov19fxca0cyjn7lm7w7u\\",\\"password\\":\\"twy94he114dfi9usyk1o\\"}" } ```  - You may find the example of <b>LwM2M</b> device and <b>RPK</b> credentials below:   Note: LwM2M device - only existing device profile ID (Transport configuration -> Transport type: "LWM2M".  ```json {   "id": {     "id":"e238d4d0-1689-11ee-98c6-1713c1be5a8e"    },   "deviceId": {     "id":"e232e160-1689-11ee-98c6-1713c1be5a8e",     "entityType":"DEVICE"    },   "credentialsType": "LWM2M_CREDENTIALS",   "credentialsId": "LwRpk00000000",   "credentialsValue":        "{\\"client\\":{ \\"endpoint\\":\\"LwRpk00000000\\", \\"securityConfigClientMode\\":\\"RPK\\", \\"key\\":\\"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEdvBZZ2vQRK9wgDhctj6B1c7bxR3Z0wYg1+YdoYFnVUKWb+rIfTTyYK9tmQJx5Vlb5fxdLnVv1RJOPiwsLIQbAA==\\"   }, \\"bootstrap\\":{ \\"bootstrapServer\\":{ \\"securityMode\\":\\"RPK\\", \\"clientPublicKeyOrId\\":\\"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEUEBxNl/RcYJNm8mk91CyVXoIJiROYDlXcSSqK6e5bDHwOW4ZiN2lNnXalyF0Jxw8MbAytnDMERXyAja5VEMeVQ==\\", \\"clientSecretKey\\":\\"MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgd9GAx7yZW37autew5KZykn4IgRpge/tZSjnudnZJnMahRANCAARQQHE2X9Fxgk2byaT3ULJVeggmJE5gOVdxJKorp7lsMfA5bhmI3aU2ddqXIXQnHDwxsDK2cMwRFfICNrlUQx5V\\"}, \\"lwm2mServer\\":{ \\"securityMode\\":\\"RPK\\", \\"clientPublicKeyOrId\\":\\"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEUEBxNl/RcYJNm8mk91CyVXoIJiROYDlXcSSqK6e5bDHwOW4ZiN2lNnXalyF0Jxw8MbAytnDMERXyAja5VEMeVQ==\\", \\"clientSecretKey\\":\\"MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgd9GAx7yZW37autew5KZykn4IgRpge/tZSjnudnZJnMahRANCAARQQHE2X9Fxgk2byaT3ULJVeggmJE5gOVdxJKorp7lsMfA5bhmI3aU2ddqXIXQnHDwxsDK2cMwRFfICNrlUQx5V\\"}} }" } ```  Update to real value:  - 'id' (this is id of Device Credentials ->  "Get Device Credentials (getDeviceCredentialsByDeviceId)",  - 'deviceId.id' (this is id of Device). Remove 'tenantId' and optionally 'customerId' from the request body example (below) to create new Device entity.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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
    mcp.tool()( assign_device_to_customer )
    mcp.tool()( assign_device_to_edge )
    mcp.tool()( assign_device_to_public_customer )
    mcp.tool()( assign_device_to_tenant )
    mcp.tool()( claim_device )
    mcp.tool()( count_by_device_profile_and_empty_ota_package )
    mcp.tool()( delete_device )
    mcp.tool()( delete_device_attributes )
    mcp.tool()( delete_device_profile )
    mcp.tool()( get_customer_device_infos )
    mcp.tool()( get_customer_devices )
    mcp.tool()( get_default_device_profile_info )
    mcp.tool()( get_device_attributes )
    mcp.tool()( get_device_by_id )
    mcp.tool()( get_device_credentials_by_device_id )
    mcp.tool()( get_device_info_by_id )
    mcp.tool()( get_device_profile_by_id )
    mcp.tool()( get_device_profile_info_by_id )
    mcp.tool()( get_device_profile_infos )
    mcp.tool()( get_device_profile_names )
    mcp.tool()( get_device_profiles )
    mcp.tool()( get_device_publish_telemetry_commands )
    mcp.tool()( get_device_types )
    mcp.tool()( get_devices_by_ids )
    mcp.tool()( get_edge_devices )
    mcp.tool()( get_persisted_rpc_by_device )
    mcp.tool()( get_tenant_device )
    mcp.tool()( get_tenant_device_infos )
    mcp.tool()( get_tenant_devices )
    mcp.tool()( handle_one_way_device_rpc_request )
    mcp.tool()( handle_one_way_device_rpc_request_v1 )
    mcp.tool()( handle_two_way_device_rpc_request )
    mcp.tool()( handle_two_way_device_rpc_request_v1 )
    mcp.tool()( post_device_attributes )
    mcp.tool()( process_devices_bulk_import )
    mcp.tool()( provision_device )
    mcp.tool()( re_claim_device )
    mcp.tool()( save_device )
    mcp.tool()( save_device_attributes )
    mcp.tool()( save_device_profile )
    mcp.tool()( save_device_with_credentials )
    mcp.tool()( set_default_device_profile )
    mcp.tool()( unassign_device_from_customer )
    mcp.tool()( unassign_device_from_edge )
    mcp.tool()( update_device_credentials )
