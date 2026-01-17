import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def get_queue_stats_by_id(queue_stats_id_json: str) -> str:
    """
    Get Queue stats entity by id (getQueueStatsById)  # noqa: E501

Fetch the Queue stats object based on the provided Queue stats id.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_queue_stats_by_id(queue_stats_id=deserialize_param(queue_stats_id_json, 'QueueId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_queue_stats_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_queue_stats_by_ids(queue_stats_ids_json: str) -> str:
    """
    Get QueueStats By Ids (getQueueStatsByIds)  # noqa: E501

Fetch the Queue stats objects based on the provided ids.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_queue_stats_by_ids(queue_stats_ids=json.loads(queue_stats_ids_json) if queue_stats_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_queue_stats_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_queue_stats(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Queue Stats entities (getTenantQueueStats)  # noqa: E501

Returns a page of queue stats objects that are designed to collect queue statistics for every service. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_queue_stats(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_queue_stats'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( get_queue_stats_by_id )
    mcp.tool()( get_queue_stats_by_ids )
    mcp.tool()( get_tenant_queue_stats )
