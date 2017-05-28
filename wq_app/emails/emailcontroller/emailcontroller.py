import smtplib

from django.core.mail import send_mail
from wq_app.emails.emailcontroller import consts, exceptions
from wq_app.logger.logger import get_logger


class EmailController(object):
    """
    Controls the email connection, which allows sending emails.
    """

    @staticmethod
    def send_email(subject, message, from_email, recipient_list, html_message=None):
        """
        Sends an email to the recipient list.
        See Django's documentation(https://docs.djangoproject.com/en/1.11/topics/email/#django.core.mail.send_mail)
        for more details.
        :param subject: The subject of the email message
        :param message: The message content
        :param from_email: The source address for the email
        :param recipient_list: A list of recipients to send the email to
        :param html_message: If 'html_message' is provided, the resulting email will be a multipart/alternative email
         with 'message' as the text/plain content type and html_message as the text/html content type.
        :return: The amount of messages sent successfully
        """
        logger = get_logger(consts.EMAIL_CONTROLLER_LOGGER_NAME)
        emails_sent = 0
        try:
            emails_sent = send_mail(subject, message, from_email, recipient_list, html_message=html_message)
        except smtplib.SMTPException as e:
            logger.exception("An error has occurred while trying to send an email.", extra={"error_message": str(e)})
        return emails_sent
