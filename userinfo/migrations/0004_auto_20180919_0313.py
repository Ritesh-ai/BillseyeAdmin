# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-19 10:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0003_auto_20180917_0418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='Phone_number',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 19, 3, 13, 34, 233000)),
        ),
    ]