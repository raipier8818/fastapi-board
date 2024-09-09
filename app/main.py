from contextlib import asynccontextmanager
from typing import Any
from fastapi import FastAPI
from config import config
from mongodb import mongodb
import router.post as post

@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:
    print("Server started")
    mongodb.connect()
    yield

    mongodb.close()
    print("Server stopped")

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)

@app.get('/info')
def info():
    return config.__dict__

@app.get("/")
def ok() -> str:
    return "OK"