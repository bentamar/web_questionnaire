import smtplib

from wq_project import config
from wq_project.emails.emailcontroller import consts, exceptions
from wq_project.logger.logger import get_logger


class EmailController(object):
    """
    Controls the email connection, which allows sending emails.
    """

    def __init__(self, host=config.Email.SMTP_SERVER_HOST, port=config.Email.SMTP_SERVER_PORT):
        """
        Initializes the object
        :param host: The host of the SMTP sever.
        :param port: The port of the SMTP sever.
        """
        self._connection = None
        self._host = host
        self._port = port
        self._logger = get_logger(consts.EMAIL_CONTROLLER_LOGGER_NAME)

    def send_mail(self, sender, receiver, message):
        """
        Sends an emails
        :param sender: The sender of the emails
        :param receiver: The receiver of the emails
        :param message: The message to send
        """
        try:
            self._connection.sendmail(sender, receiver, message)
        except smtplib.SMTPRecipientsRefused as e:
            self._logger.error("All of the given recipients were refused by the server",
                               extra={"recipients": receiver, "error": str(e)})
            raise exceptions.RecipientsRefusedError("All of the given recipients were refused by the server")
        except smtplib.SMTPSenderRefused as e:
            self._logger.error("The sender was refused by the server",
                               extra={"sender": sender, "error": str(e)})
            raise exceptions.SenderRefusedError("The sender was refused by the server")

    def connect(self):
        """
        Connects to the SMTP server
        """
        try:
            self._connection = smtplib.SMTP(self._host, self._port)
        except smtplib.SMTPConnectError as e:
            self._logger.error("An error has occurred while trying to connect to the server",
                               extra={"host": self._host, "port": self._port, "error": str(e)})
            raise exceptions.ConnectionError("An error has occurred while trying to connect to the server")

    def disconnect(self):
        """
        Disconnects from the server
        """
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
