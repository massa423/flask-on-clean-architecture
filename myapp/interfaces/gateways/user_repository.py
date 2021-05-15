from abc import ABCMeta, abstractmethod
from datetime import datetime
from logging import getLogger

from myapp.domains.user import User as UserDomain
from myapp.exceptions import DuplicateException
from myapp.interfaces.gateways.database.db import db_session
from myapp.interfaces.gateways.database.schema import User
from sqlalchemy.exc import IntegrityError

logger = getLogger(__name__)


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_user(self, user: UserDomain) -> UserDomain:
        pass

    @abstractmethod
    def find_user_by_name(self, user: UserDomain) -> UserDomain:
        pass


class UserRepositoryImpl(UserRepository):
    def create_user(self, user: UserDomain) -> UserDomain:
        now = datetime.now()

        data = User(
            name=user.name,
            password=user.password.get_secret_value(),
            email=user.email,
            created_at=now,
            updated_at=now,
        )

        try:
            db_session.add(data)
            db_session.commit()
        except IntegrityError as e:
            logger.info(e)
            raise DuplicateException

        response = User.query.filter(User.name == user.name).first()
        logger.info(f"user create success: {response}")

        return UserDomain.from_orm(response)

    def find_user_by_name(self, user: UserDomain) -> UserDomain:
        response = User.query.filter(User.name == user.name).first()
        logger.info(f"get user data: {response}")

        return UserDomain.from_orm(response)
