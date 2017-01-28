from web_questionnaire.dal import consts
from web_questionnaire.dal.querygenerators import questionnaire
from web_questionnaire.db_controllers.mongo.mongodbcontroller import MongoDbController
from web_questionnaire.logger.logger import get_logger


class QuestionnaireFetcher(object):
    """
    Fetches questionnaires data
    """

    def __init__(self, db_connection_details):
        self._logger = get_logger(consts.DAL_LOGGER_NAME)
        self._db_controller = MongoDbController(db_connection_details, consts.QUESTIONNAIRE_DB_NAME)

    def get_questionnaire(self, questionnaire_id):
        """
        Fetches a questionnaire
        :return: The questionnaire
        """
        match_dict, projection = questionnaire.get_questionnaire_query(questionnaire_id)
        return self._db_controller.find_one(consts.QUESTIONNAIRES_COLLECTION_NAME, match_dict, projection)
