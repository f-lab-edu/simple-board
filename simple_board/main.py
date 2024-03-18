from fastapi import FastAPI
from routers.post import router as post_router
from sqlmodel import SQLModel, create_engine

app = FastAPI()
app.include_router(post_router)

ENGINE = create_engine("sqlite:///C:/sqlite3/db/simpleboard.db")
SQLModel.metadata.create_all(ENGINE)
