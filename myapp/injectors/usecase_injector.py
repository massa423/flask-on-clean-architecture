from myapp.applications.user_create_usecase import (
    UserCreateUsecase,
    UserCreateUsecaseImpl,
)
from myapp.applications.user_get_usecase import UserGetUsecase, UserGetUsecaseImpl


def user_create_usecase_injector() -> UserCreateUsecase:
    return UserCreateUsecaseImpl()


def user_get_usecase_injector() -> UserGetUsecase:
    return UserGetUsecaseImpl()
