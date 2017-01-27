from web_questionnaire.dal import consts
from web_questionnaire.logger.logger import get_logger
from web_questionnaire.db_controllers.mongo.mongodbcontroller import MongoDbController


class QuestionnaireFetcher(object):
    """
    Fetches questionnaires data
    """
    def __init__(self, db_connection_details):
        self._logger = get_logger(consts.DAL_LOGGER_NAME)
        self._db_controller = MongoDbController(db_connection_details, )