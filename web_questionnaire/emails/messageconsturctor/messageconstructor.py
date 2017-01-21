from email.mime.text import MIMEText
from web_questionnaire.emails.messageconsturctor.templatefetcher import TemplateFetcher


class MessageConstructor(object):
    """
    Constructs email messages.
    """

    @staticmethod
    def construct_activate_email_message(sender, receiver, first_name, activation_url):
        """
        Constructs an emails activation message using the given arguments
        :param sender: The sender of the emails
        :param receiver: The receiver of the emails
        :param first_name: Used in the message
        :param activation_url: Used in the message
        :return: The message to send
        """
