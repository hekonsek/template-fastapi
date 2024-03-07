import os
import secrets

from fastapi import HTTPException, status, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()
token = os.getenv('TOKEN', secrets.token_urlsafe(10)[:10])
print(token)

def get_current_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    if credentials:
        if  credentials.credentials == token:
            return credentials.credentials
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication credentials"
    )