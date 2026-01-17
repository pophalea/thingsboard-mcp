import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def delete_image(_type: str, key: str, force: Optional[bool] = None) -> str:
    """
    deleteImage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_image(_type=_type, key=key, force=force)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_image'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def download_image(_type: str, key: str, if_none_match: str = "") -> str:
    """
    downloadImage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_image(_type=_type, key=key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_image'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def download_image_preview(_type: str, key: str, if_none_match: str = "") -> str:
    """
    downloadImagePreview  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_image_preview(_type=_type, key=key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_image_preview'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def download_login_favicon(type: str, key: str, if_none_match: str) -> str:
    """
    downloadLoginFavicon  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_login_favicon(type=type, key=key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_login_favicon'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def download_login_logo(type: str, key: str, if_none_match: str) -> str:
    """
    downloadLoginLogo  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_login_logo(type=type, key=key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_login_logo'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def download_public_image(public_resource_key: str, if_none_match: str = "") -> str:
    """
    downloadPublicImage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_public_image(public_resource_key=public_resource_key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_public_image'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def export_image(_type: str, key: str) -> str:
    """
    exportImage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.export_image(_type=_type, key=key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'export_image'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_image_info(_type: str, key: str) -> str:
    """
    getImageInfo  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_image_info(_type=_type, key=key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_image_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_images(page_size: int, page: int, text_search: Optional[str] = None, include_system_images: Optional[bool] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    getImages  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_images(page_size=page_size, page=page, text_search=text_search, include_system_images=include_system_images, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_images'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def import_image(body_json: str) -> str:
    """
    importImage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.import_image(body=deserialize_param(body_json, 'ImageExportData'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'import_image'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def update_image(_type: str, key: str, file: str) -> str:
    """
    updateImage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_image(_type=_type, key=key, file=file)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_image'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def update_image_info(_type: str, key: str, body_json: str) -> str:
    """
    updateImageInfo  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_image_info(_type=_type, key=key, body=deserialize_param(body_json, 'TbResourceInfo'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_image_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def update_image_public_status(_type: str, key: str, is_public: Optional[bool] = None) -> str:
    """
    updateImagePublicStatus  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_image_public_status(_type=_type, key=key, is_public=is_public)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_image_public_status'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def upload_image(title: str, file: str) -> str:
    """
    uploadImage  # noqa: E501
    """
    try:
        client = get_client()
        result = client.upload_image(title=title, file=file)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'upload_image'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( delete_image )
    mcp.tool()( download_image )
    mcp.tool()( download_image_preview )
    mcp.tool()( download_login_favicon )
    mcp.tool()( download_login_logo )
    mcp.tool()( download_public_image )
    mcp.tool()( export_image )
    mcp.tool()( get_image_info )
    mcp.tool()( get_images )
    mcp.tool()( import_image )
    mcp.tool()( update_image )
    mcp.tool()( update_image_info )
    mcp.tool()( update_image_public_status )
    mcp.tool()( upload_image )
