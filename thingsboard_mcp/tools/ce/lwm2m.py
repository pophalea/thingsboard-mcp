import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def get_lwm2m_bootstrap_security_info(is_bootstrap_server: bool) -> str:
    """
    Get Lwm2m Bootstrap SecurityInfo (getLwm2mBootstrapSecurityInfo)  # noqa: E501

Get the Lwm2m Bootstrap SecurityInfo object (of the current server) based on the provided isBootstrapServer parameter. If isBootstrapServer == true, get the parameters of the current Bootstrap Server. If isBootstrapServer == false, get the parameters of the current Lwm2m Server. Used for client settings when starting the client in Bootstrap mode.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_lwm2m_bootstrap_security_info(is_bootstrap_server=is_bootstrap_server)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_lwm2m_bootstrap_security_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( get_lwm2m_bootstrap_security_info )
