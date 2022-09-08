from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(max_length=1023, blank=True, null=True)
