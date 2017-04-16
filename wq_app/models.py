from __future__ import unicode_literals

from django.contrib.auth.models import User as DjangoUser
from django.db import models


class UserMeta(models.Model):
    """
    User login data and metadata
    """

    def __str__(self):
        return str(self.user)

    user = models.OneToOneField(DjangoUser, related_name='user_meta', on_delete=models.CASCADE)
    cell_number = models.CharField(max_length=20, null=True)
    activation_key = models.CharField(max_length=50, null=True)
    key_expiration = models.DateTimeField(null=True)

    class Meta:
        db_table = 'users'


def get_sentinel_user():
    """
    Creates a deleted user object - if it already exists, it returns it.
    :return: The user object
    """

    return UserMeta.objects.get_or_create(user__username='deleted')


class Questionnaire(models.Model):
    """
    A questionnaire object represents the metadata of a questionnaire, and its questions.
    """
    submitter = models.ForeignKey(UserMeta, on_delete=models.SET(get_sentinel_user))
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
    user = models.ForeignKey(UserMeta)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'allowed_user_referrals'


class UserChoice(models.Model):
    """
    A choice A user made on a questionnaire.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(UserMeta, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    created_at = models.DateTimeField('last modified at', auto_now_add=True)

    def __str__(self):
        return str(self.choice)

    class Meta:
        db_table = 'user_choices'
