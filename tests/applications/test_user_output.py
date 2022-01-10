import pytest

from app.applications.outbound_dto.user_output import UserOutput
from datetime import datetime


class TestUserOutput:
    @pytest.mark.freeze_time(datetime(2022, 1, 1, 23, 59, 59))
    @pytest.mark.parametrize(
        ("input", "expected"),
        [
            (
                {
                    "name": "test-user",
                    "email": "test-user@example.com",
                },
                {
                    "name": "test-user",
                    "email": "test-user@example.com",
                },
            ),
        ],
    )
    def test_user_output(self, input, expected):
        now = datetime.now()

        user_output = UserOutput(
            name=input["name"],
            email=input["email"],
            created_at=now,
            updated_at=now,
        )

        assert user_output.name == expected["name"]
        assert user_output.email == expected["email"]
        assert user_output.created_at == now
        assert user_output.updated_at == now
