import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def download_full_translation(locale_code: str) -> str:
    """
    Download end-user all-to-one translation (downloadFullTranslation)  # noqa: E501

Fetch the end-user translation for the specified locale. The result is a json file with merged user custom translation, system language translation and default locale translation.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_full_translation(locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_full_translation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_available_java_locales() -> str:
    """
    Get list of available java locales (getAvailableJavaLocales)  # noqa: E501

The result is map where key is locale code and value is locale language and country  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_available_java_locales()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_available_java_locales'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_available_locales() -> str:
    """
    Get list of available locales (getAvailableLocales)  # noqa: E501

Fetch the list of customized locales from all levels  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_available_locales()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_available_locales'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_full_translation(locale_code: str, if_none_match: Optional[str] = None, accept_encoding: Optional[str] = None) -> str:
    """
    Get end-user all-to-one translation (getFullTranslation)  # noqa: E501

Fetch the end-user translation for specified locale. The result is the merge of user custom translation, system language translation and default locale translation.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_full_translation(locale_code=locale_code, if_none_match=if_none_match, accept_encoding=accept_encoding)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_full_translation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_login_page_translation(locale_code: str, if_none_match: Optional[str] = None, accept_encoding: Optional[str] = None) -> str:
    """
    Get system translation for login page  # noqa: E501

Fetch the end-user translation for specified locale.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_login_page_translation(locale_code=locale_code, if_none_match=if_none_match, accept_encoding=accept_encoding)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_login_page_translation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_translation_for_basic_edit(locale_code: str) -> str:
    """
    Get end-user multi-translation for basic edit (getTranslationForBasicEdit)  # noqa: E501

Fetch the translation info map where value is info object containing key translation, origin translation, translation of parent level, translation status.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_translation_for_basic_edit(locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_translation_for_basic_edit'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_translation_infos() -> str:
    """
    Get Translation info (getTranslationInfos)  # noqa: E501

Fetch the list of customized locales and corresponding details such as language display name, country display name and translation progress percentage.   Response example:   ```json [   {     "localeCode": "uk_UA",     "language": "Ukrainian (українська)",     "country": "Україна",     "progress": 32   },   {     "localeCode": "es_ES",     "language": "Spanish (español)",     "country": "España",     "progress": 79   }] ```  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_translation_infos()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_translation_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( download_full_translation )
    mcp.tool()( get_available_java_locales )
    mcp.tool()( get_available_locales )
    mcp.tool()( get_full_translation )
    mcp.tool()( get_login_page_translation )
    mcp.tool()( get_translation_for_basic_edit )
    mcp.tool()( get_translation_infos )
