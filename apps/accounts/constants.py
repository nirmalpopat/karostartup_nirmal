# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db.models import TextChoices
from django.utils.translation import ugettext_lazy as _


class TokenType(TextChoices):
    SMS_TYPE = "SMS", _("sms")
    EMAIL_TYPE = "EMAIL", _("email"),
    WHATSAPP_TYPE = "WHATSAPP", _("whatsapp")


class UserTypeChoice(TextChoices):
    STUDENT = _("Student")
    COMPANY = _("Company")


class StudentProfileType(TextChoices):
    BOTH = _("Both")
    WORK_FROM_HOME = _("Work From Home")
    WORK_FROM_OFFICE = _("Work From Office")


class CompanyProfileType(TextChoices):
    PVT = _("Private Limited")
    NGO = _("Non Government Company")
    OPC = _("One Person Company")
    LLP = _("Limited Liability Partnership")
    GOVT = _("Government Company")
    PARTNERSHIP = _("Partnership")
    PROPRIETORSHIP = _("Proprietorship")


VALID_NUMBER_OF_ATTEMPTS = 3
