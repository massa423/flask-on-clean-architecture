from app.config import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    config.DATABASE_URL, convert_unicode=True, echo=config.SQL_ALCHEMY_ECHO
)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db() -> None:
    import app.interfaces.gateways.database.schema  # noqa

    Base.metadata.create_all(bind=engine)
