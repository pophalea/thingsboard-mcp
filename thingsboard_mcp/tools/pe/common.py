import json
import tb_rest_client.models.models_pe as models
from ...shared import get_client, deserialize_param, format_response, ApiException


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

def activate_instance(license_secret: str, release_date: str) -> str:
    """
    Activate edge instance (activateInstance)  # noqa: E501

Activates edge license on license portal.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.activate_instance(license_secret=license_secret, release_date=release_date)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'activate_instance'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

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

def cancel_job(id_json: str) -> str:
    """
    Cancel job (cancelJob)  # noqa: E501

Cancels the job. The status of the job must be QUEUED, PENDING or RUNNING.  For a running job, all the tasks not yet processed will be discarded.  See the example of a cancelled job result in getJobById method description.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.cancel_job(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'cancel_job'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def change_password(body_json: str) -> str:
    """
    No description available.
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
    No description available.
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

def check_instance(body_json: str = None) -> str:
    """
    Check edge license (checkInstance)  # noqa: E501

Checks license request from edge service by forwarding request to license portal.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.check_instance(body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'check_instance'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def check_repository_access(body_json: str) -> str:
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

def check_reset_token(reset_token: str) -> str:
    """
    No description available.
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

def chirp_stack_process_request_delete(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_delete(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'chirp_stack_process_request_delete'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def chirp_stack_process_request_get(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_get(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'chirp_stack_process_request_get'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def chirp_stack_process_request_head(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_head(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'chirp_stack_process_request_head'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def chirp_stack_process_request_options(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_options(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'chirp_stack_process_request_options'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def chirp_stack_process_request_patch(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_patch(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'chirp_stack_process_request_patch'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def chirp_stack_process_request_post(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_post(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'chirp_stack_process_request_post'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def chirp_stack_process_request_put(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.chirp_stack_process_request_put(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'chirp_stack_process_request_put'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def clear_events_post(entity_id_json: str, body_json: str, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.clear_events_post(entity_id=deserialize_param(entity_id_json, 'EntityId'), body=deserialize_param(body_json, 'EntityIdClearstartTimeendTimeBody'), start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'clear_events_post'."
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

def compare_entity_data_to_version(entity_id_json: str, version_id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.compare_entity_data_to_version(entity_id=deserialize_param(entity_id_json, 'EntityId'), version_id=version_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'compare_entity_data_to_version'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def count_entities_by_query(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.count_entities_by_query(body=deserialize_param(body_json, 'EntityCountQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'count_entities_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def create_custom_menu(body_json: str, assign_to_list_json: str = None, force: Optional[bool] = None) -> str:
    """
    Create Custom Menu (createCustomMenu)  # noqa: E501

The api is designed to create Custom Menu without configuration. Is not applicable for update.  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.create_custom_menu(body=deserialize_param(body_json, 'CustomMenuInfo'), assign_to_list=json.loads(assign_to_list_json) if assign_to_list_json else None, force=force)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'create_custom_menu'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def create_notification_request(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.create_notification_request(body=deserialize_param(body_json, 'NotificationRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'create_notification_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_ai_model_by_id(ai_model_id_json: str) -> str:
    """
    Delete AI model by ID (deleteAiModelById)  # noqa: E501

Deletes the AI model record by its `id`. If a record with the specified `id` exists, the record is deleted and the endpoint returns `true`. If no such record exists, the endpoint returns `false`.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_ai_model_by_id(ai_model_id=deserialize_param(ai_model_id_json, 'AiModelId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_ai_model_by_id'."
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

def delete_blob_entity(blob_entity_id_json: str) -> str:
    """
    Delete Blob Entity (deleteBlobEntity)  # noqa: E501

Delete Blob entity based on the provided Blob entity Id. Referencing non-existing Blob entity Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_blob_entity(blob_entity_id=deserialize_param(blob_entity_id_json, 'BlobEntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_blob_entity'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_calculated_field(calculated_field_id_json: str) -> str:
    """
    Delete Calculated Field (deleteCalculatedField)  # noqa: E501

Deletes the calculated field. Referencing non-existing Calculated Field Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_calculated_field(calculated_field_id=deserialize_param(calculated_field_id_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_calculated_field'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_client_registration_template(client_registration_template_id_json: str) -> str:
    """
    No description available.
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

def delete_converter(converter_id_json: str) -> str:
    """
    Delete converter (deleteConverter)  # noqa: E501

Deletes the converter and all the relations (from and to the converter). Referencing non-existing converter Id will cause an error. If the converter is associated with the integration, it will not be allowed for deletion.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_converter(converter_id=deserialize_param(converter_id_json, 'ConverterId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_converter'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_current_login_white_label_params(customer_id_json: str) -> str:
    """
    Delete Login White Labeling configuration (deleteCurrentLoginWhiteLabelParams)  # noqa: E501

Delete the Login White Labeling configuration that corresponds to the authority of the user.   Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_current_login_white_label_params(customer_id=deserialize_param(customer_id_json, 'CustomerId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_current_login_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_current_white_label_params(customer_id_json: str) -> str:
    """
    Delete General White Labeling configuration (deleteCurrentWhiteLabelParams)  # noqa: E501

Delete the White Labeling configuration that corresponds to the authority of the user.   Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_current_white_label_params(customer_id=deserialize_param(customer_id_json, 'CustomerId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_current_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_custom_menu(custom_menu_id_json: str, force: Optional[bool] = None) -> str:
    """
    Delete custom menu (deleteCustomMenu)  # noqa: E501

Deletes the custom menu based on the provided Custom Menu Id. Referencing non-existing custom menu Id will cause an error. If the custom menu is assigned to the list of users or customers bad request is returned.To delete a custom menu that has assignee list set 'force' request param to true   # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_custom_menu(custom_menu_id=deserialize_param(custom_menu_id_json, 'CustomMenuId'), force=force)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_custom_menu'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_custom_translation(locale_code: str) -> str:
    """
    Delete Custom Translation for specified locale (deleteCustomTranslation)  # noqa: E501

Delete entire custom translation settings for end-user  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_custom_translation(locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_custom_translation_key(locale_code: str, key_path: str) -> str:
    """
    Delete specified key of Custom Translation (deleteCustomTranslationKey)   # noqa: E501

The API call is designed to delete specified key of the custom translation and return as a result parent translation.(e.g. if tenant translation for key is 'value1' and customer translation is 'value2' then by deletinf key onn customer level you will get 'value1' in response)   Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_custom_translation_key(locale_code=locale_code, key_path=key_path)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_custom_translation_key'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_domain(domain_id_json: str) -> str:
    """
    Delete Domain by ID (deleteDomain)  # noqa: E501

Deletes Domain by ID. Referencing non-existing domain Id will cause an error.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_domain(domain_id=deserialize_param(domain_id_json, 'DomainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_domain'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_edge(edge_id_json: str) -> str:
    """
    Delete edge (deleteEdge)  # noqa: E501

Deletes the edge. Referencing non-existing edge Id will cause an error.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_entity_view(entity_view_id_json: str) -> str:
    """
    Delete entity view (deleteEntityView)  # noqa: E501

Delete the EntityView object based on the provided entity view id.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_entity_view(entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_entity_view'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_group_permission(group_permission_id_json: str) -> str:
    """
    Delete group permission (deleteGroupPermission)  # noqa: E501

Deletes the group permission. Referencing non-existing group permission Id will cause an error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_group_permission(group_permission_id=deserialize_param(group_permission_id_json, 'GroupPermissionId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_group_permission'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

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

def delete_job(id_json: str) -> str:
    """
    deleteJob  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_job(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_job'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_mobile_app(mobile_app_id_json: str) -> str:
    """
    Delete Mobile App by ID (deleteMobileApp)  # noqa: E501

Deletes Mobile App by ID. Referencing non-existing mobile app Id will cause an error.  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_mobile_app(mobile_app_id=deserialize_param(mobile_app_id_json, 'MobileAppId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_mobile_app'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_mobile_app_bundle(mobile_app_bundle_id_json: str) -> str:
    """
    Delete Mobile App Bundle by ID (deleteMobileAppBundle)  # noqa: E501

Deletes Mobile App Bundle by ID. Referencing non-existing mobile app bundle Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_mobile_app_bundle(mobile_app_bundle_id=deserialize_param(mobile_app_bundle_id_json, 'MobileAppBundleId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_mobile_app_bundle'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_notification(id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.delete_notification(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_notification'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_notification_request(id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.delete_notification_request(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_notification_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_notification_rule(id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.delete_notification_rule(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_notification_rule'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_notification_target_by_id(id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.delete_notification_target_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_notification_target_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_notification_template_by_id(id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.delete_notification_template_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_notification_template_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_queue(queue_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.delete_queue(queue_id=deserialize_param(queue_id_json, 'QueueId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_queue'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_report_template(report_template_id_json: str) -> str:
    """
    Delete Report Template (deleteReportTemplate)  # noqa: E501

Deletes the report template. Referencing non-existing Report Template Id will cause 'Not Found' error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_report_template(report_template_id=deserialize_param(report_template_id_json, 'ReportTemplateId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_report_template'."
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

def delete_role(role_id_json: str) -> str:
    """
    Delete role (deleteRole)  # noqa: E501

Deletes the role. Referencing non-existing role Id will cause an error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_role(role_id=deserialize_param(role_id_json, 'RoleId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_role'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_rpc(rpc_id_json: str) -> str:
    """
    Delete persistent RPC  # noqa: E501

Deletes the persistent RPC request.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_rpc(rpc_id=deserialize_param(rpc_id_json, 'RpcId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_rpc'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_secret(secret_id_json: str) -> str:
    """
    Delete secret by ID (deleteSecret)  # noqa: E501

Deletes the secret. Referencing non-existing Secret Id will cause an error.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_secret(secret_id=deserialize_param(secret_id_json, 'SecretId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_secret'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

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

def download_blob_entity(blob_entity_id_json: str) -> str:
    """
    Download Blob Entity By Id (downloadBlobEntity)  # noqa: E501

Download report file based on the provided Blob entity Id. Referencing non-existing Blob entity Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_blob_entity(blob_entity_id=deserialize_param(blob_entity_id_json, 'BlobEntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_blob_entity'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

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

def download_gateway_docker_compose(device_id_json: str) -> str:
    """
    Download generated docker-compose.yml file for gateway (downloadGatewayDockerCompose)  # noqa: E501

Download generated docker-compose.yml for gateway.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_gateway_docker_compose(device_id=deserialize_param(device_id_json, 'DeviceId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_gateway_docker_compose'."
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

def download_jks_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.download_jks_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_jks_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_js_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.download_js_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_js_resource_if_changed'."
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

def download_lwm2m_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.download_lwm2m_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_lwm2m_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_pkcs12_resource_if_changed(resource_id_json: str, if_none_match: str = "") -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.download_pkcs12_resource_if_changed(resource_id=deserialize_param(resource_id_json, 'EntityId'), if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_pkcs12_resource_if_changed'."
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

def download_resource(resource_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.download_resource(resource_id=deserialize_param(resource_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_resource'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_resource_if_changed(resource_type: str, scope: str, key: str, if_none_match: str = "") -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.download_resource_if_changed(resource_type=resource_type, scope=scope, key=key, if_none_match=if_none_match)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_resource_if_changed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_server_certificate(protocol: str) -> str:
    """
    Download server certificate using file path defined in device.connectivity properties (downloadServerCertificate)  # noqa: E501

Download server certificate.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_server_certificate(protocol=protocol)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_server_certificate'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def download_test_report(body_json: str, reports_server_endpoint_url: Optional[str] = None) -> str:
    """
    Download test report (downloadTestReport)  # noqa: E501

Generate and download test report.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.download_test_report(body=deserialize_param(body_json, 'ReportConfig'), reports_server_endpoint_url=reports_server_endpoint_url)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'download_test_report'."
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

def find_by_from(from_id_json: str, relation_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_by_from(from_id=deserialize_param(from_id_json, 'EntityId'), relation_type=relation_type, relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_from'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_from_v1(from_id_json: str, from_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_by_from_v1(from_id=deserialize_param(from_id_json, 'EntityId'), from_type=from_type, relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_from_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_query(body_json: str) -> str:
    """
    Find related assets (findByQuery)  # noqa: E501

Returns all assets that are related to the specific entity. The entity id, relation type, asset types, depth of the search, and other query parameters defined using complex 'AssetSearchQuery' object. See 'Model' tab of the Parameters for more info.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_by_query(body=deserialize_param(body_json, 'AssetSearchQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_query_v1(body_json: str) -> str:
    """
    Find related devices (findByQuery)  # noqa: E501

Returns all devices that are related to the specific entity. The entity id, relation type, device types, depth of the search, and other query parameters defined using complex 'DeviceSearchQuery' object. See 'Model' tab of the Parameters for more info.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_by_query_v1(body=deserialize_param(body_json, 'DeviceSearchQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_query_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_query_v2(body_json: str) -> str:
    """
    Find related edges (findByQuery)  # noqa: E501

Returns all edges that are related to the specific entity. The entity id, relation type, edge types, depth of the search, and other query parameters defined using complex 'EdgeSearchQuery' object. See 'Model' tab of the Parameters for more info.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_by_query_v2(body=deserialize_param(body_json, 'EdgeSearchQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_query_v2'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_query_v3(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_by_query_v3(body=deserialize_param(body_json, 'EntityRelationsQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_query_v3'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_query_v4(body_json: str) -> str:
    """
    Find related entity views (findByQuery)  # noqa: E501

Returns all entity views that are related to the specific entity. The entity id, relation type, entity view types, depth of the search, and other query parameters defined using complex 'EntityViewSearchQuery' object. See 'Model' tab of the Parameters for more info.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_by_query_v4(body=deserialize_param(body_json, 'EntityViewSearchQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_query_v4'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_to(to_id_json: str, relation_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_by_to(to_id=deserialize_param(to_id_json, 'EntityId'), relation_type=relation_type, relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_to'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_by_to_v1(to_id_json: str, to_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_by_to_v1(to_id=deserialize_param(to_id_json, 'EntityId'), to_type=to_type, relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_by_to_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_entity_data_by_query(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_entity_data_by_query(body=deserialize_param(body_json, 'EntityDataQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_entity_data_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_info_by_from(from_id_json: str, relation_type_group: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_info_by_from(from_id=deserialize_param(from_id_json, 'EntityId'), relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_info_by_from'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_info_by_query(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_info_by_query(body=deserialize_param(body_json, 'EntityRelationsQuery'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_info_by_query'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def find_info_by_to(to_id_json: str, to_type: str, relation_type_group: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.find_info_by_to(to_id=deserialize_param(to_id_json, 'EntityId'), to_type=to_type, relation_type_group=relation_type_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_info_by_to'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def getName() -> str:
    """
    Return a string used for identification purposes only.

This method is deprecated, use the name attribute instead.
    """
    try:
        client = get_client()
        result = client.getName()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'getName'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_activation_link(user_id_json: str) -> str:
    """
    Get the activation link (getActivationLink)  # noqa: E501

Get the activation link for the user. The base url for activation link is configurable in the general settings of system administrator.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_activation_link(user_id=deserialize_param(user_id_json, 'UserId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_activation_link'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_activation_link_info(user_id_json: str) -> str:
    """
    Get the activation link (getActivationLink)  # noqa: E501

Get the activation link for the user. The base url for activation link is configurable in the general settings of system administrator.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_activation_link_info(user_id=deserialize_param(user_id_json, 'UserId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_activation_link_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_ai_model_by_id(ai_model_id_json: str) -> str:
    """
    Get AI model by ID (getAiModelById)  # noqa: E501

Fetches an AI model record by its `id`.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_ai_model_by_id(ai_model_id=deserialize_param(ai_model_id_json, 'AiModelId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_ai_model_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_ai_models(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get AI models (getAiModels)  # noqa: E501

Returns a page of AI models. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_ai_models(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_ai_models'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_all_entity_view_infos(page_size: int, page: int, include_customers: Optional[bool] = None, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get All Entity View Infos for current user (getAllEntityViewInfos)  # noqa: E501

Returns a page of entity view info objects owned by the tenant or the customer of a current user. Entity Views Info extends the Entity View with owner name. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_all_entity_view_infos(page_size=page_size, page=page, include_customers=include_customers, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_all_entity_view_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_all_report_template_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, type_list: Optional[str] = None, format_list: Optional[str] = None, include_customers: Optional[bool] = None) -> str:
    """
    Get All Report Templates for current user (getAllReportTemplateInfos)  # noqa: E501

Returns a page of report template info objects owned by the tenant or the customer of a current user. Report Templates allows you to create reports according to the report template configuration. Report service uses report template configuration to generate report. See the 'Model' tab of the Response Class for more details.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_all_report_template_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, type_list=type_list, format_list=format_list, include_customers=include_customers)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_all_report_template_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_allowed_permissions() -> str:
    """
    Get Permissions (getAllowedPermissions)  # noqa: E501

Returns a complex object that describes:   * all possible (both granted and not granted) permissions for the authority of the user (Tenant or Customer);  * all granted permissions for the user;   The result impacts UI behavior and hides certain UI elements if user has no permissions to invoke the related operations. Nevertheless, all API calls check the permissions each time they are executed on the server side.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_allowed_permissions()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_allowed_permissions'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_application_redirect(user_agent: str) -> str:
    """
    getApplicationRedirect  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_application_redirect(user_agent=user_agent)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_application_redirect'."
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

def get_available_delivery_methods() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_available_delivery_methods()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_available_delivery_methods'."
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

def get_blob_entities(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    Get Blob Entities (getBlobEntities)  # noqa: E501

Returns a page of BlobEntityWithCustomerInfo object that are available for the current user. The platform uses Blob(binary large object) entities in the reporting feature, in order to store Dashboard states snapshots of different content types in base64 format. BlobEntityWithCustomerInfo represents an object that contains base info about the blob entity(name, type, contentType, etc.) and info about the customer(customerTitle, customerIsPublic) of the user that scheduled generation of the dashboard report. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_blob_entities(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_blob_entities'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_blob_entities_by_ids(blob_entity_ids_json: str) -> str:
    """
    Get Blob Entities By Ids (getBlobEntitiesByIds)  # noqa: E501

Requested blob entities must be owned by tenant or assigned to customer which user is performing the request. The platform uses Blob(binary large object) entities in the reporting feature, in order to store Dashboard states snapshots of different content types in base64 format. BlobEntityInfo represents an object that contains base info about the blob entity(name, type, contentType, etc.). See the 'Model' tab of the Response Class for more details.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_blob_entities_by_ids(blob_entity_ids=json.loads(blob_entity_ids_json) if blob_entity_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_blob_entities_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_blob_entity_info_by_id(blob_entity_id_json: str) -> str:
    """
    Get Blob Entity With Customer Info (getBlobEntityInfoById)  # noqa: E501

Fetch the BlobEntityWithCustomerInfo object based on the provided Blob entity Id. The platform uses Blob(binary large object) entities in the reporting feature, in order to store Dashboard states snapshots of different content types in base64 format. BlobEntityWithCustomerInfo represents an object that contains base info about the blob entity(name, type, contentType, etc.) and info about the customer(customerTitle, customerIsPublic) of the user that scheduled generation of the dashboard report. Referencing non-existing Blob entity Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_blob_entity_info_by_id(blob_entity_id=deserialize_param(blob_entity_id_json, 'BlobEntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_blob_entity_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_calculated_field_by_id(calculated_field_id_json: str) -> str:
    """
    Get Calculated Field (getCalculatedFieldById)  # noqa: E501

Fetch the Calculated Field object based on the provided Calculated Field Id.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_calculated_field_by_id(calculated_field_id=deserialize_param(calculated_field_id_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_calculated_field_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_calculated_fields_by_entity_id(entity_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Calculated Fields by Entity Id (getCalculatedFieldsByEntityId)  # noqa: E501

Fetch the Calculated Fields based on the provided Entity Id.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_calculated_fields_by_entity_id(entity_id=deserialize_param(entity_id_json, 'EntityId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_calculated_fields_by_entity_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_client_registration_templates() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_client_registration_templates()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_client_registration_templates'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_client_registration_templates1() -> str:
    """
    No description available.
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

def get_client_registration_templates_mail() -> str:
    """
    Get the list of all OAuth2 client registration templates (getClientRegistrationTemplates)  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501

Mail configuration template is set of default smtp settings for mail server that specific provider supports  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_client_registration_templates_mail()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_client_registration_templates_mail'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_component_descriptor_by_clazz(component_descriptor_clazz: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_component_descriptor_by_clazz(component_descriptor_clazz=component_descriptor_clazz)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_component_descriptor_by_clazz'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_component_descriptors_by_type(component_type: str, rule_chain_type: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_component_descriptors_by_type(component_type=component_type, rule_chain_type=rule_chain_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_component_descriptors_by_type'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_component_descriptors_by_types(component_types: str, rule_chain_type: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_component_descriptors_by_types(component_types=component_types, rule_chain_type=rule_chain_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_component_descriptors_by_types'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_converter_by_id(converter_id_json: str) -> str:
    """
    Get Converter (getConverterById)  # noqa: E501

Fetch the Converter object based on the provided Converter Id. The server checks that the converter is owned by the same tenant.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_converter_by_id(converter_id=deserialize_param(converter_id_json, 'ConverterId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_converter_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_converters(page_size: int, page: int, is_edge_template: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Converters (getConverters)  # noqa: E501

Returns a page of converters owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_converters(page_size=page_size, page=page, is_edge_template=is_edge_template, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_converters'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_converters_by_ids(converter_ids_json: str) -> str:
    """
    Get Converters By Ids (getConvertersByIds)  # noqa: E501

Requested converters must be owned by tenant which is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_converters_by_ids(converter_ids=json.loads(converter_ids_json) if converter_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_converters_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_current_login_white_label_params() -> str:
    """
    Get Login White Labeling configuration (getCurrentWhiteLabelParams)  # noqa: E501

Fetch the Login  White Labeling configuration that corresponds to the authority of the user. The API call is designed to load the Login White Labeling configuration for edition. So, the result is NOT merged with the parent level White Labeling configuration. Let's assume there is a custom White Labeling  configured on a system level. And there is no custom White Labeling  items configured on a tenant level. In such a case, the API call will return default object for the tenant administrator.   Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_current_login_white_label_params()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_current_login_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_current_white_label_params() -> str:
    """
    Get White Labeling configuration (getCurrentWhiteLabelParams)  # noqa: E501

Fetch the White Labeling configuration that corresponds to the authority of the user. The API call is designed to load the White Labeling configuration for edition. So, the result is NOT merged with the parent level White Labeling configuration. Let's assume there is a custom White Labeling  configured on a system level. And there is no custom White Labeling  items configured on a tenant level. In such a case, the API call will return default object for the tenant administrator.   Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_current_white_label_params()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_current_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_custom_menu() -> str:
    """
    Get end-user Custom Menu configuration (getCustomMenu)  # noqa: E501

Fetch the Custom Menu object for the end user. The custom menu is configured in the white labeling parameters. If custom menu configuration on the tenant level is present, it overrides the menu configuration of the system level. Similar, if the custom menu configuration on the customer level is present, it overrides the menu configuration of the tenant level.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_custom_menu()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_custom_menu'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_custom_menu_assignee_list(custom_menu_id_json: str) -> str:
    """
    Get Custom Menu assignee list (getCustomMenuAssigneeList)  # noqa: E501

Fetch the list of Entity Info objects that represents users or customers, or empty list if custom menu is not assigned or has NO_ASSIGN/ALL assignee type.  Security check is performed to verify that the user has 'READ' permission for the custom menu with specified id.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_custom_menu_assignee_list(custom_menu_id=deserialize_param(custom_menu_id_json, 'CustomMenuId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_custom_menu_assignee_list'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_custom_menu_config(custom_menu_id_json: str) -> str:
    """
    Get Custom Menu configuration by id (getCustomMenuConfig)  # noqa: E501

Fetch the Custom Menu configuration based on the provided Custom Menu Id.   Security check is performed to verify that the user has 'READ' permission for the custom menu with specified id.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_custom_menu_config(custom_menu_id=deserialize_param(custom_menu_id_json, 'CustomMenuId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_custom_menu_config'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_custom_menu_info_by_id(custom_menu_id_json: str) -> str:
    """
    Get Custom Menu Info (getCustomMenuInfoById)  # noqa: E501

Fetch the Custom Menu Info object based on the provided Custom Menu Id.   Security check is performed to verify that the user has 'READ' permission for the custom menu with specified id.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_custom_menu_info_by_id(custom_menu_id=deserialize_param(custom_menu_id_json, 'CustomMenuId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_custom_menu_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_custom_menu_infos(page_size: int, page: int, scope: Optional[str] = None, assignee_type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get all custom menus configured at user level (getCustomMenuInfos)  # noqa: E501

Returns a page of custom menu info objects owned by the tenant or the customer of a current user, scope and assigneeType request parameters can be used to filter the result.  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_custom_menu_infos(page_size=page_size, page=page, scope=scope, assignee_type=assignee_type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_custom_menu_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_custom_translation(locale_code: str) -> str:
    """
    Get end-user Custom Translation configuration (getCustomTranslation)  # noqa: E501

Fetch the Custom Translation map for the end user. The custom translation is configured in the white labeling parameters. If custom translation translation is defined on the tenant level, it overrides the custom translation of the system level. Similar, if the custom translation is defined on the customer level, it overrides the translation configuration of the tenant level.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_custom_translation(locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_domain_info_by_id(domain_id_json: str) -> str:
    """
    Get Domain info by Id (getDomainInfoById)  # noqa: E501

  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_domain_info_by_id(domain_id=deserialize_param(domain_id_json, 'DomainId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_domain_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_domain_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Domain infos (getDomainInfos)  # noqa: E501

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_domain_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_domain_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_downlink_converter(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get downlink converter (getDownlinkConverter)  # noqa: E501

Returns downlink converter body for the vendor, integration type and model  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_downlink_converter(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_downlink_converter'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_downlink_converter_metadata(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get downlink converter metadata (getDownlinkConverterMetadata)  # noqa: E501

Returns downlink converter metadata for the vendor, integration type and model  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_downlink_converter_metadata(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_downlink_converter_metadata'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_downlink_payload(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get downlink payload (getDownlinkPayload)  # noqa: E501

Returns payload example for the downlink converter for the vendor, integration type and model  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_downlink_payload(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_downlink_payload'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edge_by_id(edge_id_json: str) -> str:
    """
    Get Edge (getEdgeById)  # noqa: E501

Get the Edge object based on the provided Edge Id. If the user has the authority of 'Tenant Administrator', the server checks that the edge is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the edge is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_by_id(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edge_events(edge_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    Get Edge Events (getEdgeEvents)  # noqa: E501

Returns a page of edge events for the requested edge. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_events(edge_id=deserialize_param(edge_id_json, 'EdgeId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_events'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edge_install_instructions(edge_id_json: str, method: str) -> str:
    """
    Get Edge Install Instructions (getEdgeInstallInstructions)  # noqa: E501

Get an install instructions for provided edge id.If the user has the authority of 'Tenant Administrator', the server checks that the edge is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the edge is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_install_instructions(edge_id=deserialize_param(edge_id_json, 'EdgeId'), method=method)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_install_instructions'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edge_types() -> str:
    """
    Get Edge Types (getEdgeTypes)  # noqa: E501

Returns a set of unique edge types based on edges that are either owned by the tenant or assigned to the customer which user is performing the request.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_types()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_types'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edge_upgrade_instructions(edge_version: str, method: str) -> str:
    """
    Get Edge Upgrade Instructions (getEdgeUpgradeInstructions)  # noqa: E501

Get an upgrade instructions for provided edge vesion.If the user has the authority of 'Tenant Administrator', the server checks that the edge is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the edge is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_upgrade_instructions(edge_version=edge_version, method=method)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_upgrade_instructions'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edges(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Edges (getEdges)  # noqa: E501

Returns a page of edges owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edges(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edges'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edges_by_ids(edge_ids_json: str) -> str:
    """
    Get Edges By Ids (getEdgesByIds)  # noqa: E501

Requested edges must be owned by tenant or assigned to customer which user is performing the request.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edges_by_ids(edge_ids=json.loads(edge_ids_json) if edge_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edges_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_edqs_state() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_edqs_state()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edqs_state'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_entities(entity_group_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Group Entities (getEntities)  # noqa: E501

Returns a page of Short Entity View objects that belongs to specified Entity Group Id. Short Entity View object contains the entity id and number of fields (attributes, telemetry, etc). List of those fields is configurable and defined in the group configuration.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_entities(entity_group_id=deserialize_param(entity_group_id_json, 'EntityGroupId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_entities'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_entity_data_info(version_id: str, entity_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_entity_data_info(version_id=version_id, entity_id=deserialize_param(entity_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_entity_data_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_entity_view_by_id(entity_view_id_json: str) -> str:
    """
    Get entity view (getEntityViewById)  # noqa: E501

Fetch the EntityView object based on the provided entity view id. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. See the 'Model' tab for more details.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_entity_view_by_id(entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_entity_view_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_entity_view_info_by_id(entity_view_id_json: str) -> str:
    """
    Get entity view info (getEntityViewInfoById)  # noqa: E501

Fetch the Entity View info object based on the provided entity view id. Entity Views Info extends the Entity View with owner name. Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. See the 'Model' tab for more details.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_entity_view_info_by_id(entity_view_id=deserialize_param(entity_view_id_json, 'EntityViewId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_entity_view_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_entity_view_types() -> str:
    """
    Get Entity View Types (getEntityViewTypes)  # noqa: E501

Returns a set of unique entity view types based on entity views that are either owned by the tenant or assigned to the customer which user is performing the request.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_entity_view_types()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_entity_view_types'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_entity_views_by_ids(entity_view_ids_json: str) -> str:
    """
    Get Entity Views By Ids (getEntityViewsByIds)  # noqa: E501

Requested entity views must be owned by tenant or assigned to customer which user is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_entity_views_by_ids(entity_view_ids=json.loads(entity_view_ids_json) if entity_view_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_entity_views_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_events_get(entity_id_json: str, tenant_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_events_get(entity_id=deserialize_param(entity_id_json, 'EntityId'), tenant_id=deserialize_param(tenant_id_json, 'TenantId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_events_get'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_events_post(tenant_id_json: str, page_size: int, page: int, entity_id_json: str, body_json: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_events_post(tenant_id=deserialize_param(tenant_id_json, 'TenantId'), page_size=page_size, page=page, entity_id=deserialize_param(entity_id_json, 'EntityId'), body=deserialize_param(body_json, 'EventFilter'), text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_events_post'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_events_v1_get1(entity_id_json: str, event_type: str, tenant_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_events_v1_get1(entity_id=deserialize_param(entity_id_json, 'EntityId'), event_type=event_type, tenant_id=deserialize_param(tenant_id_json, 'TenantId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_events_v1_get1'."
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

def get_firmware(device_token: str, title: str, version: str, size: Optional[int] = None, chunk: Optional[int] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_firmware(device_token=device_token, title=title, version=version, size=size, chunk=chunk)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_firmware'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_firmware_by_id(group_id_json: str, firmware_type: str) -> str:
    """
    getFirmwareById  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_firmware_by_id(group_id=deserialize_param(group_id_json, 'EntityGroupId'), firmware_type=firmware_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_firmware_by_id'."
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

def get_group_entity(entity_group_id_json: str, entity_id_json: str) -> str:
    """
    Get Group Entity (getGroupEntity)  # noqa: E501

Fetch the Short Entity View object based on the group and entity id. Short Entity View object contains the entity id and number of fields (attributes, telemetry, etc). List of those fields is configurable and defined in the group configuration.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_group_entity(entity_group_id=deserialize_param(entity_group_id_json, 'EntityGroupId'), entity_id=deserialize_param(entity_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_group_entity'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_group_permission_by_id(group_permission_id_json: str) -> str:
    """
    Get Group Permission (getGroupPermissionById)  # noqa: E501

Fetch the Group Permission object based on the provided Group Permission Id. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_group_permission_by_id(group_permission_id=deserialize_param(group_permission_id_json, 'GroupPermissionId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_group_permission_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_group_permission_info_by_id(group_permission_id_json: str, is_user_group: bool) -> str:
    """
    Get Group Permission Info (getGroupPermissionInfoById)  # noqa: E501

Fetch the Group Permission Info object based on the provided Group Permission Id and the flag that controls what additional information to load: User or Entity Group. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;   Group Permission Info object extends the Group Permissions with the full information about Role and User and/or Entity Groups.  Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_group_permission_info_by_id(group_permission_id=deserialize_param(group_permission_id_json, 'GroupPermissionId'), is_user_group=is_user_group)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_group_permission_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_help_base_url() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_help_base_url()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_help_base_url'."
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

def get_job_by_id(id_json: str) -> str:
    """
    Get job by id (getJobById)  # noqa: E501

Fetches job info by id.  Example of a RUNNING CF_REPROCESSING job response: ```json {   "id": {     "entityType": "JOB",     "id": "475e94e0-2f2d-11f0-8240-91e99922a704"   },   "createdTime": 1747053196590,   "tenantId": {     "entityType": "TENANT",     "id": "46859a00-2f2d-11f0-8240-91e99922a704"   },   "type": "CF_REPROCESSING",   "key": "474e4130-2f2d-11f0-8240-91e99922a704",   "entityId": {     "entityType": "DEVICE_PROFILE",     "id": "9fd41f20-31a1-11f0-933e-27998d6db02e"    },   "status": "RUNNING",   "configuration": {     "type": "CF_REPROCESSING",     "calculatedFieldId": {       "entityType": "CALCULATED_FIELD",       "id": "474e4130-2f2d-11f0-8240-91e99922a704"     },     "startTs": 1747051995760,     "endTs": 1747052895760,     "tasksKey": "c3cdbd42-799e-4d3a-9aad-9310f767aa36",     "toReprocess": null   },   "result": {     "jobType": "CF_REPROCESSING",     "successfulCount": 1,     "failedCount": 0,     "discardedCount": 0,     "totalCount": 2,     "results": [],     "generalError": null,     "startTs": 1747323069445,     "finishTs": 1747323070585,     "cancellationTs": 0   } }  ```  Example of a CF_REPROCESSING job with failures: ```json {   ...,   "status": "FAILED",   ...,   "result": {     "jobType": "CF_REPROCESSING",     "successfulCount": 0,     "failedCount": 2,     "discardedCount": 0,     "totalCount": 2,     "results": [       {         "jobType": "CF_REPROCESSING",         "key": "c3cdbd42-799e-4d3a-9aad-9310f767aa36",         "success": false,         "discarded": false,         "failure": {           "error": "Failed to fetch temperature: Failed to fetch timeseries data",           "entityInfo": {             "id": {               "entityType": "DEVICE",               "id": "9fd41f20-31a1-11f0-933e-27998d6db02e"             },             "name": "Test device 1"           }         }       },       {         "jobType": "CF_REPROCESSING",         "key": "c3cdbd42-799e-4d3a-9aad-9310f767aa36",         "success": false,         "discarded": false,         "failure": {           "error": "Failed to fetch temperature: Failed to fetch timeseries data",           "entityInfo": {             "id": {               "entityType": "DEVICE",               "id": "9ffc4090-31a1-11f0-933e-27998d6db02e"             },             "name": "Test device 2"           }         }       }     ],     "generalError": null,     "startTs": 1747323069445,     "finishTs": 1747323070585,     "cancellationTs": 0   } }  ```  Example of a FAILED job result with general error: ```json {   ...,   "status": "FAILED",   ...,   "result": {     "jobType": "CF_REPROCESSING",     "successfulCount": 1,     "failedCount": 0,     "discardedCount": 0,     "totalCount": null,     "results": [],     "generalError": "Timeout to find devices by profile",     "cancellationTs": 0   } }  ```  Example of a CANCELLED job result: ```json {   ...,   "status": "CANCELLED",   ...,   "result": {     "jobType": "CF_REPROCESSING",     "successfulCount": 15,     "failedCount": 0,     "discardedCount": 85,     "totalCount": 100,     "results": [],     "generalError": null,     "cancellationTs": 1747065908414   } }  ```  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_job_by_id(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_job_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_jobs(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None) -> str:
    """
    Get jobs (getJobs)  # noqa: E501

Returns the page of jobs.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_jobs(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, start_time=start_time, end_time=end_time)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_jobs'."
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

def get_last_calculated_field_reprocessing_job(id_json: str) -> str:
    """
    getLastCalculatedFieldReprocessingJob  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_last_calculated_field_reprocessing_job(id=deserialize_param(id_json, 'CalculatedFieldId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_last_calculated_field_reprocessing_job'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_latest_calculated_field_debug_event(calculated_field_id_json: str) -> str:
    """
    Get latest calculated field debug event (getLatestCalculatedFieldDebugEvent)  # noqa: E501

Gets latest calculated field debug event for specified calculated field id. Referencing non-existing calculated field id will cause an error.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_latest_calculated_field_debug_event(calculated_field_id=deserialize_param(calculated_field_id_json, 'CalculatedFieldId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_latest_calculated_field_debug_event'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_latest_converter_debug_input(converter_id_json: str, integration_json: str) -> str:
    """
    Get latest debug input event (getLatestConverterDebugInput)  # noqa: E501

Returns a JSON object of the latest debug event representing the input message the converter processed.   ## Uplink Converter Debug Input Event Example  ```json {    "inContentType":"JSON",    "inContent":"{\\"temp\\":40}",    "inMetadata":"{\\"Header:sec-ch-ua\\":\\"\\\\\\"Chromium\\\\\\";v=\\\\\\"94\\\\\\", \\\\\\"Google Chrome\\\\\\";v=\\\\\\"94\\\\\\", \\\\\\";Not A Brand\\\\\\";v=\\\\\\"99\\\\\\"\\",\\"Header:user-agent\\":\\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36\\",\\"integrationName\\":\\"Integration\\",\\"Header:cookie\\":\\"GUID=zYSs8hymSwZKv8kHALKY; redirect_to=%2F; JSESSIONID=B0A7C8E481409CE7924E738DB04F62F9\\",\\"Header:sec-ch-ua-platform\\":\\"\\\\\\"Linux\\\\\\"\\",\\"Header:accept\\":\\"*/*\\",\\"Header:origin\\":\\"http://localhost:8080\\",\\"Header:sec-fetch-site\\":\\"same-origin\\",\\"Header:connection\\":\\"keep-alive\\",\\"Header:accept-encoding\\":\\"gzip, deflate, br\\",\\"Header:content-type\\":\\"application/json\\",\\"Header:content-length\\":\\"16\\",\\"Header:sec-fetch-mode\\":\\"cors\\",\\"Header:sec-ch-ua-mobile\\":\\"?0\\",\\"Header:sec-fetch-dest\\":\\"empty\\",\\"Header:host\\":\\"localhost:8080\\",\\"Header:referer\\":\\"http://localhost:8080/swagger-ui.html\\",\\"Header:accept-language\\":\\"en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,uk;q=0.6,und;q=0.5\\"}" } ```   * 'inContentType' - content type of the message received by the integration;   * 'inContent' - message data received;   * 'inMetadata' - integration metadata (e.g. headers).  ## Downlink Converter Debug Input Event Example  ```json {    "inContentType":"JSON",    "inContent":"{\\"temp\\":42,\\"humidity\\":77}",    "inMsgType":"POST_TELEMETRY_REQUEST",    "inMetadata":"{\\"data\\":\\"40\\"}",    "inIntegrationMetadata":"{\\"integrationName\\":\\"Integration\\"}" } ```   * 'inContentType' - content type of the message received by the integration;   * 'inContent' - content of the message pushed from the rule engine;   * 'inMsgType' - type of the message pushed from the rule engine;   * 'inMetadata' - content of the message metadata pushed from the rule engine;   * 'inIntegrationMetadata' - integration metadata.     Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_latest_converter_debug_input(converter_id=deserialize_param(converter_id_json, 'ConverterId'), integration=deserialize_param(integration_json, 'Integration'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_latest_converter_debug_input'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_latest_rule_node_debug_input(rule_node_id_json: str) -> str:
    """
    Get latest input message (getLatestRuleNodeDebugInput)  # noqa: E501

Gets the input message from the debug events for specified Rule Chain Id. Referencing non-existing rule chain Id will cause an error.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_latest_rule_node_debug_input(rule_node_id=deserialize_param(rule_node_id_json, 'RuleNodeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_latest_rule_node_debug_input'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_license_usage_info() -> str:
    """
    Get license usage info (getLicenseUsageInfo)  # noqa: E501

Get license usage info.   Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_license_usage_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_license_usage_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_login_mobile_info(pkg_name: str, platform: str) -> str:
    """
    Get mobile app login info (getLoginMobileInfo)  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_login_mobile_info(pkg_name=pkg_name, platform=platform)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_login_mobile_info'."
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

def get_login_processing_url() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_login_processing_url()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_login_processing_url'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_login_white_label_params(logo_image_checksum: str, favicon_checksum: str) -> str:
    """
    Get Login White Labeling parameters  # noqa: E501

Returns login white-labeling parameters based on the hostname from request.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_login_white_label_params(logo_image_checksum=logo_image_checksum, favicon_checksum=favicon_checksum)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_login_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_lwm2m_bootstrap_security_info(is_bootstrap_server: bool) -> str:
    """
    Get Lwm2m Bootstrap SecurityInfo (getLwm2mBootstrapSecurityInfo)  # noqa: E501

Get the Lwm2m Bootstrap SecurityInfo object (of the current server) based on the provided isBootstrapServer parameter. If isBootstrapServer == true, get the parameters of the current Bootstrap Server. If isBootstrapServer == false, get the parameters of the current Lwm2m Server. Used for client settings when starting the client in Bootstrap mode.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_lwm2m_bootstrap_security_info(is_bootstrap_server=is_bootstrap_server)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_lwm2m_bootstrap_security_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_lwm2m_list_objects(sort_order: str, sort_property: str, object_ids_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_lwm2m_list_objects(sort_order=sort_order, sort_property=sort_property, object_ids=json.loads(object_ids_json) if object_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_lwm2m_list_objects'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_lwm2m_list_objects_page(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_lwm2m_list_objects_page(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_lwm2m_list_objects_page'."
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

def get_max_datapoints_limit() -> str:
    """
    Get max data points limit (getMaxDatapointsLimit)  # noqa: E501

Get the maximum number of data points that dashboard may request from the server per in a single subscription command. This value impacts the time window behavior. It impacts 'Max values' parameter in case user selects 'None' as 'Data aggregation function'. It also impacts the 'Grouping interval' in case of any other 'Data aggregation function' is selected. The actual value of the limit is configurable in the system configuration file.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_max_datapoints_limit()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_max_datapoints_limit'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_merged_custom_translation(locale_code: str) -> str:
    """
    Get end-user Custom Translation configuration (getMergedCustomTranslation)  # noqa: E501

Fetch end-user Custom Translation for specified locale. The custom translation is configured in the white labeling parameters. If custom translation translation is defined on the tenant level, it overrides the custom translation of the system level. Similar, if the custom translation is defined on the customer level, it overrides the translation configuration of the tenant level.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_merged_custom_translation(locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_merged_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_merged_mobile_app_settings() -> str:
    """
    Get QR code configuration for home page (getMobileAppQrCodeConfig)  # noqa: E501

The response payload contains ui configuration of qr code  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_merged_mobile_app_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_merged_mobile_app_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_app_bundle_info_by_id(mobile_app_bundle_id_json: str) -> str:
    """
    Get mobile app bundle info by id (getMobileAppBundleInfoById)  # noqa: E501

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_app_bundle_info_by_id(mobile_app_bundle_id=deserialize_param(mobile_app_bundle_id_json, 'MobileAppBundleId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_app_bundle_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_app_by_id(mobile_app_id_json: str) -> str:
    """
    Get mobile info by id (getMobileAppInfoById)  # noqa: E501

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_app_by_id(mobile_app_id=deserialize_param(mobile_app_id_json, 'MobileAppId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_app_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_app_deep_link() -> str:
    """
    Get the deep link to the associated mobile application (getMobileAppDeepLink)  # noqa: E501

Fetch the url that takes user to linked mobile application   Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_app_deep_link()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_app_deep_link'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_app_info_by_id(mobile_app_id_json: str) -> str:
    """
    Get mobile info by id (getMobileAppInfoById)  # noqa: E501

  Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_app_info_by_id(mobile_app_id=deserialize_param(mobile_app_id_json, 'MobileAppId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_app_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_app_settings() -> str:
    """
    Get Mobile application settings (getMobileAppSettings)  # noqa: E501

The response payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_app_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_app_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_mobile_session(x_mobile_token: str) -> str:
    """
    getMobileSession  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_mobile_session(x_mobile_token=x_mobile_token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_mobile_session'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_request_by_id(id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_notification_request_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_request_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_request_preview(body_json: str, recipients_preview_size: Optional[int] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_notification_request_preview(body=deserialize_param(body_json, 'NotificationRequest'), recipients_preview_size=recipients_preview_size)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_request_preview'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_requests(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_notification_requests(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_requests'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_rule_by_id(id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_notification_rule_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_rule_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_rules(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_notification_rules(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_rules'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_settings() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_notification_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_target_by_id(id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_notification_target_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_target_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_targets(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_notification_targets(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_targets'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_targets_by_ids(ids_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_notification_targets_by_ids(ids=json.loads(ids_json) if ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_targets_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_targets_by_supported_notification_type(notification_type: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_notification_targets_by_supported_notification_type(notification_type=notification_type, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_targets_by_supported_notification_type'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_template_by_id(id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_notification_template_by_id(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_template_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notification_templates(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_notification_templates(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notification_templates'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_notifications(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, delivery_method: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_notifications(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order, delivery_method=delivery_method)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_notifications'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_owner_info(owner_type: str, owner_id: str) -> str:
    """
    Get Owner Info (getOwnerInfo)  # noqa: E501

Fetch the owner info (tenant or customer) presented as Entity Info object based on the provided owner Id.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_owner_info(owner_type=owner_type, owner_id=owner_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_owner_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_owner_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Owner Infos (getOwnerInfos)  # noqa: E501

Provides a rage view of Customers that the current user has READ access to. If the current user is Tenant administrator, the result set also contains the tenant. The call is designed for the UI auto-complete component to show tenant and all possible Customers that the user may select to change the owner of the particular entity or entity group.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_owner_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_owner_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_owners(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Owners (getOwners)  # noqa: E501

Provides a rage view of Customers that the current user has READ access to. If the current user is Tenant administrator, the result set also contains the tenant. The call is designed for the UI auto-complete component to show tenant and all possible Customers that the user may select to change the owner of the particular entity or entity group.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_owners(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_owners'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_persisted_rpc(rpc_id_json: str) -> str:
    """
    Get persistent RPC request  # noqa: E501

Get information about the status of the RPC call.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_persisted_rpc(rpc_id=deserialize_param(rpc_id_json, 'RpcId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_persisted_rpc'."
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

def get_qr_code_settings() -> str:
    """
    Get Mobile application settings (getMobileAppSettings)  # noqa: E501

The response payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for any authorized user.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_qr_code_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_qr_code_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_queue_by_id(queue_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_queue_by_id(queue_id=deserialize_param(queue_id_json, 'QueueId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_queue_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_queue_by_name(queue_name: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_queue_by_name(queue_name=queue_name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_queue_by_name'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_queue_stats_by_id(queue_stats_id_json: str) -> str:
    """
    Get Queue stats entity by id (getQueueStatsById)  # noqa: E501

Fetch the Queue stats object based on the provided Queue stats id.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_queue_stats_by_id(queue_stats_id=deserialize_param(queue_stats_id_json, 'QueueId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_queue_stats_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_queue_stats_by_ids(queue_stats_ids_json: str) -> str:
    """
    Get QueueStats By Ids (getQueueStatsByIds)  # noqa: E501

Fetch the Queue stats objects based on the provided ids.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_queue_stats_by_ids(queue_stats_ids=json.loads(queue_stats_ids_json) if queue_stats_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_queue_stats_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_recipients_for_notification_target_config(page_size: int, page: int) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_recipients_for_notification_target_config(page_size=page_size, page=page)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_recipients_for_notification_target_config'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_report_template_by_id(report_template_id_json: str) -> str:
    """
    Get Report Template (getReportTemplateById)  # noqa: E501

Fetch the ReportTemplate object based on the provided report template Id. Report Template extends Report Template Info object and adds 'configuration' - a JSON structure of report template configuration. See the 'Model' tab of the Response Class for more details. Referencing non-existing Report Template Id will cause 'Not Found' error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_report_template_by_id(report_template_id=deserialize_param(report_template_id_json, 'ReportTemplateId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_report_template_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_report_template_info_by_id(report_template_id_json: str) -> str:
    """
    Get Report Template Info (getReportTemplateInfoById)  # noqa: E501

Fetch the ReportTemplateInfo object based on the provided report template Id. Report Templates allows you to create reports according to the report template configuration. Report service uses report template configuration to generate report. See the 'Model' tab of the Response Class for more details. Referencing non-existing Report Template Id will cause 'Not Found' error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_report_template_info_by_id(report_template_id=deserialize_param(report_template_id_json, 'ReportTemplateId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_report_template_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_report_templates_by_ids(report_template_ids_json: str) -> str:
    """
    Get report templates by Report Template Ids (getReportTemplatesByIds)  # noqa: E501

Returns a list of ReportTemplateInfo objects based on the provided ids. Filters the list based on the user permissions.   Available for users with 'TENANT_ADMIN' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_report_templates_by_ids(report_template_ids=json.loads(report_template_ids_json) if report_template_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_report_templates_by_ids'."
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

def get_resource_by_id(resource_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_resource_by_id(resource_id=deserialize_param(resource_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_resource_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_resource_info_by_id(resource_id_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_resource_info_by_id(resource_id=deserialize_param(resource_id_json, 'EntityId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_resource_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_resources(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_resources(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_resources'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_role_by_id(role_id_json: str) -> str:
    """
    Get Role by Id (getRoleById)  # noqa: E501

Fetch the Role object based on the provided Role Id. Role Contains a set of permissions. Role has two types. Generic Role may be assigned to the user group and will provide permissions for all entities of a certain type. Group Role may be assigned to both user and entity group and will provides permissions only for the entities that belong to specified entity group. The assignment of the Role to the User Group is done using [Group Permission Controller](/swagger-ui.html#/group-permission-controller). Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_role_by_id(role_id=deserialize_param(role_id_json, 'RoleId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_role_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_roles(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Roles (getRoles)  # noqa: E501

Returns a page of roles that are available for the current user. Role Contains a set of permissions. Role has two types. Generic Role may be assigned to the user group and will provide permissions for all entities of a certain type. Group Role may be assigned to both user and entity group and will provides permissions only for the entities that belong to specified entity group. The assignment of the Role to the User Group is done using [Group Permission Controller](/swagger-ui.html#/group-permission-controller).You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_roles(page_size=page_size, page=page, type=type, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_roles'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_roles_by_ids(role_ids_json: str) -> str:
    """
    Get Roles By Ids (getRolesByIds)  # noqa: E501

Returns the list of rows based on their ids.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_roles_by_ids(role_ids=json.loads(role_ids_json) if role_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_roles_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_secret_info_by_id(secret_id_json: str) -> str:
    """
    Get Secret info by Id (getSecretInfoById)  # noqa: E501

  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_secret_info_by_id(secret_id=deserialize_param(secret_id_json, 'SecretId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_secret_info_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_secret_info_by_name(name: str) -> str:
    """
    Get Secret info by name (getSecretInfoByName)  # noqa: E501

  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_secret_info_by_name(name=name)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_secret_info_by_name'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_secret_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Tenant Secret infos (getSecretInfos)  # noqa: E501

Returns a page of secret infos owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_secret_infos(page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_secret_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_secret_names() -> str:
    """
    Get Tenant Secret names (getSecretNames)  # noqa: E501

Returns a page of secret names owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_secret_names()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_secret_names'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_security_settings() -> str:
    """
    Get the Security Settings object  # noqa: E501

Get the Security Settings object that contains password policy, etc.  Available for users with 'SYS_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.  # noqa: E501
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

def get_server_time() -> str:
    """
    Get server time (getServerTime)  # noqa: E501

Get the server time (milliseconds since January 1, 1970 UTC). Used to adjust view of the dashboards according to the difference between browser and server time.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_server_time()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_server_time'."
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

def get_software(device_token: str, title: str, version: str, size: Optional[int] = None, chunk: Optional[int] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_software(device_token=device_token, title=title, version=version, size=size, chunk=chunk)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_software'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_solution_template_details(solution_template_id_json: str) -> str:
    """
    Get Solution template details (getSolutionTemplateDetails)  # noqa: E501

Get a solution template details based on the provided id   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_solution_template_details(solution_template_id=deserialize_param(solution_template_id_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_solution_template_details'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_solution_template_infos() -> str:
    """
    Get Solution templates (getSolutionTemplateInfos)  # noqa: E501

Get a list of solution template descriptors   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_solution_template_infos()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_solution_template_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_solution_template_instructions(solution_template_id_json: str) -> str:
    """
    Get Solution Template Instructions (getSolutionTemplateInstructions)  # noqa: E501

Get a solution template instructions based on the provided id   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_solution_template_instructions(solution_template_id=deserialize_param(solution_template_id_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_solution_template_instructions'."
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

def get_trendz_settings() -> str:
    """
    Get Trendz Settings (getTrendzSettings)  # noqa: E501

Retrieves Trendz settings for this tenant.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_trendz_settings()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_trendz_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_unread_notifications_count(delivery_method: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_unread_notifications_count(delivery_method=delivery_method)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_unread_notifications_count'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_uplink_converter(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get uplink converter (getUplinkConverter)  # noqa: E501

Returns uplink converter body for the vendor, integration type and model  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_uplink_converter(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_uplink_converter'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_uplink_converter_metadata(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get uplink converter metadata (getUplinkConverterMetadata)  # noqa: E501

Returns uplink converter metadata for the vendor, integration type and model  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_uplink_converter_metadata(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_uplink_converter_metadata'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_uplink_payload(integration_type: str, vendor_name: str, model: str) -> str:
    """
    Get uplink payload (getUplinkPayload)  # noqa: E501

Returns payload example for the uplink converter for the vendor, integration type and model  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_uplink_payload(integration_type=integration_type, vendor_name=vendor_name, model=model)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_uplink_payload'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_vendor_models(integration_type: str, vendor_name: str, converter_type: str) -> str:
    """
    Get vendor models (getVendorModels)  # noqa: E501

Returns a list of models for the vendor, integration type and converter type  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_vendor_models(integration_type=integration_type, vendor_name=vendor_name, converter_type=converter_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_vendor_models'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_vendors(integration_type: str) -> str:
    """
    Get vendors (getVendors)  # noqa: E501

Returns a list of vendors for the integration type  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_vendors(integration_type=integration_type)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_vendors'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_version_create_request_status(request_id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_version_create_request_status(request_id=request_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_version_create_request_status'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_version_load_request_status(request_id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.get_version_load_request_status(request_id=request_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_version_load_request_status'."
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

def get_white_label_params(logo_image_checksum: str, favicon_checksum: str) -> str:
    """
    Get White Labeling parameters  # noqa: E501

Returns white-labeling parameters for the current user.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_white_label_params(logo_image_checksum=logo_image_checksum, favicon_checksum=favicon_checksum)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_rule_engine_request(entity_id_json: str, timeout: int, body: Optional[str] = None) -> str:
    """
    Push entity message with timeout to the rule engine (handleRuleEngineRequest)  # noqa: E501

Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses specified Entity Id as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. The platform expects the timeout value in milliseconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.handle_rule_engine_request(entity_id=deserialize_param(entity_id_json, 'EntityId'), timeout=timeout, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'handle_rule_engine_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_rule_engine_request_v1(entity_id_json: str, body: Optional[str] = None, queue_name: Optional[str] = None, timeout: Optional[int] = None) -> str:
    """
    Push entity message with timeout and specified queue to the rule engine (handleRuleEngineRequest)  # noqa: E501

Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses specified Entity Id as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. If request sent for Device/Device Profile or Asset/Asset Profile entity, specified queue will be used instead of the queue selected in the device or asset profile. The platform expects the timeout value in milliseconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.handle_rule_engine_request_v1(entity_id=deserialize_param(entity_id_json, 'EntityId'), body=body, queue_name=queue_name, timeout=timeout)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'handle_rule_engine_request_v1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_rule_engine_request_v2(entity_id_json: str, body: Optional[str] = None) -> str:
    """
    Push entity message to the rule engine (handleRuleEngineRequest)  # noqa: E501

Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses specified Entity Id as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. The default timeout of the request processing is 10 seconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.handle_rule_engine_request_v2(entity_id=deserialize_param(entity_id_json, 'EntityId'), body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'handle_rule_engine_request_v2'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def http_check_status_get(routing_key: str, request_params_json: str, request_headers_json: str) -> str:
    """
    checkStatus  # noqa: E501
    """
    try:
        client = get_client()
        result = client.http_check_status_get(routing_key=routing_key, request_params=json.loads(request_params_json) if request_params_json else None, request_headers=json.loads(request_headers_json) if request_headers_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'http_check_status_get'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def http_process_request_v1_post1(routing_key: str, suffix: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.http_process_request_v1_post1(routing_key=routing_key, suffix=suffix)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'http_process_request_v1_post1'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def http_process_request_v2_post2(routing_key: str, suffix: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.http_process_request_v2_post2(routing_key=routing_key, suffix=suffix)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'http_process_request_v2_post2'."
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

def install_solution_template(solution_template_id_json: str) -> str:
    """
    Install Solution Template (installSolutionTemplate)  # noqa: E501

Install solution template based on the provided id   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.install_solution_template(solution_template_id=deserialize_param(solution_template_id_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'install_solution_template'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def isDaemon() -> str:
    """
    Return whether this thread is a daemon.

This method is deprecated, use the daemon attribute instead.
    """
    try:
        client = get_client()
        result = client.isDaemon()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'isDaemon'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def is_alive() -> str:
    """
    Return whether the thread is alive.

This method returns True just before the run() method starts until just
after the run() method terminates. See also the module function
enumerate().
    """
    try:
        client = get_client()
        result = client.is_alive()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'is_alive'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def is_edge_upgrade_available(edge_id_json: str) -> str:
    """
    Is edge upgrade enabled (isEdgeUpgradeAvailable)  # noqa: E501

Returns 'true' if upgrade available for connected edge, 'false' - otherwise.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.is_edge_upgrade_available(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'is_edge_upgrade_available'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def is_edges_support_enabled() -> str:
    """
    Is edges support enabled (isEdgesSupportEnabled)  # noqa: E501

Returns 'true' if edges support enabled on server, 'false' - otherwise.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.is_edges_support_enabled()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'is_edges_support_enabled'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def is_edqs_api_enabled() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.is_edqs_api_enabled()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'is_edqs_api_enabled'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def is_tbel_enabled() -> str:
    """
    Is TBEL script executor enabled  # noqa: E501

Returns 'True' if the TBEL script execution is enabled  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.is_tbel_enabled()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'is_tbel_enabled'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def is_white_labeling_allowed() -> str:
    """
    Check White Labeling Allowed  # noqa: E501

Check if the White Labeling is enabled for the current user owner (tenant or customer)  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.is_white_labeling_allowed()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'is_white_labeling_allowed'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def join(timeout_json: str) -> str:
    """
    Wait until the thread terminates.

This blocks the calling thread until the thread whose join() method is
called terminates -- either normally or through an unhandled exception
or until the optional timeout occurs.

When the timeout argument is present and not None, it should be a
floating-point number specifying a timeout for the operation in seconds
(or fractions thereof). As join() always returns None, you must call
is_alive() after join() to decide whether a timeout happened -- if the
thread is still alive, the join() call timed out.

When the timeout argument is not present or None, the operation will
block until the thread terminates.

A thread can be join()ed many times.

join() raises a RuntimeError if an attempt is made to join the current
thread as that would cause a deadlock. It is also an error to join() a
thread before it has been started and attempts to do so raises the same
exception.
    """
    try:
        client = get_client()
        result = client.join(timeout=deserialize_param(timeout_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'join'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def list_all_entities_at_version(version_id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.list_all_entities_at_version(version_id=version_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'list_all_entities_at_version'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def list_branches() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.list_branches()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'list_branches'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def list_entities_at_version(entity_type: str, version_id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.list_entities_at_version(entity_type=entity_type, version_id=version_id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'list_entities_at_version'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def list_entity_type_versions(entity_type: str, branch: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.list_entity_type_versions(entity_type=entity_type, branch=branch, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'list_entity_type_versions'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def list_entity_versions(entity_type: str, external_entity_uuid: str, branch: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.list_entity_versions(entity_type=entity_type, external_entity_uuid=external_entity_uuid, branch=branch, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'list_entity_versions'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def list_slack_conversations(type: str, token: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.list_slack_conversations(type=type, token=token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'list_slack_conversations'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def list_versions(branch: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.list_versions(branch=branch, page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'list_versions'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def load_entities_version(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.load_entities_version(body=deserialize_param(body_json, 'VersionLoadRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'load_entities_version'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def mark_all_notifications_as_read() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.mark_all_notifications_as_read()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'mark_all_notifications_as_read'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def mark_notification_as_read(id: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.mark_notification_as_read(id=id)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'mark_notification_as_read'."
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

def patch_custom_translation(body_json: str, locale_code: str) -> str:
    """
    Update Custom Translation for specified translation keys only (patchCustomTranslation)  # noqa: E501

The API call is designed to update the custom translation for specified key only.    Request example:   ```json {"notification.active":"active"} ```  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.patch_custom_translation(body=deserialize_param(body_json, 'CustomTranslation'), locale_code=locale_code)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'patch_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def post_rpc_request(device_token: str, body_json: str = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.post_rpc_request(device_token=device_token, body=json.loads(body_json) if body_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'post_rpc_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def preview_white_label_params(body_json: str) -> str:
    """
    Preview Login White Labeling configuration (saveWhiteLabelParams)  # noqa: E501

Merge the White Labeling configuration with the parent configuration and return the result.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.preview_white_label_params(body=deserialize_param(body_json, 'WhiteLabelingParams'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'preview_white_label_params'."
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

def process_edges_bulk_import(body_json: str) -> str:
    """
    Import the bulk of edges (processEdgesBulkImport)  # noqa: E501

There's an ability to import the bulk of edges using the only .csv file.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.process_edges_bulk_import(body=deserialize_param(body_json, 'BulkImportRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'process_edges_bulk_import'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def process_system_edqs_request(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.process_system_edqs_request(body=deserialize_param(body_json, 'ToCoreEdqsRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'process_system_edqs_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def refresh() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.refresh()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'refresh'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def remove_mobile_session(x_mobile_token: str) -> str:
    """
    removeMobileSession  # noqa: E501
    """
    try:
        client = get_client()
        result = client.remove_mobile_session(x_mobile_token=x_mobile_token)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'remove_mobile_session'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def reply_to_command(device_token: str, request_id: int, body: Optional[str] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.reply_to_command(device_token=device_token, request_id=request_id, body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'reply_to_command'."
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

def reprocess_calculated_field(id_json: str, start_ts: int, end_ts: int) -> str:
    """
    Reprocess Calculated Field (reprocessCalculatedField)  # noqa: E501

Reprocesses the calculated field.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.reprocess_calculated_field(id=deserialize_param(id_json, 'CalculatedFieldId'), start_ts=start_ts, end_ts=end_ts)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'reprocess_calculated_field'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def reprocess_job(id_json: str) -> str:
    """
    Reprocess job (reprocessJob)  # noqa: E501

Reprocesses the job. Failures are located at job.result.results list. Platform iterates over this list and submits new tasks for them. Doesn't create new job entity but updates the existing one. Successfully reprocessed job will look the same as completed one.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.reprocess_job(id=deserialize_param(id_json, 'JobId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'reprocess_job'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def request_reset_password_by_email(body_json: str) -> str:
    """
    No description available.
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

def reset_password(body_json: str) -> str:
    """
    No description available.
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

def rpc_v2_get_persisted_rpc(rpc_id_json: str) -> str:
    """
    Get persistent RPC request  # noqa: E501

Get information about the status of the RPC call.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.rpc_v2_get_persisted_rpc(rpc_id=deserialize_param(rpc_id_json, 'RpcId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'rpc_v2_get_persisted_rpc'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def run() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.run()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'run'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_ai_model(body_json: str) -> str:
    """
    Create or update AI model (saveAiModel)  # noqa: E501

Creates or updates an AI model record.  • **Create:** Omit the `id` to create a new record. The platform assigns a UUID to the new record and returns it in the `id` field of the response.  • **Update:** Include an existing `id` to modify that record. If no matching record exists, the API responds with **404 Not Found**.  Tenant ID for the AI model will be taken from the authenticated user making the request, regardless of any value provided in the request body.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_ai_model(body=deserialize_param(body_json, 'AiModel'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_ai_model'."
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

def save_calculated_field(body_json: str) -> str:
    """
    Create Or Update Calculated Field (saveCalculatedField)  # noqa: E501

Creates or Updates the Calculated Field. When creating calculated field, platform generates Calculated Field Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Calculated Field Id will be present in the response. Specify existing Calculated Field Id to update the calculated field. Referencing non-existing Calculated Field Id will cause 'Not Found' error. Remove 'id', 'tenantId' from the request body example (below) to create new Calculated Field entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_calculated_field(body=deserialize_param(body_json, 'CalculatedField'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_calculated_field'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_client_registration_template(body_json: str) -> str:
    """
    No description available.
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

def save_converter(body_json: str) -> str:
    """
    Create Or Update Converter (saveConverter)  # noqa: E501

Create or update the Converter. When creating converter, platform generates Converter Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created converter id will be present in the response. Specify existing Converter id to update the converter. Referencing non-existing converter Id will cause 'Not Found' error. Converter name is unique in the scope of tenant.   # Converter Configuration  Converter configuration (**'configuration'** field) is the JSON object that should contain one of two possible fields: **'decoder'** or **'encoder'**. The former is used when the converter has UPLINK type, the latter is used - when DOWNLINK type. It can contain both 'decoder' and 'encoder' fields, when the correct one is specified for the appropriate converter type, another one can be set to 'null'. See the examples of each one below.   ## Uplink Converter Configuration  ***Default converter may be different, depending on integration type***.  ```json {    "decoder":"// Decode an uplink message from a buffer\\n// payload - array of bytes\\n// metadata - key/value object\\n\\n/** Decoder **/\\n\\n// decode payload to string\\nvar payloadStr = decodeToString(payload);\\n\\n// decode payload to JSON\\n// var data = decodeToJson(payload);\\n\\nvar deviceName = 'Device A';\\nvar deviceType = 'thermostat';\\nvar customerName = 'customer';\\nvar groupName = 'thermostat devices';\\nvar manufacturer = 'Example corporation';\\n// use assetName and assetType instead of deviceName and deviceType\\n// to automatically create assets instead of devices.\\n// var assetName = 'Asset A';\\n// var assetType = 'building';\\n\\n// Result object with device/asset attributes/telemetry data\\nvar result = {\\n// Use deviceName and deviceType or assetName and assetType, but not both.\\n   deviceName: deviceName,\\n   deviceType: deviceType,\\n// assetName: assetName,\\n// assetType: assetType,\\n   customerName: customerName,\\n   groupName: groupName,\\n   contentAwareAttributeKeys: ['manufacturer'],\\n   attributes: {\\n       model: 'Model A',\\n       serialNumber: 'SN111',\\n       integrationName: metadata['integrationName'],\\n       manufacturer: manufacturer\\n   },\\n   telemetry: {\\n       temperature: 42,\\n       humidity: 80,\\n       rawData: payloadStr\\n   }\\n};\\n\\n/** Helper functions **/\\n\\nfunction decodeToString(payload) {\\n   return String.fromCharCode.apply(String, payload);\\n}\\n\\nfunction decodeToJson(payload) {\\n   // covert payload to string.\\n   var str = decodeToString(payload);\\n\\n   // parse string to JSON\\n   var data = JSON.parse(str);\\n   return data;\\n}\\n\\nreturn result;",    "encoder":null } ```  Decoder field in the more readable form:  ```text // Decode an uplink message from a buffer // payload - array of bytes // metadata - key/value object  /** Decoder **/  // decode payload to string var payloadStr = decodeToString(payload);  // decode payload to JSON // var data = decodeToJson(payload);  var deviceName = 'Device A'; var deviceType = 'thermostat'; var customerName = 'customer'; var groupName = 'thermostat devices'; var manufacturer = 'Example corporation'; // use assetName and assetType instead of deviceName and deviceType // to automatically create assets instead of devices. // var assetName = 'Asset A'; // var assetType = 'building';  // Result object with device/asset attributes/telemetry data var result = { // Use deviceName and deviceType or assetName and assetType, but not both.    deviceName: deviceName,    deviceType: deviceType, // assetName: assetName, // assetType: assetType,    customerName: customerName,    groupName: groupName,    attributes: {        model: 'Model A',        serialNumber: 'SN111',        integrationName: metadata['integrationName']        manufacturer: manufacturer,    },    telemetry: {        temperature: 42,        humidity: 80,        rawData: payloadStr    } };  /** Helper functions **/  function decodeToString(payload) {    return String.fromCharCode.apply(String, payload); }  function decodeToJson(payload) {    // covert payload to string.    var str = decodeToString(payload);     // parse string to JSON    var data = JSON.parse(str);    return data; }  return result; ```  ## Downlink Converter Configuration  ```json {    "decoder":null,    "encoder":"// Encode downlink data from incoming Rule Engine message\\n\\n// msg - JSON message payload downlink message json\\n// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.\\n// metadata - list of key-value pairs with additional data about the message\\n// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter\\n\\n/** Encoder **/\\n\\nvar data = {};\\n\\n// Process data from incoming message and metadata\\n\\ndata.tempFreq = msg.temperatureUploadFrequency;\\ndata.humFreq = msg.humidityUploadFrequency;\\n\\ndata.devSerialNumber = metadata['ss_serialNumber'];\\n\\n// Result object with encoded downlink payload\\nvar result = {\\n\\n    // downlink data content type: JSON, TEXT or BINARY (base64 format)\\n    contentType: \\"JSON\\",\\n\\n    // downlink data\\n    data: JSON.stringify(data),\\n\\n    // Optional metadata object presented in key/value format\\n    metadata: {\\n            topic: metadata['deviceType']+'/'+metadata['deviceName']+'/upload'\\n    }\\n\\n};\\n\\nreturn result;" } ```  Encoder field in the more readable form:  ```text // Encode downlink data from incoming Rule Engine message  // msg - JSON message payload downlink message json // msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc. // metadata - list of key-value pairs with additional data about the message // integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter  /** Encoder **/  var data = {};  // Process data from incoming message and metadata  data.tempFreq = msg.temperatureUploadFrequency; data.humFreq = msg.humidityUploadFrequency;  data.devSerialNumber = metadata['ss_serialNumber'];  // Result object with encoded downlink payload var result = {      // downlink data content type: JSON, TEXT or BINARY (base64 format)     contentType: "JSON",      // downlink data     data: JSON.stringify(data),      // Optional metadata object presented in key/value format     metadata: {             topic: metadata['deviceType']+'/'+metadata['deviceName']+'/upload'     }  };  return result; ```  Remove 'id', 'tenantId' from the request body example (below) to create new converter entity.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_converter(body=deserialize_param(body_json, 'Converter'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_converter'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_custom_translation(locale_code: str, body_json: str) -> str:
    """
    Create Or Update Custom Translation (saveCustomTranslation)  # noqa: E501

Creates or Updates the Custom Translation map.   Request example:   ```json {"translationMap":{"es_ES":"{\\"home\\":\\"MyHome\\"}"}} ```  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_custom_translation(locale_code=locale_code, body=deserialize_param(body_json, 'CustomTranslation'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_custom_translation'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_domain(body_json: str, oauth2_client_ids: Optional[str] = None) -> str:
    """
    Save or Update Domain (saveDomain)  # noqa: E501

Create or update the Domain. When creating domain, platform generates Domain Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Domain Id will be present in the response. Specify existing Domain Id to update the domain. Referencing non-existing Domain Id will cause 'Not Found' error.  Domain name is unique for entire platform setup.    Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_domain(body=deserialize_param(body_json, 'Domain'), oauth2_client_ids=oauth2_client_ids)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_domain'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_edge(body_json: str) -> str:
    """
    Create Or Update Edge (saveEdge)  # noqa: E501

Create or update the Edge. When creating edge, platform generates Edge Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created edge id will be present in the response. Specify existing Edge id to update the edge. Referencing non-existing Edge Id will cause 'Not Found' error.  Edge name is unique in the scope of tenant. Use unique identifiers like MAC or IMEI for the edge names and non-unique 'label' field for user-friendly visualization purposes.Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Edge entity.   # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_edge(body=deserialize_param(body_json, 'Edge'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_entities_version(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.save_entities_version(body=deserialize_param(body_json, 'VersionCreateRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_entities_version'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_entity_view(body_json: str, entity_group_id_json: str, entity_group_ids_json: str = None) -> str:
    """
    Save or update entity view (saveEntityView)  # noqa: E501

Entity Views limit the degree of exposure of the Device or Asset telemetry and attributes to the Customers. Every Entity View references exactly one entity (device or asset) and defines telemetry and attribute keys that will be visible to the assigned Customer. As a Tenant Administrator you are able to create multiple EVs per Device or Asset and assign them to different Customers. See the 'Model' tab for more details.Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Entity View entity.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_entity_view(body=deserialize_param(body_json, 'EntityView'), entity_group_id=deserialize_param(entity_group_id_json, 'EntityGroupId'), entity_group_ids=json.loads(entity_group_ids_json) if entity_group_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_entity_view'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_group_permission(body_json: str) -> str:
    """
    Create Or Update Group Permission (saveGroupPermission)  # noqa: E501

Creates or Updates the Group Permission. When creating group permission, platform generates Group Permission Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Group Permission id will be present in the response. Specify existing Group Permission id to update the permission. Referencing non-existing Group Permission Id will cause 'Not Found' error.  Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_group_permission(body=deserialize_param(body_json, 'GroupPermission'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_group_permission'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_jwt_settings(body_json: str) -> str:
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

def save_login_white_label_params(body_json: str) -> str:
    """
    Create Or Update Login White Labeling configuration (saveWhiteLabelParams)  # noqa: E501

Creates or Updates the White Labeling configuration.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_login_white_label_params(body=deserialize_param(body_json, 'LoginWhiteLabelingParams'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_login_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_mobile_app(body_json: str, oauth2_client_ids: Optional[str] = None) -> str:
    """
    Save Or update Mobile app (saveMobileApp)  # noqa: E501

Create or update the Mobile app. When creating mobile app, platform generates Mobile App Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Mobile App Id will be present in the response. Specify existing Mobile App Id to update the mobile app. Referencing non-existing Mobile App Id will cause 'Not Found' error.  Mobile app package name is unique for entire platform setup.    Available for users with 'SYS_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_mobile_app(body=deserialize_param(body_json, 'MobileApp'), oauth2_client_ids=oauth2_client_ids)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_mobile_app'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_mobile_app_bundle(body_json: str, oauth2_client_ids_json: str = None) -> str:
    """
    Save Or update Mobile app bundle (saveMobileAppBundle)  # noqa: E501

Create or update the Mobile app bundle that represents tha pair of ANDROID and IOS app and mobile settings like oauth2 clients, self-registration and layout configuration.When creating mobile app bundle, platform generates Mobile App Bundle Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Mobile App Bundle Id will be present in the response. Referencing non-existing Mobile App Bundle Id will cause 'Not Found' error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_mobile_app_bundle(body=deserialize_param(body_json, 'MobileAppBundle'), oauth2_client_ids=json.loads(oauth2_client_ids_json) if oauth2_client_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_mobile_app_bundle'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_mobile_app_settings(body_json: str) -> str:
    """
    Create Or Update the Mobile application settings (saveMobileAppSettings)  # noqa: E501

The request payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_mobile_app_settings(body=deserialize_param(body_json, 'MobileAppSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_mobile_app_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_mobile_session(x_mobile_token: str, body_json: str) -> str:
    """
    saveMobileSession  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_mobile_session(x_mobile_token=x_mobile_token, body=deserialize_param(body_json, 'MobileSessionInfo'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_mobile_session'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_notification_rule(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.save_notification_rule(body=deserialize_param(body_json, 'NotificationRule'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_notification_rule'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_notification_settings(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.save_notification_settings(body=deserialize_param(body_json, 'NotificationSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_notification_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_notification_target(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.save_notification_target(body=deserialize_param(body_json, 'NotificationTarget'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_notification_target'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_notification_template(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.save_notification_template(body=deserialize_param(body_json, 'NotificationTemplate'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_notification_template'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_qr_code_settings(body_json: str) -> str:
    """
    Create Or Update the Mobile application settings (saveMobileAppSettings)  # noqa: E501

The request payload contains configuration for android/iOS applications and platform qr code widget settings.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_qr_code_settings(body=deserialize_param(body_json, 'QrCodeSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_qr_code_settings'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_queue(service_type: str, body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.save_queue(service_type=service_type, body=deserialize_param(body_json, 'Queue'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_queue'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_report_template(body_json: str) -> str:
    """
    Save Report Template (saveReportTemplate)  # noqa: E501

Creates or Updates report template. Report Template extends Report Template Info object and adds 'configuration' - a JSON structure of report template configuration. See the 'Model' tab of the Response Class for more details. When creating report template, platform generates report template Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created report template id will be present in the response. Specify existing report template id to update the report template. Referencing non-existing report template Id will cause 'Not Found' error. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Report Template entity.   Available for users with 'TENANT_ADMIN' authority.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_report_template(body=deserialize_param(body_json, 'ReportTemplate'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_report_template'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_repository_settings(body_json: str) -> str:
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

def save_resource(body_json: str) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.save_resource(body=deserialize_param(body_json, 'TbResource'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_resource'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_role(body_json: str) -> str:
    """
    Create Or Update Role (saveRole)  # noqa: E501

Creates or Updates the Role. When creating Role, platform generates Role Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Role id will be present in the response. Specify existing Role id to update the permission. Referencing non-existing Group Permission Id will cause 'Not Found' error.  Role Contains a set of permissions. Role has two types. Generic Role may be assigned to the user group and will provide permissions for all entities of a certain type. Group Role may be assigned to both user and entity group and will provides permissions only for the entities that belong to specified entity group. The assignment of the Role to the User Group is done using [Group Permission Controller](/swagger-ui.html#/group-permission-controller).  Example of Generic Role with read-only permissions for any resource and all permissions for the 'DEVICE' and 'PROFILE' resources is listed below:   ```json {   "name": "Read-Only User",   "type": "GENERIC",   "permissions": {     "ALL": [       "READ",       "RPC_CALL",       "READ_CREDENTIALS",       "READ_ATTRIBUTES",       "READ_TELEMETRY"     ],     "DEVICE": [       "ALL"     ]     "PROFILE": [       "ALL"     ]   },   "additionalInfo": {     "description": "Read-only permissions for everything, Write permissions for devices and own profile."   } } ```  Example of Group Role with read-only permissions. Note that the group role has no association with the resources. The type of the resource is taken from the entity group that this role is assigned to:   ```json {   "name": "Entity Group Read-only User",   "type": "GROUP",   "permissions": [     "READ",     "RPC_CALL",     "READ_CREDENTIALS",     "READ_ATTRIBUTES",     "READ_TELEMETRY"   ],   "additionalInfo": {     "description": "Read-only permissions."   } } ```   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_role(body=deserialize_param(body_json, 'Role'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_role'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_secret(body_json: str) -> str:
    """
    Save or Update Secret (saveSecret)  # noqa: E501

Create or update the Secret. When creating secret, platform generates Secret Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Secret Id will be present in the response. Specify existing Secret Id to update the secret. Secret name is not updatable, only value could be changed. Referencing non-existing Secret Id will cause 'Not Found' error.  Secret name is unique in the scope of tenant.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_secret(body=deserialize_param(body_json, 'Secret'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_secret'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def save_security_settings(body_json: str) -> str:
    """
    Update Security Settings (saveSecuritySettings)  # noqa: E501

Updates the Security Settings object that contains password policy, etc.  Available for users with 'SYS_ADMIN' authority.  Security check is performed to verify that the user has 'WRITE' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.  # noqa: E501
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

def save_self_registration_params(body_json: str) -> str:
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

def save_trendz_settings(body_json: str) -> str:
    """
    Save Trendz settings (saveTrendzSettings)  # noqa: E501

Saves Trendz settings for this tenant.   Here is an example of the Trendz settings: ```json {   "enabled": true,   "baseUrl": "https://some.domain.com:18888/also_necessary_prefix" } ```  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_trendz_settings(body=deserialize_param(body_json, 'TrendzSettings'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_trendz_settings'."
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

def save_white_label_params(body_json: str) -> str:
    """
    Create Or Update White Labeling configuration (saveWhiteLabelParams)  # noqa: E501

Creates or Updates the White Labeling configuration.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_white_label_params(body=deserialize_param(body_json, 'WhiteLabelingParams'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_white_label_params'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def send_activation_email(email: str) -> str:
    """
    Send or re-send the activation email  # noqa: E501

Force send the activation email to the user. Useful to resend the email if user has accidentally deleted it.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.send_activation_email(email=email)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'send_activation_email'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def send_chat_request(body_json: str) -> str:
    """
    Send request to AI chat model (sendChatRequest)  # noqa: E501

Submits a single prompt - made up of an optional system message and a required user message - to the specified AI chat model and returns either the generated answer or an error envelope.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.send_chat_request(body=deserialize_param(body_json, 'TbChatRequest'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'send_chat_request'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def send_password_was_reset_email(body_json: str) -> str:
    """
    sendPasswordWasResetEmail  # noqa: E501
    """
    try:
        client = get_client()
        result = client.send_password_was_reset_email(body=deserialize_param(body_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'send_password_was_reset_email'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def send_reset_password_email(body_json: str) -> str:
    """
    sendResetPasswordEmail  # noqa: E501
    """
    try:
        client = get_client()
        result = client.send_reset_password_email(body=deserialize_param(body_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'send_reset_password_email'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def send_test_mail(body_json: str) -> str:
    """
    Send test email (sendTestMail)  # noqa: E501

Attempts to send test email using Mail Settings provided as a parameter. Email is sent to the address specified in the profile of user who is performing the requestYou may change the 'To' email in the user profile of the System/Tenant Administrator.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.  # noqa: E501
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

def send_test_sms(body_json: str) -> str:
    """
    Send test sms (sendTestMail)  # noqa: E501

Attempts to send test sms to the System Administrator User using SMS Settings and phone number provided as a parameters of the request.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the 'ADMIN_SETTINGS' (for 'SYS_ADMIN' authority) or 'WHITE_LABELING' (for 'TENANT_ADMIN' authority) resource.  # noqa: E501
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

def setDaemon(daemonic_json: str) -> str:
    """
    Set whether this thread is a daemon.

This method is deprecated, use the .daemon property instead.
    """
    try:
        client = get_client()
        result = client.setDaemon(daemonic=deserialize_param(daemonic_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'setDaemon'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def setName(name_json: str) -> str:
    """
    Set the name string for this thread.

This method is deprecated, use the name attribute instead.
    """
    try:
        client = get_client()
        result = client.setName(name=deserialize_param(name_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'setName'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sig_fox_process_request_v11_post11(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v11_post11(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sig_fox_process_request_v11_post11'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sig_fox_process_request_v3_delete3(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_delete3(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sig_fox_process_request_v3_delete3'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sig_fox_process_request_v3_get3(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_get3(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sig_fox_process_request_v3_get3'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sig_fox_process_request_v3_head3(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_head3(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sig_fox_process_request_v3_head3'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sig_fox_process_request_v3_options3(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_options3(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sig_fox_process_request_v3_options3'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sig_fox_process_request_v3_patch3(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_patch3(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sig_fox_process_request_v3_patch3'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sig_fox_process_request_v3_put3(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sig_fox_process_request_v3_put3(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sig_fox_process_request_v3_put3'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sign_up(body_json: str) -> str:
    """
    User Sign Up (signUp)  # noqa: E501

Process user sign up request. Creates the Customer and corresponding User based on self Registration parameters for the domain. See [Self Registration Controller](/swagger-ui.html#/self-registration-controller) for more details.  The result is either 'SUCCESS' or 'INACTIVE_USER_EXISTS'. If Success, the user will receive an email with instruction to activate the account. The content of the email is customizable via the mail templates.  # noqa: E501
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

def start() -> str:
    """
    Start the thread's activity.

It must be called at most once per thread object. It arranges for the
object's run() method to be invoked in a separate thread of control.

This method will raise a RuntimeError if called more than once on the
same thread object.
    """
    try:
        client = get_client()
        result = client.start()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'start'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def stop() -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.stop()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'stop'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def subscribe_to_commands(device_token: str, timeout: Optional[int] = None) -> str:
    """
    No description available.
    """
    try:
        client = get_client()
        result = client.subscribe_to_commands(device_token=device_token, timeout=timeout)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'subscribe_to_commands'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def sync_edge(edge_id_json: str) -> str:
    """
    Sync edge (syncEdge)  # noqa: E501

Starts synchronization process between edge and cloud.  All entities that are assigned to particular edge are going to be send to remote edge service.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.sync_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'sync_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def t_mobile_iot_cdp_process_request_v12_post12(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v12_post12(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 't_mobile_iot_cdp_process_request_v12_post12'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def t_mobile_iot_cdp_process_request_v4_delete4(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_delete4(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 't_mobile_iot_cdp_process_request_v4_delete4'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def t_mobile_iot_cdp_process_request_v4_get4(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_get4(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 't_mobile_iot_cdp_process_request_v4_get4'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def t_mobile_iot_cdp_process_request_v4_head4(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_head4(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 't_mobile_iot_cdp_process_request_v4_head4'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def t_mobile_iot_cdp_process_request_v4_options4(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_options4(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 't_mobile_iot_cdp_process_request_v4_options4'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def t_mobile_iot_cdp_process_request_v4_patch4(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_patch4(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 't_mobile_iot_cdp_process_request_v4_patch4'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def t_mobile_iot_cdp_process_request_v4_put4(body: str, request_headers_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.t_mobile_iot_cdp_process_request_v4_put4(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 't_mobile_iot_cdp_process_request_v4_put4'."
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

def test_down_link_converter(body_json: str = None, script_lang: Optional[str] = None) -> str:
    """
    Test converter function (testDownLinkConverter)  # noqa: E501

Returns a JSON object representing the result of the processed incoming message.   ## Request Body Example  ```json {    "metadata":{       "data":"40"    },    "msg":"{\\n    \\"temp\\": 42,\\n    \\"humidity\\": 77\\n}",    "msgType":"POST_TELEMETRY_REQUEST",    "integrationMetadata":{       "integrationName":"Integration"    },    "encoder":"// Encode downlink data from incoming Rule Engine message\\n\\n// msg - JSON message payload downlink message json\\n// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.\\n// metadata - list of key-value pairs with additional data about the message\\n// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter\\n\\n/** Encoder **/\\n\\nvar data = {};\\n\\n// Process data from incoming message and metadata\\n\\ndata.tempValue = msg.temp;\\ndata.humValue = msg.humidity;\\n\\ndata.devSerialNumber = metadata['ss_serialNumber'];\\n\\n// Result object with encoded downlink payload\\nvar result = {\\n\\n    // downlink data content type: JSON, TEXT or BINARY (base64 format)\\n    contentType: \\"JSON\\",\\n\\n    // downlink data\\n    data: JSON.stringify(data),\\n\\n    // Optional metadata object presented in key/value format\\n    metadata: {\\n            topic: metadata['deviceType']+'/'+metadata['deviceName']+'/upload'\\n    }\\n\\n};\\n\\nreturn result;" } ```   * 'metadata' - message metadata pushed from the rule engine;   * 'msg' - message data pushed from the rule engine;   * 'msgType' - type of the message pushed from the rule engine;   * 'integrationMetadata' - integration metadata object;   * 'encoder' - string representation of the encoder configuration.  ## Response Body Example  ```json {    "contentType":"JSON",    "data":"{\\"tempValue\\":42,\\"humValue\\":77}",    "metadata":{       "topic":"sensor/Temp Sensor/upload"    } } ```   * 'contentType' - downlink data content type;   * 'data' - downlink data;   * 'metadata' - optional metadata object.    # noqa: E501
    """
    try:
        client = get_client()
        result = client.test_down_link_converter(body=json.loads(body_json) if body_json else None, script_lang=script_lang)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'test_down_link_converter'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def test_script(body_json: str) -> str:
    """
    Test Script function  # noqa: E501

Execute the Script function and return the result. The format of request:   ```json {   "script": "Your Function as String",   "scriptType": "One of: update, generate, filter, switch, json, string",   "argNames": ["msg", "metadata", "type"],   "msg": "{\\"temperature\\": 42}",    "metadata": {     "deviceName": "Device A",     "deviceType": "Thermometer"   },   "msgType": "POST_TELEMETRY_REQUEST" } ```   Expected result JSON contains "output" and "error".  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.test_script(body=deserialize_param(body_json, 'RuleChain'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'test_script'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def test_up_link_converter(body_json: str = None, script_lang: Optional[str] = None) -> str:
    """
    Test converter function (testUpLinkConverter)  # noqa: E501

Returns a JSON object representing the result of the processed incoming message.   ## Request Body Example  ```json {    "metadata":{    },    "payload":"ewogICAgImRhdGEiOiAiZGF0YSIKfQ==",    "decoder":"// Decode an uplink message from a buffer\\n// payload - array of bytes\\n// metadata - key/value object\\n\\n/** Decoder **/\\n\\n// decode payload to string\\nvar payloadStr = decodeToString(payload);\\n\\n// decode payload to JSON\\n// var data = decodeToJson(payload);\\n\\nvar deviceName = 'Device A';\\nvar deviceType = 'thermostat';\\nvar customerName = 'customer';\\nvar groupName = 'thermostat devices';\\nvar manufacturer = 'Example corporation';\\n// use assetName and assetType instead of deviceName and deviceType\\n// to automatically create assets instead of devices.\\n// var assetName = 'Asset A';\\n// var assetType = 'building';\\n\\n// Result object with device/asset attributes/telemetry data\\nvar result = {\\n// Use deviceName and deviceType or assetName and assetType, but not both.\\n   deviceName: deviceName,\\n   deviceType: deviceType,\\n// assetName: assetName,\\n// assetType: assetType,\\n   customerName: customerName,\\n   groupName: groupName,\\n   attributes: {\\n       model: 'Model A',\\n       serialNumber: 'SN111',\\n       integrationName: metadata['integrationName']\\n       manufacturer: manufacturer\\n   },\\n   telemetry: {\\n       temperature: 42,\\n       humidity: 80,\\n       rawData: payloadStr\\n   }\\n};\\n\\n/** Helper functions **/\\n\\nfunction decodeToString(payload) {\\n   return String.fromCharCode.apply(String, payload);\\n}\\n\\nfunction decodeToJson(payload) {\\n   // covert payload to string.\\n   var str = decodeToString(payload);\\n\\n   // parse string to JSON\\n   var data = JSON.parse(str);\\n   return data;\\n}\\n\\nreturn result;" } ```   * 'metadata' - integration metadata;   * 'payload' - base64 string representation of the data;   * 'decoder' - string representation of the decoder configuration.  ## Response Body Example  ```json {    "output":"{\\"deviceName\\":\\"Device A\\",\\"deviceType\\":\\"thermostat\\",\\"customerName\\":\\"customer\\",\\"groupName\\":\\"thermostat devices\\",\\"attributes\\":{\\"model\\":\\"Model A\\",\\"serialNumber\\":\\"SN111\\"},\\"telemetry\\":{\\"temperature\\":42,\\"humidity\\":80,\\"rawData\\":\\"{\\\\n    \\\\\\"data\\\\\\": \\\\\\"data\\\\\\"\\\\n}\\"}}",    "error":"" } ```   * 'output' - string representation of the output message;   * 'error' - string representation of the error message.    # noqa: E501
    """
    try:
        client = get_client()
        result = client.test_up_link_converter(body=json.loads(body_json) if body_json else None, script_lang=script_lang)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'test_up_link_converter'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_tpe_delete(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequestTPE  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_delete(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_tpe_delete'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_tpe_get(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequestTPE  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_get(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_tpe_get'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_tpe_head(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequestTPE  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_head(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_tpe_head'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_tpe_options(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequestTPE  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_options(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_tpe_options'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_tpe_patch(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequestTPE  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_patch(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_tpe_patch'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_tpe_post(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequestTPE  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_post(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_tpe_post'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_tpe_put(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequestTPE  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_tpe_put(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_tpe_put'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_v13_post13(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v13_post13(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_v13_post13'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_v5_delete5(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_delete5(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_v5_delete5'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_v5_get5(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_get5(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_v5_get5'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_v5_head5(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_head5(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_v5_head5'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_v5_options5(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_options5(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_v5_options5'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_v5_patch5(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_patch5(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_v5_patch5'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def thing_park_process_request_v5_put5(body: str, request_headers_json: str, all_request_params_json: str, routing_key: str) -> str:
    """
    processRequest  # noqa: E501
    """
    try:
        client = get_client()
        result = client.thing_park_process_request_v5_put5(body=body, request_headers=json.loads(request_headers_json) if request_headers_json else None, all_request_params=json.loads(all_request_params_json) if all_request_params_json else None, routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'thing_park_process_request_v5_put5'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def uninstall_solution_template(solution_template_id_json: str) -> str:
    """
    Uninstall Solution Template (uninstallSolutionTemplate)  # noqa: E501

Uninstall solution template based on the provided id   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.uninstall_solution_template(solution_template_id=deserialize_param(solution_template_id_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'uninstall_solution_template'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_custom_menu_assignee_list(id_json: str, assignee_type: str, body_json: str, force: Optional[bool] = None) -> str:
    """
    Update custom menu assignee list (updateCustomMenuAssigneeList)  # noqa: E501

The api designed to update the list of assignees or assignee type based on the provided Custom Menu Id. To change assignee type, put new assignee type in path parameter.  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_custom_menu_assignee_list(id=deserialize_param(id_json, 'CustomMenuId'), assignee_type=assignee_type, body=json.loads(body_json) if body_json else None, force=force)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_custom_menu_assignee_list'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_custom_menu_config(id_json: str, body_json: str) -> str:
    """
    Update Custom Menu configuration based on the provided Custom Menu Id (updateCustomMenuConfig)  # noqa: E501

  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_custom_menu_config(id=deserialize_param(id_json, 'CustomMenuId'), body=deserialize_param(body_json, 'CustomMenuConfig'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_custom_menu_config'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_custom_menu_name(id_json: str, body: str) -> str:
    """
    Update Custom Menu name based on the provided Custom Menu Id (updateCustomMenuName)  # noqa: E501

  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_custom_menu_name(id=deserialize_param(id_json, 'CustomMenuId'), body=body)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_custom_menu_name'."
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

def update_secret_description(id_json: str, description: str) -> str:
    """
    Update Secret Description  # noqa: E501

Updates the description of the existing Secret by secretId. Only the description can be updated. Referencing a non-existing Secret Id will cause a 'Not Found' error.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_secret_description(id=deserialize_param(id_json, 'SecretId'), description=description)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_secret_description'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def update_secret_value(id_json: str, value: str) -> str:
    """
    Update Secret value  # noqa: E501

Updates the value of the existing Secret by secretId. Referencing a non-existing Secret Id will cause a 'Not Found' error.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.update_secret_value(id=deserialize_param(id_json, 'SecretId'), value=value)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'update_secret_value'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def upload_custom_translation(locale_code: str, file_json: str) -> str:
    """
    Upload Custom Translation (uploadCustomTranslation)  # noqa: E501

Upload the Custom Translation for specified locale.   Request example:   ```json {"home":"MyHome"} ```  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.upload_custom_translation(locale_code=locale_code, file=deserialize_param(file_json, '_empty'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'upload_custom_translation'."
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

def validate_calculated_field_reprocessing(id_json: str) -> str:
    """
    Validate reprocessing capability of a calculated field (validateCalculatedFieldReprocessing)  # noqa: E501

Checks whether the specified calculated field can be reprocessed. Returns a validation result indicating if reprocessing is allowed and, if not, provides a reason.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.validate_calculated_field_reprocessing(id=deserialize_param(id_json, 'CalculatedFieldId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'validate_calculated_field_reprocessing'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"

def register(mcp):
    mcp.tool()( accept_terms_of_use )
    mcp.tool()( activate_email )
    mcp.tool()( activate_instance )
    mcp.tool()( auto_commit_settings_exists )
    mcp.tool()( cancel_job )
    mcp.tool()( change_password )
    mcp.tool()( check_activate_token )
    mcp.tool()( check_instance )
    mcp.tool()( check_repository_access )
    mcp.tool()( check_reset_token )
    mcp.tool()( check_updates )
    mcp.tool()( chirp_stack_process_request_delete )
    mcp.tool()( chirp_stack_process_request_get )
    mcp.tool()( chirp_stack_process_request_head )
    mcp.tool()( chirp_stack_process_request_options )
    mcp.tool()( chirp_stack_process_request_patch )
    mcp.tool()( chirp_stack_process_request_post )
    mcp.tool()( chirp_stack_process_request_put )
    mcp.tool()( clear_events_post )
    mcp.tool()( code_processing_url )
    mcp.tool()( compare_entity_data_to_version )
    mcp.tool()( count_entities_by_query )
    mcp.tool()( create_custom_menu )
    mcp.tool()( create_notification_request )
    mcp.tool()( delete_ai_model_by_id )
    mcp.tool()( delete_auto_commit_settings )
    mcp.tool()( delete_blob_entity )
    mcp.tool()( delete_calculated_field )
    mcp.tool()( delete_client_registration_template )
    mcp.tool()( delete_converter )
    mcp.tool()( delete_current_login_white_label_params )
    mcp.tool()( delete_current_white_label_params )
    mcp.tool()( delete_custom_menu )
    mcp.tool()( delete_custom_translation )
    mcp.tool()( delete_custom_translation_key )
    mcp.tool()( delete_domain )
    mcp.tool()( delete_edge )
    mcp.tool()( delete_entity_view )
    mcp.tool()( delete_group_permission )
    mcp.tool()( delete_image )
    mcp.tool()( delete_job )
    mcp.tool()( delete_mobile_app )
    mcp.tool()( delete_mobile_app_bundle )
    mcp.tool()( delete_notification )
    mcp.tool()( delete_notification_request )
    mcp.tool()( delete_notification_rule )
    mcp.tool()( delete_notification_target_by_id )
    mcp.tool()( delete_notification_template_by_id )
    mcp.tool()( delete_queue )
    mcp.tool()( delete_report_template )
    mcp.tool()( delete_repository_settings )
    mcp.tool()( delete_role )
    mcp.tool()( delete_rpc )
    mcp.tool()( delete_secret )
    mcp.tool()( delete_self_registration_params )
    mcp.tool()( delete_web_self_registration_params )
    mcp.tool()( download_blob_entity )
    mcp.tool()( download_full_translation )
    mcp.tool()( download_gateway_docker_compose )
    mcp.tool()( download_image )
    mcp.tool()( download_image_preview )
    mcp.tool()( download_jks_resource_if_changed )
    mcp.tool()( download_js_resource_if_changed )
    mcp.tool()( download_login_favicon )
    mcp.tool()( download_login_logo )
    mcp.tool()( download_lwm2m_resource_if_changed )
    mcp.tool()( download_pkcs12_resource_if_changed )
    mcp.tool()( download_public_image )
    mcp.tool()( download_resource )
    mcp.tool()( download_resource_if_changed )
    mcp.tool()( download_server_certificate )
    mcp.tool()( download_test_report )
    mcp.tool()( export_image )
    mcp.tool()( find_by_from )
    mcp.tool()( find_by_from_v1 )
    mcp.tool()( find_by_query )
    mcp.tool()( find_by_query_v1 )
    mcp.tool()( find_by_query_v2 )
    mcp.tool()( find_by_query_v3 )
    mcp.tool()( find_by_query_v4 )
    mcp.tool()( find_by_to )
    mcp.tool()( find_by_to_v1 )
    mcp.tool()( find_entity_data_by_query )
    mcp.tool()( find_info_by_from )
    mcp.tool()( find_info_by_query )
    mcp.tool()( find_info_by_to )
    mcp.tool()( getName )
    mcp.tool()( get_activation_link )
    mcp.tool()( get_activation_link_info )
    mcp.tool()( get_ai_model_by_id )
    mcp.tool()( get_ai_models )
    mcp.tool()( get_all_entity_view_infos )
    mcp.tool()( get_all_report_template_infos )
    mcp.tool()( get_allowed_permissions )
    mcp.tool()( get_application_redirect )
    mcp.tool()( get_auto_commit_settings )
    mcp.tool()( get_available_delivery_methods )
    mcp.tool()( get_available_java_locales )
    mcp.tool()( get_available_locales )
    mcp.tool()( get_blob_entities )
    mcp.tool()( get_blob_entities_by_ids )
    mcp.tool()( get_blob_entity_info_by_id )
    mcp.tool()( get_calculated_field_by_id )
    mcp.tool()( get_calculated_fields_by_entity_id )
    mcp.tool()( get_client_registration_templates )
    mcp.tool()( get_client_registration_templates1 )
    mcp.tool()( get_client_registration_templates_mail )
    mcp.tool()( get_component_descriptor_by_clazz )
    mcp.tool()( get_component_descriptors_by_type )
    mcp.tool()( get_component_descriptors_by_types )
    mcp.tool()( get_converter_by_id )
    mcp.tool()( get_converters )
    mcp.tool()( get_converters_by_ids )
    mcp.tool()( get_current_login_white_label_params )
    mcp.tool()( get_current_white_label_params )
    mcp.tool()( get_custom_menu )
    mcp.tool()( get_custom_menu_assignee_list )
    mcp.tool()( get_custom_menu_config )
    mcp.tool()( get_custom_menu_info_by_id )
    mcp.tool()( get_custom_menu_infos )
    mcp.tool()( get_custom_translation )
    mcp.tool()( get_domain_info_by_id )
    mcp.tool()( get_domain_infos )
    mcp.tool()( get_downlink_converter )
    mcp.tool()( get_downlink_converter_metadata )
    mcp.tool()( get_downlink_payload )
    mcp.tool()( get_edge_by_id )
    mcp.tool()( get_edge_events )
    mcp.tool()( get_edge_install_instructions )
    mcp.tool()( get_edge_types )
    mcp.tool()( get_edge_upgrade_instructions )
    mcp.tool()( get_edges )
    mcp.tool()( get_edges_by_ids )
    mcp.tool()( get_edqs_state )
    mcp.tool()( get_entities )
    mcp.tool()( get_entity_data_info )
    mcp.tool()( get_entity_view_by_id )
    mcp.tool()( get_entity_view_info_by_id )
    mcp.tool()( get_entity_view_types )
    mcp.tool()( get_entity_views_by_ids )
    mcp.tool()( get_events_get )
    mcp.tool()( get_events_post )
    mcp.tool()( get_events_v1_get1 )
    mcp.tool()( get_features_info )
    mcp.tool()( get_firmware )
    mcp.tool()( get_firmware_by_id )
    mcp.tool()( get_full_translation )
    mcp.tool()( get_group_entity )
    mcp.tool()( get_group_permission_by_id )
    mcp.tool()( get_group_permission_info_by_id )
    mcp.tool()( get_help_base_url )
    mcp.tool()( get_image_info )
    mcp.tool()( get_images )
    mcp.tool()( get_job_by_id )
    mcp.tool()( get_jobs )
    mcp.tool()( get_jwt_setting )
    mcp.tool()( get_last_calculated_field_reprocessing_job )
    mcp.tool()( get_latest_calculated_field_debug_event )
    mcp.tool()( get_latest_converter_debug_input )
    mcp.tool()( get_latest_rule_node_debug_input )
    mcp.tool()( get_license_usage_info )
    mcp.tool()( get_login_mobile_info )
    mcp.tool()( get_login_page_translation )
    mcp.tool()( get_login_processing_url )
    mcp.tool()( get_login_white_label_params )
    mcp.tool()( get_lwm2m_bootstrap_security_info )
    mcp.tool()( get_lwm2m_list_objects )
    mcp.tool()( get_lwm2m_list_objects_page )
    mcp.tool()( get_mail_processing_url )
    mcp.tool()( get_max_datapoints_limit )
    mcp.tool()( get_merged_custom_translation )
    mcp.tool()( get_merged_mobile_app_settings )
    mcp.tool()( get_mobile_app_bundle_info_by_id )
    mcp.tool()( get_mobile_app_by_id )
    mcp.tool()( get_mobile_app_deep_link )
    mcp.tool()( get_mobile_app_info_by_id )
    mcp.tool()( get_mobile_app_settings )
    mcp.tool()( get_mobile_session )
    mcp.tool()( get_notification_request_by_id )
    mcp.tool()( get_notification_request_preview )
    mcp.tool()( get_notification_requests )
    mcp.tool()( get_notification_rule_by_id )
    mcp.tool()( get_notification_rules )
    mcp.tool()( get_notification_settings )
    mcp.tool()( get_notification_target_by_id )
    mcp.tool()( get_notification_targets )
    mcp.tool()( get_notification_targets_by_ids )
    mcp.tool()( get_notification_targets_by_supported_notification_type )
    mcp.tool()( get_notification_template_by_id )
    mcp.tool()( get_notification_templates )
    mcp.tool()( get_notifications )
    mcp.tool()( get_owner_info )
    mcp.tool()( get_owner_infos )
    mcp.tool()( get_owners )
    mcp.tool()( get_persisted_rpc )
    mcp.tool()( get_privacy_policy )
    mcp.tool()( get_qr_code_settings )
    mcp.tool()( get_queue_by_id )
    mcp.tool()( get_queue_by_name )
    mcp.tool()( get_queue_stats_by_id )
    mcp.tool()( get_queue_stats_by_ids )
    mcp.tool()( get_recipients_for_notification_target_config )
    mcp.tool()( get_report_template_by_id )
    mcp.tool()( get_report_template_info_by_id )
    mcp.tool()( get_report_templates_by_ids )
    mcp.tool()( get_repository_settings )
    mcp.tool()( get_repository_settings_info )
    mcp.tool()( get_resource_by_id )
    mcp.tool()( get_resource_info_by_id )
    mcp.tool()( get_resources )
    mcp.tool()( get_role_by_id )
    mcp.tool()( get_roles )
    mcp.tool()( get_roles_by_ids )
    mcp.tool()( get_secret_info_by_id )
    mcp.tool()( get_secret_info_by_name )
    mcp.tool()( get_secret_infos )
    mcp.tool()( get_secret_names )
    mcp.tool()( get_security_settings )
    mcp.tool()( get_self_registration_params )
    mcp.tool()( get_server_time )
    mcp.tool()( get_sign_up_self_registration_params )
    mcp.tool()( get_software )
    mcp.tool()( get_solution_template_details )
    mcp.tool()( get_solution_template_infos )
    mcp.tool()( get_solution_template_instructions )
    mcp.tool()( get_system_info )
    mcp.tool()( get_terms_of_use )
    mcp.tool()( get_translation_for_basic_edit )
    mcp.tool()( get_translation_infos )
    mcp.tool()( get_trendz_settings )
    mcp.tool()( get_unread_notifications_count )
    mcp.tool()( get_uplink_converter )
    mcp.tool()( get_uplink_converter_metadata )
    mcp.tool()( get_uplink_payload )
    mcp.tool()( get_vendor_models )
    mcp.tool()( get_vendors )
    mcp.tool()( get_version_create_request_status )
    mcp.tool()( get_version_load_request_status )
    mcp.tool()( get_web_self_registration_params )
    mcp.tool()( get_white_label_params )
    mcp.tool()( handle_rule_engine_request )
    mcp.tool()( handle_rule_engine_request_v1 )
    mcp.tool()( handle_rule_engine_request_v2 )
    mcp.tool()( http_check_status_get )
    mcp.tool()( http_process_request_v1_post1 )
    mcp.tool()( http_process_request_v2_post2 )
    mcp.tool()( import_image )
    mcp.tool()( install_solution_template )
    mcp.tool()( isDaemon )
    mcp.tool()( is_alive )
    mcp.tool()( is_edge_upgrade_available )
    mcp.tool()( is_edges_support_enabled )
    mcp.tool()( is_edqs_api_enabled )
    mcp.tool()( is_tbel_enabled )
    mcp.tool()( is_white_labeling_allowed )
    mcp.tool()( join )
    mcp.tool()( list_all_entities_at_version )
    mcp.tool()( list_branches )
    mcp.tool()( list_entities_at_version )
    mcp.tool()( list_entity_type_versions )
    mcp.tool()( list_entity_versions )
    mcp.tool()( list_slack_conversations )
    mcp.tool()( list_versions )
    mcp.tool()( load_entities_version )
    mcp.tool()( mark_all_notifications_as_read )
    mcp.tool()( mark_notification_as_read )
    mcp.tool()( mobile_login )
    mcp.tool()( patch_custom_translation )
    mcp.tool()( post_rpc_request )
    mcp.tool()( preview_white_label_params )
    mcp.tool()( privacy_policy_accepted )
    mcp.tool()( process_edges_bulk_import )
    mcp.tool()( process_system_edqs_request )
    mcp.tool()( refresh )
    mcp.tool()( remove_mobile_session )
    mcp.tool()( reply_to_command )
    mcp.tool()( repository_settings_exists )
    mcp.tool()( reprocess_calculated_field )
    mcp.tool()( reprocess_job )
    mcp.tool()( request_reset_password_by_email )
    mcp.tool()( resend_email_activation )
    mcp.tool()( reset_password )
    mcp.tool()( rpc_v2_get_persisted_rpc )
    mcp.tool()( run )
    mcp.tool()( save_ai_model )
    mcp.tool()( save_auto_commit_settings )
    mcp.tool()( save_calculated_field )
    mcp.tool()( save_client_registration_template )
    mcp.tool()( save_converter )
    mcp.tool()( save_custom_translation )
    mcp.tool()( save_domain )
    mcp.tool()( save_edge )
    mcp.tool()( save_entities_version )
    mcp.tool()( save_entity_view )
    mcp.tool()( save_group_permission )
    mcp.tool()( save_jwt_settings )
    mcp.tool()( save_login_white_label_params )
    mcp.tool()( save_mobile_app )
    mcp.tool()( save_mobile_app_bundle )
    mcp.tool()( save_mobile_app_settings )
    mcp.tool()( save_mobile_session )
    mcp.tool()( save_notification_rule )
    mcp.tool()( save_notification_settings )
    mcp.tool()( save_notification_target )
    mcp.tool()( save_notification_template )
    mcp.tool()( save_qr_code_settings )
    mcp.tool()( save_queue )
    mcp.tool()( save_report_template )
    mcp.tool()( save_repository_settings )
    mcp.tool()( save_resource )
    mcp.tool()( save_role )
    mcp.tool()( save_secret )
    mcp.tool()( save_security_settings )
    mcp.tool()( save_self_registration_params )
    mcp.tool()( save_trendz_settings )
    mcp.tool()( save_web_self_registration_params )
    mcp.tool()( save_white_label_params )
    mcp.tool()( send_activation_email )
    mcp.tool()( send_chat_request )
    mcp.tool()( send_password_was_reset_email )
    mcp.tool()( send_reset_password_email )
    mcp.tool()( send_test_mail )
    mcp.tool()( send_test_sms )
    mcp.tool()( setDaemon )
    mcp.tool()( setName )
    mcp.tool()( sig_fox_process_request_v11_post11 )
    mcp.tool()( sig_fox_process_request_v3_delete3 )
    mcp.tool()( sig_fox_process_request_v3_get3 )
    mcp.tool()( sig_fox_process_request_v3_head3 )
    mcp.tool()( sig_fox_process_request_v3_options3 )
    mcp.tool()( sig_fox_process_request_v3_patch3 )
    mcp.tool()( sig_fox_process_request_v3_put3 )
    mcp.tool()( sign_up )
    mcp.tool()( start )
    mcp.tool()( stop )
    mcp.tool()( subscribe_to_commands )
    mcp.tool()( sync_edge )
    mcp.tool()( t_mobile_iot_cdp_process_request_v12_post12 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_delete4 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_get4 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_head4 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_options4 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_patch4 )
    mcp.tool()( t_mobile_iot_cdp_process_request_v4_put4 )
    mcp.tool()( terms_of_use_accepted )
    mcp.tool()( test_down_link_converter )
    mcp.tool()( test_script )
    mcp.tool()( test_up_link_converter )
    mcp.tool()( thing_park_process_request_tpe_delete )
    mcp.tool()( thing_park_process_request_tpe_get )
    mcp.tool()( thing_park_process_request_tpe_head )
    mcp.tool()( thing_park_process_request_tpe_options )
    mcp.tool()( thing_park_process_request_tpe_patch )
    mcp.tool()( thing_park_process_request_tpe_post )
    mcp.tool()( thing_park_process_request_tpe_put )
    mcp.tool()( thing_park_process_request_v13_post13 )
    mcp.tool()( thing_park_process_request_v5_delete5 )
    mcp.tool()( thing_park_process_request_v5_get5 )
    mcp.tool()( thing_park_process_request_v5_head5 )
    mcp.tool()( thing_park_process_request_v5_options5 )
    mcp.tool()( thing_park_process_request_v5_patch5 )
    mcp.tool()( thing_park_process_request_v5_put5 )
    mcp.tool()( uninstall_solution_template )
    mcp.tool()( update_custom_menu_assignee_list )
    mcp.tool()( update_custom_menu_config )
    mcp.tool()( update_custom_menu_name )
    mcp.tool()( update_image )
    mcp.tool()( update_image_info )
    mcp.tool()( update_image_public_status )
    mcp.tool()( update_secret_description )
    mcp.tool()( update_secret_value )
    mcp.tool()( upload_custom_translation )
    mcp.tool()( upload_image )
    mcp.tool()( validate_calculated_field_reprocessing )
