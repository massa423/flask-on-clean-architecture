from logging import Formatter, getLogger, StreamHandler
from flask import request, has_request_context
from myapp.config import config
import sys


class RequestFormatter(Formatter):
    def format(self, record):
        if has_request_context():
            record.remote_addr = request.remote_addr
        else:
            record.remote_addr = None

        return super().format(record)


class Logger:
    """
    ロガー
    """

    def __init__(self):
        """
        ロガー初期化
        """

        formatter = RequestFormatter("[%(asctime)s] %(remote_addr)s %(levelname)s: %(name)s(%(process)d): %(message)s")

        handler = StreamHandler(sys.stdout)
        handler.setFormatter(formatter)

        # ルートロガーを変更する必要がある。
        logger = getLogger()
        logger.setLevel(config.LOG_LEVEL)
        logger.addHandler(handler)

        getLogger("werkzeug").disabled = True

        logger.info("logging initialized.")
