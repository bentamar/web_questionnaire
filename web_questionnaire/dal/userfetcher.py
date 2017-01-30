from web_questionnaire import config
from web_questionnaire.dal import consts
from web_questionnaire.dal.querygenerators import user
from web_questionnaire.db_controllers.mongo.mongodbcontroller import MongoDbController
from web_questionnaire.logger.logger import get_logger


class QuestionnaireFetcher(object):
    """
    Fetches user data
    """

    def __init__(self, db_connection_details):
        self._logger = get_logger(consts.DAL_LOGGER_NAME)
        self._db_controller = MongoDbController(db_connection_details, consts.QUESTIONNAIRE_DB_NAME)

    def get_user_type(self, user_id):
        """
        Fetches the user type.
        :param user_id: The ID of the user to fetch
        :return: The user type
        """
        match_dict, projection = user.get_user_type_query(user_id)
        result = self._db_controller.find_one(consts.USERS_COLLECTION_NAME, match_dict, projection)
        if result:
            return result["user_type"]
        return {}

    def authenticate_user(self, email, password_hash):
        """
        Authenticates the given validation details.
        :param email: The email of the user
        :param password_hash: The hash of the user's password
        :return: If authenticated, the user's ID, otherwise an empty dictionary.
        """
        match_dict, projection = user.get_authenticate_user_query(email, password_hash)
        result = self._db_controller.find_one(consts.USERS_COLLECTION_NAME, match_dict, projection)
        if result:
            return result["user_id"]
        return {}

    def register_user(self, first_name, last_name, email, password_hash, cell_number):
        # todo
        pass

    def is_allowed_to_submit_questionnaire(self, user_id):
        user_type = self.get_user_type(user_id)
        if not user_type:
            return False
        return user_type in config.Users.USER_TYPES_ALLOWED_TO_SUBMIT_QUESTIONNAIRES
