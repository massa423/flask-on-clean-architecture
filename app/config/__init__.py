import os
from typing import Any, Optional

from app.exceptions import EnvironmentError

DEVELOPMENT = "development"
STAGING = "staging"
PRODUCTION = "production"
TEST = "test"


def config(env: Optional[str] = os.getenv("APP_ENV", DEVELOPMENT)) -> Any:

    config: Any

    if env == DEVELOPMENT:
        from app.config.environment.development import DevelopmentConfig

        config = DevelopmentConfig()
    elif env == STAGING:
        from app.config.environment.staging import StagingConfig

        config = StagingConfig()
    elif env == PRODUCTION:
        from app.config.environment.production import ProductionConfig

        config = ProductionConfig()
    elif env == TEST:
        from app.config.environment.test import TestConfig

        config = TestConfig()
    else:
        raise EnvironmentError

    return config
