from myapp.applications.create_user_usecase import (
    CreateUserUsecase,
    CreateUserUsecaseImpl,
)


def create_user_usecase_injector() -> CreateUserUsecase:
    return CreateUserUsecaseImpl()
