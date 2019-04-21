import os
from datetime import datetime

from django.db import models
from django.dispatch import receiver


class Message(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING, related_name='message_user')
    text = models.CharField(max_length=2048)
    file = models.FileField(upload_to='pitts/%Y/%m/%d/')
    date = models.DateTimeField(default=datetime.now)


@receiver(models.signals.post_delete, sender=Message)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
