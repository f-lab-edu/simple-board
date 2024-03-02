
class TokenConfig():
    SECRET_KEY: str = "salt_for_password"
    ALGORITHM: str = "HS256"
    TOKEN_EXPIRE_MINUTES: int = 30