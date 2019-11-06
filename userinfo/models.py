# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class UserInfo(models.Model):
    user = models.OneToOneField(User)

    # Additional Fields
    Date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    # Address = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username