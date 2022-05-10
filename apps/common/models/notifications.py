# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

# Project imports
from apps.common import constants
from apps.common.managers.notifications import (NotificationManager,
                                               NotificationQueryset)
from utils.core.models import TimeStampable

USER = get_user_model()


class Notification(TimeStampable):
    """
    Description of Notification Model
    """

    user = models.ForeignKey(
        verbose_name=_("User"), to=USER, on_delete=models.CASCADE, related_name="user_notifications"
    )
    subject = models.TextField(verbose_name=_("Notification Subject"))
    notification = models.TextField(verbose_name=_("Notification"), max_length=256)
    notification_type = models.CharField(
        verbose_name=_("Type of notification"),
        choices=constants.NotificationTypeChoice.choices,
        default=constants.NotificationTypeChoice.PUSH,
        max_length=32,
    )

    objects = NotificationManager.from_queryset(NotificationQueryset)()

    class Meta:
        app_label = "common"
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
        indexes = [models.Index(fields=["notification_type"])]

    def __str__(self):
        return f"{self.id} - {self.user_id}"

    def __unicode__(self):
        return f"{self.id} - {self.user_id}"
