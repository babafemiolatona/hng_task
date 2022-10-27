from email.policy import default
from django.db import models

class Info(models.Model):
    slackUsername = models.CharField(max_length=100)
    backend = models.BooleanField(default=True)
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.slackUsername