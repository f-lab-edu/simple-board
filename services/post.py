from datetime import datetime
from typing import List

import uuid

from schemas.post import Post, PostCreateInput

POST_DB: dict[str: Post] = {"1": Post(id="1", title="안녕하세요~", content="반갑습니다", author="admin", created_at=datetime.now())}

def get_post_list() -> List[Post]:
    return list(POST_DB.values())

def get_post_detail(post_id: str) -> Post:
    return POST_DB[post_id]

def insert_post(post: PostCreateInput) -> bool:
    try:
        post_id: str = str(uuid.uuid4())
        POST_DB[post_id] = Post(id=post_id, title=post.title, content=post.content, author=post.author, created_at=datetime.now())
    except:
        return False
    return True