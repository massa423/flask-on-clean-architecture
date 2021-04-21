import os
from logging import DEBUG

from myapp.config.environment.default import *  # noqa

# database
DATABASE_USER = os.getenv("DATABASE_USER", None)
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", None)
DATABASE_HOST = os.getenv("DATABASE_HOST", None)
DATABASE_PORT = os.getenv("DATABASE_PORT", None)
DATABASE_NAME = os.getenv("DATABASE_NAME", None)
DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"  # noqa

SECRET_KEY = b".\xa3\x1b5\x11\x9c$d\x02zS\x87\x9a;\x94\x03"
LOG_LEVEL = DEBUG
