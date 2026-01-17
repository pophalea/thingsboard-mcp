import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def get_component_descriptor_by_clazz(component_descriptor_clazz: str) -> str:
    """
    Get Component Descriptor (getComponentDescriptorByClazz)  # noqa: E501

Gets the Component Descriptor object using class name from the path parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_component_descriptor_by_clazz(component_descriptor_clazz=component_descriptor_clazz)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_component_descriptor_by_clazz'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_component_descriptors_by_type(component_type: str, rule_chain_type: Optional[str] = None) -> str:
    """
    Get Component Descriptors (getComponentDescriptorsByType)  # noqa: E501

Gets the Component Descriptors using rule node type and optional rule chain type request parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_component_descriptors_by_type(component_type=component_type, rule_chain_type=rule_chain_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_component_descriptors_by_type'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_component_descriptors_by_types(component_types: str, rule_chain_type: Optional[str] = None) -> str:
    """
    Get Component Descriptors (getComponentDescriptorsByTypes)  # noqa: E501

Gets the Component Descriptors using coma separated list of rule node types and optional rule chain type request parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_component_descriptors_by_types(component_types=component_types, rule_chain_type=rule_chain_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_component_descriptors_by_types'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( get_component_descriptor_by_clazz )
    mcp.tool()( get_component_descriptors_by_type )
    mcp.tool()( get_component_descriptors_by_types )
