import json
import tb_rest_client.models.models_pe as models
from ...shared import get_client, deserialize_param, format_response, ApiException


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

def delete_oauth2_client(id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.delete_oauth2_client(id=deserialize_param(id_json, 'OAuth2ClientId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_oauth2_client'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_two_fa_account_config(provider_type: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.delete_two_fa_account_config(provider_type=provider_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_two_fa_account_config'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def generate_two_fa_account_config(provider_type: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.generate_two_fa_account_config(provider_type=provider_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'generate_two_fa_account_config'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_account_two_fa_settings() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_account_two_fa_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_account_two_fa_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_authorization_url() -> str:
    """
    Redirect user to mail provider login page.   # noqa: E501

After user logged in and provided accessprovider sends authorization code to specified redirect uri.)  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_authorization_url()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_authorization_url'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_available_two_fa_providers() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_available_two_fa_providers()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_available_two_fa_providers'."
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

def get_current_o_auth2_info() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_current_o_auth2_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_current_o_auth2_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_o_auth2_client_by_id(id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_o_auth2_client_by_id(id=deserialize_param(id_json, 'OAuth2ClientId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_o_auth2_client_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_o_auth2_clients(pkg_name: Optional[str] = None, platform: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_o_auth2_clients(pkg_name=pkg_name, platform=platform)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_o_auth2_clients'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_platform_two_fa_settings() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_platform_two_fa_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_platform_two_fa_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def mobile_app_update_oauth2_clients(body_json: str, id: str) -> str:
    """
    Update oauth2 clients (updateOauth2Clients)  # noqa: E501

Update oauth2 clients of the specified mobile app.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.mobile_app_update_oauth2_clients(body=json.loads(body_json) if body_json else None, id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'mobile_app_update_oauth2_clients'."
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

def save_o_auth2_client(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.save_o_auth2_client(body=deserialize_param(body_json, 'OAuth2Client'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_o_auth2_client'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_o_auth2_info(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.save_o_auth2_info(body=deserialize_param(body_json, 'OAuth2Info'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_o_auth2_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_platform_two_fa_settings(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.save_platform_two_fa_settings(body=deserialize_param(body_json, 'PlatformTwoFaSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_platform_two_fa_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def submit_two_fa_account_config(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.submit_two_fa_account_config(body=deserialize_param(body_json, 'TwoFaAccountConfig'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'submit_two_fa_account_config'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_oauth2_clients(body_json: str, id: str) -> str:
    """
    Update oauth2 clients (updateOauth2Clients)  # noqa: E501

Update oauth2 clients for the specified domain.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_oauth2_clients(body=json.loads(body_json) if body_json else None, id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_oauth2_clients'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_two_fa_account_config(provider_type: str, body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.update_two_fa_account_config(provider_type=provider_type, body=deserialize_param(body_json, 'TwoFaAccountConfigUpdateRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_two_fa_account_config'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def verify_and_save_two_fa_account_config(body_json: str, verification_code: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.verify_and_save_two_fa_account_config(body=deserialize_param(body_json, 'TwoFaAccountConfig'), verification_code=verification_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'verify_and_save_two_fa_account_config'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def register(mcp):
    mcp.tool()( check_two_fa_verification_code )
    mcp.tool()( delete_oauth2_client )
    mcp.tool()( delete_two_fa_account_config )
    mcp.tool()( generate_two_fa_account_config )
    mcp.tool()( get_account_two_fa_settings )
    mcp.tool()( get_authorization_url )
    mcp.tool()( get_available_two_fa_providers )
    mcp.tool()( get_available_two_fa_providers_v1 )
    mcp.tool()( get_current_o_auth2_info )
    mcp.tool()( get_o_auth2_client_by_id )
    mcp.tool()( get_o_auth2_clients )
    mcp.tool()( get_platform_two_fa_settings )
    mcp.tool()( mobile_app_update_oauth2_clients )
    mcp.tool()( request_two_fa_verification_code )
    mcp.tool()( save_o_auth2_client )
    mcp.tool()( save_o_auth2_info )
    mcp.tool()( save_platform_two_fa_settings )
    mcp.tool()( submit_two_fa_account_config )
    mcp.tool()( update_oauth2_clients )
    mcp.tool()( update_two_fa_account_config )
    mcp.tool()( verify_and_save_two_fa_account_config )
