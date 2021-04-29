from myapp.interfaces.gateways.user_repository import UserRepositoryImpl, UserRepository
from myapp.domains.user import User
import pytest


def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get("/")
    assert b"This is a top page" in rv.data


def test_repository(client):
    obj = UserRepositoryImpl()
    u = User(
        name="hoge",
        password="password",
        email="unko@example.com",
    )
    response = obj.create_user(u)

    assert u.name == response.name
    assert u.password == response.password
    assert u.email == response.email

    response = obj.find_user_by_name(u)

    assert u.name == response.name
    assert u.password == response.password
    assert u.email == response.email


def test_repository_interface(client):
    with pytest.raises(TypeError):
        UserRepository()
