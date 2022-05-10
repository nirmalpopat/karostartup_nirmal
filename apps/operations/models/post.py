# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

import uuid

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# import base models from utils
from utils.core.models import TimeStampable

# project imports
from .categories import Category
from apps.operations.managers.post import PostManager, PostQuerySet

USER = get_user_model()


def upload_to(instance, filename):
    path = f"posts/images/"
    try:
        ext = filename.split(".")[-1]
    except IndexError:
        ext = filename
    filename = path + "{}{}.{}".format(filename, uuid.uuid4().hex, ext)
    return filename


class Post(TimeStampable):
    user = models.ForeignKey(verbose_name=_("User"), to=USER, on_delete=models.CASCADE)
    categories = models.ManyToManyField(verbose_name=_("Categories"), to=Category)
    is_internship = models.BooleanField(verbose_name=_("Is Internship"), default=False)
    is_part_time = models.BooleanField(verbose_name=_("Is Part Time"), default=False)
    title = models.CharField(verbose_name=_("Title"), max_length=30)
    image = models.ImageField(verbose_name=_("Image"), upload_to=upload_to)
    opening_count = models.IntegerField(verbose_name=_("Opening Count"), blank=True, null=True)
    is_work_from_home = models.BooleanField(verbose_name=_("Is Work From Home"), default=False)
    description = models.TextField(verbose_name=_("Description"))
    compensation = models.IntegerField(verbose_name=_("Compensation"))
    working_days = models.IntegerField(verbose_name=_("Working Days"))
    working_hours = models.IntegerField(verbose_name=_("Working Hours"))
    address_line_2 = models.CharField(verbose_name=_("Address Line 2"), max_length=64, blank=True, null=True)
    city = models.CharField(verbose_name=_("City"), max_length=64, blank=True, null=True)
    state = models.CharField(verbose_name=_("State"), max_length=64, blank=True, null=True)
    pin_code = models.CharField(verbose_name=_("Pin Code"), max_length=12, blank=True, null=True)

    objects = PostManager.from_queryset(PostQuerySet)()

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        app_label = "operations"
        indexes = [models.Index(fields=["title"])]
        ordering = ("-id",)

    def __str__(self):
        return self.title


