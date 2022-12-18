
from django.contrib import admin

from login.models import FormData


@admin.register(FormData)
class PersonAdmin(admin.ModelAdmin):
    pass







