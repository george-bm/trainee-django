from datetime import datetime

from django.db import models

class Message(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=2048)
    file = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
