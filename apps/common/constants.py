# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db.models import TextChoices
from django.utils.translation import ugettext_lazy as _


class DeviceTypeChoice(TextChoices):
    ANDROID = _("Android")
    IPHONE = _("IPhone")
    WEBSITE = _("Website")


class NotificationTypeChoice(TextChoices):
    EMAIL = _("Email Notification")
    SMS = _("SMS Notification")
    PUSH = _("Push Notification")
    WHATSAPP = _("Whatsapp Notification")


class ActivityChoice(TextChoices):
    OTP_TRIGGER = _("Accounts User OTP")
    ACCOUNT_USER_LOGIN_OTP = _("Accounts User Login OTP")
