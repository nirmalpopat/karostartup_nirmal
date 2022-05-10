# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# project imports
from utils.core.models import TimeStampable
from apps.accounts.managers.education import EducationManager, EducationQueryset


class Education(TimeStampable):
    """
    Education model description
    """
    course_name = models.CharField(verbose_name=_("Course Name"), max_length=30)
    institute = models.CharField(verbose_name=_("Institute Name"), max_length=100)
    city = models.CharField(verbose_name=_("City"), max_length=124)
    start_date = models.DateField(verbose_name=_("Start Date"))
    is_present = models.BooleanField(verbose_name=_("Is Present"), default=False)
    end_date = models.DateField(verbose_name=_("End Date"), blank=True, null=True)
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    gpa = models.CharField(verbose_name=_("GPA"), max_length=10)

    objects = EducationManager.from_queryset(EducationQueryset)()

    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Education list")
        app_label = "accounts"
        indexes = [models.Index(fields=["course_name", "institute"])]
        ordering = ("-id",)

    def __unicode__(self):
        return f"{self.course_name} - {self.institute}"

    def __str__(self):
        return f"{self.course_name} - {self.institute}"
