from pymongo.errors import AutoReconnect

from wq_project import config
from wq_project.db_controllers import exceptions


def run_safe_query(func):
    """
    Safely runs a query function. If an AutoRetry exception occurs, the decorator will try to run the query again.
    It is thrown because the connection to the Mongo server has been lost, but a retry is recommended.
    :param func: The function to run.
    :return: The decorator
    """
    def query_function(*args, **kwargs):
        """
        The function to run.
        """
        for i in xrange(config.Mongo.MAX_NUM_OF_RETRIES):
            try:
                return func(*args, **kwargs)
            except AutoReconnect:
                continue
            except Exception as e:
                raise exceptions.QueryRunError(str(e))

    return query_function
