import os

import pytest
from app.config import config
from app.interfaces.gateways.database.db import db_session, init_db, engine
from app.main import app
from sqlalchemy import text


@pytest.fixture(scope="function")
def client_with_testdata():
    app.config["TESTING"] = True

    with app.test_client() as client:
        init_db()

        file = open("./tests/api/v1/sample_data.sql", mode="r", encoding="utf-8")
        engine.execute(text(file.read()))

        yield client

    db_session.remove()
    os.unlink(config().DATABASE_URL.replace("sqlite:///", ""))
