import sys
from logging import Formatter, StreamHandler, getLogger

from flask import has_request_context, request
from myapp.config import config


class RequestFormatter(Formatter):
    def format(self, record) -> str:
        if has_request_context():
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

        # ルートロガーを変更する必要がある。
        logger = getLogger()
        logger.setLevel(config.LOG_LEVEL)
        logger.addHandler(handler)

        getLogger("werkzeug").disabled = True

        logger.info("logging initialized.")
