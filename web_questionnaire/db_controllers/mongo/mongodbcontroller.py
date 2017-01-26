from pymongo import MongoClient
from pymongo import errors

from web_questionnaire.db_controllers.mongo.retrydecorator import run_safe_query
from web_questionnaire.db_controllers import exceptions


class MongoDbController(object):
    """
    Controls data manipulation and fetching, such as:
        find, aggregate, remove and update.
    """

    def __init__(self, hosts, db_name=None):
        """
        Initiates the object
        :param hosts: The hosts of the Mongo servers to connect to.
        :param db_name: The name of the DB to use
        """
        try:
            self._connection = MongoClient(hosts)
        except errors.ConnectionFailure as e:
            raise exceptions.ConnectionError(str(e))
        self._db = self._connection[db_name]

    @run_safe_query
    def find(self, collection_name, match_filter, projection):
        cursor = self._db[collection_name].find(match_filter, projection)
        if cursor:
            return list(cursor)
        return []

    @run_safe_query
    def find_one(self, collection_name, match_filter, projection):
        result = self._db[collection_name].find_one(match_filter, projection)
        if result:
            return result
        return {}

    @run_safe_query
    def update_one(self, collection_name, match_filter, update_dict):
        cursor = self._db[collection_name].update_one(match_filter, update_dict)
        return cursor.modified_count

    @run_safe_query
    def update_many(self, collection_name, match_filter, update_dict):
        cursor = self._db[collection_name].update_many(match_filter, update_dict)
        return cursor.modified_count

    @run_safe_query
    def delete_many(self, collection_name, match_filter):
        cursor = self._db[collection_name].delete_many(match_filter)
        return cursor.deleted_count

    @run_safe_query
    def delete_many(self, collection_name, match_filter):
        cursor = self._db[collection_name].delete_one(match_filter)
        return cursor.deleted_count
