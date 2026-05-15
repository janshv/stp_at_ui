import logging
from config import settings


def get_logger(name: str) -> logging.Logger:
    log_level = settings.log_level

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    handler = logging.StreamHandler()
    handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger

