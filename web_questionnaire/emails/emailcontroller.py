import smtplib
from web_questionnaire import config


class EmailController(object):
    """
    Controls the email connection, which allows sending emails.
    """

    def __init__(self, host=config.SMTP_SERVER_HOST, port=config.SMTP_SERVER_PORT):
        """
        Initializes the object
        :param host: The host of the SMTP sever.
        :param port: The port of the SMTP sever.
        """
        self._connection = None
        self._host = host
        self._port = port

    def send_mail(self, sender, receiver, message):
        """
        Sends an emails
        :param sender: The sender of the emails
        :param receiver: The receiver of the emails
        :param message: The message to send
        """
        # todo: except except except
        self._connection.sendmail(sender, receiver, message)

    def connect(self):
        """
        Connects to the SMTP server
        """
        # todo: except except except
        self._connection = smtplib.SMTP(self._host, self._port)

    def disconnect(self):
        """
        Disconnects from the server
        """
        # todo: except except except
        if self._connection:
            self._connection.quit()

    def __enter__(self):
        """
        Connects to the server
        """
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Disconnects from the server
        """
        self.disconnect()
