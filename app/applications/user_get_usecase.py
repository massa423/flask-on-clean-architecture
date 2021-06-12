from abc import ABCMeta, abstractmethod

from injector import inject
from app.applications.outbound_dto.user_output import UserOutput
from app.domains.user import User
from app.interfaces.gateways.user_repository import UserRepository


class UserGetUsecase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, name: str) -> UserOutput:
        pass


class UserGetUsecaseImpl(UserGetUsecase):
    @inject
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def handle(self, name: str) -> UserOutput:
        data = User(name=name)

        return UserOutput(**self.user_repository.find_user_by_name(data).dict())
