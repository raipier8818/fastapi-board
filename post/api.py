from http.client import FORBIDDEN, INTERNAL_SERVER_ERROR, NOT_FOUND
import requests
from post.dto import PostDto, dictToPostDto


def get_post_by_id(id: str) -> PostDto:
    response = requests.get('http://localhost:3000/post/{}'.format(id))
    return dictToPostDto(response.json())

def get_all_post() -> list[PostDto]:
    try:
        response = requests.get('http://localhost:3000/post')
        if response.status_code == FORBIDDEN:
            raise Exception('Forbidden')
        if response.status_code == NOT_FOUND:
            raise Exception('Not Found')
        if response.status_code == INTERNAL_SERVER_ERROR:
            raise Exception('Database Internal Server Error')
            
        result = []
        for post in response.json():
            result.append(dictToPostDto(post))
        return result
    except Exception as e:
        raise Exception('Internal Server Error')