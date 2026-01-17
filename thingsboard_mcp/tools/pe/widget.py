import json
import tb_rest_client.models.models_pe as models
from ...shared import get_client, deserialize_param, format_response, ApiException


def delete_widget_type(widget_type_id_json: str) -> str:
    """
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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

def get_widgets_bundles_by_ids(widget_bundle_ids_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_widgets_bundles_by_ids(widget_bundle_ids=json.loads(widget_bundle_ids_json) if widget_bundle_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_widgets_bundles_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_widgets_bundles_v1(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, tenant_only: Optional[bool] = None, full_search: Optional[bool] = None) -> str:
    """
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    No description available.
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
    mcp.tool()( get_widgets_bundles_by_ids )
    mcp.tool()( get_widgets_bundles_v1 )
    mcp.tool()( save_widget_type )
    mcp.tool()( save_widgets_bundle )
    mcp.tool()( update_widgets_bundle_widget_fqns )
    mcp.tool()( update_widgets_bundle_widget_types )
