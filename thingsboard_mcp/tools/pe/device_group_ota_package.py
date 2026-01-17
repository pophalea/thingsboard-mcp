import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_device_group_ota_package(id: str) -> str:
    """
    deleteDeviceGroupOtaPackage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_device_group_ota_package(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_device_group_ota_package'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_firmware_by_id(group_id_json: str, firmware_type: str) -> str:
    """
    getFirmwareById  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_firmware_by_id(group_id=deserialize_param(group_id_json, 'EntityGroupId'), firmware_type=firmware_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_firmware_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_device_group_ota_package(body_json: str = None) -> str:
    """
    saveDeviceGroupOtaPackage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_device_group_ota_package(body=deserialize_param(body_json, 'DeviceGroupOtaPackage'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_device_group_ota_package'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_device_group_ota_package )
    mcp.tool()( get_firmware_by_id )
    mcp.tool()( save_device_group_ota_package )
