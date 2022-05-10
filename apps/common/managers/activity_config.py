# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models

# project imports
from utils.core.managers import TimeStampableMixin


class ActivityConfigQuerySet(TimeStampableMixin):
    def get_activity_name(self, activity_name):
        return self.get(activity_name=activity_name)

    def select_relate_email_template(self):
        return self.select_related("email_template")

    def select_relate_sms_template(self):
        return self.select_related("sms_template")

    def select_relate_push_template(self):
        return self.select_related("push_template")


class ActivityConfigManager(models.Manager):
    def get_queryset(self):
        return ActivityConfigQuerySet(self.model, using=self._db)
