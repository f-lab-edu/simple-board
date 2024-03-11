from datetime import datetime
from pydantic import BaseModel
from typing import Optional
import uuid

class Post(BaseModel):
    id: str
    title: str
    content: str | None
    author: str
    created_at: datetime

class PostCreateInput(Post):
    id: str = str(uuid.uuid4())
    title: str
    content: str
    author: str
    created_at: datetime = datetime.now()

