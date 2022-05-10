# -*- coding: utf-8 -*-
"""
Register your models here.
"""
# python imports
from __future__ import unicode_literals

from django.conf import settings
# lib imports
from django.contrib import admin


class CustomModelAdmin(admin.ModelAdmin):
    """
    Custom Model Admin
    """

    readonly_fields = ("created_at", "modified_at")
    list_per_page = settings.DEFAULT_PAGE_SIZE

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True
