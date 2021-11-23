import os
import pytest


@pytest.fixture(scope="function")
def staging_config():
    os.environ["APP_ENV"] = "staging"

    os.environ["DATABASE_USER"] = "staging_user"
    os.environ["DATABASE_PASSWORD"] = "staging_password"
    os.environ["DATABASE_HOST"] = "staging_host"
    os.environ["DATABASE_PORT"] = "15432"
    os.environ["DATABASE_NAME"] = "staging_database"
    os.environ["SWAGGER_HOST"] = "localhost"


@pytest.fixture(scope="function")
def production_config():
    os.environ["APP_ENV"] = "production"

    os.environ["DATABASE_USER"] = "prod_user"
    os.environ["DATABASE_PASSWORD"] = "prod_password"
    os.environ["DATABASE_HOST"] = "prod_host"
    os.environ["DATABASE_PORT"] = "15432"
    os.environ["DATABASE_NAME"] = "prod_database"
    os.environ["SECRET_KEY"] = "prod_secretkey"
    os.environ["SWAGGER_HOST"] = "localhost"
