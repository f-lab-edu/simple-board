from fastapi import FastAPI
from routers.login import router as login_router

app = FastAPI()

app.include_router(login_router)