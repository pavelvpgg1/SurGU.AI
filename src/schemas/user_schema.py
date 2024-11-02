from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    id: int


class UserListResponse(BaseModel):
    id: int | None = None
    name: str | None = None
