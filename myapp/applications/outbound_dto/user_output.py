from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, SecretStr


class UserOutput(BaseModel):
    """
    User output DTO
    """

    name: str = Field(None)
    password1: SecretStr = Field(None)
    email: EmailStr = Field(None)
    created_at: datetime = Field(None)
    updated_at: datetime = Field(None)
