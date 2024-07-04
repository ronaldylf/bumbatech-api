from fastapi.security import APIKeyHeader
from fastapi import Security, HTTPException, status
from dotenv import load_dotenv
import os

load_dotenv('.env')
api_key_header = APIKeyHeader(name="access_token")
allowed_api_keys = eval(os.getenv('api_keys'))

def check_access_token(token: str = Security(api_key_header)):
    if (token in allowed_api_keys): return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Missing or invalid API key"
    )