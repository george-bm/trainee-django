from django.db import models


class Follower(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING, related_name='user')
    follow = models.ForeignKey('users.User', on_delete=models.DO_NOTHING, related_name='follow')
