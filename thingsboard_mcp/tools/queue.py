import json
from typing import Optional
from .shared import get_client, deserialize_param, format_response, ApiException


def delete_queue(queue_id_json: str) -> str:
    """
    Delete Queue (deleteQueue)  # noqa: E501

Deletes the Queue.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str queue_id: A string value representing the queue id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_queue(queue_id=deserialize_param(queue_id_json, 'QueueId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_queue'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_queue_by_id(queue_id_json: str) -> str:
    """
    Get Queue (getQueueById)  # noqa: E501

Fetch the Queue object based on the provided Queue Id.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str queue_id: A string value representing the queue id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
:return: Queue
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_queue_by_id(queue_id=deserialize_param(queue_id_json, 'QueueId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_queue_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_queue_by_name(queue_name: str) -> str:
    """
    Get Queue (getQueueByName)  # noqa: E501

Fetch the Queue object based on the provided Queue name.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str queue_name: A string value representing the queue id. For example, 'Main' (required)
:return: Queue
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_queue_by_name(queue_name=queue_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_queue_by_name'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_queue_stats_by_id(queue_stats_id_json: str) -> str:
    """
    Get Queue stats entity by id (getQueueStatsById)  # noqa: E501

Fetch the Queue stats object based on the provided Queue stats id.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str queue_stats_id: A string value representing the queue stats id. For example, '687f294c-42b6-435a-983c-b7beff2784f9' (required)
:return: QueueStats
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_queue_stats_by_id(queue_stats_id=deserialize_param(queue_stats_id_json, 'QueueId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_queue_stats_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_queue_stats_by_ids(queue_stats_ids_json: str) -> str:
    """
    Get QueueStats By Ids (getQueueStatsByIds)  # noqa: E501

Fetch the Queue stats objects based on the provided ids.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str queue_stats_ids: A list of queue stats ids, separated by comma ',' (required)
:return: list[QueueStats]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_queue_stats_by_ids(queue_stats_ids=json.loads(queue_stats_ids_json) if queue_stats_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_queue_stats_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_queue(service_type: str, body: Optional[str] = None) -> str:
    """
    Create Or Update Queue (saveQueue)  # noqa: E501

Create or update the Queue. When creating queue, platform generates Queue Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). Specify existing Queue id to update the queue. Referencing non-existing Queue Id will cause 'Not Found' error.  Queue name is unique in the scope of sysadmin. Remove 'id', 'tenantId' from the request body example (below) to create new Queue entity.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str service_type: Service type (implemented only for the TB-RULE-ENGINE) (required)
:param Queue body:
:return: Queue
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_queue(service_type=service_type, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_queue'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    """Register tools with FastMCP server"""
    mcp.tool()( delete_queue )
    mcp.tool()( get_queue_by_id )
    mcp.tool()( get_queue_by_name )
    mcp.tool()( get_queue_stats_by_id )
    mcp.tool()( get_queue_stats_by_ids )
    mcp.tool()( save_queue )
