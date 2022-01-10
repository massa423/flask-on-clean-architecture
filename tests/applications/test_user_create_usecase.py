import pytest
from app.applications.inbound_dto.user_input import UserInput
from app.applications.user_create_usecase import UserCreateUsecaseImpl
from app.domains.user import User
from app.interfaces.gateways.user_repository import UserRepository


class UserRepositoryMock(UserRepository):
    def create_user(self, user: User) -> User:
        return user

    def find_user_by_name(self, user: User) -> User:
        return user


class TestUserCreate:
    @pytest.mark.parametrize(
        "input",
        [
            UserInput(
                name="test1",
                password1="password",
                password2="password",
                email="sample@example.com",
            )
        ],
    )
    def test_user_create(self, input):
        uc = UserCreateUsecaseImpl(UserRepositoryMock())

        res = uc.handle(input)

        assert res.name == input.name
        assert res.email == input.email
