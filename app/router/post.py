from fastapi import APIRouter

from post.dto import CreatePostRequestDto, PostResponseDto, UpdatePostRequestDto


router = APIRouter(prefix="/post")

@router.get("/")
def get_posts() -> list[PostResponseDto]:
    pass

@router.get("/{id}")
def get_post(id: str) -> PostResponseDto:
    pass

@router.post("/")
def create_post(create_post_request_dto: CreatePostRequestDto) -> PostResponseDto:
    pass

@router.put("/{id}")
def update_post(update_post_request_dto: UpdatePostRequestDto) -> PostResponseDto:
    pass

@router.delete("/{id}")
def delete_post(id: str) -> None:
    pass