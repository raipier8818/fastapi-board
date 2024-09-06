from typing import Union

from fastapi import FastAPI

from router import user

app = FastAPI()

app.include_router(user.router, prefix="/user")

@app.get("/")
def ok() -> str:
    return "OK"