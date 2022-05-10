# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# project import
from utils.core.models import TimeStampable
from apps.accounts.constants import StudentProfileType
from apps.accounts.models.education import Education
from apps.operations.models.categories import Category
from apps.accounts.managers.student_profile import StudentProfileManager, StudentProfileQueryset

USER = get_user_model()


def upload_to(instance, filename):
    path = f"student/images/upload/"
    try:
        ext = filename.split(".")[-1]
    except IndexError:
        ext = filename
    filename = path + "{}{}.{}".format(filename, uuid.uuid4().hex, ext)
    return filename


class StudentProfile(TimeStampable):
    """
    StudentProfile model description
    """
    user = models.OneToOneField(verbose_name=_("User"), to=USER, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_user")
    categories = models.ManyToManyField(verbose_name=_("Categories"), to=Category, blank=True, related_name="%(app_label)s_%(class)s_categories")
    preferred = models.CharField(verbose_name=_("Preferred"), max_length=30, choices=StudentProfileType.choices, blank=True, null=True)
    date_of_birth = models.DateField(verbose_name=_("Date Of Birth"), blank=True, null=True)
    education = models.ManyToManyField(verbose_name=_("Education"), to=Education, blank=True, related_name="%(app_label)s_%(class)s_education")
    photo = models.ImageField(verbose_name=_("Profile Photo"), upload_to=upload_to, blank=True, null=True)
    address_line_1 = models.CharField(verbose_name=_("Address Line 1"), max_length=30, blank=True, null=True)
    address_line_2 = models.CharField(verbose_name=_("Address Line 2"), max_length=30, null=True, blank=True)
    city = models.CharField(verbose_name=_("City"), max_length=30, blank=True, null=True)
    state = models.CharField(verbose_name=_("State"), max_length=30, blank=True, null=True)
    pin_code = models.CharField(verbose_name=_("Pin Code"), max_length=10, blank=True, null=True)

    objects = StudentProfileManager.from_queryset(StudentProfileQueryset)()

    class Meta:
        verbose_name = _("Student Profile")
        verbose_name_plural = _("Student Profiles")
        app_label = "accounts"
        indexes = [models.Index(fields=["preferred"])]
        ordering = ("-id",)

    def __str__(self):
        return self.user.phone
