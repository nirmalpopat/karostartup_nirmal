# python imports
from __future__ import unicode_literals
import datetime

# lib imports
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

# project imports
from apps.accounts.constants import UserTypeChoice
from apps.accounts.models import (
    User,
    VerificationToken,
    Education,
    CompanyProfile,
    StudentProfile
)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("id", "username", "email", "first_name", "last_name", "phone")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "phone", "whatsapp_phone_number")}),
        (
            _("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions", "user_type")},
        ),
        (_("Important dates"), {"fields": ("date_joined",)}),
    )
    readonly_fields = ("date_joined",)


@admin.register(VerificationToken)
class VerificationTokenAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "token", "token_type", "is_valid")
    readonly_fields = ("create_date", "modified_date")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("id", "course_name", "institute", "city")
    readonly_fields = ("create_date", "modified_date")
    search_fields = ("course_name", "institute", "city")


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "city", "pin_code")
    readonly_fields = ("create_date", "modified_date", "verified_by", "verified_at")
    list_filter = ("type", "state", "is_verified")
    search_fields = ("name", "city", "pin_code", )

    def save_model(self, request, obj, form, change):
        if request.user.user_type != UserTypeChoice.COMPANY:
            raise ValidationError("This user type can not make company profile")
        if obj.is_verified:
            obj.verified_by = request.user
            obj.verified_at = timezone.now()
        super().save_model(request, obj, form, change)


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "preferred", "user")
    list_filter = ("state", "preferred")
    readonly_fields = ("create_date", "modified_date")
    search_fields = ("city",)
