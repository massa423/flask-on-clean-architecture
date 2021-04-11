from flask import Flask
from myapp.interfaces.gateways.database.db import init_db

app = Flask(__name__)


@app.cli.command("init-db")
def init_db_from_cli():
    init_db()
