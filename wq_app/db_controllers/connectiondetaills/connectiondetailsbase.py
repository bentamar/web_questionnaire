from abc import ABCMeta, abstractmethod


class ConnectionDetailsBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, *args):
        """
        Initializes the object
        :param args: The arguments needed for connection details
        """
        pass
