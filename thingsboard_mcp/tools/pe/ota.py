import json
import tb_rest_client.models.models_pe as models
from ...shared import get_client, deserialize_param, format_response, ApiException


def delete_ota_package(ota_package_id_json: str) -> str:
    """
    Delete OTA Package (deleteOtaPackage)  # noqa: E501

Deletes the OTA Package. Referencing non-existing OTA Package Id will cause an error. Can't delete the OTA Package if it is referenced by existing devices or device profile.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_ota_package(ota_package_id=deserialize_param(ota_package_id_json, 'OtaPackageId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_ota_package'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_ota_package(ota_package_id_json: str) -> str:
    """
    Download OTA Package (downloadOtaPackage)  # noqa: E501

Download OTA Package based on the provided OTA Package Id.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_ota_package(ota_package_id=deserialize_param(ota_package_id_json, 'OtaPackageId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_ota_package'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_group_ota_packages(group_id_json: str, type: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get group OTA Package Infos (getGroupOtaPackages)  # noqa: E501

Returns a page of OTA Package Info objects owned by tenant, and by entity group. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. OTA Package Info is a lightweight object that includes main information about the OTA Package excluding the heavyweight data.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_group_ota_packages(group_id=deserialize_param(group_id_json, 'EntityGroupId'), type=type, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_group_ota_packages'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_ota_package_by_id(ota_package_id_json: str) -> str:
    """
    Get OTA Package (getOtaPackageById)  # noqa: E501

Fetch the OTA Package object based on the provided OTA Package Id. The server checks that the OTA Package is owned by the same tenant. OTA Package is a heavyweight object that includes main information about the OTA Package and also data.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_ota_package_by_id(ota_package_id=deserialize_param(ota_package_id_json, 'OtaPackageId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_ota_package_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_ota_package_info_by_id(ota_package_id_json: str) -> str:
    """
    Get OTA Package Info (getOtaPackageInfoById)  # noqa: E501

Fetch the OTA Package Info object based on the provided OTA Package Id. OTA Package Info is a lightweight object that includes main information about the OTA Package excluding the heavyweight data.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_ota_package_info_by_id(ota_package_id=deserialize_param(ota_package_id_json, 'OtaPackageId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_ota_package_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_ota_packages(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get OTA Package Infos (getOtaPackages)  # noqa: E501

Returns a page of OTA Package Info objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. OTA Package Info is a lightweight object that includes main information about the OTA Package excluding the heavyweight data.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_ota_packages(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_ota_packages'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_ota_packages_v1(device_profile_id_json: str, type: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get OTA Package Infos (getOtaPackages)  # noqa: E501

Returns a page of OTA Package Info objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. OTA Package Info is a lightweight object that includes main information about the OTA Package excluding the heavyweight data.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_ota_packages_v1(device_profile_id=deserialize_param(device_profile_id_json, 'DeviceProfileId'), type=type, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_ota_packages_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_ota_package_data(ota_package_id_json: str, checksum_json: str, checksum_algorithm: Optional[str] = None, file_json: str) -> str:
    """
    Save OTA Package data (saveOtaPackageData)  # noqa: E501

Update the OTA Package. Adds the date to the existing OTA Package Info  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_ota_package_data(ota_package_id=deserialize_param(ota_package_id_json, 'OtaPackageId'), checksum=deserialize_param(checksum_json, '_empty'), checksum_algorithm=checksum_algorithm, file=deserialize_param(file_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_ota_package_data'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_ota_package_info(body_json: str) -> str:
    """
    Create Or Update OTA Package Info (saveOtaPackageInfo)  # noqa: E501

Create or update the OTA Package Info. When creating OTA Package Info, platform generates OTA Package id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created OTA Package id will be present in the response. Specify existing OTA Package id to update the OTA Package Info. Referencing non-existing OTA Package Id will cause 'Not Found' error.   OTA Package combination of the title with the version is unique in the scope of tenant.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_ota_package_info(body=deserialize_param(body_json, 'SaveOtaPackageInfoRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_ota_package_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def register(mcp):
    mcp.tool()( delete_ota_package )
    mcp.tool()( download_ota_package )
    mcp.tool()( get_group_ota_packages )
    mcp.tool()( get_ota_package_by_id )
    mcp.tool()( get_ota_package_info_by_id )
    mcp.tool()( get_ota_packages )
    mcp.tool()( get_ota_packages_v1 )
    mcp.tool()( save_ota_package_data )
    mcp.tool()( save_ota_package_info )
