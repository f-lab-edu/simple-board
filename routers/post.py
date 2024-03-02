from fastapi import APIRouter
from typing import List

from schemas.post import Post
import services.post as post_service


router = APIRouter()

@router.get("/", response_model=List[Post])
async def get_post_list_api():
    return post_service.get_post_list()

