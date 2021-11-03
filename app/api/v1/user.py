from logging import getLogger
from typing import Any

from app.applications.user_get_usecase import UserGetUsecase
from flask import Blueprint, jsonify
from flasgger import swag_from
from injector import inject

logger = getLogger(__name__)

bp = Blueprint("api.v1", __name__, url_prefix="/api/v1")


@inject
@bp.route("/users/<name>")
@swag_from("swagger/users.yml")
def users(name: str, user_get_usecase: UserGetUsecase) -> Any:

    response = user_get_usecase.handle(name)

    return jsonify(response.dict())
