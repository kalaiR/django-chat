from django.db import models
from django.contrib.auth.models import User

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