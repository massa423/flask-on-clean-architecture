from myapp.applications.create_user_usecase import (
    CreateUserUsecase,
    CreateUserUsecaseImpl,
)
from myapp.applications.get_user_usecase import GetUserUsecase, GetUserUsecaseImpl


def create_user_usecase_injector() -> CreateUserUsecase:
    return CreateUserUsecaseImpl()


def get_user_usecase_injector() -> GetUserUsecase:
    return GetUserUsecaseImpl()
