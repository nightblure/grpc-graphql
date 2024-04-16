from dataclasses import dataclass, asdict, field
from datetime import datetime

from pydantic import BaseModel, Field


@dataclass
class PostRead:
    user_id: int
    text: str

    def to_dict(self):
        return asdict(self)


@dataclass
class PostCreate(PostRead):
    pass


@dataclass
class UserCreate:
    username: str
    email: str
    phone_number: str
    birth_date: datetime
    posts: list[PostRead] = field(default_factory=lambda: [])

    def to_dict(self):
        return asdict(self)


class UserRead(BaseModel):
    id: int
    username: str
    email: str
    phone_number: str
    birth_date: datetime
    posts: list[PostRead]


class UserReadGrpc(BaseModel):
    username: str
    email: str
    phone_number: str = Field(alias='phoneNumber')
    birth_date: int = Field(alias='birthDate')


class UsersResponse(BaseModel):
    items: list[UserReadGrpc]
