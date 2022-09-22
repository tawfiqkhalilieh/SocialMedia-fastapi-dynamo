from fastapi.security import APIKeyHeader
from app.config import settings
api_key_header = APIKeyHeader(name='X-API-Key', auto_error=True)
api_key = "tawfiq" # I should Update this to the User id soon
users_table = settings.table