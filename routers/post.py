from fastapi import APIRouter
from typing import List

from schemas.post import Post
import services.post as post_service


router = APIRouter()

@router.get("/posts/{post_id}", response_model=Post)
async def get_post_detail_api(post_id: str):
    return post_service.get_post_detail(post_id)

