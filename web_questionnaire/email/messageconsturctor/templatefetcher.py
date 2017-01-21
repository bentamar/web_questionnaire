import os
from web_questionnaire.email.messageconsturctor import config, consts


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
        try:
            template_file_name = os.path.join(config.TEMPLATES_DIRECTORY,
                                              config.TEMPLATE_NAMES_TO_FILENAMES[template_name])
        except KeyError:
            
        with open(template_file_name, "rb") as template_file:
            return template_file.read()
