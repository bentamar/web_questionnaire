from __future__ import unicode_literals

from django.db import models


def get_sentinel_user():
    return User.objects.get_or_create(first_name='deleted')


class Questionnaire(models.Model):
    """
    A questionnaire object represents the metadata of a questionnaire, and its questions.
    """
    submitter = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    created_at = models.DateTimeField('date created')
    modified_at = models.DateTimeField('date modified')
    max_answer_time_minutes = models.FloatField()


class Question(models.Model):
    """
    Question metadata
    """
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300)


class Choice(models.Model):
    """
    A possible choice of a question
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class UserType(models.Model):
    """
    Different user types. For example - simple user, admin.
    """
    type = models.CharField(max_length=50)


class User(models.Model):
    """
    User login data and metadata
    """
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cell_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    user_state = models.CharField(max_length=30)
    modified_at = models.DateTimeField('last modified at')
    password_hash = models.CharField(max_length=50)
    verification_hash = models.CharField(max_length=50)


class AllowedUserReferrals(models.Model):
    """
    Only the referrals listed here are allowed to occur.
    This table exists so it is harder to fake a referrer.
    """
    questionnaire = models.ForeignKey(Questionnaire)
    user = models.ForeignKey(User)
