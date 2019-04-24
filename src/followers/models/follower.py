from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user')
    follow = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='follow')
