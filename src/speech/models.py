from datetime import datetime

from django.db import models


class User(models.Model):
    login = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    lang = models.CharField(max_length=5)
    reg_date = models.DateTimeField(default=datetime.now)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=2048)
    file = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    follow = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow')
