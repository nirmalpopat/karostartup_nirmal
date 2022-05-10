# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# project imports
from utils.core.models import TimeStampable
from apps.operations.models.sub_category import SubCategory
from apps.operations.managers.categories import CategoryManager, CategoryQuerySet


class Category(TimeStampable):
    """
    Category model description
    """
    name = models.CharField(verbose_name=_("Category Name"), max_length=30)
    sub_categories = models.ManyToManyField(verbose_name=_("Sub Categories"), to=SubCategory)

    objects = CategoryManager.from_queryset(CategoryQuerySet)()

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        app_label = "operations"
        indexes = [models.Index(fields=["name"])]
        ordering = ("-id",)

    def __str__(self):
        return self.name
