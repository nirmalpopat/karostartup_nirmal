# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.contrib import admin
from django.utils.html import format_html
from django.conf import settings

# project imports
from apps.operations.models import (
    Category, 
    SubCategory, 
    Post,
    Trainer,
    Bootcamp
)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "city", "state")
    list_filter = ("is_internship", "is_part_time", "is_work_from_home")
    list_display = ("id", "title", "opening_count", "compensation")
    readonly_fields = ("create_date", "modified_date")


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("id", "name")
    readonly_fields = ("create_date", "modified_date")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("id", "name")
    readonly_fields = ("create_date", "modified_date")
    
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    search_fields = ("first_name", "last_name", "photo", "description")
    list_filter = ("first_name", "last_name", "photo", "description")
    list_display = ("first_name", "last_name", "photo", "description")
    readonly_fields = ("create_date", "modified_date")

@admin.register(Bootcamp)
class BootcampAdmin(admin.ModelAdmin):
    search_fields = ("trainer", "image", "class_name", "mode", "timing", "outcome")
    list_filter = ("trainer", "image", "class_name", "mode", "timing", "outcome")
    list_display = ("trainer", "image", "class_name", "mode", "timing", "outcome")
    readonly_fields = ("create_date", "modified_date")
    
    # def photo_tag(self, obj):
    #     return format_html(f"<img src='http://127.0.0.1:8000{settings.MEDIA_URL}{obj.image}' style='width:100px; height:100px; border-radius: 50%;'")