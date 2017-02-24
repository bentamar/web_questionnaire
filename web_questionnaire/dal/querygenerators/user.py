def get_user_type_query(user_id):
    match_dict = {"user_id": user_id}
    projection = {"_id": False,
                  "user_type": True}
    return match_dict, projection


def get_authenticate_user_query(email, password_hash):
    match_dict = {"email": email, "password_hash": password_hash}
    projection = {"_id": False, "user_id": True}
    return match_dict, projection
