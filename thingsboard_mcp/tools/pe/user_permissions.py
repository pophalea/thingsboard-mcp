import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def get_allowed_permissions() -> str:
    """
    Get Permissions (getAllowedPermissions)  # noqa: E501

Returns a complex object that describes:   * all possible (both granted and not granted) permissions for the authority of the user (Tenant or Customer);  * all granted permissions for the user;   The result impacts UI behavior and hides certain UI elements if user has no permissions to invoke the related operations. Nevertheless, all API calls check the permissions each time they are executed on the server side.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_allowed_permissions()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_allowed_permissions'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( get_allowed_permissions )
