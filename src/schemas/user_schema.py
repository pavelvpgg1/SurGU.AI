from pydantic import BaseModel


class UserBase(BaseModel):
    id: str
    name: str
    is_man: bool
    age: int


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    name: str
    is_man: bool
    age: int


class UserResponse(UserBase):
    pass


class UserListResponse(BaseModel):
    id: int | None = None
    name: str | None = None
