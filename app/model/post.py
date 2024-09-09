from typing import Optional
from pydantic import BaseModel


class CreatePostRequestDto(BaseModel):
    title: str
    content: str
    
class UpdatePostRequestDto(CreatePostRequestDto):
    pass

class UpdatePostDto(UpdatePostRequestDto):
    id: str   
    
class CreatePostDto(CreatePostRequestDto):
    author: str
    created_at: str

class PostResponseDto(CreatePostDto):
    id: str
    updated_at: Optional[str]