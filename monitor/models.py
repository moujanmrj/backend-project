from django.db import models
from core.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Url(models.Model):
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="urls")
    address = models.CharField(max_length=255)
    threshold = models.IntegerField(blank=True, null=True)
    failed_times = models.IntegerField(blank=True, null=True)


class Requests(models.Model):
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    url = models.ForeignKey(Url, on_delete=models.CASCADE, related_name="requests")
    result = models.IntegerField(max_length=50)