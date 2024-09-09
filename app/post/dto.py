from typing import Optional
from pydantic import BaseModel


class CreatePostRequestDto(BaseModel):
    title: str
    content: str

class CreatePostDto(CreatePostRequestDto):
    pass

class UpdatePostRequestDto(BaseModel):
    title: Optional[str]
    content: Optional[str]

class UpdatePostDto(UpdatePostRequestDto):
    id: str    

class PostQueryDto(BaseModel):
    title: Optional[str]
    author: Optional[str]

class PostResponseDto(BaseModel):
    id: str
    title: str
    content: str
    author: str
    createdAt: str
    updatedAt: str

