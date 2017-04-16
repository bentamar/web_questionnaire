from __future__ import unicode_literals

from django.db import models


class UserType(models.Model):
    """
    Different user types. For example - simple user, admin.
    """
    ADMIN = 'AD'
    REFERRER = 'RF'
    NORMAL = 'NR'
    DELETED = 'DL'
    USER_STATES = [
        (ADMIN, 'Administrator'),
        (REFERRER, "Referrer"),
        (NORMAL, "Normal user"),
        (DELETED, "Deleted")
    ]

    type = models.CharField(max_length=50, choices=USER_STATES, default=NORMAL)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'user_types'


class User(models.Model):
    """
    User login data and metadata
    """
    ACTIVATED = 'AC'
    UNACTIVATED = 'UA'
    USER_STATES = [
        (ACTIVATED, 'Activated'),
        (UNACTIVATED, "Unactivated")
    ]

    def __str__(self):
        return self.email

    user_type = models.ForeignKey(UserType, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cell_number = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50)
    user_state = models.CharField(max_length=30, choices=USER_STATES, default=UNACTIVATED)
    modified_at = models.DateTimeField('last modified at', auto_now=True)
    password_hash = models.CharField(max_length=50)
    verification_hash = models.CharField(max_length=50)

    def is_admin(self):
        """
        Returns whether or not the user is an administrator
        :return: Whether or not the user is an administrator
        """
        return self.user_type.type == UserType.ADMIN

    class Meta:
        db_table = 'users'


def get_sentinel_user():
    """
    Creates a deleted user object - if it already exists, it returns it.
    :return: The user object
    """

    return User.objects.get_or_create(first_name='deleted', last_name='deleted', user_state='deleted',
                                      email='deleted', )


class Questionnaire(models.Model):
    """
    A questionnaire object represents the metadata of a questionnaire, and its questions.
    """
    submitter = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    created_at = models.DateTimeField('date created')
    modified_at = models.DateTimeField('date modified', auto_now=True)
    max_answer_time_minutes = models.FloatField()

    def __str__(self):
        return str(self.submitter)

    class Meta:
        db_table = 'questionnaires'


class Question(models.Model):
    """
    Question metadata
    """
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300)

    def __str__(self):
        return self.question_text

    class Meta:
        db_table = 'questions'


class Choice(models.Model):
    """
    A possible choice of a question
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    attribute_key = models.CharField(max_length=50)
    attribute_value = models.FloatField()

    def __str__(self):
        return self.choice_text

    class Meta:
        db_table = 'choices'


class AllowedUserReferrals(models.Model):
    """
    Only the referrals listed here are allowed to occur.
    This table exists so it is harder to fake a referrer.
    """
    questionnaire = models.ForeignKey(Questionnaire)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'allowed_user_referrals'


class UserChoice(models.Model):
    """
    A choice A user made on a questionnaire.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    created_at = models.DateTimeField('last modified at', auto_now_add=True)

    def __str__(self):
        return str(self.choice)

    class Meta:
        db_table = 'user_choices'
