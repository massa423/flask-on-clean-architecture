from logging import getLogger
from typing import Dict
from flask import Blueprint
from myapp.injectors.usecase_injector import get_user_usecase_injector

logger = getLogger(__name__)

bp = Blueprint("api.v1", __name__, url_prefix="/api/v1")


@bp.route("/users/<name>")
def users(name) -> Dict:
    injector = get_user_usecase_injector()

    response = injector.handle(name)

    return response
