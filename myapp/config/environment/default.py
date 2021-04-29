from pydantic import BaseSettings


class DefaultConfig(BaseSettings):
    """
    Default config class
    """

    APP_VERSION = "0.1.0"

    # database
    SQL_ALCHEMY_ECHO = False
