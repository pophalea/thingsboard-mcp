import json
from typing import Optional
import tb_rest_client.models.models_ce as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def auto_commit_settings_exists() -> str:
    """
    Check auto commit settings exists (autoCommitSettingsExists)  # noqa: E501

Check whether the auto commit settings exists.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.auto_commit_settings_exists()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'auto_commit_settings_exists'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def check_repository_access(body_json: str = None) -> str:
    """
    Check repository access (checkRepositoryAccess)  # noqa: E501

Attempts to check repository access.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.check_repository_access(body=deserialize_param(body_json, 'RepositorySettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'check_repository_access'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def check_updates() -> str:
    """
    Check for new Platform Releases (checkUpdates)  # noqa: E501

Check notifications about new platform releases.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.check_updates()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'check_updates'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def code_processing_url(code: str, state: str) -> str:
    """
    codeProcessingUrl  # noqa: E501
    """
    try:
        client = get_client()
        result = client.code_processing_url(code=code, state=state)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'code_processing_url'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_auto_commit_settings() -> str:
    """
    Delete auto commit settings (deleteAutoCommitSettings)  # noqa: E501

Deletes the auto commit settings.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_auto_commit_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_auto_commit_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_repository_settings() -> str:
    """
    Delete repository settings (deleteRepositorySettings)  # noqa: E501

Deletes the repository settings.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_repository_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_repository_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_admin_settings(key: str) -> str:
    """
    Get the Administration Settings object using key (getAdminSettings)  # noqa: E501

Get the Administration Settings object using specified string key. Referencing non-existing key will cause an error.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_admin_settings(key=key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_admin_settings'."
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


def get_auto_commit_settings() -> str:
    """
    Get auto commit settings (getAutoCommitSettings)  # noqa: E501

Get the auto commit settings object.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_auto_commit_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_auto_commit_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_features_info() -> str:
    """
    Get features info (getFeaturesInfo)  # noqa: E501

Get information about enabled/disabled features.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_features_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_features_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_jwt_setting() -> str:
    """
    Get the JWT Settings object (getJwtSettings)  # noqa: E501

Get the JWT Settings object that contains JWT token policy, etc.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_jwt_setting()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_jwt_setting'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_mail_processing_url() -> str:
    """
    Get OAuth2 log in processing URL (getMailProcessingUrl)  # noqa: E501

Returns the URL enclosed in double quotes. After successful authentication with OAuth2 provider and user consent for requested scope, it makes a redirect to this path so that the platform can do further log in processing and generating access tokens.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mail_processing_url()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mail_processing_url'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_repository_settings() -> str:
    """
    Get repository settings (getRepositorySettings)  # noqa: E501

Get the repository settings object.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_repository_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_repository_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_repository_settings_info() -> str:
    """
    getRepositorySettingsInfo  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_repository_settings_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_repository_settings_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_security_settings() -> str:
    """
    Get the Security Settings object  # noqa: E501

Get the Security Settings object that contains password policy, etc.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_security_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_security_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_system_info() -> str:
    """
    Get system info (getSystemInfo)  # noqa: E501

Get main information about system.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_system_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_system_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def repository_settings_exists() -> str:
    """
    Check repository settings exists (repositorySettingsExists)  # noqa: E501

Check whether the repository settings exists.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.repository_settings_exists()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'repository_settings_exists'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_admin_settings(body_json: str = None) -> str:
    """
    Get the Administration Settings object using key (getAdminSettings)  # noqa: E501

Creates or Updates the Administration Settings. Platform generates random Administration Settings Id during settings creation. The Administration Settings Id will be present in the response. Specify the Administration Settings Id when you would like to update the Administration Settings. Referencing non-existing Administration Settings Id will cause an error.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_admin_settings(body=deserialize_param(body_json, 'AdminSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_admin_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_auto_commit_settings(body_json: str = None) -> str:
    """
    Creates or Updates the auto commit settings (saveAutoCommitSettings)  # noqa: E501

Creates or Updates the auto commit settings object.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_auto_commit_settings(body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_auto_commit_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_jwt_settings(body_json: str = None) -> str:
    """
    Update JWT Settings (saveJwtSettings)  # noqa: E501

Updates the JWT Settings object that contains JWT token policy, etc. The tokenSigningKey field is a Base64 encoded string.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_jwt_settings(body=deserialize_param(body_json, 'JwtSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_jwt_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_repository_settings(body_json: str = None) -> str:
    """
    Creates or Updates the repository settings (saveRepositorySettings)  # noqa: E501

Creates or Updates the repository settings object.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_repository_settings(body=deserialize_param(body_json, 'RepositorySettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_repository_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_security_settings(body_json: str = None) -> str:
    """
    Update Security Settings (saveSecuritySettings)  # noqa: E501

Updates the Security Settings object that contains password policy, etc.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_security_settings(body=deserialize_param(body_json, 'SecuritySettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_security_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def send_test_mail(body_json: str = None) -> str:
    """
    Send test email (sendTestMail)  # noqa: E501

Attempts to send test email to the System Administrator User using Mail Settings provided as a parameter. You may change the 'To' email in the user profile of the System Administrator.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.send_test_mail(body=deserialize_param(body_json, 'AdminSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'send_test_mail'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def send_test_sms(body_json: str = None) -> str:
    """
    Send test sms (sendTestMail)  # noqa: E501

Attempts to send test sms to the System Administrator User using SMS Settings and phone number provided as a parameters of the request.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.send_test_sms(body=deserialize_param(body_json, 'TestSmsRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'send_test_sms'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( auto_commit_settings_exists )
    mcp.tool()( check_repository_access )
    mcp.tool()( check_updates )
    mcp.tool()( code_processing_url )
    mcp.tool()( delete_auto_commit_settings )
    mcp.tool()( delete_repository_settings )
    mcp.tool()( get_admin_settings )
    mcp.tool()( get_authorization_url )
    mcp.tool()( get_auto_commit_settings )
    mcp.tool()( get_features_info )
    mcp.tool()( get_jwt_setting )
    mcp.tool()( get_mail_processing_url )
    mcp.tool()( get_repository_settings )
    mcp.tool()( get_repository_settings_info )
    mcp.tool()( get_security_settings )
    mcp.tool()( get_system_info )
    mcp.tool()( repository_settings_exists )
    mcp.tool()( save_admin_settings )
    mcp.tool()( save_auto_commit_settings )
    mcp.tool()( save_jwt_settings )
    mcp.tool()( save_repository_settings )
    mcp.tool()( save_security_settings )
    mcp.tool()( send_test_mail )
    mcp.tool()( send_test_sms )
