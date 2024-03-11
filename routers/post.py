
from fastapi import APIRouter, Body, status, HTTPException
from typing import List

from schemas.post import Post, PostCreateInput
import services.post as post_service


router = APIRouter()

@router.get("/", response_model=List[Post], status_code=status.HTTP_200_OK)
async def get_post_list_api():
    return  post_service.get_post_list()


@router.get("/posts/{post_id}", response_model=Post, status_code=status.HTTP_200_OK)
async def get_post_detail_api(post_id: str):
    try:
        return post_service.get_post_detail(post_id)
    except KeyError:
        raise HTTPException(status_code=404,detail="Not Found")


@router.post("/posts/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def insert_post_api(post: PostCreateInput = Body(...)):
    if post_service.insert_post(post):
        return {"message": "게시글을 작성했습니다."}
    raise HTTPException(status_code=400,detail="Bad Request")
