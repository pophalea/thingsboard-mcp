import os
import json
from typing import Any, Optional

try:
    if "PE" == "PE":
        from tb_rest_client.rest_client_pe import RestClientPE as RestClient
        import tb_rest_client.models.models_pe as models_pe
        import tb_rest_client.models.models_ce as models_ce
        
        def get_model_class(name):
            if hasattr(models_pe, name): return getattr(models_pe, name)
            if hasattr(models_ce, name): return getattr(models_ce, name)
            return None
    else:
        from tb_rest_client.rest_client_ce import RestClientCE as RestClient
        import tb_rest_client.models.models_ce as models_ce
        
        def get_model_class(name):
            if hasattr(models_ce, name): return getattr(models_ce, name)
            return None

    from tb_rest_client.rest import ApiException
except ImportError:
    pass

TB_URL = os.getenv("TB_URL", "http://localhost:8080")
TB_USERNAME = os.getenv("TB_USERNAME", "tenant@thingsboard.org")
TB_PASSWORD = os.getenv("TB_PASSWORD", "tenant")

_client = None

def get_client():
    global _client
    if not _client:
        _client = RestClient(base_url=TB_URL)
        _client.login(username=TB_USERNAME, password=TB_PASSWORD)
    return _client

def deserialize_param(value: str, model_name: str):
    if not value: return None
    try:
        data = json.loads(value)
        clazz = get_model_class(model_name)
        if clazz: return clazz(**data)
        return data
    except: return value

def format_response(resp: Any) -> str:
    if hasattr(resp, 'to_dict'):
        return json.dumps(resp.to_dict(), indent=2, default=str)
    if isinstance(resp, list):
        return json.dumps([x.to_dict() if hasattr(x, 'to_dict') else x for x in resp], indent=2, default=str)
    return str(resp)
