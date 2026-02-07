import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_report_template(report_template_id_json: str) -> str:
    """
    Delete Report Template (deleteReportTemplate)  # noqa: E501

Deletes the report template. Referencing non-existing Report Template Id will cause 'Not Found' error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (ReportTemplateId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.delete_report_template(report_template_id=deserialize_param(report_template_id_json, 'ReportTemplateId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_report_template'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_all_report_template_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, type_list: Optional[str] = None, format_list: Optional[str] = None, include_customers: Optional[bool] = None) -> str:
    """
    Get All Report Templates for current user (getAllReportTemplateInfos)  # noqa: E501

Returns a page of report template info objects owned by the tenant or the customer of a current user. Report Templates allows you to create reports according to the report template configuration. Report service uses report template configuration to generate report. See the 'Model' tab of the Response Class for more details.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_all_report_template_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, type_list=type_list, format_list=format_list, include_customers=include_customers)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_all_report_template_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_report_template_by_id(report_template_id_json: str) -> str:
    """
    Get Report Template (getReportTemplateById)  # noqa: E501

Fetch the ReportTemplate object based on the provided report template Id. Report Template extends Report Template Info object and adds 'configuration' - a JSON structure of report template configuration. See the 'Model' tab of the Response Class for more details. Referencing non-existing Report Template Id will cause 'Not Found' error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (ReportTemplateId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_report_template_by_id(report_template_id=deserialize_param(report_template_id_json, 'ReportTemplateId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_report_template_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_report_template_info_by_id(report_template_id_json: str) -> str:
    """
    Get Report Template Info (getReportTemplateInfoById)  # noqa: E501

Fetch the ReportTemplateInfo object based on the provided report template Id. Report Templates allows you to create reports according to the report template configuration. Report service uses report template configuration to generate report. See the 'Model' tab of the Response Class for more details. Referencing non-existing Report Template Id will cause 'Not Found' error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (ReportTemplateId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_report_template_info_by_id(report_template_id=deserialize_param(report_template_id_json, 'ReportTemplateId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_report_template_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_report_templates_by_ids(report_template_ids_json: str) -> str:
    """
    Get report templates by Report Template Ids (getReportTemplatesByIds)  # noqa: E501

Returns a list of ReportTemplateInfo objects based on the provided ids. Filters the list based on the user permissions.   Available for users with 'TENANT_ADMIN' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_report_templates_by_ids(report_template_ids=json.loads(report_template_ids_json) if report_template_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_report_templates_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_report_template(body_json: str) -> str:
    """
    Save Report Template (saveReportTemplate)  # noqa: E501

Creates or Updates report template. Report Template extends Report Template Info object and adds 'configuration' - a JSON structure of report template configuration. See the 'Model' tab of the Response Class for more details. When creating report template, platform generates report template Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created report template id will be present in the response. Specify existing report template id to update the report template. Referencing non-existing report template Id will cause 'Not Found' error. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Report Template entity.   Available for users with 'TENANT_ADMIN' authority.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501

    ---------------------------
    Expected JSON Structure (ReportTemplate):
    - `id` (ReportTemplateId)
    - `created_time` (int)
    - `tenant_id` (TenantId)
    - `customer_id` (CustomerId)
    - `name` (str)
    - `format` (str)
    - `type` (str)
    - `description` (str)
    - `version` (str)
    - `configuration` (JsonNode)
    - `owner_id` (EntityId)
    """
    try:
        client = get_client()
        result = client.save_report_template(body=deserialize_param(body_json, 'ReportTemplate'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_report_template'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_report_template )
    mcp.tool()( get_all_report_template_infos )
    mcp.tool()( get_report_template_by_id )
    mcp.tool()( get_report_template_info_by_id )
    mcp.tool()( get_report_templates_by_ids )
    mcp.tool()( save_report_template )
