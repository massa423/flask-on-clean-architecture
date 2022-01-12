import pytest
from app.applications.user_get_usecase import UserGetUsecaseImpl
from app.domains.user import User
from app.interfaces.gateways.user_repository import UserRepository


class UserRepositoryMock(UserRepository):
    def create_user(self, user: User) -> User:
        return user

    def find_user_by_name(self, user: User) -> User:
        return user


class TestUserCreate:
    @pytest.mark.parametrize(
        "name",
        ["test1"],
    )
    def test_user_get(self, name):
        uc = UserGetUsecaseImpl(UserRepositoryMock())

        res = uc.handle(name)

        assert res.name == name
