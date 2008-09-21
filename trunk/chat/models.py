from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Post(models.Model):
    u"""
    """
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, blank=True)
    message = models.CharField(max_length=255)
    
    def summary(self):
        return self.message[:100]
    def __unicode__(self):
        return self.summary()

class UserData(models.Model):
    """
    """
    user = models.ForeignKey(User, unique=True)
    last_req = models.DateTimeField(default=datetime.now())
    refresh_period = models.IntegerField(default=5)
    connected = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'User data'
        verbose_name_plural = 'Users data'
        