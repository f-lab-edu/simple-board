from common.db_info import engine
from schemas.post import Post, PostCreateInput, PostDelInput, PostUpdateInput
from sqlmodel import Session, insert, select

# init_posted_data = PostCreateInput(
#     title="안녕하세요~", content="반갑습니다", author="admin"
# )
# POST_DB: dict[str, Post] = {init_posted_data.id: init_posted_data}


def get_post_list(db_session: Session) -> list[Post]:
    statement = select(Post)
    return db_session.exec(statement)


def get_post_detail(post_id: int, db_session: Session) -> Post:
    statement = select(Post).where(Post.id == post_id)
    return db_session.exec(statement).one()


def insert_post(post: PostCreateInput, db_session: Session) -> Post:
    try:
        new_post: Post = Post(
            title=post.title, content=post.content, author=post.author
        )
        db_session.add(new_post)
        db_session.commit()
        return new_post
    except:
        return None


def is_valid_author(post_id: int, author: str, db_session: Session) -> bool:
    statement = select(Post).where(Post.id == post_id)
    if selected_data := db_session.exec(statement).one():
        if selected_data.author == author:
            return True
    return False


# 선행조건: 동일한 author인 것이 확인되어 있는 상태 == 조회한 데이터가 null이 아님
def update_post(post_id: int, post: PostUpdateInput, db_session: Session) -> Post:
    statement = select(Post).where(Post.id == post_id)
    cur_post = db_session.exec(statement).one()
    for key, value in post.model_dump().items():
        if value is not None:
            setattr(cur_post, key, value)
    db_session.add(cur_post)
    db_session.commit()
    return cur_post


# 선행조건: 동일한 author인 것이 확인되어 있는 상태 == 조회한 데이터가 null이 아님
def del_post(post_id: str, post: PostDelInput, db_session: Session) -> bool:
    statement = select(Post).where(Post.id == post_id)
    cur_post = db_session.exec(statement).one()
    db_session.delete(cur_post)
    db_session.commit()
    return True
