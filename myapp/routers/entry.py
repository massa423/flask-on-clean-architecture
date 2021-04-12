from logging import getLogger
from typing import Union

from flask import Blueprint, flash, redirect, render_template, request, url_for
from myapp.applications.dto.user_input import UserInput
from myapp.exceptions import DuplicateException
from myapp.injectors.usecase_injector import create_user_usecase_injector
from pydantic import ValidationError
from werkzeug.wrappers.response import Response

logger = getLogger(__name__)

bp = Blueprint("entry", __name__, url_prefix="/entry")


@bp.route("/")
@bp.route("index")
def index() -> str:
    # g.name = "global name test"

    return render_template("entry/index.html")


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

        return redirect(url_for("entry.index"))

    return render_template(
        "entry/confirm.html",
        input=input.dict(exclude={"password"}),
        password=input.password1.get_secret_value(),
    )


@bp.route("done", methods=["POST"])
def done() -> Union[str, Response]:
    input = UserInput(
        name=request.form["name"],
        password1=request.form["password"],
        password2=request.form["password"],
        email=request.form["email"],
    )

    logger.debug(f"input data: {input}")
    try:
        response = create_user_usecase_injector().handle(input)
    except DuplicateException as e:
        logger.info(e)
        flash("you input data already registerd.")
        return redirect(url_for("entry.index"))

    return render_template("entry/done.html", response=response)
