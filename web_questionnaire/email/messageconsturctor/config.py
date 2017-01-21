from web_questionnaire.email.messageconsturctor import consts

TEMPLATE_NAMES_TO_FILENAMES = {consts.ACTIVATE_EMAIL_TEMPLATE_NAME: "activate_email.html",
                               consts.QUESTIONNAIRE_RESULTS_TEMPLATE_NAME: "questionnaire_results.html",
                               consts.RESET_PASSWORD_TEMPLATE_NAME: "reset_password.html"}

TEMPLATES_DIRECTORY = "../templates"
