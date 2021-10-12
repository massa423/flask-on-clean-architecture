export APP_ENV=test
export PYTEST_ADDOPTS='-v --ff --cov=app/ --cov-report=term-missing'
pytest
