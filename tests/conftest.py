import os

import pytest
from myapp.config import config
from myapp.interfaces.gateways.database.db import init_db
from myapp.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        init_db()
        yield client

    os.unlink(config.DATABASE_URL.replace("sqlite:///", ""))
