from pydantic import BaseModel

class PostDto(BaseModel):
    id: str
    title: str
    content: str
    createdAt: str
    updatedAt: str | None
    author: str
    
class UpdatePostDto(BaseModel):
    title: str
    content: str
    
class CreatePostDto(BaseModel):
    title: str
    content: str
    author: str
    
def dictToPostDto(obj: dict) -> PostDto:
    if 'updatedAt' not in obj:
        obj['updatedAt'] = None
    return PostDto(id=obj['id'], title=obj['title'], content=obj['content'], createdAt=obj['createdAt'], updatedAt=obj['updatedAt'], author=obj['author'])

def dictToCreatePostDto(obj: dict) -> CreatePostDto:
    return CreatePostDto(title=obj['title'], content=obj['content'], author=obj['author'])

def dictToUpdatePostDto(obj: dict) -> UpdatePostDto:
    return UpdatePostDto(title=obj['title'], content=obj['content'])