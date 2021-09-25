import os
from logging import INFO
from typing import Optional

from app.config.environment.default import DefaultConfig


class ProductionConfig(DefaultConfig):
    """
    Production config
    """

    # database
    DATABASE_USER: Optional[str] = os.getenv("DATABASE_USER", None)
    DATABASE_PASSWORD: Optional[str] = os.getenv("DATABASE_PASSWORD", None)
    DATABASE_HOST: Optional[str] = os.getenv("DATABASE_HOST", None)
    DATABASE_PORT: Optional[str] = os.getenv("DATABASE_PORT", "5432")
    DATABASE_NAME: Optional[str] = os.getenv("DATABASE_NAME", None)
    DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"  # noqa

    SECRET_KEY: Optional[str] = os.getenv("SECRET_KEY", None)
    LOG_LEVEL = INFO
