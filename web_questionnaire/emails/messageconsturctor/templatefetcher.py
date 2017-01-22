import os

from web_questionnaire import config


class TemplateFetcher(object):
    """
    Fetches email messages templates.
    """

    @staticmethod
    def fetch_template(template_name):
        """
        Fetches a template by the given name
        :param template_name: The name of the template to fetch
        :return: The template
        """
        template_file_name = os.path.join(config.Email.EMAIL_TEMPLATES_DIRECTORY,
                                          )
        with open(template_file_name, "rb") as template_file:
            return template_file.read()
