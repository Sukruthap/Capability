# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-15 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_complexity',
            name='acronym',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question_type',
            name='acronym',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
