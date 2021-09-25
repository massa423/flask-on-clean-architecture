import os

import pytest
from app.config import config
from app.interfaces.gateways.database.db import db_session, init_db
from app.main import app


@pytest.fixture(scope="function")
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        init_db()
        yield client

    db_session.remove()
    os.unlink(config().DATABASE_URL.replace("sqlite:///", ""))
