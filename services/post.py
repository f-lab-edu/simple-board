from datetime import datetime
from typing import List

import uuid
from schemas.post import Post, PostCreateInput

init_posted_data = Post(id=str(uuid.uuid4()), title="안녕하세요~", content="반갑습니다", author="admin", created_at=datetime.now())
POST_DB: dict[str, Post] = {init_posted_data.id: init_posted_data}

def get_post_list() -> List[Post]:
    return list(POST_DB.values())

def get_post_detail(post_id: str) -> Post:
    return POST_DB[post_id]

def insert_post(post: PostCreateInput) -> bool:
    try:
        new_post: Post = PostCreateInput(title=post.title, content=post.content, author=post.author)
        POST_DB[new_post.id] = new_post 
    except:
        return False
    return True