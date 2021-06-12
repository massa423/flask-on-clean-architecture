from app.applications.user_create_usecase import (
    UserCreateUsecase,
    UserCreateUsecaseImpl,
)
from app.applications.user_get_usecase import UserGetUsecase, UserGetUsecaseImpl
from injector import Binder, Module


class UsecaseDIModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(UserCreateUsecase, to=UserCreateUsecaseImpl)
        binder.bind(UserGetUsecase, to=UserGetUsecaseImpl)
