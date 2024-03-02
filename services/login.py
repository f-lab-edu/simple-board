from datetime import datetime, timedelta
from fastapi import HTTPException, status
import jwt

from constants.variables import TokenConfig
from schemas.login import LoginData, User, Token

user_db: dict[str: User] = {"firstUser": {"id":"firstUser", "user_name":"뉴비", "password":"1234"}}

def authenicate_user(login_data: LoginData) -> User:
    if login_data.id in user_db and user_db[login_data.id]["password"] == login_data.password:
        return user_db[login_data.id]
    return None

def generate_token(login_data: LoginData) -> Token:
    user_data: dict = authenicate_user(login_data)
    if not user_data:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid User")
    expire_time: datetime = datetime.utcnow() + timedelta(minutes=TokenConfig.TOKEN_EXPIRE_MINUTES)
    user_data["exp"] = expire_time
    token: dict = jwt.encode(user_data, TokenConfig.SECRET_KEY, TokenConfig.ALGORITHM)
    return Token(access_token=token, token_type="bearer")


