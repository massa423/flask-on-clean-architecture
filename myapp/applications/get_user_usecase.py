from abc import ABCMeta, abstractmethod
from typing import Dict

from myapp.domains.user import User
from myapp.injectors.repository_injector import user_repository_injector


class GetUserUsecase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, name: str) -> Dict:
        pass


class GetUserUsecaseImpl(GetUserUsecase):
    def __init__(self):
        self.user_repository = user_repository_injector()

    def handle(self, name: str) -> Dict:
        data = User(name=name)

        return self.user_repository.find_user_by_name(data).dict()
