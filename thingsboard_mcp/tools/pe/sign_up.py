import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def accept_terms_of_use() -> str:
    """
    Accept Terms of Use (acceptTermsOfUse)  # noqa: E501

Accept Terms of Use by the current user.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.accept_terms_of_use()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'accept_terms_of_use'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def activate_email(email_code: str, pkg_name: Optional[str] = None) -> str:
    """
    Activate User using code from Email (activateEmail)  # noqa: E501

Activate the user using code(link) from the activation email. Validates the code an redirects according to the signup flow. Checks that user was not activated yet.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.activate_email(email_code=email_code, pkg_name=pkg_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'activate_email'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def activate_user_by_email_code(email_code: str, pkg_name: Optional[str] = None) -> str:
    """
    Activate and login using code from Email (activateUserByEmailCode)  # noqa: E501

Activate the user using code(link) from the activation email and return the JWT Token. Sends the notification and email about user activation. Checks that user was not activated yet.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.activate_user_by_email_code(email_code=email_code, pkg_name=pkg_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'activate_user_by_email_code'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def mobile_login(pkg_name: str) -> str:
    """
    Mobile Login redirect (mobileLogin)  # noqa: E501

This method generates redirect to the special link that is handled by mobile application. Useful for email verification flow on mobile app.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.mobile_login(pkg_name=pkg_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'mobile_login'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def privacy_policy_accepted() -> str:
    """
    Check privacy policy (privacyPolicyAccepted)  # noqa: E501

Checks that current user accepted the privacy policy.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.privacy_policy_accepted()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'privacy_policy_accepted'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def resend_email_activation(email: str, pkg_name: Optional[str] = None) -> str:
    """
    Resend Activation Email (resendEmailActivation)  # noqa: E501

Request to resend the activation email for the user. Checks that user was not activated yet.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.resend_email_activation(email=email, pkg_name=pkg_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'resend_email_activation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def sign_up(body_json: str = None) -> str:
    """
    User Sign Up (signUp)  # noqa: E501

Process user sign up request. Creates the Customer and corresponding User based on self Registration parameters for the domain. See [Self Registration Controller](/swagger-ui.html#/self-registration-controller) for more details.  The result is either 'SUCCESS' or 'INACTIVE_USER_EXISTS'. If Success, the user will receive an email with instruction to activate the account. The content of the email is customizable via the mail templates.  # noqa: E501

    ---------------------------
    Expected JSON Structure (SignUpRequest):
    - `first_name` (str)
    - `last_name` (str)
    - `email` (str)
    - `password` (str)
    - `recaptcha_response` (str)
    - `pkg_name` (str)
    - `app_secret` (str)
    """
    try:
        client = get_client()
        result = client.sign_up(body=deserialize_param(body_json, 'SignUpRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sign_up'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def terms_of_use_accepted() -> str:
    """
    Check Terms Of User (termsOfUseAccepted)  # noqa: E501

Checks that current user accepted the privacy policy.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.terms_of_use_accepted()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'terms_of_use_accepted'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( accept_terms_of_use )
    mcp.tool()( activate_email )
    mcp.tool()( activate_user_by_email_code )
    mcp.tool()( mobile_login )
    mcp.tool()( privacy_policy_accepted )
    mcp.tool()( resend_email_activation )
    mcp.tool()( sign_up )
    mcp.tool()( terms_of_use_accepted )
