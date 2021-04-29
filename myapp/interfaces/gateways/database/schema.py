from datetime import datetime

from myapp.interfaces.gateways.database.db import Base
from sqlalchemy import Column, DateTime, Integer, String


class User(Base):
    __tablename__ = "users"
    no = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    email = Column(String(120), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __init__(
        self,
        name: str,
        password: str,
        email: str,
        created_at: datetime,
        updated_at: datetime,
    ):
        self.name = name
        self.password = password
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self) -> str:
        return f"<User name: {self.name}, password: *****, email: {self.email}, created_at: {self.created_at}, updated_at: {self.updated_at}>"  # noqa
