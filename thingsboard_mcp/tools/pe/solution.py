import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def get_solution_template_details(solution_template_id_json: str) -> str:
    """
    Get Solution template details (getSolutionTemplateDetails)  # noqa: E501

Get a solution template details based on the provided id   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_solution_template_details(solution_template_id=deserialize_param(solution_template_id_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_solution_template_details'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_solution_template_infos() -> str:
    """
    Get Solution templates (getSolutionTemplateInfos)  # noqa: E501

Get a list of solution template descriptors   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_solution_template_infos()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_solution_template_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_solution_template_instructions(solution_template_id_json: str) -> str:
    """
    Get Solution Template Instructions (getSolutionTemplateInstructions)  # noqa: E501

Get a solution template instructions based on the provided id   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_solution_template_instructions(solution_template_id=deserialize_param(solution_template_id_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_solution_template_instructions'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def install_solution_template(solution_template_id_json: str) -> str:
    """
    Install Solution Template (installSolutionTemplate)  # noqa: E501

Install solution template based on the provided id   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.install_solution_template(solution_template_id=deserialize_param(solution_template_id_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'install_solution_template'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def uninstall_solution_template(solution_template_id_json: str) -> str:
    """
    Uninstall Solution Template (uninstallSolutionTemplate)  # noqa: E501

Uninstall solution template based on the provided id   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.uninstall_solution_template(solution_template_id=deserialize_param(solution_template_id_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'uninstall_solution_template'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( get_solution_template_details )
    mcp.tool()( get_solution_template_infos )
    mcp.tool()( get_solution_template_instructions )
    mcp.tool()( install_solution_template )
    mcp.tool()( uninstall_solution_template )
