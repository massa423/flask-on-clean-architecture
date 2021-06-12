from injector import Module
from app.interfaces.gateways.user_repository import UserRepository, UserRepositoryImpl


class RepositoryDIModule(Module):
    def configure(self, binder):
        binder.bind(UserRepository, to=UserRepositoryImpl)
