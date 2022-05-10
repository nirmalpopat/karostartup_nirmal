# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampable(models.Model):
    """
    Record timestamps of a Content.
    * Model instance is never deleted, its marked as deleted with is_deleted.
    """

    create_date = models.DateTimeField(verbose_name=_("Created At"), auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name=_("Modified At"), auto_now=True)
    is_deleted = models.BooleanField(verbose_name=_("Is Instance marked deleted"), default=False)
    is_active = models.BooleanField(verbose_name=_("Is Instance marked Active"), default=True)
    extra_data = models.JSONField(verbose_name=_("Extra Data"), default=dict, blank=True, null=True)

    class Meta:
        abstract = True
