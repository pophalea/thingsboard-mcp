import json
import tb_rest_client.models.models_ce as models
from ...shared import get_client, deserialize_param, format_response, ApiException


def delete_widget_type(widget_type_id_json: str) -> str:
    """
    Delete widget type (deleteWidgetType)  # noqa: E501

Deletes the  Widget Type. Referencing non-existing Widget Type Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_widget_type(widget_type_id=deserialize_param(widget_type_id_json, 'WidgetTypeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_widget_type'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_widgets_bundle(widgets_bundle_id_json: str) -> str:
    """
    Delete widgets bundle (deleteWidgetsBundle)  # noqa: E501

Deletes the widget bundle. Referencing non-existing Widget Bundle Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_widgets_bundle(widgets_bundle_id=deserialize_param(widgets_bundle_id_json, 'WidgetsBundleId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_widgets_bundle'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_bundle_widget_type_fqns(widgets_bundle_id_json: str) -> str:
    """
    Get all Widget type fqns for specified Bundle (getBundleWidgetTypeFqns)  # noqa: E501

Returns an array of Widget Type fqns that belong to specified Widget Bundle.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_bundle_widget_type_fqns(widgets_bundle_id=deserialize_param(widgets_bundle_id_json, 'WidgetsBundleId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_bundle_widget_type_fqns'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_bundle_widget_types(widgets_bundle_id_json: str) -> str:
    """
    Get all Widget types for specified Bundle (getBundleWidgetTypes)  # noqa: E501

Returns an array of Widget Type objects that belong to specified Widget Bundle.Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_bundle_widget_types(widgets_bundle_id=deserialize_param(widgets_bundle_id_json, 'WidgetsBundleId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_bundle_widget_types'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_bundle_widget_types_by_bundle_alias(is_system: bool, bundle_alias: str) -> str:
    """
    Get all Widget types for specified Bundle (getBundleWidgetTypesByBundleAlias) (Deprecated)  # noqa: E501

Returns an array of Widget Type objects that belong to specified Widget Bundle.Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_bundle_widget_types_by_bundle_alias(is_system=is_system, bundle_alias=bundle_alias)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_bundle_widget_types_by_bundle_alias'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_bundle_widget_types_details(widgets_bundle_id_json: str, inline_images: Optional[bool] = None) -> str:
    """
    Get all Widget types details for specified Bundle (getBundleWidgetTypesDetails)  # noqa: E501

Returns an array of Widget Type Details objects that belong to specified Widget Bundle.Widget Type Details extend Widget Type and add image and description properties. Those properties are useful to edit the Widget Type but they are not required for Dashboard rendering.    Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_bundle_widget_types_details(widgets_bundle_id=deserialize_param(widgets_bundle_id_json, 'WidgetsBundleId'), inline_images=inline_images)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_bundle_widget_types_details'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_bundle_widget_types_details_by_bundle_alias(is_system: bool, bundle_alias: str) -> str:
    """
    Get all Widget types details for specified Bundle (getBundleWidgetTypesDetailsByBundleAlias) (Deprecated)  # noqa: E501

Returns an array of Widget Type Details objects that belong to specified Widget Bundle.Widget Type Details extend Widget Type and add image and description properties. Those properties are useful to edit the Widget Type but they are not required for Dashboard rendering.    Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_bundle_widget_types_details_by_bundle_alias(is_system=is_system, bundle_alias=bundle_alias)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_bundle_widget_types_details_by_bundle_alias'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_bundle_widget_types_infos(widgets_bundle_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, full_search: Optional[bool] = None, deprecated_filter: Optional[str] = None, widget_type_list_json: str = None) -> str:
    """
    Get Widget Type Info objects (getBundleWidgetTypesInfos)  # noqa: E501

Get the Widget Type Info objects based on the provided parameters. Widget Type Info is a lightweight object that represents Widget Type but does not contain the heavyweight widget descriptor JSON  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_bundle_widget_types_infos(widgets_bundle_id=deserialize_param(widgets_bundle_id_json, 'WidgetsBundleId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, full_search=full_search, deprecated_filter=deprecated_filter, widget_type_list=json.loads(widget_type_list_json) if widget_type_list_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_bundle_widget_types_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_bundle_widget_types_infos_by_bundle_alias(is_system: bool, bundle_alias: str) -> str:
    """
    Get Widget Type Info objects (getBundleWidgetTypesInfosByBundleAlias) (Deprecated)  # noqa: E501

Get the Widget Type Info objects based on the provided parameters. Widget Type Info is a lightweight object that represents Widget Type but does not contain the heavyweight widget descriptor JSON  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_bundle_widget_types_infos_by_bundle_alias(is_system=is_system, bundle_alias=bundle_alias)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_bundle_widget_types_infos_by_bundle_alias'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_widget_type(fqn_json: str) -> str:
    """
    Get Widget Type (getWidgetType)  # noqa: E501

Get the Widget Type by FQN. Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_widget_type(fqn=deserialize_param(fqn_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_widget_type'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_widget_type_by_bundle_alias_and_type_alias(is_system: bool, bundle_alias: str, alias: str) -> str:
    """
    Get Widget Type (getWidgetTypeByBundleAliasAndTypeAlias) (Deprecated)  # noqa: E501

Get the Widget Type based on the provided parameters. Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_widget_type_by_bundle_alias_and_type_alias(is_system=is_system, bundle_alias=bundle_alias, alias=alias)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_widget_type_by_bundle_alias_and_type_alias'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_widget_type_by_id(widget_type_id_json: str, inline_images: Optional[bool] = None) -> str:
    """
    Get Widget Type Details (getWidgetTypeById)  # noqa: E501

Get the Widget Type Details based on the provided Widget Type Id. Widget Type Details extend Widget Type and add image and description properties. Those properties are useful to edit the Widget Type but they are not required for Dashboard rendering.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_widget_type_by_id(widget_type_id=deserialize_param(widget_type_id_json, 'WidgetTypeId'), inline_images=inline_images)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_widget_type_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_widget_type_info_by_id(widget_type_id_json: str) -> str:
    """
    Get Widget Type Info (getWidgetTypeInfoById)  # noqa: E501

Get the Widget Type Info based on the provided Widget Type Id. Widget Type Details extend Widget Type and add image and description properties. Those properties are useful to edit the Widget Type but they are not required for Dashboard rendering.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_widget_type_info_by_id(widget_type_id=deserialize_param(widget_type_id_json, 'WidgetTypeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_widget_type_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_widget_types(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, tenant_only: Optional[bool] = None, full_search: Optional[bool] = None, deprecated_filter: Optional[str] = None, widget_type_list_json: str = None) -> str:
    """
    Get Widget Types (getWidgetTypes)  # noqa: E501

Returns a page of Widget Type objects available for current user. Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_widget_types(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, tenant_only=tenant_only, full_search=full_search, deprecated_filter=deprecated_filter, widget_type_list=json.loads(widget_type_list_json) if widget_type_list_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_widget_types'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_widgets_bundle_by_id(widgets_bundle_id_json: str, inline_images: Optional[bool] = None) -> str:
    """
    Get Widget Bundle (getWidgetsBundleById)  # noqa: E501

Get the Widget Bundle based on the provided Widget Bundle Id. Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.   Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_widgets_bundle_by_id(widgets_bundle_id=deserialize_param(widgets_bundle_id_json, 'WidgetsBundleId'), inline_images=inline_images)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_widgets_bundle_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_widgets_bundles() -> str:
    """
    Get all Widget Bundles (getWidgetsBundles)  # noqa: E501

Returns an array of Widget Bundle objects that are available for current user.Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.    Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_widgets_bundles()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_widgets_bundles'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_widgets_bundles_v1(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, tenant_only: Optional[bool] = None, full_search: Optional[bool] = None) -> str:
    """
    Get Widget Bundles (getWidgetsBundles)  # noqa: E501

Returns a page of Widget Bundle objects available for current user. Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_widgets_bundles_v1(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, tenant_only=tenant_only, full_search=full_search)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_widgets_bundles_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_widget_type(body_json: str, update_existing_by_fqn: Optional[bool] = None) -> str:
    """
    Create Or Update Widget Type (saveWidgetType)  # noqa: E501

Create or update the Widget Type. Widget Type represents the template for widget creation. Widget Type and Widget are similar to class and object in OOP theory. When creating the Widget Type, platform generates Widget Type Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Widget Type Id will be present in the response. Specify existing Widget Type id to update the Widget Type. Referencing non-existing Widget Type Id will cause 'Not Found' error.  Widget Type fqn is unique in the scope of System or Tenant. Special Tenant Id '13814000-1dd2-11b2-8080-808080808080' is automatically used if the create request is sent by user with 'SYS_ADMIN' authority.Remove 'id', 'tenantId' rom the request body example (below) to create new Widget Type entity.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_widget_type(body=deserialize_param(body_json, 'WidgetTypeDetails'), update_existing_by_fqn=update_existing_by_fqn)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_widget_type'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_widgets_bundle(body_json: str) -> str:
    """
    Create Or Update Widget Bundle (saveWidgetsBundle)  # noqa: E501

Create or update the Widget Bundle. Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.  When creating the bundle, platform generates Widget Bundle Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Widget Bundle Id will be present in the response. Specify existing Widget Bundle id to update the Widget Bundle. Referencing non-existing Widget Bundle Id will cause 'Not Found' error.  Widget Bundle alias is unique in the scope of tenant. Special Tenant Id '13814000-1dd2-11b2-8080-808080808080' is automatically used if the create bundle request is sent by user with 'SYS_ADMIN' authority.Remove 'id', 'tenantId' from the request body example (below) to create new Widgets Bundle entity.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_widgets_bundle(body=deserialize_param(body_json, 'WidgetsBundle'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_widgets_bundle'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_widgets_bundle_widget_fqns(widgets_bundle_id_json: str, body_json: str) -> str:
    """
    Update widgets bundle widgets list from widget type FQNs list (updateWidgetsBundleWidgetFqns)  # noqa: E501

Updates widgets bundle widgets list from widget type FQNs list.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_widgets_bundle_widget_fqns(widgets_bundle_id=deserialize_param(widgets_bundle_id_json, 'WidgetsBundleId'), body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_widgets_bundle_widget_fqns'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_widgets_bundle_widget_types(widgets_bundle_id_json: str, body_json: str) -> str:
    """
    Update widgets bundle widgets types list (updateWidgetsBundleWidgetTypes)  # noqa: E501

Updates widgets bundle widgets list.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_widgets_bundle_widget_types(widgets_bundle_id=deserialize_param(widgets_bundle_id_json, 'WidgetsBundleId'), body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_widgets_bundle_widget_types'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def register(mcp):
    mcp.tool()( delete_widget_type )
    mcp.tool()( delete_widgets_bundle )
    mcp.tool()( get_bundle_widget_type_fqns )
    mcp.tool()( get_bundle_widget_types )
    mcp.tool()( get_bundle_widget_types_by_bundle_alias )
    mcp.tool()( get_bundle_widget_types_details )
    mcp.tool()( get_bundle_widget_types_details_by_bundle_alias )
    mcp.tool()( get_bundle_widget_types_infos )
    mcp.tool()( get_bundle_widget_types_infos_by_bundle_alias )
    mcp.tool()( get_widget_type )
    mcp.tool()( get_widget_type_by_bundle_alias_and_type_alias )
    mcp.tool()( get_widget_type_by_id )
    mcp.tool()( get_widget_type_info_by_id )
    mcp.tool()( get_widget_types )
    mcp.tool()( get_widgets_bundle_by_id )
    mcp.tool()( get_widgets_bundles )
    mcp.tool()( get_widgets_bundles_v1 )
    mcp.tool()( save_widget_type )
    mcp.tool()( save_widgets_bundle )
    mcp.tool()( update_widgets_bundle_widget_fqns )
    mcp.tool()( update_widgets_bundle_widget_types )
