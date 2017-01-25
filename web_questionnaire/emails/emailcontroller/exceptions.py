class GenericEmailError(Exception):
    """
    A base class for emails exceptions
    """
    pass


class RecipientsRefusedError(GenericEmailError):
    """
    The server rejected ALL recipients, which means no mails were sent
    """
    pass


class SenderRefusedError(GenericEmailError):
    """
    The server rejected the sender
    """


class ConnectionError(GenericEmailError):
    """
    An error with the connection to the server
    """
