
from django.contrib import admin

from login.models import Purchase


@admin.register(Purchase)
class PersonAdmin(admin.ModelAdmin):
    pass







