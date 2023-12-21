import sys
from functools import lru_cache

from loguru import logger

LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD at HH:mm:ss}</green> | "
    "node_app | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
    " {extra} {exception}"
)
logger.remove()
logger.add(
    sys.stderr,
    format=LOG_FORMAT,
    level="ERROR",
    backtrace=True,
    diagnose=True,
    serialize=True,
    enqueue=True,
    catch=True,
)
logger.add(
    sys.stdout,
    format=LOG_FORMAT,
    level="INFO",
    enqueue=True,
    colorize=True,
)
metadata = {"microservice_name": "employee_app"}
logger = logger.bind(**metadata)


@lru_cache
def get_logger():
    return logger


logging = get_logger()
