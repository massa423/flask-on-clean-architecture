from logging import DEBUG, INFO
import os
import pytest

from app.exceptions import EnvironmentError


class TestConfig:
    """
    Config Test
    """

    def test_default(self):

        from app.config import config

        config().APP_VERSION = '0.1.0'
        config().SQL_ALCHEMY_ECHO = False

    def test_staging(self, staging_config):

        from app.config import config

        env = os.getenv("APP_ENV")

        assert (
            config(env).DATABASE_URL
            == "postgresql://staging_user:staging_password@staging_host:15432/staging_database"
        )
        assert config(env).SECRET_KEY == b".\xa3\x1b5\x11\x9c$d\x02zS\x87\x9a;\x94\x03"
        assert config(env).LOG_LEVEL == DEBUG

    def test_production(self, production_config):

        from app.config import config

        env = os.getenv("APP_ENV")

        assert (
            config(env).DATABASE_URL
            == "postgresql://prod_user:prod_password@prod_host:15432/prod_database"
        )
        assert config(env).SECRET_KEY == "prod_secretkey"
        assert config(env).LOG_LEVEL == INFO

    def test_invalid_env(self):
        from app.config import config

        with pytest.raises(EnvironmentError):
            _ = config("hoge")
