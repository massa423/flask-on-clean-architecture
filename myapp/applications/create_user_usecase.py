from abc import ABCMeta, abstractmethod
from typing import Dict

from myapp.applications.dto.user_input import UserInput
from myapp.domains.user import User
from myapp.injectors import user_repository_injector


class CreateUserUsecase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, input: UserInput) -> Dict:
        pass


class CreateUserUsecaseImpl(CreateUserUsecase):
    def __init__(self):
        self.user_repository = user_repository_injector()

    def handle(self, input: UserInput) -> Dict:
        data = User(name=input.name, password=input.password1, email=input.email)

        return self.user_repository.create_user(data).dict()
