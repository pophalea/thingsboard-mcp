import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_ai_model_by_id(ai_model_id_json: str) -> str:
    """
    Delete AI model by ID (deleteAiModelById)  # noqa: E501

Deletes the AI model record by its `id`. If a record with the specified `id` exists, the record is deleted and the endpoint returns `true`. If no such record exists, the endpoint returns `false`.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_ai_model_by_id(ai_model_id=deserialize_param(ai_model_id_json, 'AiModelId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_ai_model_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_ai_model_by_id(ai_model_id_json: str) -> str:
    """
    Get AI model by ID (getAiModelById)  # noqa: E501

Fetches an AI model record by its `id`.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_ai_model_by_id(ai_model_id=deserialize_param(ai_model_id_json, 'AiModelId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_ai_model_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_ai_models(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get AI models (getAiModels)  # noqa: E501

Returns a page of AI models. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_ai_models(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_ai_models'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_ai_model(body_json: str) -> str:
    """
    Create or update AI model (saveAiModel)  # noqa: E501

Creates or updates an AI model record.  • **Create:** Omit the `id` to create a new record. The platform assigns a UUID to the new record and returns it in the `id` field of the response.  • **Update:** Include an existing `id` to modify that record. If no matching record exists, the API responds with **404 Not Found**.  Tenant ID for the AI model will be taken from the authenticated user making the request, regardless of any value provided in the request body.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_ai_model(body=deserialize_param(body_json, 'AiModel'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_ai_model'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def send_chat_request(body_json: str) -> str:
    """
    Send request to AI chat model (sendChatRequest)  # noqa: E501

Submits a single prompt - made up of an optional system message and a required user message - to the specified AI chat model and returns either the generated answer or an error envelope.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.send_chat_request(body=deserialize_param(body_json, 'TbChatRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'send_chat_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_ai_model_by_id )
    mcp.tool()( get_ai_model_by_id )
    mcp.tool()( get_ai_models )
    mcp.tool()( save_ai_model )
    mcp.tool()( send_chat_request )
