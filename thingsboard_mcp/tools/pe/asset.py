import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_asset(asset_id_json: str) -> str:
    """
    Delete asset (deleteAsset)  # noqa: E501

Deletes the asset and all the relations (from and to the asset). Referencing non-existing asset Id will cause an error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_asset(asset_id=deserialize_param(asset_id_json, 'AssetId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_asset'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def find_by_query(body_json: str = None) -> str:
    """
    Find related assets (findByQuery)  # noqa: E501

Returns all assets that are related to the specific entity. The entity id, relation type, asset types, depth of the search, and other query parameters defined using complex 'AssetSearchQuery' object. See 'Model' tab of the Parameters for more info.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
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


def get_all_asset_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, include_customers: Optional[bool] = None, asset_profile_id_json: str = None) -> str:
    """
    Get All Asset Infos for current user (getAllAssetInfos)  # noqa: E501

Returns a page of asset info objects owned by the tenant or the customer of a current user. Asset Info is an extension of the default Asset object that contains information about the owner name.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_all_asset_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, include_customers=include_customers, asset_profile_id=deserialize_param(asset_profile_id_json, 'AssetProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_all_asset_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_asset_by_id(asset_id_json: str) -> str:
    """
    Get Asset (getAssetById)  # noqa: E501

Fetch the Asset object based on the provided Asset Id. If the user has the authority of 'Tenant Administrator', the server checks that the asset is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the asset is assigned to the same customer.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_asset_by_id(asset_id=deserialize_param(asset_id_json, 'AssetId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_asset_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_asset_info_by_id(asset_id_json: str) -> str:
    """
    Get Asset Info (getAssetInfoById)  # noqa: E501

Fetch the Asset Info object based on the provided Asset Id. If the user has the authority of 'Tenant Administrator', the server checks that the asset is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the asset is assigned to the same customer.Asset Info is an extension of the default Asset object that contains information about the owner name.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_asset_info_by_id(asset_id=deserialize_param(asset_id_json, 'AssetId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_asset_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_asset_types() -> str:
    """
    Get Asset Types (getAssetTypes)  # noqa: E501

Deprecated. See 'getAssetProfileNames' API from Asset Profile Controller instead.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_asset_types()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_asset_types'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_assets_by_entity_group_id(entity_group_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get assets by Entity Group Id (getAssetsByEntityGroupId)  # noqa: E501

Returns a page of asset objects that belongs to specified Entity Group Id. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.    Security check is performed to verify that the user has 'READ' permission for specified group.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_assets_by_entity_group_id(entity_group_id=deserialize_param(entity_group_id_json, 'EntityGroupId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_assets_by_entity_group_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_assets_by_ids(asset_ids_json: str) -> str:
    """
    Get Assets By Ids (getAssetsByIds)  # noqa: E501

Requested assets must be owned by tenant or assigned to customer which user is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_assets_by_ids(asset_ids=json.loads(asset_ids_json) if asset_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_assets_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_customer_asset_infos(customer_id_json: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, asset_profile_id_json: str = None) -> str:
    """
    Get Customer Asset Infos (getCustomerAssetInfos)  # noqa: E501

Returns a page of asset info objects owned by the specified customer. Asset Info is an extension of the default Asset object that contains information about the owner name.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_customer_asset_infos(customer_id=deserialize_param(customer_id_json, 'CustomerId'), page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order, asset_profile_id=deserialize_param(asset_profile_id_json, 'AssetProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_customer_asset_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_customer_assets(customer_id_json: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Customer Assets (getCustomerAssets)  # noqa: E501

Returns a page of assets objects owned by customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_customer_assets(customer_id=deserialize_param(customer_id_json, 'CustomerId'), page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_customer_assets'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_asset(asset_name: str) -> str:
    """
    Get Tenant Asset (getTenantAsset)  # noqa: E501

Requested asset must be owned by tenant that the user belongs to. Asset name is an unique property of asset. So it can be used to identify the asset.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_asset(asset_name=asset_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_asset'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_assets(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Assets (getTenantAssets)  # noqa: E501

Returns a page of assets owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_assets(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_assets'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_user_assets(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, asset_profile_id_json: str = None) -> str:
    """
    Get Assets (getUserAssets)  # noqa: E501

Returns a page of assets objects available for the current user. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. Asset Info is an extension of the default Asset object that contains information about the owner name.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_user_assets(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order, asset_profile_id=deserialize_param(asset_profile_id_json, 'AssetProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_user_assets'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def process_asset_bulk_import(body_json: str = None) -> str:
    """
    Import the bulk of assets (processAssetsBulkImport)  # noqa: E501

There's an ability to import the bulk of assets using the only .csv file.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.process_asset_bulk_import(body=deserialize_param(body_json, 'BulkImportRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'process_asset_bulk_import'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_asset(body_json: str = None, entity_group_id_json: str = None, entity_group_ids: Optional[str] = None) -> str:
    """
    Create Or Update Asset (saveAsset)  # noqa: E501

Creates or Updates the Asset. When creating asset, platform generates Asset Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Asset id will be present in the response. Specify existing Asset id to update the asset. Referencing non-existing Asset Id will cause 'Not Found' error. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Asset entity.    Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_asset(body=deserialize_param(body_json, 'Asset'), entity_group_id=deserialize_param(entity_group_id_json, 'EntityGroupId'), entity_group_ids=entity_group_ids)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_asset'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_asset )
    mcp.tool()( find_by_query )
    mcp.tool()( get_all_asset_infos )
    mcp.tool()( get_asset_by_id )
    mcp.tool()( get_asset_info_by_id )
    mcp.tool()( get_asset_types )
    mcp.tool()( get_assets_by_entity_group_id )
    mcp.tool()( get_assets_by_ids )
    mcp.tool()( get_customer_asset_infos )
    mcp.tool()( get_customer_assets )
    mcp.tool()( get_tenant_asset )
    mcp.tool()( get_tenant_assets )
    mcp.tool()( get_user_assets )
    mcp.tool()( process_asset_bulk_import )
    mcp.tool()( save_asset )
