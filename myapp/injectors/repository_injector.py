from myapp.interfaces.gateways.user_repository import UserRepository, UserRepositoryImpl


def user_repository_injector() -> UserRepository:
    return UserRepositoryImpl()
