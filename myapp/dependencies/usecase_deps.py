from injector import Module
from myapp.applications.user_create_usecase import (
    UserCreateUsecase,
    UserCreateUsecaseImpl,
)
from myapp.applications.user_get_usecase import UserGetUsecase, UserGetUsecaseImpl


class UsecaseDIModule(Module):
    def configure(self, binder):
        binder.bind(UserCreateUsecase, to=UserCreateUsecaseImpl)
        binder.bind(UserGetUsecase, to=UserGetUsecaseImpl)
