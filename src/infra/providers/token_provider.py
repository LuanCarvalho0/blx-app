from datetime import datetime, timedelta
from jose import jwt

# CONFIG
SECRET_KEY = 'dd960d42bb47da21af3b3b0c31684540'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3000

def criar_access_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    dados.update({'exp': expiracao})

    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt

def verificar_access_token(token: str):
    carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return carga.get('sub')


