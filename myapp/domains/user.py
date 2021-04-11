from pydantic import BaseModel, EmailStr, Field, SecretStr
from datetime import datetime


class User(BaseModel):
    name: str = Field(None)
    password: SecretStr = Field(None)
    email: EmailStr = Field(None)
    created_at: datetime = Field(None)
    updated_at: datetime = Field(None)

    class Config:
        orm_mode = True
