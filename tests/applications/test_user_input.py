import pytest

from app.applications.inbound_dto.user_input import UserInput


class TestUserInput:
    @pytest.mark.parametrize(
        ("input", "expected"),
        [
            (
                {
                    "name": "test-123_USER",
                    "password1": "abcdefg",
                    "password2": "abcdefg",
                    "email": "sample@example.com",
                },
                {
                    "name": "test-123_USER",
                    "password1": "abcdefg",
                    "password2": "abcdefg",
                    "email": "sample@example.com",
                },
            ),
            (
                {
                    "name": "aa",
                    "password1": "abcdefg123456",
                    "password2": "abcdefg123456",
                    "email": "sample@mb.example.com",
                },
                {
                    "name": "aa",
                    "password1": "abcdefg123456",
                    "password2": "abcdefg123456",
                    "email": "sample@mb.example.com",
                },
            ),
            (
                {
                    "name": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "password1": "abcdefg123456",
                    "password2": "abcdefg123456",
                    "email": "sample@mb.example.com",
                },
                {
                    "name": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "password1": "abcdefg123456",
                    "password2": "abcdefg123456",
                    "email": "sample@mb.example.com",
                },
            ),
        ],
    )
    def test_user_input(self, input, expected):
        u = UserInput(
            name=input["name"],
            password1=input["password1"],
            password2=input["password2"],
            email=input["email"],
        )

        assert u.name == expected["name"]
        assert u.get_raw_password() == expected["password1"]
        assert u.get_raw_password() == expected["password2"]
        assert u.email == expected["email"]

    def test_invalid_params(self):
        with pytest.raises(
            ValueError,
            match=r"UserInput\nname\n  ensure this value has at most 50 characters",
        ):
            UserInput(
                name="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                password1="abcdefg",
                password2="abcdefg",
                email="sample@mb.example.com",
            )

        with pytest.raises(
            ValueError,
            match=r"UserInput\nname\n  ensure this value has at least 2 characters",
        ):
            UserInput(
                name="a",
                password1="abcdefg",
                password2="abcdefg",
                email="sample@mb.example.com",
            )

        with pytest.raises(
            ValueError,
            match="invalid name",
        ):
            UserInput(
                name="!!!",
                password1="abcdefg",
                password2="abcdefg",
                email="sample@mb.example.com",
            )

        with pytest.raises(
            ValueError,
            match=r"UserInput\npassword1\n  ensure this value has at least 6 characters",
        ):
            UserInput(
                name="abc",
                password1="abcde",
                password2="abcde",
                email="sample@mb.example.com",
            )

        with pytest.raises(
            ValueError,
            match="passwords do not match",
        ):
            UserInput(
                name="abc",
                password1="abcdefg",
                password2="abcdefgh",
                email="sample@mb.example.com",
            )

        with pytest.raises(
            ValueError,
            match=r"UserInput\nemail\n  value is not a valid email address",
        ):
            UserInput(
                name="abc",
                password1="abcdefg",
                password2="abcdefg",
                email="invalid_email",
            )
