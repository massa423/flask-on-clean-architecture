import os
from logging import INFO

from myapp.config.environment.default import *  # noqa

# database
DATABASE_URL = ""

SECRET_KEY = os.getenv("SECRET_KEY", None)
LOG_LEVEL = INFO
