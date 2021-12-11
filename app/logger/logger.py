import logging
import sys
from logging import Formatter, StreamHandler, getLogger
from typing import Any

from app.config import config
from flask import has_request_context, request


class RequestFormatter(Formatter):
    def format(self, record: Any) -> str:
        if has_request_context():  # type: ignore
            if request.headers.get("X-Forwarded-For"):
                record.remote_addr = request.headers.get("X-Forwarded-For")
            else:
                record.remote_addr = request.remote_addr
        else:
            record.remote_addr = None

        return super().format(record)


class Logger:
    """
    ロガー
    """

    def __init__(self) -> None:
        """
        ロガー初期化
        """

        formatter = RequestFormatter(
            "[%(asctime)s] %(remote_addr)s %(levelname)s: %(name)s(%(process)d): %(message)s"  # noqa
        )

        handler = StreamHandler(sys.stdout)
        handler.setFormatter(formatter)

        logger = getLogger("app")
        logger.setLevel(config().LOG_LEVEL)
        logger.addHandler(handler)

        # SQLAlchemyもフォーマットを揃える。
        # https://github.com/sqlalchemy/sqlalchemy/blob/main/lib/sqlalchemy/engine/base.py
        sqla_logger = getLogger("sqlalchemy.engine.Engine")
        for h in sqla_logger.handlers:
            sqla_logger.removeHandler(h)
        sqla_logger.addHandler(handler)

        getLogger("werkzeug").disabled = True

        logger.info("logging initialized.")
