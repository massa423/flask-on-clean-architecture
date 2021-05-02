from logging import getLogger
from typing import Any

from flask import Blueprint, jsonify
from myapp.injectors.usecase_injector import user_get_usecase_injector

logger = getLogger(__name__)

bp = Blueprint("api.v1", __name__, url_prefix="/api/v1")


@bp.route("/users/<name>")
def users(name: str) -> Any:
    # inject
    user_get_usecase = user_get_usecase_injector()

    response = user_get_usecase.handle(name)

    return jsonify(response.dict())
