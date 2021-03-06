from abc import ABCMeta, abstractmethod
from datetime import datetime
from logging import getLogger

from app.domains.user import User as UserDomain
from app.exceptions import DuplicateException
from app.interfaces.gateways.database.db import db_session
from app.interfaces.gateways.database.schema import User
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
            password=user.get_raw_password(),
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
