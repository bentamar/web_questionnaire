# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wq_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedUserReferrals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=300)),
                ('attribute_key', models.CharField(max_length=50)),
                ('attribute_value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('max_answer_time_minutes', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('cell_number', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=50)),
                ('user_state', models.CharField(max_length=30)),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='last modified at')),
                ('password_hash', models.CharField(max_length=50)),
                ('verification_hash', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='last modified at')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wq_app.Choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wq_app.Question')),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wq_app.Questionnaire')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wq_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wq_app.UserType'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='submitter',
            field=models.ForeignKey(on_delete=models.SET(wq_app.models.get_sentinel_user), to='wq_app.User'),
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wq_app.Questionnaire'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wq_app.Question'),
        ),
        migrations.AddField(
            model_name='alloweduserreferrals',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wq_app.Questionnaire'),
        ),
        migrations.AddField(
            model_name='alloweduserreferrals',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wq_app.User'),
        ),
    ]
