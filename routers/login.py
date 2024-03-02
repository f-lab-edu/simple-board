from fastapi import APIRouter, Body, Depends, HTTPException, status

from dependencies.auth import check_auth
from schemas.login import LoginData, Token, User
import services.login as login_service


router = APIRouter()

@router.post("/login/", response_model=Token, status_code=status.HTTP_200_OK)
async def login(login_data: LoginData= Body(...)):
    return login_service.generate_token(login_data)

@router.get("/users/me")
async def go_to_my_page(user: User = Depends(check_auth)):
    return user

