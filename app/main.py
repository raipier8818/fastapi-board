from contextlib import asynccontextmanager
from fastapi import FastAPI
from mongodb import mongodb
import router.post as post

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server started")
    mongodb.connect()
    yield

    mongodb.close()
    print("Server stopped")

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)

@app.get("/")
def ok() -> str:
    return "OK"