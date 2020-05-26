from __future__ import print_function, absolute_import

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import UnlimitedExample


class UnlimitedExampleAdmin(ModelAdmin):
    list_display = ["name", "code"]


admin.site.register(UnlimitedExample, UnlimitedExampleAdmin)
