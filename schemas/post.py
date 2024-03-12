from datetime import datetime
from pydantic import BaseModel, Field
import uuid

class Post(BaseModel):
    id: str
    title: str
    content: str | None
    author: str
    created_at: datetime

class PostCreateInput(Post):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    content: str
    author: str
    created_at: datetime = Field(default_factory=datetime.now)
    

