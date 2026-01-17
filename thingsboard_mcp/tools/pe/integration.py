import json
from typing import Optional
import tb_rest_client.models.models_pe as models
from ..shared import get_client, deserialize_param, format_response, ApiException


def assign_integration_to_edge(edge_id_json: str, integration_id_json: str) -> str:
    """
    Assign integration to edge (assignIntegrationToEdge)  # noqa: E501

Creates assignment of an existing integration edge template to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment integration (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once integration will be delivered to edge service, it's going to start locally.   Only integration edge template can be assigned to edge.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.assign_integration_to_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), integration_id=deserialize_param(integration_id_json, 'IntegrationId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'assign_integration_to_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def check_integration_connection(body_json: str = None) -> str:
    """
    Check integration connectivity (checkIntegrationConnection)  # noqa: E501

Checks if the connection to the integration is established. Throws an error if the connection is not established. Example: Failed to connect to MQTT broker at host:port.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.check_integration_connection(body=deserialize_param(body_json, 'Integration'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'check_integration_connection'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def delete_integration(integration_id_json: str) -> str:
    """
    Delete integration (deleteIntegration)  # noqa: E501

Deletes the integration and all the relations (from and to the integration). Referencing non-existing integration Id will cause an error.    Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.delete_integration(integration_id=deserialize_param(integration_id_json, 'IntegrationId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'delete_integration'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def find_all_related_edges_missing_attributes(integration_id_json: str) -> str:
    """
    Find missing attributes for all related edges (findAllRelatedEdgesMissingAttributes)  # noqa: E501

Returns list of attribute names of all related edges that are missing in the integration configuration.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_all_related_edges_missing_attributes(integration_id=deserialize_param(integration_id_json, 'IntegrationId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_all_related_edges_missing_attributes'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def find_edge_missing_attributes_get(edge_id_json: str, integration_ids: str) -> str:
    """
    Find edge missing attributes for assigned integrations (findEdgeMissingAttributes)  # noqa: E501

Returns list of edge attribute names that are missing in assigned integrations.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.find_edge_missing_attributes_get(edge_id=deserialize_param(edge_id_json, 'EdgeId'), integration_ids=integration_ids)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'find_edge_missing_attributes_get'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_edge_integration_infos(edge_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Edge Integrations (getEdgeIntegrationInfos)  # noqa: E501

Returns a page of Integrations assigned to the specified edge. The integration object contains information about the Integration, including the heavyweight configuration object. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_integration_infos(edge_id=deserialize_param(edge_id_json, 'EdgeId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_integration_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_edge_integrations(edge_id_json: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Edge Integrations (getEdgeIntegrations)  # noqa: E501

Returns a page of Integrations assigned to the specified edge. The integration object contains information about the Integration, including the heavyweight configuration object. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_edge_integrations(edge_id=deserialize_param(edge_id_json, 'EdgeId'), page_size=page_size, page=page, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_edge_integrations'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_integration_by_id(integration_id_json: str) -> str:
    """
    Get Integration (getIntegrationById)  # noqa: E501

Fetch the Integration object based on the provided Integration Id. The server checks that the integration is owned by the same tenant.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_integration_by_id(integration_id=deserialize_param(integration_id_json, 'IntegrationId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_integration_by_id'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_integration_by_routing_key(routing_key: str) -> str:
    """
    Get Integration by Routing Key (getIntegrationByRoutingKey)  # noqa: E501

Fetch the Integration object based on the provided routing key. The server checks that the integration is owned by the same tenant.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_integration_by_routing_key(routing_key=routing_key)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_integration_by_routing_key'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_integration_infos(page_size: int, page: int, is_edge_template: bool, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Integration Infos (getIntegrationInfos)  # noqa: E501

Returns a page of integration infos owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_integration_infos(page_size=page_size, page=page, is_edge_template=is_edge_template, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_integration_infos'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_integrations(page_size: int, page: int, is_edge_template: bool, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None) -> str:
    """
    Get Integrations (getIntegrations)  # noqa: E501

Returns a page of integrations owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_integrations(page_size=page_size, page=page, is_edge_template=is_edge_template, text_search=text_search, sort_property=sort_property, sort_order=sort_order)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_integrations'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_integrations_by_ids(integration_ids_json: str) -> str:
    """
    Get Integrations By Ids (getIntegrationsByIds)  # noqa: E501

Requested integrations must be owned by tenant which is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_integrations_by_ids(integration_ids=json.loads(integration_ids_json) if integration_ids_json else None)
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_integrations_by_ids'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def get_integrations_converters_info() -> str:
    """
    Get Integrations Converters info (getIntegrationsConvertersInfo)  # noqa: E501

Returns a JSON object containing information about existing tenant converters and converters available in library.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.get_integrations_converters_info()
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'get_integrations_converters_info'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def save_integration(body_json: str = None) -> str:
    """
    Create Or Update Integration (saveIntegration)  # noqa: E501

Create or update the Integration. When creating integration, platform generates Integration Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created integration id will be present in the response. Specify existing Integration id to update the integration. Referencing non-existing integration Id will cause 'Not Found' error. Integration configuration is validated for each type of the integration before it can be created.   # Integration Configuration  Integration configuration (**'configuration'** field) is the JSON object representing the special configuration per integration type with the connectivity fields and other important parameters dependent on the specific integration type. Let's review the configuration object for the MQTT Integration type below.   ```json {    "clientConfiguration":{       "host":"broker.hivemq.com",       "port":1883,       "cleanSession":false,       "ssl":false,       "connectTimeoutSec":10,       "clientId":"",       "maxBytesInMessage":32368,       "credentials":{          "type":"anonymous"       }    },    "downlinkTopicPattern":"${topic}",    "topicFilters":[       {          "filter":"tb/mqtt-integration-tutorial/sensors/+/temperature",          "qos":0       }    ],    "metadata":{    } } ```  Remove 'id', 'tenantId' from the request body example (below) to create new Integration entity.   Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.save_integration(body=deserialize_param(body_json, 'Integration'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'save_integration'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def unassign_integration_from_edge(edge_id_json: str, integration_id_json: str) -> str:
    """
    Unassign integration from edge (unassignIntegrationFromEdge)  # noqa: E501

Clears assignment of the integration to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove integration (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove integration locally.  Available for users with 'TENANT_ADMIN' authority.  # noqa: E501
    """
    try:
        client = get_client()
        result = client.unassign_integration_from_edge(edge_id=deserialize_param(edge_id_json, 'EdgeId'), integration_id=deserialize_param(integration_id_json, 'IntegrationId'))
        return format_response(result)
    except ApiException as e:
        if e.status == 403:
            return "PERMISSION DENIED: You do not have permission to perform 'unassign_integration_from_edge'."
        if e.status == 401:
            return "AUTH ERROR: Credentials invalid or session expired. Check TB_USERNAME/TB_PASSWORD."
        return f"API Error {e.status}: {e.reason}\n{e.body}"
    except Exception as e:
        return f"Error: {str(e)}"


def register(mcp):
    mcp.tool()( assign_integration_to_edge )
    mcp.tool()( check_integration_connection )
    mcp.tool()( delete_integration )
    mcp.tool()( find_all_related_edges_missing_attributes )
    mcp.tool()( find_edge_missing_attributes_get )
    mcp.tool()( get_edge_integration_infos )
    mcp.tool()( get_edge_integrations )
    mcp.tool()( get_integration_by_id )
    mcp.tool()( get_integration_by_routing_key )
    mcp.tool()( get_integration_infos )
    mcp.tool()( get_integrations )
    mcp.tool()( get_integrations_by_ids )
    mcp.tool()( get_integrations_converters_info )
    mcp.tool()( save_integration )
    mcp.tool()( unassign_integration_from_edge )
