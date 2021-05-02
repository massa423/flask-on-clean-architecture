from abc import ABCMeta, abstractmethod

from myapp.applications.inbound_dto.user_input import UserInput
from myapp.applications.outbound_dto.user_output import UserOutput
from myapp.domains.user import User
from myapp.injectors import user_repository_injector


class UserCreateUsecase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, input: UserInput) -> UserOutput:
        pass


class UserCreateUsecaseImpl(UserCreateUsecase):
    def __init__(self) -> None:
        # inject
        self.user_repository = user_repository_injector()

    def handle(self, input: UserInput) -> UserOutput:
        data = User(name=input.name, password=input.password1, email=input.email)

        return UserOutput(**self.user_repository.create_user(data).dict())
