from fastapi import APIRouter
from typing import List

from schemas.post import Post, PostCreateInput
from services.post import get_post_list


router = APIRouter()

@router.get("/", response_model=List[Post])
async def get_post_list_api():
    return get_post_list()

