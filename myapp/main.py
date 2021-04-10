from flask import Flask, session, render_template, redirect, url_for, flash, abort, request, g, has_request_context
from werkzeug.wrappers import Response
from markupsafe import escape
from myapp.routers import entry
from myapp.config import config
from myapp.logger.logger import Logger
from logging import getLogger
from myapp.libs.request_headers import RequestHeaders

logger = getLogger(__name__)


def before_action():
    if has_request_context:
        rh = RequestHeaders(host=request.headers.get("HOST"), user_agent=request.headers.get("USER_AGENT"))
    # app.loggerで出力するとflask loggerのsetLevelが適用される。
    logger.info(f"request: {request.url}")
    app.logger.debug(f"Host: {rh.host}, UserAgent: {rh.user_agent}")

    # リクエスト時にはinit_appを通らないのでこれはコケる
    # getLogger(__name__).info(g.what_time)

    # リダイレクトも可能
    # return redirect('https://www.google.com')


def after_action(response):
    logger.info(f"status_code: {response._status_code}")
    return response


def init_app():
    """
    アプリ起動時、リロード時にしか呼ばれない
    """
    Logger()

    app = Flask(__name__)

    # flask環境変数指定
    app.secret_key = config.SECRET_KEY

    # Bliueprint
    app.register_blueprint(entry.bp)

    app.before_request(before_action)
    app.after_request(after_action)

    from datetime import datetime

    # リクエスト時にはapp_contextが存在しない？
    # なのでapp_contectを入れないと怒られる。
    with app.app_context():
        g.what_time = datetime.now()
        logger.info(f"init: {g.what_time}")

    logger.info("app initialized")
    return app


app = init_app()


@app.route("/")
@app.route("/index")
def index() -> str:
    return render_template("index.html")


@app.route("/redirect")
def redirect_to_index() -> Response:
    """リダイレクトとflashのテスト"""
    flash("redirect from /redirect")
    return redirect(url_for("index"))


@app.route("/user/<username>")
def show_user_profile(username: str) -> str:
    """セッションのテスト"""
    if username not in session:
        session["username"] = username
        logger.info(f"session add username: {username}")

    return "User %s" % escape(username)


@app.route("/server_error")
def error_500():
    abort(500)


@app.errorhandler(404)
@app.errorhandler(405)
def not_found(error):
    return render_template("404.html"), error.code


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), error.code
