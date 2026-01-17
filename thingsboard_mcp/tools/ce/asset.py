import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def assign_asset_to_customer(customer_id_json: str, asset_id_json: str) -> str:
    """
    Assign asset to customer (assignAssetToCustomer)  # noqa: E501

Creates assignment of the asset to customer. Customer will be able to query asset afterwards.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_asset_to_customer(customer_id=deserialize_param(customer_id_json, 'CustomerId'), asset_id=deserialize_param(asset_id_json, 'AssetId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_asset_to_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def assign_asset_to_edge(edge_id_json: str, asset_id_json: str) -> str:
    """
    Assign asset to edge (assignAssetToEdge)  # noqa: E501

Creates assignment of an existing asset to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment asset (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once asset will be delivered to edge service, it's going to be available for usage on remote edge instance.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_asset_to_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), asset_id=deserialize_param(asset_id_json, 'AssetId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_asset_to_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def assign_asset_to_public_customer(asset_id_json: str) -> str:
    """
    Make asset publicly available (assignAssetToPublicCustomer)  # noqa: E501

Asset will be available for non-authorized (not logged-in) users. This is useful to create dashboards that you plan to share/embed on a publicly available website. However, users that are logged-in and belong to different tenant will not be able to access the asset.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_asset_to_public_customer(asset_id=deserialize_param(asset_id_json, 'AssetId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_asset_to_public_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_asset(asset_id_json: str) -> str:
    """
    Delete asset (deleteAsset)  # noqa: E501

Deletes the asset and all the relations (from and to the asset). Referencing non-existing asset Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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


def get_asset_by_id(asset_id_json: str) -> str:
    """
    Get Asset (getAssetById)  # noqa: E501

Fetch the Asset object based on the provided Asset Id. If the user has the authority of 'Tenant Administrator', the server checks that the asset is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the asset is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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

Fetch the Asset Info object based on the provided Asset Id. If the user has the authority of 'Tenant Administrator', the server checks that the asset is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the asset is assigned to the same customer. Asset Info is an extension of the default Asset object that contains information about the assigned customer name.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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


def get_assets_by_ids(asset_ids_json: str) -> str:
    """
    Get Assets By Ids (getAssetsByIds)  # noqa: E501

Requested assets must be owned by tenant or assigned to customer which user is performing the request.   # noqa: E501
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

Returns a page of assets info objects assigned to customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. Asset Info is an extension of the default Asset object that contains information about the assigned customer name.   # noqa: E501
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

Returns a page of assets objects assigned to customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # noqa: E501
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


def get_edge_assets(edge_id_json: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    Get assets assigned to edge (getEdgeAssets)  # noqa: E501

Returns a page of assets assigned to edge. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_assets(edge_id=deserialize_param(edge_id_json, 'EdgeId'), page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_assets'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_asset(asset_name: str) -> str:
    """
    Get Tenant Asset (getTenantAsset)  # noqa: E501

Requested asset must be owned by tenant that the user belongs to. Asset name is an unique property of asset. So it can be used to identify the asset.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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


def get_tenant_asset_infos(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, asset_profile_id_json: str = None) -> str:
    """
    Get Tenant Asset Infos (getTenantAssetInfos)  # noqa: E501

Returns a page of assets info objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details. Asset Info is an extension of the default Asset object that contains information about the assigned customer name.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_asset_infos(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order, asset_profile_id=deserialize_param(asset_profile_id_json, 'AssetProfileId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_asset_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_assets(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Assets (getTenantAssets)  # noqa: E501

Returns a page of assets owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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


def process_assets_bulk_import(body_json: str) -> str:
    """
    Import the bulk of assets (processAssetsBulkImport)  # noqa: E501

There's an ability to import the bulk of assets using the only .csv file.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.process_assets_bulk_import(body=deserialize_param(body_json, 'BulkImportRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'process_assets_bulk_import'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_asset(body_json: str = None) -> str:
    """
    Create Or Update Asset (saveAsset)  # noqa: E501

Creates or Updates the Asset. When creating asset, platform generates Asset Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Asset id will be present in the response. Specify existing Asset id to update the asset. Referencing non-existing Asset Id will cause 'Not Found' error. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Asset entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_asset(body=deserialize_param(body_json, 'Asset'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_asset'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def unassign_asset_from_customer(asset_id_json: str) -> str:
    """
    Unassign asset from customer (unassignAssetFromCustomer)  # noqa: E501

Clears assignment of the asset to customer. Customer will not be able to query asset afterwards.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.unassign_asset_from_customer(asset_id=deserialize_param(asset_id_json, 'AssetId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unassign_asset_from_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def unassign_asset_from_edge(edge_id_json: str, asset_id_json: str) -> str:
    """
    Unassign asset from edge (unassignAssetFromEdge)  # noqa: E501

Clears assignment of the asset to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove asset (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove asset locally.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.unassign_asset_from_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), asset_id=deserialize_param(asset_id_json, 'AssetId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unassign_asset_from_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( assign_asset_to_customer )
    mcp.tool()( assign_asset_to_edge )
    mcp.tool()( assign_asset_to_public_customer )
    mcp.tool()( delete_asset )
    mcp.tool()( find_by_query )
    mcp.tool()( get_asset_by_id )
    mcp.tool()( get_asset_info_by_id )
    mcp.tool()( get_asset_types )
    mcp.tool()( get_assets_by_ids )
    mcp.tool()( get_customer_asset_infos )
    mcp.tool()( get_customer_assets )
    mcp.tool()( get_edge_assets )
    mcp.tool()( get_tenant_asset )
    mcp.tool()( get_tenant_asset_infos )
    mcp.tool()( get_tenant_assets )
    mcp.tool()( process_assets_bulk_import )
    mcp.tool()( save_asset )
    mcp.tool()( unassign_asset_from_customer )
    mcp.tool()( unassign_asset_from_edge )
