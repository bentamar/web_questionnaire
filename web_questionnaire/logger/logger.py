import logging
from logging.handlers import RotatingFileHandler

from web_questionnaire import config

logger_instances = []


class ExtraLogger(logging.Logger):
    """
    Allows for 'extra' data to be logged conveniently.
    For example, instead of using logger.info('message', extra={'extra': {'x': 1}}),
     this logger allows the following syntax: logger.info('message', extra={'x': 1})
    """

    def _log(self, level, msg, args, exc_info=None, extra=None):
        if extra is not None:
            extra = {'extra': extra}
        else:
            extra = {'extra': {}}
        super(ExtraLogger, self)._log(level, msg, args, exc_info, extra)


def get_logger(logger_name):
    if logger_name in logger_instances:
        return logging.getLogger(logger_name)
    logger_instances.append(logger_name)
    logging.setLoggerClass(ExtraLogger)
    logger = logging.getLogger(logger_name)
    handler = RotatingFileHandler(config.Logging.LOG_FILE_NAME, maxBytes=config.Logging.MAX_LOG_FILE_SIZE_MB,
                                  backupCount=config.Logging.MAX_LOG_FILES)
    formatter = logging.Formatter(config.Logging.LOG_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(config.Logging.LOGGING_LEVEL)
    return logger
