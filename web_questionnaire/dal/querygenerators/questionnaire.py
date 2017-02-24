def get_questionnaire_query(questionnaire_id):
    """
    Generates a get_questionnaire query
    :return: The match dict and the projection query
    """
    match_dict = {"questionnaire_id": questionnaire_id}
    projection = {"_id": False, "questions": True, "max_answer_time_minutes": True}
    return match_dict, projection
