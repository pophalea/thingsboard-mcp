import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def get_downlink_converter(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get downlink converter (getDownlinkConverter)  # noqa: E501

Returns downlink converter body for the vendor, integration type and model  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_downlink_converter(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_downlink_converter'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_downlink_converter_metadata(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get downlink converter metadata (getDownlinkConverterMetadata)  # noqa: E501

Returns downlink converter metadata for the vendor, integration type and model  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_downlink_converter_metadata(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_downlink_converter_metadata'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_downlink_payload(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get downlink payload (getDownlinkPayload)  # noqa: E501

Returns payload example for the downlink converter for the vendor, integration type and model  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_downlink_payload(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_downlink_payload'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_uplink_converter(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get uplink converter (getUplinkConverter)  # noqa: E501

Returns uplink converter body for the vendor, integration type and model  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_uplink_converter(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_uplink_converter'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_uplink_converter_metadata(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get uplink converter metadata (getUplinkConverterMetadata)  # noqa: E501

Returns uplink converter metadata for the vendor, integration type and model  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_uplink_converter_metadata(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_uplink_converter_metadata'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_uplink_payload(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get uplink payload (getUplinkPayload)  # noqa: E501

Returns payload example for the uplink converter for the vendor, integration type and model  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_uplink_payload(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_uplink_payload'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_vendor_models(integration_type: str, vendor_name: str, converter_type: str) -> str:
    """
    Get vendor models (getVendorModels)  # noqa: E501

Returns a list of models for the vendor, integration type and converter type  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_vendor_models(integration_type=integration_type, vendor_name=vendor_name, converter_type=converter_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_vendor_models'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_vendors(integration_type: str) -> str:
    """
    Get vendors (getVendors)  # noqa: E501

Returns a list of vendors for the integration type  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_vendors(integration_type=integration_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_vendors'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( get_downlink_converter )
    mcp.tool()( get_downlink_converter_metadata )
    mcp.tool()( get_downlink_payload )
    mcp.tool()( get_uplink_converter )
    mcp.tool()( get_uplink_converter_metadata )
    mcp.tool()( get_uplink_payload )
    mcp.tool()( get_vendor_models )
    mcp.tool()( get_vendors )
