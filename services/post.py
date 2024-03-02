from datetime import datetime
from typing import List

from schemas.post import Post

POST_DB: dict[str: Post] = {"test1": Post(id="test1", title="안녕하세요~", content="반갑습니다", author="admin", created_at=datetime.now())}

def get_post_list() -> List[Post]:
    return POST_DB.values()