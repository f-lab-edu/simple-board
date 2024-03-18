from datetime import datetime

from pydantic import BaseModel, Field
from sqlmodel import Field, SQLModel


class Post(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    content: str | None
    author: str
    created_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime | None = None


class PostCreateInput(BaseModel):
    title: str
    content: str
    author: str


class PostUpdateInput(BaseModel):
    title: str | None = None
    content: str | None = None
    author: str
    modified_at: datetime = Field(default_factory=datetime.now)


class PostDelInput(BaseModel):
    author: str
