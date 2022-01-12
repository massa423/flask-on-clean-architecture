from datetime import datetime

import pytest
from app.domains.user import User


class TestUser:
    @pytest.mark.freeze_time(datetime(2022, 1, 1, 23, 59, 59))
    @pytest.mark.parametrize(
        ("input", "expected"),
        [
            (
                {
                    "name": "test-user",
                    "password": "password",
                    "email": "test-user@example.com",
                },
                {
                    "name": "test-user",
                    "password": "password",
                    "email": "test-user@example.com",
                },
            ),
        ],
    )
    def test_user(self, input, expected):
        now = datetime.now()

        user = User(
            name=input["name"], password=input["password"], email=input["email"], created_at=now, updated_at=now
        )

        assert user.name == expected["name"]
        assert user.password != expected["password"]
        assert user.get_raw_password() == expected["password"]
        assert user.email == expected["email"]
        assert user.created_at == now
        assert user.updated_at == now
