# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# project imports
from utils.core.models import TimeStampable
from apps.operations.managers.sub_category import SubCategoryManager, SubCategoryQuerySet


class SubCategory(TimeStampable):
    name = models.CharField(verbose_name=_("Sub Category Name"), max_length=30)

    objects = SubCategoryManager.from_queryset(SubCategoryQuerySet)()

    class Meta:
        verbose_name = _("SubCategory")
        verbose_name_plural = _("SubCategories")
        app_label = "operations"
        indexes = [models.Index(fields=["name"])]
        ordering = ("-id",)

    def __str__(self):
        return self.name
