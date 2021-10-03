from typing import Optional
from sqlmodel import Field, SQLModel
from pydantic import HttpUrl, EmailStr


class Profile(SQLModel, table=True):
    sub: str = Field(primary_key=True)
    nickname: str
    email: EmailStr
    display_name: Optional[str]
    picture: Optional[HttpUrl]
