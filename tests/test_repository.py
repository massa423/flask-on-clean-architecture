import pytest
from myapp.domains.user import User
from myapp.exceptions import DuplicateException
from myapp.interfaces.gateways.user_repository import UserRepository, UserRepositoryImpl


class TestRepostory:
    """
    Repository Test
    """

    def test_repository(self, client):
        obj = UserRepositoryImpl()

        u = User(
            name="hoge",
            password="password",
            email="unko@example.com",
        )
        # user is nothing.
        response = obj.find_user_by_name(u)

        assert response.name is None
        assert response.password is None
        assert response.email is None

        # test data created.
        response = obj.create_user(u)

        assert u.name == response.name
        assert u.password == response.password
        assert u.email == response.email

        # test user exists.
        response = obj.find_user_by_name(u)

        assert u.name == response.name
        assert u.password == response.password
        assert u.email == response.email

        # regist same data.
        with pytest.raises(DuplicateException):
            obj.create_user(u)

    def test_repository_interface(self):
        with pytest.raises(TypeError):
            UserRepository()
