
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt

from constants.variables import TokenConfig
from schemas.login import User, Token


oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="login")

def check_auth(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, TokenConfig.SECRET_KEY, algorithms=[TokenConfig.ALGORITHM])
        if "exp" not in payload or payload["exp"] - datetime.now().timestamp() < 0:
            raise Exception
        return User(id=payload["id"], user_name=payload["user_name"])
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token")