from datetime import datetime, timedelta
from jose import jwt

# CONFIG
SECRET_KEY = 'dd960d42bb47da21af3b3b0c31684540'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3000

def criar_access_token(data: dict):
    return 'token23423423'

def verificar_access_token(token: str):
    return '(19) 99999-9999'


