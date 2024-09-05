from typing import Union
from fastapi import FastAPI
from post.dto import PostDto
from post.api import get_all_post, get_post_by_id

app = FastAPI()

@app.get('/post/{id}')
def read_post_by_id(id: str) -> PostDto:
    try:
        return get_post_by_id(id)
    except Exception as e:
        return {'error': str(e)}

@app.get('/post')
def read_all_post() -> list[PostDto]:
    try:
        return get_all_post()
    except Exception as e:
        return {'error': str(e)}