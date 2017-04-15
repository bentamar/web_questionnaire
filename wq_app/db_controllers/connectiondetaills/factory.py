from web_questionnaire.db_controllers.connectiondetaills import exceptions
from web_questionnaire.db_controllers.connectiondetaills.mongoconnectiondetails import MongoConnectionDetails

DB_TYPE_TO_CLASS = {
    "Mongo": MongoConnectionDetails
}


def get_db_connection_details(db_type, *args):
    """
    Creates a DB connection details object
    :param db_type: The type of the DB to get the connection details for
    :param args: The arguments to pass to the connection details class
    :return: The connection details object
    """
    if db_type not in DB_TYPE_TO_CLASS:
        raise exceptions.UnknownDbConnectionType(
            "An unknown connection type {db_type} was given".format(db_type=db_type))
    return DB_TYPE_TO_CLASS[db_type](*args)
