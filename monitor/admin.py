from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Url, Requests


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'deleted_at', 'updated_at']

@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'deleted_at', 'updated_at', 'result']