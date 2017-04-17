from django.contrib import admin

from .models import Question, Questionnaire, AllowedUserReferrals, UserMeta, UserChoice, Choice

admin.site.register([Question, Questionnaire, AllowedUserReferrals, UserMeta, UserChoice, Choice])
