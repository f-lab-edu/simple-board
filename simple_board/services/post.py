from schemas.post import Post, PostCreateInput, PostDelInput, PostUpdateInput

init_posted_data = PostCreateInput(
    title="안녕하세요~", content="반갑습니다", author="admin"
)
POST_DB: dict[str, Post] = {init_posted_data.id: init_posted_data}


def get_post_list() -> list[Post]:
    return list(POST_DB.values())


def get_post_detail(post_id: str) -> Post:
    if post_id in POST_DB:
        return POST_DB[post_id]
    return None


def insert_post(post: PostCreateInput) -> Post:
    try:
        new_post: Post = PostCreateInput(
            title=post.title, content=post.content, author=post.author
        )
        POST_DB[new_post.id] = new_post
        return POST_DB[new_post.id]
    except:
        return None


def is_valid_author(post_id: str, author: str) -> bool:
    if post_id in POST_DB and POST_DB[post_id].author == author:
        return True
    return False


def update_post(post_id: str, post: PostUpdateInput) -> Post:
    if post_id in POST_DB:
        for key, value in post.model_dump().items():
            if value is not None:
                setattr(POST_DB[post_id], key, value)
        return POST_DB[post_id]
    return None


def del_post(post_id: str, post: PostDelInput) -> bool:
    if post_id in POST_DB:
        del POST_DB[post_id]
        return True
    return None
