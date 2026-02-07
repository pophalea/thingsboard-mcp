import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_customer(customer_id_json: str) -> str:
    """
    Delete Customer (deleteCustomer)  # noqa: E501

Deletes the Customer and all customer Users. All assigned Dashboards, Assets, Devices, etc. will be unassigned but not deleted. Referencing non-existing Customer Id will cause an error.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomerId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.delete_customer(customer_id=deserialize_param(customer_id_json, 'CustomerId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_customer_by_id(customer_id_json: str) -> str:
    """
    Get Customer (getCustomerById)  # noqa: E501

Get the Customer object based on the provided Customer Id. If the user has the authority of 'Tenant Administrator', the server checks that the customer is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the user belongs to the customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomerId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_customer_by_id(customer_id=deserialize_param(customer_id_json, 'CustomerId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_customer_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_customer_title_by_id(customer_id_json: str) -> str:
    """
    Get Customer Title (getCustomerTitleById)  # noqa: E501

Get the title of the customer. If the user has the authority of 'Tenant Administrator', the server checks that the customer is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the user belongs to the customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomerId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_customer_title_by_id(customer_id=deserialize_param(customer_id_json, 'CustomerId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_customer_title_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_customers(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Customers (getCustomers)  # noqa: E501

Returns a page of customers owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_customers(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_customers'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_short_customer_info_by_id(customer_id_json: str) -> str:
    """
    Get short Customer info (getShortCustomerInfoById)  # noqa: E501

Get the short customer object that contains only the title and 'isPublic' flag. If the user has the authority of 'Tenant Administrator', the server checks that the customer is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the user belongs to the customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (CustomerId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.get_short_customer_info_by_id(customer_id=deserialize_param(customer_id_json, 'CustomerId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_short_customer_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_tenant_customer(customer_title: str) -> str:
    """
    Get Tenant Customer by Customer title (getTenantCustomer)  # noqa: E501

Get the Customer using Customer Title.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_tenant_customer(customer_title=customer_title)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_tenant_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_customer(body_json: str = None) -> str:
    """
    Create or update Customer (saveCustomer)  # noqa: E501

Creates or Updates the Customer. When creating customer, platform generates Customer Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Customer Id will be present in the response. Specify existing Customer Id to update the Customer. Referencing non-existing Customer Id will cause 'Not Found' error.Remove 'id', 'tenantId' from the request body example (below) to create new Customer entity.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501

    ---------------------------
    Expected JSON Structure (Customer):
    - `id` (CustomerId)
    - `created_time` (int)
    - `country` (str)
    - `state` (str)
    - `city` (str)
    - `address` (str)
    - `address2` (str)
    - `zip` (str)
    - `phone` (str)
    - `email` (str)
    - `title` (str)
    - `tenant_id` (TenantId)
    - `version` (int)
    - `name` (str)
    - `additional_info` (JsonNode)
    """
    try:
        client = get_client()
        result = client.save_customer(body=deserialize_param(body_json, 'Customer'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_customer'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_customer )
    mcp.tool()( get_customer_by_id )
    mcp.tool()( get_customer_title_by_id )
    mcp.tool()( get_customers )
    mcp.tool()( get_short_customer_info_by_id )
    mcp.tool()( get_tenant_customer )
    mcp.tool()( save_customer )
