import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def cancel_job(id_json: str) -> str:
    """
    cancelJob  # noqa: E501

    ---------------------------
    Expected JSON Structure (JobId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.cancel_job(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'cancel_job'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_job(id_json: str) -> str:
    """
    deleteJob  # noqa: E501

    ---------------------------
    Expected JSON Structure (JobId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.delete_job(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_job'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_job_by_id(id_json: str) -> str:
    """
    getJobById  # noqa: E501

    ---------------------------
    Expected JSON Structure (JobId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_job_by_id(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_job_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_jobs(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    getJobs  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_jobs(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_jobs'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def reprocess_job(id_json: str) -> str:
    """
    reprocessJob  # noqa: E501

    ---------------------------
    Expected JSON Structure (JobId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.reprocess_job(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'reprocess_job'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( cancel_job )
    mcp.tool()( delete_job )
    mcp.tool()( get_job_by_id )
    mcp.tool()( get_jobs )
    mcp.tool()( reprocess_job )
