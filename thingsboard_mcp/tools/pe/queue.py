import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_queue(queue_id_json: str) -> str:
    """
    Delete Queue (deleteQueue)  # noqa: E501

Deletes the Queue.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_queue(queue_id=deserialize_param(queue_id_json, 'QueueId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_queue'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_queue_by_id(queue_id_json: str) -> str:
    """
    Get Queue (getQueueById)  # noqa: E501

Fetch the Queue object based on the provided Queue Id.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_queue_by_id(queue_id=deserialize_param(queue_id_json, 'QueueId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_queue_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_queue_by_name(queue_name: str) -> str:
    """
    Get Queue (getQueueByName)  # noqa: E501

Fetch the Queue object based on the provided Queue name.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_queue_by_name(queue_name=queue_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_queue_by_name'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_queues_by_service_type(service_type: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Queues (getTenantQueuesByServiceType)  # noqa: E501

Returns a page of queues registered in the platform. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_queues_by_service_type(service_type=service_type, page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_queues_by_service_type'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_queue(service_type: str, body_json: str = None) -> str:
    """
    Create Or Update Queue (saveQueue)  # noqa: E501

Create or update the Queue. When creating queue, platform generates Queue Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). Specify existing Queue id to update the queue. Referencing non-existing Queue Id will cause 'Not Found' error.  Queue name is unique in the scope of sysadmin. Remove 'id', 'tenantId' from the request body example (below) to create new Queue entity.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_queue(service_type=service_type, body=deserialize_param(body_json, 'Queue'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_queue'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_queue )
    mcp.tool()( get_queue_by_id )
    mcp.tool()( get_queue_by_name )
    mcp.tool()( get_tenant_queues_by_service_type )
    mcp.tool()( save_queue )
