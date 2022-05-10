
# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# project imports
from apps.common.constants import ActivityChoice
from apps.common.managers.activity_config import (ActivityConfigManager,
                                                  ActivityConfigQuerySet)
from utils.core.models import TimeStampable

from .notification_templates import NotificationTemplate


class ActivityConfig(TimeStampable):
    """
    Description of ActivityConfig Model
    """

    activity_name = models.CharField(
        verbose_name=_("Activity Name"),
        max_length=64,
        choices=ActivityChoice.choices,
        unique=True,
    )

    email_template = models.ForeignKey(
        to=NotificationTemplate,
        on_delete=models.CASCADE,
        verbose_name=_("Email Template"),
        related_name="email_template_activity_configs",
        null=True,
        blank=True,
    )

    sms_template = models.ForeignKey(
        to=NotificationTemplate,
        on_delete=models.CASCADE,
        verbose_name=_("SMS Template"),
        related_name="sms_template_activity_configs",
        null=True,
        blank=True,
    )
    push_template = models.ForeignKey(
        to=NotificationTemplate,
        on_delete=models.CASCADE,
        verbose_name=_("Push Template"),
        related_name="push_template_activity_configs",
        null=True,
        blank=True,
    )
    whatsapp_template = models.ForeignKey(
        to=NotificationTemplate,
        on_delete=models.CASCADE,
        verbose_name=_("Whatsapp Template"),
        related_name="whatsapp_template_activity_configs",
        null=True,
        blank=True,
    )

    objects = ActivityConfigManager.from_queryset(ActivityConfigQuerySet)()

    class Meta:
        app_label = "common"
        verbose_name = _("Activity Config")
        verbose_name_plural = _("Activity Configs")

    def __unicode__(self):
        return self.activity_name

    def __str__(self):
        return self.activity_name
