from django.db import models
from django.utils import timezone


class Business_Secs(models.Model):
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
