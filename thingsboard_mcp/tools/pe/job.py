import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def cancel_job(id_json: str) -> str:
    """
    Cancel job (cancelJob)  # noqa: E501

Cancels the job. The status of the job must be QUEUED, PENDING or RUNNING.  For a running job, all the tasks not yet processed will be discarded.  See the example of a cancelled job result in getJobById method description.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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
    Get job by id (getJobById)  # noqa: E501

Fetches job info by id.  Example of a RUNNING CF_REPROCESSING job response: ```json {   "id": {     "entityType": "JOB",     "id": "475e94e0-2f2d-11f0-8240-91e99922a704"   },   "createdTime": 1747053196590,   "tenantId": {     "entityType": "TENANT",     "id": "46859a00-2f2d-11f0-8240-91e99922a704"   },   "type": "CF_REPROCESSING",   "key": "474e4130-2f2d-11f0-8240-91e99922a704",   "entityId": {     "entityType": "DEVICE_PROFILE",     "id": "9fd41f20-31a1-11f0-933e-27998d6db02e"    },   "status": "RUNNING",   "configuration": {     "type": "CF_REPROCESSING",     "calculatedFieldId": {       "entityType": "CALCULATED_FIELD",       "id": "474e4130-2f2d-11f0-8240-91e99922a704"     },     "startTs": 1747051995760,     "endTs": 1747052895760,     "tasksKey": "c3cdbd42-799e-4d3a-9aad-9310f767aa36",     "toReprocess": null   },   "result": {     "jobType": "CF_REPROCESSING",     "successfulCount": 1,     "failedCount": 0,     "discardedCount": 0,     "totalCount": 2,     "results": [],     "generalError": null,     "startTs": 1747323069445,     "finishTs": 1747323070585,     "cancellationTs": 0   } }  ```  Example of a CF_REPROCESSING job with failures: ```json {   ...,   "status": "FAILED",   ...,   "result": {     "jobType": "CF_REPROCESSING",     "successfulCount": 0,     "failedCount": 2,     "discardedCount": 0,     "totalCount": 2,     "results": [       {         "jobType": "CF_REPROCESSING",         "key": "c3cdbd42-799e-4d3a-9aad-9310f767aa36",         "success": false,         "discarded": false,         "failure": {           "error": "Failed to fetch temperature: Failed to fetch timeseries data",           "entityInfo": {             "id": {               "entityType": "DEVICE",               "id": "9fd41f20-31a1-11f0-933e-27998d6db02e"             },             "name": "Test device 1"           }         }       },       {         "jobType": "CF_REPROCESSING",         "key": "c3cdbd42-799e-4d3a-9aad-9310f767aa36",         "success": false,         "discarded": false,         "failure": {           "error": "Failed to fetch temperature: Failed to fetch timeseries data",           "entityInfo": {             "id": {               "entityType": "DEVICE",               "id": "9ffc4090-31a1-11f0-933e-27998d6db02e"             },             "name": "Test device 2"           }         }       }     ],     "generalError": null,     "startTs": 1747323069445,     "finishTs": 1747323070585,     "cancellationTs": 0   } }  ```  Example of a FAILED job result with general error: ```json {   ...,   "status": "FAILED",   ...,   "result": {     "jobType": "CF_REPROCESSING",     "successfulCount": 1,     "failedCount": 0,     "discardedCount": 0,     "totalCount": null,     "results": [],     "generalError": "Timeout to find devices by profile",     "cancellationTs": 0   } }  ```  Example of a CANCELLED job result: ```json {   ...,   "status": "CANCELLED",   ...,   "result": {     "jobType": "CF_REPROCESSING",     "successfulCount": 15,     "failedCount": 0,     "discardedCount": 85,     "totalCount": 100,     "results": [],     "generalError": null,     "cancellationTs": 1747065908414   } }  ```  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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
    Get jobs (getJobs)  # noqa: E501

Returns the page of jobs.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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
    Reprocess job (reprocessJob)  # noqa: E501

Reprocesses the job. Failures are located at job.result.results list. Platform iterates over this list and submits new tasks for them. Doesn't create new job entity but updates the existing one. Successfully reprocessed job will look the same as completed one.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
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
