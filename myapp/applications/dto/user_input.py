import re

from pydantic import BaseModel, EmailStr, Field, SecretStr, validator


class UserInput(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    password1: SecretStr = Field(..., min_length=6)
    password2: SecretStr = Field(..., min_length=6)
    email: EmailStr = Field(...)

    @validator("name", allow_reuse=True)
    def check_name(cls, v):
        if not re.match(r"^[a-zA-Z0-9-_]+$", v):
            raise ValueError("invalid name")
        return v

    @validator("password2", allow_reuse=True)
    def passwords_match(cls, v, values, **kwargs):
        if "password1" in values and v != values["password1"]:
            raise ValueError("passwords do not match")
        return v
