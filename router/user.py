from fastapi import APIRouter

from dto.user_dto import CreateUserRequestDto, UpdateUserResponseDto

router = APIRouter()

@router.get("/")
async def get_users():
    pass

@router.get("/{id}")
async def get_user(id: str):
    pass

@router.post("/")
async def create_user(create_user_request_dto: CreateUserRequestDto):
    pass

@router.put("/{id}")
async def update_user(id: str, update_user_request_dto: UpdateUserResponseDto):
    pass

@router.delete("/{id}")
async def delete_user(id: str):
    
    pass