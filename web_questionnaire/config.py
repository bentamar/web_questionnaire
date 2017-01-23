import logging

from web_questionnaire.emails.messageconsturctor import consts


class Email(object):
    SMTP_SERVER_HOST = "127.0.0.1"
    SMTP_SERVER_PORT = 25
    TEMPLATE_NAMES_TO_FILENAMES = {consts.ACTIVATE_EMAIL_TEMPLATE_NAME: "activate_email.html",
                                   consts.QUESTIONNAIRE_RESULTS_TEMPLATE_NAME: "questionnaire_results.html",
                                   consts.RESET_PASSWORD_TEMPLATE_NAME: "reset_password.html"}
    EMAIL_TEMPLATES_DIRECTORY = "../templates"


class Logging(object):
    LOG_FILE_NAME = "WebQuestionnaire.log"
    MAX_LOG_FILE_SIZE_MB = 1024 * 1024 * 5
    MAX_LOG_FILES = 5
    LOGGING_LEVEL = logging.DEBUG
    LOG_FORMAT = "%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s - %(extra)s"
