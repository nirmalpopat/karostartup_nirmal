# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# project imports
from apps.common import constants
from apps.common.managers.notification_templates import (
    NotificationTemplateManager, NotificationTemplateQuerySet)
from utils.core.models import TimeStampable


class NotificationTemplate(TimeStampable):
    """
    Description of NotificationTemplate Model
    """

    name = models.CharField(verbose_name=_("Notification template name"), max_length=64)
    notification_type = models.CharField(
        verbose_name=_("Notification Type"),
        max_length=24,
        choices=constants.NotificationTypeChoice.choices,
    )
    subject = models.TextField(verbose_name=_("Notification Subject"))
    content = models.TextField(verbose_name=_("Notification Content"))

    objects = NotificationTemplateManager.from_queryset(NotificationTemplateQuerySet)()

    class Meta:
        app_label = "common"
        verbose_name = _("Notification Template")
        verbose_name_plural = _("Notification Templates")
        indexes = [models.Index(fields=["notification_type"])]

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
