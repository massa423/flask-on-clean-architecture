from app.interfaces.gateways.database.db import init_db
from flask import Flask

app = Flask(__name__)


@app.cli.command("init-db")
def init_db_from_cli() -> None:
    init_db()
