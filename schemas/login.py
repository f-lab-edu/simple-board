from pydantic import BaseModel

class LoginData(BaseModel):
    id: str
    password: str
    
class User(BaseModel):
    id: str
    user_name: str

class Token(BaseModel):
    access_token: str
    token_type: str