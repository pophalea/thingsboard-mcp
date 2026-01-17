import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_self_registration_params(domain_name: str) -> str:
    """
    deleteSelfRegistrationParams  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_self_registration_params(domain_name=domain_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_self_registration_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_web_self_registration_params() -> str:
    """
    deleteWebSelfRegistrationParams  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_web_self_registration_params()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_web_self_registration_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_privacy_policy() -> str:
    """
    Get Privacy Policy for Self Registration form (getPrivacyPolicy)  # noqa: E501

Fetch the Privacy Policy based on the domain name from the request. Available for non-authorized users.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_privacy_policy()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_privacy_policy'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_self_registration_params() -> str:
    """
    Get Self Registration parameters (getSelfRegistrationParams)  # noqa: E501

Fetch the Self Registration parameters object for the tenant of the current user.   Available for users with 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_self_registration_params()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_self_registration_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_sign_up_self_registration_params(pkg_name: Optional[str] = None) -> str:
    """
    Get Self Registration form parameters without authentication (getSignUpSelfRegistrationParams)  # noqa: E501

Fetch the Self Registration parameters based on the domain name from the request. Available for non-authorized users. Contains the information to customize the sign-up form.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_sign_up_self_registration_params(pkg_name=pkg_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_sign_up_self_registration_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_terms_of_use() -> str:
    """
    Get Terms of Use for Self Registration form (getTermsOfUse)  # noqa: E501

Fetch the Terms of Use based on the domain name from the request. Available for non-authorized users.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_terms_of_use()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_terms_of_use'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_web_self_registration_params() -> str:
    """
    Get Self Registration parameters (getSelfRegistrationParams)  # noqa: E501

Fetch the Self Registration parameters object for the tenant of the current user.   Available for users with 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_web_self_registration_params()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_web_self_registration_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_self_registration_params(body_json: str = None) -> str:
    """
    Create Or Update Self Registration parameters (saveSelfRegistrationParams)  # noqa: E501

Creates or Updates the Self Registration parameters. When creating, platform generates Admin Settings Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Admin Settings Id will be present in the response. Specify existing Admin Settings Id to update the Self Registration parameters. Referencing non-existing Admin Settings Id will cause 'Not Found' error.  Self Registration allows users to signup for using the platform and automatically create a Customer account for them. You may configure default dashboard and user roles that will be assigned for this Customer. This allows you to build out-of-the-box solutions for customers. Ability to white-label the login and main pages helps to brand the platform.  Available for users with 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_self_registration_params(body=deserialize_param(body_json, 'SelfRegistrationParams'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_self_registration_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_web_self_registration_params(body_json: str) -> str:
    """
    Create Or Update Self Registration parameters (saveSelfRegistrationParams)  # noqa: E501

Creates or Updates the Self Registration parameters. When creating, platform generates Admin Settings Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Admin Settings Id will be present in the response. Specify existing Admin Settings Id to update the Self Registration parameters. Referencing non-existing Admin Settings Id will cause 'Not Found' error.  Self Registration allows users to signup for using the platform and automatically create a Customer account for them. You may configure default dashboard and user roles that will be assigned for this Customer. This allows you to build out-of-the-box solutions for customers. Ability to white-label the login and main pages helps to brand the platform.  Available for users with 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_web_self_registration_params(body=deserialize_param(body_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_web_self_registration_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_self_registration_params )
    mcp.tool()( delete_web_self_registration_params )
    mcp.tool()( get_privacy_policy )
    mcp.tool()( get_self_registration_params )
    mcp.tool()( get_sign_up_self_registration_params )
    mcp.tool()( get_terms_of_use )
    mcp.tool()( get_web_self_registration_params )
    mcp.tool()( save_self_registration_params )
    mcp.tool()( save_web_self_registration_params )
