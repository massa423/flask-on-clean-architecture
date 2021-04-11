from myapp.config.environment.default import *  # noqa
import os
from logging import INFO

# database
DATABASE_URL = ""

SECRET_KEY = os.getenv("SECRET_KEY", None)
LOG_LEVEL = INFO
