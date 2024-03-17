import services.post as post_service
from fastapi import APIRouter, Body, HTTPException, status
from schemas.post import Post, PostCreateInput

router = APIRouter()


@router.get("/", response_model=list[Post], status_code=status.HTTP_200_OK)
def get_post_list_api() -> list:
    return post_service.get_post_list()


@router.get("/posts/{post_id}", response_model=Post, status_code=status.HTTP_200_OK)
def get_post_detail_api(post_id: str) -> Post:
    if cur_post := post_service.get_post_detail(post_id):
        return cur_post
    raise HTTPException(status_code=404, detail="Not Found")


@router.post("/posts/", response_model=dict, status_code=status.HTTP_201_CREATED)
def insert_post_api(post: PostCreateInput) -> dict:
    if post_service.insert_post(post):
        return {"message": "게시글을 작성했습니다."}
    raise HTTPException(status_code=400, detail="Bad Request")
