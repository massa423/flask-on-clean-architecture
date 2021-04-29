import os
from logging import INFO


from myapp.config.environment.default import DefaultConfig


class ProductionConfig(DefaultConfig):
    """
    Production config
    """

    # database
    DATABASE_USER = os.getenv("DATABASE_USER", None)
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", None)
    DATABASE_HOST = os.getenv("DATABASE_HOST", None)
    DATABASE_PORT = os.getenv("DATABASE_PORT", None)
    DATABASE_NAME = os.getenv("DATABASE_NAME", None)
    DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"  # noqa

    SECRET_KEY = os.getenv("SECRET_KEY", None)
    LOG_LEVEL = INFO
