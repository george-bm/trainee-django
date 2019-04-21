from datetime import datetime

from django.db import models


class Message(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING, related_name='message_user')
    text = models.CharField(max_length=2048)
    file = models.FileField(upload_to='pitts/%Y/%m/%d/')
    date = models.DateTimeField(default=datetime.now)
