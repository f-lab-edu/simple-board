import services.post as post_service
from common.db_info import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.post import Post, PostCreateInput, PostDelInput, PostUpdateInput
from sqlmodel import Session

router = APIRouter()


@router.get("/", response_model=list[Post], status_code=status.HTTP_200_OK)
def get_post_list_api(db_session: Session = Depends(get_db)) -> list:
    return post_service.get_post_list(db_session)


@router.get("/posts/{post_id}", response_model=Post, status_code=status.HTTP_200_OK)
def get_post_detail_api(post_id: int, db_session: Session = Depends(get_db)) -> Post:
    if cur_post := post_service.get_post_detail(post_id, db_session):
        return cur_post
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="해당 리소스를 찾을 수 없습니다"
    )


@router.post("/posts/", response_model=dict, status_code=status.HTTP_201_CREATED)
def insert_post_api(
    post: PostCreateInput, db_session: Session = Depends(get_db)
) -> dict:
    if post_service.insert_post(post, db_session):
        return {"message": "게시글을 작성했습니다."}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="잘못된 요청입니다"
    )


@router.patch("/posts/{post_id}", response_model=Post, status_code=status.HTTP_200_OK)
def update_post_api(
    post_id: int, post: PostUpdateInput, db_session: Session = Depends(get_db)
) -> Post:
    if post_service.is_valid_author(post_id, post.author, db_session):
        if updated_post := post_service.update_post(post_id, post, db_session):
            return updated_post
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="잘못된 요청입니다"
        )
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="권한이 없습니다")


@router.delete("/posts/{post_id}", response_model=dict, status_code=status.HTTP_200_OK)
def update_post_api(
    post_id: int, post: PostDelInput, db_session: Session = Depends(get_db)
) -> dict:
    if post_service.is_valid_author(post_id, post.author, db_session):
        if post_service.del_post(post_id, post, db_session):
            return {"message": "게시글을 삭제했습니다."}
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="잘못된 요청입니다"
        )
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="권한이 없습니다")
