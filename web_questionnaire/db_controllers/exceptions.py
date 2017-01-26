class GeneralDbError(Exception):
    """
    A base exception class for DB errors.
    """


class MaxRetriesError(GeneralDbError):
    """
    An exceptions for reaching the maximum amount of tries to do an action on the DB.
    """


class QueryRunError(GeneralDbError):
    """
    An exception for a query run failure.
    """

class ConnectionError(GeneralDbError):
    """
    A connection failure with the DB.
    """