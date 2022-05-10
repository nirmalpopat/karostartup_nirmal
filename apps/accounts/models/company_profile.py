# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals
import uuid


# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# project imports
from utils.core.models import TimeStampable
from apps.accounts.constants import CompanyProfileType
from apps.accounts.managers.company_profile import CompanyProfileManager, CompanyProfileQueryset


USER = get_user_model()


def upload_to(instance, filename):
    path = f"company/images/upload/"
    try:
        ext = filename.split(".")[-1]
    except IndexError:
        ext = filename
    filename = path + "{}{}.{}".format(filename, uuid.uuid4().hex, ext)
    return filename


class CompanyProfile(TimeStampable):
    user = models.OneToOneField(to=USER, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_user")
    name = models.CharField(verbose_name=_("Company Name"), max_length=64, blank=True, null=True)
    photo = models.ImageField(verbose_name=_("Profile Photo"), upload_to=upload_to, blank=True, null=True)
    type = models.CharField(verbose_name=_("Company Type"), choices=CompanyProfileType.choices, max_length=64, blank=True, null=True)
    address_line_1 = models.CharField(verbose_name=_("Address Line 1"), max_length=64, blank=True, null=True)
    address_line_2 = models.CharField(verbose_name=_("Address Line 2"), max_length=64, blank=True, null=True)
    city = models.CharField(verbose_name=_("City"), max_length=64, blank=True, null=True)
    state = models.CharField(verbose_name=_("State"), max_length=64, blank=True, null=True)
    pin_code = models.CharField(verbose_name=_("Pin Code"), max_length=12, blank=True, null=True)
    is_verified = models.BooleanField(verbose_name=_("Is Verified"), default=False, blank=True, null=True)
    verified_by = models.ForeignKey(verbose_name=_("Verified By"), to=USER, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_verified_by", editable=False, blank=True, null=True,)
    verified_at = models.DateTimeField(verbose_name=_("Verified At"), blank=True, null=True, editable=False)

    objects = CompanyProfileManager.from_queryset(CompanyProfileQueryset)()

    class Meta:
        verbose_name = _("Company Profile")
        verbose_name_plural = _("Company Profiles")
        indexes = [models.Index(fields=["name"])]
        app_label = "accounts"
        ordering = ("-id",)

    def __str__(self):
        return self.name
