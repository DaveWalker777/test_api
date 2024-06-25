from django.db import models
from django.contrib.auth.models import User


class Ad(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    views = models.PositiveIntegerField()
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


