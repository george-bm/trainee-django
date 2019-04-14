from datetime import datetime

from django.db import models


class User(models.Model):
    login = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    lang = models.CharField(max_length=5)
    reg_date = models.DateTimeField(default=datetime.now)