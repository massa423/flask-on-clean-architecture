from logging import getLogger
from typing import Any

from flask import Blueprint, jsonify
from injector import inject
from app.applications.user_get_usecase import UserGetUsecase

logger = getLogger(__name__)

bp = Blueprint("api.v1", __name__, url_prefix="/api/v1")


@inject
@bp.route("/users/<name>")
def users(name: str, user_get_usecase: UserGetUsecase) -> Any:

    response = user_get_usecase.handle(name)

    return jsonify(response.dict())
