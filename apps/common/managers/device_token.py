# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# lib imports
from django.db import models
from utils.core.managers import TimeStampableMixin


class DeviceTokenQueryset(TimeStampableMixin):
    def filter_device_type(self, device_type):
        return self.filter(device_type=device_type)

    def filter_user_id(self, user_id):
        return self.filter(user_id=user_id)

    def select_relate_user(self):
        return self.select_related("user")


class DeviceTokenManager(models.Manager):
    def get_queryset(self):
        return DeviceTokenQueryset(self.model, using=self._db)
