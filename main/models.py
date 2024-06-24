from django.db import models
from django.contrib.auth.models import User


class Ad(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    views = models.PositiveIntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.title


