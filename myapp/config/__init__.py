import os

DEVELOPMENT = "development"
STAGING = "staging"
PRODUCTION = "production"
TEST = "test"


env = os.getenv("APP_ENV", DEVELOPMENT)

if env == DEVELOPMENT:
    from myapp.config.environment.development import DevelopmentConfig

    config = DevelopmentConfig()
elif env == STAGING:
    from myapp.config.environment.staging import StagingConfig

    config = StagingConfig()
elif env == PRODUCTION:
    from myapp.config.environment.production import ProductionConfig

    config = ProductionConfig()
elif env == TEST:
    from myapp.config.environment.test import TestConfig

    config = TestConfig()
