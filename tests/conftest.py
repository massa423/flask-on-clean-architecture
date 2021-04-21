import os

import pytest

from myapp.config import config
from myapp.main import app
from myapp.interfaces.gateways.database.db import init_db


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        init_db()
        yield client

    os.unlink(config.DATABASE_URL.replace("sqlite:///", ""))
