from logging import getLogger
from typing import Union

from flask import Blueprint, flash, redirect, render_template, request, url_for
from injector import inject
from myapp.applications.inbound_dto.user_input import UserInput
from myapp.applications.user_create_usecase import UserCreateUsecase
from myapp.exceptions import DuplicateException
from pydantic import ValidationError
from werkzeug.wrappers.response import Response

logger = getLogger(__name__)

bp = Blueprint("signup", __name__, url_prefix="/signup")


@bp.route("/")
@bp.route("index")
def index() -> str:
    return render_template("signup/index.html")


@bp.route("confirm", methods=["POST"])
def confirm() -> Union[str, Response]:

    try:
        input = UserInput(
            name=request.form["name"],
            password1=request.form["password1"],
            password2=request.form["password2"],
            email=request.form["email"],
        )

        logger.debug(f"input data: {input}")
    except ValidationError as e:
        logger.info(e)
        msg = [x["msg"] for x in e.errors()]

        for m in msg:
            flash(m)

        return redirect(url_for("signup.index"))

    return render_template(
        "signup/confirm.html",
        input=input.dict(exclude={"password"}),
        password=input.password1.get_secret_value(),
    )


@inject
@bp.route("done", methods=["POST"])
def done(user_create_usecase: UserCreateUsecase) -> Union[str, Response]:

    input = UserInput(
        name=request.form["name"],
        password1=request.form["password"],
        password2=request.form["password"],
        email=request.form["email"],
    )
    logger.debug(f"input data: {input}")

    try:
        response = user_create_usecase.handle(input)
    except DuplicateException as e:
        logger.info(e)
        flash("you input data already registerd.")
        return redirect(url_for("signup.index"))

    return render_template("signup/done.html", response=response.dict())
