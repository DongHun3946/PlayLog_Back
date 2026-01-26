from pydantic import BaseModel, ConfigDict, EmailStr

class UserBase(BaseModel):
    nick_name: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    is_deleted: bool


class UserResponse(UserBase):
    id: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)