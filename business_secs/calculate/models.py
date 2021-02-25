from django.db import models
from django.utils import timezone


class Business_Secs(models.Model):
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)
    business_seconds = models.DateTimeField(blank=True)
