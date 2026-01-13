import json
from typing import Optional
from .shared import get_client, deserialize_param, format_response, ApiException


def check_two_fa_verification_code(provider_type: str, verification_code: str) -> str:
    """
    Check 2FA verification code (checkTwoFaVerificationCode)  # noqa: E501

Checks 2FA verification code, and if it is correct the method returns a regular access and refresh token pair.  The API method is rate limited (using rate limit config from TwoFactorAuthSettings), and also will block a user after X unsuccessful verification attempts if such behavior is configured (in TwoFactorAuthSettings).  Will return a Bad Request error if provider is not configured for usage, and Too Many Requests error if rate limits are exceeded.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str provider_type: providerType (required)
:param str verification_code: verificationCode (required)
:return: JwtPair
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.check_two_fa_verification_code(provider_type=provider_type, verification_code=verification_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'check_two_fa_verification_code'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_oauth2_client(id_json: str) -> str:
    """
    Delete oauth2 client (deleteOauth2Client)  # noqa: E501

Deletes the oauth2 client. Referencing non-existing oauth2 client Id will cause an error.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_oauth2_client(id=deserialize_param(id_json, 'OAuth2ClientId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_oauth2_client'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_two_fa_account_config(provider_type: str) -> str:
    """
    Delete 2FA account config (deleteTwoFaAccountConfig)  # noqa: E501

Delete 2FA config for a given 2FA provider type.  Returns whole account's 2FA settings object.   Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str provider_type: providerType (required)
:return: AccountTwoFaSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.delete_two_fa_account_config(provider_type=provider_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'delete_two_fa_account_config'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def generate_two_fa_account_config(provider_type: str) -> str:
    """
    Generate 2FA account config (generateTwoFaAccountConfig)  # noqa: E501

Generate new 2FA account config template for specified provider type.   For TOTP, this will return a corresponding account config template with a generated OTP auth URL (with new random secret key for each API call) that can be then converted to a QR code to scan with an authenticator app. Example: ``` {   "providerType": "TOTP",   "useByDefault": false,   "authUrl": "otpauth://totp/TB%202FA:tenant@thingsboard.org?issuer=TB+2FA&secret=PNJDNWJVAK4ZTUYT7RFGPQLXA7XGU7PX" } ```  For EMAIL, the generated config will contain email from user's account: ``` {   "providerType": "EMAIL",   "useByDefault": false,   "email": "tenant@thingsboard.org" } ```  For SMS 2FA this method will just return a config with empty/default values as there is nothing to generate/preset: ``` {   "providerType": "SMS",   "useByDefault": false,   "phoneNumber": null } ```  Will throw an error (Bad Request) if the provider is not configured for usage.   Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str provider_type: 2FA provider type to generate new account config for (required)
:return: TwoFaAccountConfig
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.generate_two_fa_account_config(provider_type=provider_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'generate_two_fa_account_config'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_account_two_fa_settings() -> str:
    """
    Get account 2FA settings (getAccountTwoFaSettings)  # noqa: E501

Get user's account 2FA configuration. Configuration contains configs for different 2FA providers.  Example: ``` {   "configs": {     "EMAIL": {       "providerType": "EMAIL",       "useByDefault": true,       "email": "tenant@thingsboard.org"     },     "TOTP": {       "providerType": "TOTP",       "useByDefault": false,       "authUrl": "otpauth://totp/TB%202FA:tenant@thingsboard.org?issuer=TB+2FA&secret=P6Z2TLYTASOGP6LCJZAD24ETT5DACNNX"     },     "SMS": {       "providerType": "SMS",       "useByDefault": false,       "phoneNumber": "+380501253652"     }   } } ```  Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: AccountTwoFaSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_account_two_fa_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_account_two_fa_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_authorization_url() -> str:
    """
    Redirect user to mail provider login page.   # noqa: E501

After user logged in and provided accessprovider sends authorization code to specified redirect uri.)  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: str
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_authorization_url()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_authorization_url'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_available_two_fa_providers() -> str:
    """
    Get available 2FA providers (getAvailableTwoFaProviders)  # noqa: E501

Get the list of provider types available for user to use (the ones configured by tenant or sysadmin). Example of response: ``` [   "TOTP",   "EMAIL",   "SMS" ] ```  Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: list[str]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_available_two_fa_providers()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_available_two_fa_providers'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_available_two_fa_providers_v1() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_available_two_fa_providers_v1()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_available_two_fa_providers_v1'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_current_o_auth2_info() -> str:
    """
    Get current OAuth2 settings (getCurrentOAuth2Info)  # noqa: E501

  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: OAuth2Info
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_current_o_auth2_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_current_o_auth2_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_o_auth2_client_by_id(id_json: str) -> str:
    """
    Get OAuth2 Client by id (getOAuth2ClientById)  # noqa: E501

  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str id: (required)
:return: OAuth2Client
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_o_auth2_client_by_id(id=deserialize_param(id_json, 'OAuth2ClientId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_o_auth2_client_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_o_auth2_clients(pkg_name: Optional[str] = None, platform: Optional[str] = None) -> str:
    """
    Get OAuth2 clients (getOAuth2Clients)  # noqa: E501

Get the list of OAuth2 clients to log in with, available for such domain scheme (HTTP or HTTPS) (if x-forwarded-proto request header is present - the scheme is known from it) and domain name and port (port may be known from x-forwarded-port header)  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str pkg_name: Mobile application package name, to find OAuth2 clients where there is configured mobile application with such package name
:param str platform: Platform type to search OAuth2 clients for which the usage with this platform type is allowed in the settings. If platform type is not one of allowable values - it will just be ignored
:return: list[OAuth2ClientInfo]
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_o_auth2_clients(pkg_name=pkg_name, platform=platform)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_o_auth2_clients'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_platform_two_fa_settings() -> str:
    """
    Get platform 2FA settings (getPlatformTwoFaSettings)  # noqa: E501

Get platform settings for 2FA. The settings are described for savePlatformTwoFaSettings API method. If 2FA is not configured, then an empty response will be returned.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:return: PlatformTwoFaSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.get_platform_two_fa_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'get_platform_two_fa_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def mobile_app_update_oauth2_clients(body_json: str, id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.mobile_app_update_oauth2_clients(body=json.loads(body_json) if body_json else None, id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'mobile_app_update_oauth2_clients'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def request_two_fa_verification_code(provider_type: str) -> str:
    """
    Request 2FA verification code (requestTwoFaVerificationCode)  # noqa: E501

Request 2FA verification code.  To make a request to this endpoint, you need an access token with the scope of PRE_VERIFICATION_TOKEN, which is issued on username/password auth if 2FA is enabled.  The API method is rate limited (using rate limit config from TwoFactorAuthSettings). Will return a Bad Request error if provider is not configured for usage, and Too Many Requests error if rate limits are exceeded.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str provider_type: providerType (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.request_two_fa_verification_code(provider_type=provider_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'request_two_fa_verification_code'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_o_auth2_client(body: Optional[str] = None) -> str:
    """
    Save OAuth2 Client (saveOAuth2Client)  # noqa: E501

  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param OAuth2Client body: (required)
:return: OAuth2Client
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_o_auth2_client(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_o_auth2_client'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_o_auth2_info(body: Optional[str] = None) -> str:
    """
    Save OAuth2 settings (saveOAuth2Info)  # noqa: E501

  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param OAuth2Info body:
:return: OAuth2Info
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_o_auth2_info(body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_o_auth2_info'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_platform_two_fa_settings(body_json: str) -> str:
    """
    Save platform 2FA settings (savePlatformTwoFaSettings)  # noqa: E501

Save 2FA settings for platform. The settings have following properties: - `providers` - the list of 2FA providers' configs. Users will only be allowed to use 2FA providers from this list.   - `minVerificationCodeSendPeriod` - minimal period in seconds to wait after verification code send request to send next request.  - `verificationCodeCheckRateLimit` - rate limit configuration for verification code checking. The format is standard: 'amountOfRequests:periodInSeconds'. The value of '1:60' would limit verification code checking requests to one per minute. - `maxVerificationFailuresBeforeUserLockout` - maximum number of verification failures before a user gets disabled. - `totalAllowedTimeForVerification` - total amount of time in seconds allotted for verification. Basically, this property sets a lifetime for pre-verification token. If not set, default value of 30 minutes is used.   TOTP 2FA provider config has following settings: - `issuerName` - issuer name that will be displayed in an authenticator app near a username. Must not be blank.  For SMS 2FA provider: - `smsVerificationMessageTemplate` - verification message template.  Available template variables are ${code} and ${userEmail}. It must not be blank and must contain verification code variable. - `verificationCodeLifetime` - verification code lifetime in seconds. Required to be positive.  For EMAIL provider type: - `verificationCodeLifetime` - the same as for SMS.  Example of the settings: ``` {   "providers": [     {       "providerType": "TOTP",       "issuerName": "TB"     },     {       "providerType": "EMAIL",       "verificationCodeLifetime": 60     },     {       "providerType": "SMS",       "verificationCodeLifetime": 60,       "smsVerificationMessageTemplate": "Here is your verification code: ${code}"     }   ],   "minVerificationCodeSendPeriod": 60,   "verificationCodeCheckRateLimit": "4.1.0",   "maxVerificationFailuresBeforeUserLockout": 10,   "totalAllowedTimeForVerification": 600 } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param PlatformTwoFaSettings body:
:return: PlatformTwoFaSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.save_platform_two_fa_settings(body=deserialize_param(body_json, 'PlatformTwoFaSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'save_platform_two_fa_settings'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def submit_two_fa_account_config(body_json: str) -> str:
    """
    Submit 2FA account config (submitTwoFaAccountConfig)  # noqa: E501

Submit 2FA account config to prepare for a future verification. Basically, this method will send a verification code for a given account config, if this has sense for a chosen 2FA provider. This code is needed to then verify and save the account config.  Example of EMAIL 2FA account config: ``` {   "providerType": "EMAIL",   "useByDefault": true,   "email": "separate-email-for-2fa@thingsboard.org" } ```  Example of SMS 2FA account config: ``` {   "providerType": "SMS",   "useByDefault": false,   "phoneNumber": "+38012312321" } ```  For TOTP this method does nothing.  Will throw an error (Bad Request) if submitted account config is not valid, or if the provider is not configured for usage.   Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param TwoFaAccountConfig body:
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.submit_two_fa_account_config(body=deserialize_param(body_json, 'TwoFaAccountConfig'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'submit_two_fa_account_config'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_oauth2_clients(body_json: str, id: str) -> str:
    """
    Update oauth2 clients (updateOauth2Clients)  # noqa: E501

Update oauth2 clients of the specified mobile app.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param list[str] body: (required)
:param str id: (required)
:return: None
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.update_oauth2_clients(body=json.loads(body_json) if body_json else None, id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'update_oauth2_clients'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_two_fa_account_config(provider_type: str, body_json: str) -> str:
    """
    Update 2FA account config (updateTwoFaAccountConfig)  # noqa: E501

Update config for a given provider type.  Update request example: ``` {   "useByDefault": true } ``` Returns whole account's 2FA settings object.   Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param str provider_type: providerType (required)
:param TwoFaAccountConfigUpdateRequest body:
:return: AccountTwoFaSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.update_two_fa_account_config(provider_type=provider_type, body=deserialize_param(body_json, 'TwoFaAccountConfigUpdateRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'update_two_fa_account_config'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def verify_and_save_two_fa_account_config(body_json: str, verification_code: str) -> str:
    """
    Verify and save 2FA account config (verifyAndSaveTwoFaAccountConfig)  # noqa: E501

Checks the verification code for submitted config, and if it is correct, saves the provided account config.   Returns whole account's 2FA settings object. Will throw an error (Bad Request) if the provider is not configured for usage.   Available for any authorized user.   # noqa: E501
This method makes a synchronous HTTP request by default. To make an
asynchronous HTTP request, please pass async_req=True

:param async_req bool
:param TwoFaAccountConfig body:
:param str verification_code: verificationCode
:return: AccountTwoFaSettings
         If the method is called asynchronously,
         returns the request thread.
    """
    try:
        client = get_client()
        result = client.verify_and_save_two_fa_account_config(body=deserialize_param(body_json, 'TwoFaAccountConfig'), verification_code=verification_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: Your role cannot perform 'verify_and_save_two_fa_account_config'."
        if e.status == 401:
            return "AUTH ERROR: Session expired."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    """Register tools with FastMCP server"""
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
