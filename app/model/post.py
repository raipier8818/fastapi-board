from typing import Optional
from pydantic import BaseModel


class CreatePostRequestDto(BaseModel):
    title: str
    content: str
    
class UpdatePostRequestDto(CreatePostRequestDto):
    pass

class UpdatePostDto(UpdatePostRequestDto):
    _id: str 
    updatedAt: str
    
class CreatePostDto(CreatePostRequestDto):
    author: str
    createdAt: str

class PostResponseDto(CreatePostDto):
    id: str
    updatedAt: Optional[str]