import abc


class MessageConstructorBase(object):
    """
    A base class for constructing email messages.
    """
    __metaclass__ = abc.ABCMeta

    @classmethod
    @abc.abstractmethod
    def construct_activate_email_message(cls, sender, receiver, subject, first_name, activation_url):
        """
        Constructs an activation message email
        """
        pass

    @classmethod
    @abc.abstractmethod
    def construct_reset_password_message(cls, sender, receiver, subject, first_name, reset_url):
        """
        Constructs a password reset email
        """
        pass

    @classmethod
    @abc.abstractmethod
    def construct_questionnaire_results_message(cls, sender, receiver, subject, full_name, answers, attributes_results):
        """
        Constructs a questionnaire results email
        """
        pass
