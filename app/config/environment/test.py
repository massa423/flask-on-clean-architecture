from logging import DEBUG

from app.config.environment.default import DefaultConfig


class TestConfig(DefaultConfig):
    """
    Test config
    """

    # database
    DATABASE_URL = "sqlite:///test.sqlite3"
    SQL_ALCHEMY_ECHO = True

    SECRET_KEY = b".\xa3\x1b5\x11\x9c$d\x02zS\x87\x9a;\x94\x03"
    LOG_LEVEL = DEBUG

    SWAGGER_HOST = "127.0.0.1:5000"
