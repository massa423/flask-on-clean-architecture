from abc import ABCMeta, abstractmethod
from typing import Any, Dict

from myapp.applications.dto.user_input import UserInput
from myapp.domains.user import User
from myapp.injectors import user_repository_injector


class UserCreateUsecase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, input: UserInput) -> Dict[str, Any]:
        pass


class UserCreateUsecaseImpl(UserCreateUsecase):
    def __init__(self) -> None:
        # inject
        self.user_repository = user_repository_injector()

    def handle(self, input: UserInput) -> Dict[str, Any]:
        data = User(name=input.name, password=input.password1, email=input.email)

        return self.user_repository.create_user(data).dict()
