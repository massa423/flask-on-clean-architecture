from abc import ABCMeta, abstractmethod

from injector import inject
from app.applications.inbound_dto.user_input import UserInput
from app.applications.outbound_dto.user_output import UserOutput
from app.domains.user import User
from app.interfaces.gateways.user_repository import UserRepository


class UserCreateUsecase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, input: UserInput) -> UserOutput:
        pass


class UserCreateUsecaseImpl(UserCreateUsecase):
    @inject
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def handle(self, input: UserInput) -> UserOutput:
        data = User(name=input.name, password=input.password1, email=input.email)

        return UserOutput(**self.user_repository.create_user(data).dict())
