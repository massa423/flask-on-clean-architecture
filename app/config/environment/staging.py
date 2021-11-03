import os
from logging import DEBUG
from typing import Optional

from app.config.environment.default import DefaultConfig


class StagingConfig(DefaultConfig):
    """
    Staging config
    """

    # database
    DATABASE_USER: Optional[str] = os.getenv("DATABASE_USER", None)
    DATABASE_PASSWORD: Optional[str] = os.getenv("DATABASE_PASSWORD", None)
    DATABASE_HOST: Optional[str] = os.getenv("DATABASE_HOST", None)
    DATABASE_PORT: Optional[str] = os.getenv("DATABASE_PORT", "5432")
    DATABASE_NAME: Optional[str] = os.getenv("DATABASE_NAME", None)
    DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"  # noqa

    SECRET_KEY = b".\xa3\x1b5\x11\x9c$d\x02zS\x87\x9a;\x94\x03"
    LOG_LEVEL = DEBUG

    SWAGGER_HOST = os.getenv("SWAGGER_HOST", None)
