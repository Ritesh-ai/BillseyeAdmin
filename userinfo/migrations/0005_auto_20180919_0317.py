# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-19 10:17
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0004_auto_20180919_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='Phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 19, 3, 17, 54, 45000)),
        ),
    ]
