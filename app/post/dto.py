from pydantic import BaseModel


class CreatePostRequestDto(BaseModel):
    title: str
    content: str

class UpdatePostRequestDto(CreatePostRequestDto):
    pass

class PostQueryDto(BaseModel):
    title: str
    author: str

class PostResponseDto(BaseModel):
    id: str
    title: str
    content: str
    author: str
    createdAt: str
    updatedAt: str
