import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_client_registration_template(client_registration_template_id_json: str) -> str:
    """
    Delete OAuth2 client registration template by id (deleteClientRegistrationTemplate)  Available for users with 'SYS_ADMIN' authority.  # noqa: E501

Client registration template is OAuth2 provider configuration template with default settings for registering new OAuth2 clients  # noqa: E501

    ---------------------------
    Expected JSON Structure (EntityId):
    - `id` (str)
    - `entity_type` (str)
    """
    try:
        client = get_client()
        result = client.delete_client_registration_template(client_registration_template_id=deserialize_param(client_registration_template_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_client_registration_template'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_client_registration_templates1() -> str:
    """
    Get the list of all OAuth2 client registration templates (getClientRegistrationTemplates)  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501

Client registration template is OAuth2 provider configuration template with default settings for registering new OAuth2 clients  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_client_registration_templates1()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_client_registration_templates1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_client_registration_template(body_json: str = None) -> str:
    """
    Create or update OAuth2 client registration template (saveClientRegistrationTemplate)  Available for users with 'SYS_ADMIN' authority.  # noqa: E501

Client registration template is OAuth2 provider configuration template with default settings for registering new OAuth2 clients  # noqa: E501

    ---------------------------
    Expected JSON Structure (OAuth2ClientRegistrationTemplate):
    - `id` (OAuth2ClientRegistrationTemplateId)
    - `created_time` (int)
    - `provider_id` (str)
    - `mapper_config` (OAuth2MapperConfig)
    - `authorization_uri` (str)
    - `access_token_uri` (str)
    - `scope` (list[str])
    - `user_info_uri` (str)
    - `user_name_attribute_name` (str)
    - `jwk_set_uri` (str)
    - `client_authentication_method` (str)
    - `comment` (str)
    - `login_button_icon` (str)
    - `login_button_label` (str)
    - `help_link` (str)
    - `name` (str)
    - `additional_info` (JsonNode)
    """
    try:
        client = get_client()
        result = client.save_client_registration_template(body=deserialize_param(body_json, 'OAuth2ClientRegistrationTemplate'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_client_registration_template'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_client_registration_template )
    mcp.tool()( get_client_registration_templates1 )
    mcp.tool()( save_client_registration_template )
