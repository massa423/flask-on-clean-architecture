from flask import Blueprint, render_template, g, request


bp = Blueprint("entry", __name__, url_prefix="/entry")


@bp.route("/")
@bp.route("index")
def index():
    g.name = "global name test"
    return render_template("entry/index.html")


@bp.route("done", methods=["POST"])
def done():
    data = {"name": request.form["name"], "password": request.form["password"]}

    return render_template("entry/done.html", data=data)
