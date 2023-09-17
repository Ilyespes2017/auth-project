from enum import Enum

from pydantic import BaseModel, EmailStr


class Roles(Enum):
    user = "user"
    admin = "admin"


class UserSchema(BaseModel):
    email: EmailStr = "email@test.com"
    username: str = "username"
    password: str = "password"
    is_active: bool = True
    role: Roles = "user"

    class Config:
        orm_mode = True
