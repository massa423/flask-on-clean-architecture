import os

DEVELOPMENT = "development"
STAGING = "staging"
PRODUCTION = "production"
TEST = "test"


env = os.getenv("APP_ENV", DEVELOPMENT)

if env == DEVELOPMENT:
    from myapp.config.environment.development import *  # noqa
elif env == STAGING:
    from myapp.config.environment.staging import *  # noqa
elif env == PRODUCTION:
    from myapp.config.environment.production import *  # noqa
elif env == TEST:
    from myapp.config.environment.test import *  # noqa
