from logging import DEBUG

from myapp.config.environment.default import *  # noqa

# database
DATABASE_URL = "sqlite:///test.sqlite3"
SQL_ALCHEMY_ECHO = True

SECRET_KEY = b".\xa3\x1b5\x11\x9c$d\x02zS\x87\x9a;\x94\x03"
LOG_LEVEL = DEBUG