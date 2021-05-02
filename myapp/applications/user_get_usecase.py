from abc import ABCMeta, abstractmethod

from myapp.applications.outbound_dto.user_output import UserOutput
from myapp.domains.user import User
from myapp.injectors import user_repository_injector


class UserGetUsecase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, name: str) -> UserOutput:
        pass


class UserGetUsecaseImpl(UserGetUsecase):
    def __init__(self) -> None:
        # inject
        self.user_repository = user_repository_injector()

    def handle(self, name: str) -> UserOutput:
        data = User(name=name)

        return UserOutput(**self.user_repository.find_user_by_name(data).dict())
