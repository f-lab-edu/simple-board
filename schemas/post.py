from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    id: str
    title: str
    content: Optional[str] = None
    author: str
    created_at: datetime

class PostCreateInput(BaseModel):
    title: str
    content: str
    author: str