from email.mime.text import MIMEText

from flask import render_template

from web_questionnaire import config
from web_questionnaire.emails.messageconsturctor import consts
from web_questionnaire.emails.messageconsturctor.messageconsturctorbase import MessageConstructorBase


class FlaskMessageConstructor(MessageConstructorBase):
    """
    Constructs email messages.
    """

    @staticmethod
    def construct_generic_email_message(sender, receiver, subject, template_name, **message_context):
        """
        Constructs an email message.
        :param sender: The sender of the emails
        :param receiver: The receiver of the emails
        :param subject: The subject of the email message.
        :param template_name: The name of the template to use to construct
        :param message_context: The context of the template variables
        :return: The constructed message
        """
        template_name = config.Email.TEMPLATE_NAMES_TO_FILENAMES[template_name]
        contents = render_template(template_name, **message_context)
        email_message = MIMEText(contents)
        email_message[consts.SUBJECT_MESSAGE_KEY] = subject
        email_message[consts.FROM_MESSAGE_KEY] = sender
        email_message[consts.TO_MESSAGE_KEY] = receiver
        return email_message.as_string()

    @classmethod
    def construct_activate_email_message(cls, sender, receiver, subject, first_name, activation_url):
        """
        Constructs an activation message email
        """
        return cls.construct_generic_email_message(sender, receiver, subject, consts.ACTIVATE_EMAIL_TEMPLATE_NAME,
                                                   first_name=first_name, activation_url=activation_url)

    @classmethod
    def construct_reset_password_message(cls, sender, receiver, subject, first_name, reset_url):
        """
        Constructs a password reset email
        """
        return cls.construct_generic_email_message(sender, receiver, subject, consts.RESET_PASSWORD_TEMPLATE_NAME,
                                                   first_name=first_name, reset_url=reset_url)

    @classmethod
    def construct_questionnaire_results_message(cls, sender, receiver, subject, full_name, answers, attributes_results):
        """
        Constructs a questionnaire results email
        """
        return cls.construct_generic_email_message(sender, receiver, subject,
                                                   consts.QUESTIONNAIRE_RESULTS_TEMPLATE_NAME,
                                                   full_name=full_name, answers=answers,
                                                   attributes_results=attributes_results)
