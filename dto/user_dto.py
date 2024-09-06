from pydantic import BaseModel

class CreateUserRequestDto(BaseModel):
    name: str
    email: str
    
class UpdateUserResponseDto(BaseModel):
    name: str
    email: str

