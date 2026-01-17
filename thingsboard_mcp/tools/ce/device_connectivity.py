import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def download_gateway_docker_compose(device_id_json: str) -> str:
    """
    Download generated docker-compose.yml file for gateway (downloadGatewayDockerCompose)  # noqa: E501

Download generated docker-compose.yml for gateway.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_gateway_docker_compose(device_id=deserialize_param(device_id_json, 'DeviceId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_gateway_docker_compose'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def download_server_certificate(protocol: str) -> str:
    """
    Download server certificate using file path defined in device.connectivity properties (downloadServerCertificate)  # noqa: E501

Download server certificate.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_server_certificate(protocol=protocol)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_server_certificate'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_device_publish_telemetry_commands(device_id_json: str) -> str:
    """
    Get commands to publish device telemetry (getDevicePublishTelemetryCommands)  # noqa: E501

Fetch the list of commands to publish device telemetry based on device profile If the user has the authority of 'Tenant Administrator', the server checks that the device is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the device is assigned to the same customer.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
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


def register(mcp):
    mcp.tool()( download_gateway_docker_compose )
    mcp.tool()( download_server_certificate )
    mcp.tool()( get_device_publish_telemetry_commands )
