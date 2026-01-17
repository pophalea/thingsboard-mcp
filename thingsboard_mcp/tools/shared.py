
import os, json, time
from typing import Any

TB_URL = os.getenv("TB_URL", "http://localhost:8080")
TB_USERNAME = os.getenv("TB_USERNAME", "tenant@thingsboard.org")
TB_PASSWORD = os.getenv("TB_PASSWORD", "tenant")
EDITION = os.getenv("TB_EDITION", "PE")

try:
    if EDITION == "PE":
        from tb_rest_client.rest_client_pe import RestClientPE as RestClient
        import tb_rest_client.models.models_pe as models
    else:
        from tb_rest_client.rest_client_ce import RestClientCE as RestClient
        import tb_rest_client.models.models_ce as models
    from tb_rest_client.rest import ApiException
except ImportError:
    pass

_client = None
_last_login = 0

def get_client():
    global _client, _last_login
    if _client is None:
        print(f"Logging in to {TB_URL} as {TB_USERNAME} ({EDITION})...")
        _client = RestClient(base_url=TB_URL)
        _client.login(username=TB_USERNAME, password=TB_PASSWORD)
        _last_login = time.time()
    
    if time.time() - _last_login > 7200:
         try:
             _client.login(username=TB_USERNAME, password=TB_PASSWORD)
             _last_login = time.time()
         except: pass

    return _client

def deserialize_param(value: str, model_name: str):
    if not value: return None
    try:
        data = json.loads(value)
        if hasattr(models, model_name):
            clazz = getattr(models, model_name)
            # Some models expect kwargs, some might be enums
            # We assume it's a Pydantic-like or Dictionary model
            return clazz(**data)
        return data
    except: return value

def format_response(resp: Any) -> str:
    if hasattr(resp, 'to_dict'): return json.dumps(resp.to_dict(), indent=2, default=str)
    if isinstance(resp, list): return json.dumps([x.to_dict() if hasattr(x, 'to_dict') else x for x in resp], indent=2, default=str)
    return str(resp)
