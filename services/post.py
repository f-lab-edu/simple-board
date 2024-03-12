from datetime import datetime

import uuid
from schemas.post import Post, PostCreateInput

init_posted_data = PostCreateInput(title="안녕하세요~", content="반갑습니다", author="admin")
POST_DB: dict[str, Post] = {init_posted_data.id: init_posted_data}

def get_post_list() -> list[Post]:
    return list(POST_DB.values())

def get_post_detail(post_id: str) -> Post:
    if post_id in POST_DB:
        return POST_DB[post_id]
    return None

def insert_post(post: PostCreateInput) -> Post:
    try:
        new_post: Post = PostCreateInput(title=post.title, content=post.content, author=post.author)
        POST_DB[new_post.id] = new_post
        return POST_DB[new_post.id]
    except:
        return None