import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_widgets_bundle(widgets_bundle_id_json: str) -> str:
    """
    Delete widgets bundle (deleteWidgetsBundle)  # noqa: E501

Deletes the widget bundle. Referencing non-existing Widget Bundle Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (WidgetsBundleId):
    - `id` (str)
    - `entity_type` (str)
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


def get_widgets_bundle_by_id(widgets_bundle_id_json: str, inline_images: Optional[bool] = None) -> str:
    """
    Get Widget Bundle (getWidgetsBundleById)  # noqa: E501

Get the Widget Bundle based on the provided Widget Bundle Id. Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.   Available for any authorized user.   # noqa: E501

    ---------------------------
    Expected JSON Structure (WidgetsBundleId):
    - `id` (str)
    - `entity_type` (str)
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


def save_widgets_bundle(body_json: str = None) -> str:
    """
    Create Or Update Widget Bundle (saveWidgetsBundle)  # noqa: E501

Create or update the Widget Bundle. Widget Bundle represents a group(bundle) of widgets. Widgets are grouped into bundle by type or use case.  When creating the bundle, platform generates Widget Bundle Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Widget Bundle Id will be present in the response. Specify existing Widget Bundle id to update the Widget Bundle. Referencing non-existing Widget Bundle Id will cause 'Not Found' error.  Widget Bundle alias is unique in the scope of tenant. Special Tenant Id '13814000-1dd2-11b2-8080-808080808080' is automatically used if the create bundle request is sent by user with 'SYS_ADMIN' authority.Remove 'id', 'tenantId' from the request body example (below) to create new Widgets Bundle entity.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (WidgetsBundle):
    - `id` (WidgetsBundleId)
    - `created_time` (int)
    - `tenant_id` (TenantId)
    - `alias` (str)
    - `title` (str)
    - `image` (str)
    - `scada` (bool)
    - `description` (str)
    - `order` (int)
    - `version` (int)
    - `name` (str)
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

    ---------------------------
    Expected JSON Structure (WidgetsBundleId):
    - `id` (str)
    - `entity_type` (str)
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

    ---------------------------
    Expected JSON Structure (WidgetsBundleId):
    - `id` (str)
    - `entity_type` (str)
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
    mcp.tool()( delete_widgets_bundle )
    mcp.tool()( get_widgets_bundle_by_id )
    mcp.tool()( get_widgets_bundles )
    mcp.tool()( get_widgets_bundles_v1 )
    mcp.tool()( save_widgets_bundle )
    mcp.tool()( update_widgets_bundle_widget_fqns )
    mcp.tool()( update_widgets_bundle_widget_types )
