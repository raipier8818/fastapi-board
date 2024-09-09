from pydantic import BaseModel


class CreateUserRequestDto(BaseModel):
    name: str
    email: str
    
class UpdateUserRequestDto(BaseModel):
    name: str
    email: str