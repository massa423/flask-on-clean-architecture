from app.interfaces.gateways.user_repository import UserRepository, UserRepositoryImpl
from injector import Binder, Module


class RepositoryDIModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(UserRepository, to=UserRepositoryImpl)
