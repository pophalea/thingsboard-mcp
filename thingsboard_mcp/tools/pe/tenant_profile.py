import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_tenant_profile(tenant_profile_id_json: str) -> str:
    """
    Delete Tenant Profile (deleteTenantProfile)  # noqa: E501

Deletes the tenant profile. Referencing non-existing tenant profile Id will cause an error. Referencing profile that is used by the tenants will cause an error.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_tenant_profile(tenant_profile_id=deserialize_param(tenant_profile_id_json, 'TenantProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_tenant_profile'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_default_tenant_profile_info() -> str:
    """
    Get default Tenant Profile Info (getDefaultTenantProfileInfo)  # noqa: E501

Fetch the default Tenant Profile Info object based. Tenant Profile Info is a lightweight object that contains only id and name of the profile.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_default_tenant_profile_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_default_tenant_profile_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_profile_by_id(tenant_profile_id_json: str) -> str:
    """
    Get Tenant Profile (getTenantProfileById)  # noqa: E501

Fetch the Tenant Profile object based on the provided Tenant Profile Id.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_profile_by_id(tenant_profile_id=deserialize_param(tenant_profile_id_json, 'TenantProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_profile_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_profile_info_by_id(tenant_profile_id_json: str) -> str:
    """
    Get Tenant Profile Info (getTenantProfileInfoById)  # noqa: E501

Fetch the Tenant Profile Info object based on the provided Tenant Profile Id. Tenant Profile Info is a lightweight object that contains only id and name of the profile.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_profile_info_by_id(tenant_profile_id=deserialize_param(tenant_profile_id_json, 'TenantProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_profile_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_profile_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Profiles Info (getTenantProfileInfos)  # noqa: E501

Returns a page of tenant profile info objects registered in the platform. Tenant Profile Info is a lightweight object that contains only id and name of the profile. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_profile_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_profile_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_profiles(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Profiles (getTenantProfiles)  # noqa: E501

Returns a page of tenant profiles registered in the platform. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_profiles(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_profiles'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_profiles_by_ids(ids_json: str) -> str:
    """
    getTenantProfilesByIds  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_profiles_by_ids(ids=json.loads(ids_json) if ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_profiles_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_tenant_profile(body_json: str = None) -> str:
    """
    Create Or update Tenant Profile (saveTenantProfile)  # noqa: E501

Create or update the Tenant Profile. When creating tenant profile, platform generates Tenant Profile Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Tenant Profile Id will be present in the response. Specify existing Tenant Profile Id id to update the Tenant Profile. Referencing non-existing Tenant Profile Id will cause 'Not Found' error.   Update of the tenant profile configuration will cause immediate recalculation of API limits for all affected Tenants.   The **'profileData'** object is the part of Tenant Profile that defines API limits and Rate limits.   You have an ability to define maximum number of devices ('maxDevice'), assets ('maxAssets') and other entities. You may also define maximum number of messages to be processed per month ('maxTransportMessages', 'maxREExecutions', etc). The '*RateLimit' defines the rate limits using simple syntax. For example, '1000:1,20000:60' means up to 1000 events per second but no more than 20000 event per minute. Let's review the example of tenant profile data below:   ```json {   "name": "Default",   "description": "Default tenant profile",   "isolatedTbRuleEngine": false,   "profileData": {     "configuration": {       "type": "DEFAULT",       "maxDevices": 0,       "maxAssets": 0,       "maxCustomers": 0,       "maxUsers": 0,       "maxDashboards": 0,       "maxRuleChains": 0,       "maxResourcesInBytes": 0,       "maxOtaPackagesInBytes": 0,       "maxResourceSize": 0,       "transportTenantMsgRateLimit": "1000:1,20000:60",       "transportTenantTelemetryMsgRateLimit": "1000:1,20000:60",       "transportTenantTelemetryDataPointsRateLimit": "1000:1,20000:60",       "transportDeviceMsgRateLimit": "20:1,600:60",       "transportDeviceTelemetryMsgRateLimit": "20:1,600:60",       "transportDeviceTelemetryDataPointsRateLimit": "20:1,600:60",       "maxTransportMessages": 10000000,       "maxTransportDataPoints": 10000000,       "maxREExecutions": 4000000,       "maxJSExecutions": 5000000,       "maxDPStorageDays": 0,       "maxRuleNodeExecutionsPerMessage": 50,       "maxEmails": 0,       "maxSms": 0,       "maxCreatedAlarms": 1000,       "defaultStorageTtlDays": 0,       "alarmsTtlDays": 0,       "rpcTtlDays": 0,       "queueStatsTtlDays": 0,       "ruleEngineExceptionsTtlDays": 0,       "warnThreshold": 0     }   },   "default": true } ```Remove 'id', from the request body example (below) to create new Tenant Profile entity.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_tenant_profile(body=deserialize_param(body_json, 'TenantProfile'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_tenant_profile'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def set_default_tenant_profile(tenant_profile_id_json: str) -> str:
    """
    Make tenant profile default (setDefaultTenantProfile)  # noqa: E501

Makes specified tenant profile to be default. Referencing non-existing tenant profile Id will cause an error.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.set_default_tenant_profile(tenant_profile_id=deserialize_param(tenant_profile_id_json, 'TenantProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'set_default_tenant_profile'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_tenant_profile )
    mcp.tool()( get_default_tenant_profile_info )
    mcp.tool()( get_tenant_profile_by_id )
    mcp.tool()( get_tenant_profile_info_by_id )
    mcp.tool()( get_tenant_profile_infos )
    mcp.tool()( get_tenant_profiles )
    mcp.tool()( get_tenant_profiles_by_ids )
    mcp.tool()( save_tenant_profile )
    mcp.tool()( set_default_tenant_profile )
