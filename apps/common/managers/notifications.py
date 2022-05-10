# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models

from utils.core.managers import TimeStampableMixin


class NotificationQueryset(TimeStampableMixin):
    def filter_by_user_and_type(self, user_id: int, notification_type: str = "PUSH"):
        return self.filter(user_id=user_id, notification_type=notification_type)

    def select_relate_user(self):
        return self.select_related("user")

    def get_by_id_type_user(self, pk: int, user_id: int, notification_type: int):
        return self.get(pk=pk, user_id=user_id, notification_type=notification_type)


class NotificationManager(models.Manager):
    def get_queryset(self):
        return NotificationQueryset(self.model, using=self._db)
