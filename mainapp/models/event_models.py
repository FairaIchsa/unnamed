from django.db import models
from django.utils import timezone

from .user_models import User


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)    # pk = 1 'Other' should be set
    host = models.ForeignKey(User, related_name='host_of', null=True, on_delete=models.SET_NULL)
    participants = models.ManyToManyField(User, related_name='participant_of', blank=True)
    location = models.CharField(max_length=255)
    description = models.TextField(max_length=1023, blank=True, null=True, default=None)
    time = models.DateTimeField(default=timezone.now)
    latitude = models.DecimalField(max_digits=15, decimal_places=12, null=True, default=None)
    longitude = models.DecimalField(max_digits=15, decimal_places=12, null=True, default=None)


    def __str__(self):
        return self.title
