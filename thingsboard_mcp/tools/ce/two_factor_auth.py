import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def check_two_fa_verification_code(provider_type: str, verification_code: str) -> str:
    """
    Check 2FA verification code (checkTwoFaVerificationCode)  # noqa: E501

Checks 2FA verification code, and if it is correct the method returns a regular access and refresh token pair.  The API method is rate limited (using rate limit config from TwoFactorAuthSettings), and also will block a user after X unsuccessful verification attempts if such behavior is configured (in TwoFactorAuthSettings).  Will return a Bad Request error if provider is not configured for usage, and Too Many Requests error if rate limits are exceeded.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.check_two_fa_verification_code(provider_type=provider_type, verification_code=verification_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'check_two_fa_verification_code'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_available_two_fa_providers_v1() -> str:
    """
    Get available 2FA providers (getAvailableTwoFaProviders)  # noqa: E501

Get the list of 2FA provider infos available for user to use. Example: ``` [   {     "type": "EMAIL",     "default": true,     "contact": "ab*****ko@gmail.com"   },   {     "type": "TOTP",     "default": false,     "contact": null   },   {     "type": "SMS",     "default": false,     "contact": "+38********12"   } ] ```  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_available_two_fa_providers_v1()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_available_two_fa_providers_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def request_two_fa_verification_code(provider_type: str) -> str:
    """
    Request 2FA verification code (requestTwoFaVerificationCode)  # noqa: E501

Request 2FA verification code.  To make a request to this endpoint, you need an access token with the scope of PRE_VERIFICATION_TOKEN, which is issued on username/password auth if 2FA is enabled.  The API method is rate limited (using rate limit config from TwoFactorAuthSettings). Will return a Bad Request error if provider is not configured for usage, and Too Many Requests error if rate limits are exceeded.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.request_two_fa_verification_code(provider_type=provider_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'request_two_fa_verification_code'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( check_two_fa_verification_code )
    mcp.tool()( get_available_two_fa_providers_v1 )
    mcp.tool()( request_two_fa_verification_code )
