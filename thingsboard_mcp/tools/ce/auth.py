import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def activate_user(body_json: str, send_activation_mail: bool) -> str:
    """
    Activate User  # noqa: E501

Checks the activation token and updates corresponding user password in the database. Now the user may start using his password to login. The response already contains the [JWT](https://jwt.io) activation and refresh tokens, to simplify the user activation flow and avoid asking user to input password again after activation. If token is valid, returns the object that contains [JWT](https://jwt.io/) access and refresh tokens. If token is not valid, returns '404 Bad Request'.  # noqa: E501

    ---------------------------
    Expected JSON Structure (ActivateUserRequest):
    - `activate_token` (str)
    - `password` (str)
    """
    try:
        client = get_client()
        result = client.activate_user(body=deserialize_param(body_json, 'ActivateUserRequest'), send_activation_mail=send_activation_mail)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'activate_user'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def change_password(body_json: str = None) -> str:
    """
    Change password for current User (changePassword)  # noqa: E501

Change the password for the User which credentials are used to perform this REST API call. Be aware that previously generated [JWT](https://jwt.io/) tokens will be still valid until they expire.  # noqa: E501

    ---------------------------
    Expected JSON Structure (ChangePasswordRequest):
    - `current_password` (str)
    - `new_password` (str)
    """
    try:
        client = get_client()
        result = client.change_password(body=deserialize_param(body_json, 'ChangePasswordRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'change_password'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def check_activate_token(activate_token: str) -> str:
    """
    Check Activate User Token (checkActivateToken)  # noqa: E501

Checks the activation token and forwards user to 'Create Password' page. If token is valid, returns '303 See Other' (redirect) response code with the correct address of 'Create Password' page and same 'activateToken' specified in the URL parameters. If token is not valid, returns '409 Conflict'.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.check_activate_token(activate_token=activate_token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'check_activate_token'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def check_reset_token(reset_token: str) -> str:
    """
    Check password reset token (checkResetToken)  # noqa: E501

Checks the password reset token and forwards user to 'Reset Password' page. If token is valid, returns '303 See Other' (redirect) response code with the correct address of 'Reset Password' page and same 'resetToken' specified in the URL parameters. If token is not valid, returns '409 Conflict'.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.check_reset_token(reset_token=reset_token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'check_reset_token'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_user() -> str:
    """
    Get current User (getUser)  # noqa: E501

Get the information about the User which credentials are used to perform this REST API call.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_user()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_user'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_user_password_policy() -> str:
    """
    Get the current User password policy (getUserPasswordPolicy)  # noqa: E501

API call to get the password policy for the password validation form(s).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_user_password_policy()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_user_password_policy'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def request_reset_password_by_email(body_json: str = None) -> str:
    """
    Request reset password email (requestResetPasswordByEmail)  # noqa: E501

Request to send the reset password email if the user with specified email address is present in the database. Always return '200 OK' status for security purposes.  # noqa: E501

    ---------------------------
    Expected JSON Structure (ResetPasswordEmailRequest):
    - `email` (str)
    """
    try:
        client = get_client()
        result = client.request_reset_password_by_email(body=deserialize_param(body_json, 'ResetPasswordEmailRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'request_reset_password_by_email'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def reset_password(body_json: str = None) -> str:
    """
    Reset password (resetPassword)  # noqa: E501

Checks the password reset token and updates the password. If token is valid, returns the object that contains [JWT](https://jwt.io/) access and refresh tokens. If token is not valid, returns '404 Bad Request'.  # noqa: E501

    ---------------------------
    Expected JSON Structure (ResetPasswordRequest):
    - `reset_token` (str)
    - `password` (str)
    """
    try:
        client = get_client()
        result = client.reset_password(body=deserialize_param(body_json, 'ResetPasswordRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'reset_password'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( activate_user )
    mcp.tool()( change_password )
    mcp.tool()( check_activate_token )
    mcp.tool()( check_reset_token )
    mcp.tool()( get_user )
    mcp.tool()( get_user_password_policy )
    mcp.tool()( request_reset_password_by_email )
    mcp.tool()( reset_password )
