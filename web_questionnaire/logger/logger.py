import logging
from logging.handlers import RotatingFileHandler

from web_questionnaire import config

def get_logger(logger_name):
    logger = logging.Logger(logger_name)
    handler = RotatingFileHandler(config.LOG_FILE_NAME, maxBytes=)
    logger.addHandler()