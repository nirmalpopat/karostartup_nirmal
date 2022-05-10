# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# project imports
from apps.accounts.constants import UserTypeChoice
from apps.accounts.managers.users import UserManager, UserQuerySet


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model description
    """
    email = models.EmailField(
        verbose_name=_("Email address"), max_length=256, null=True, blank=True
    )
    is_email_verified = models.BooleanField(verbose_name=_("is email verified"), default=False)
    whatsapp_phone_number = models.CharField(verbose_name=_("Whatsapp phone number"), max_length=10, unique=True, blank=True, null=True)
    is_whatsapp_phone_number_verified = models.BooleanField(verbose_name=_("is whatsapp phone number verified"), default=False)

    user_type = models.CharField(verbose_name=_("User type"), choices=UserTypeChoice.choices, max_length=10)
    username = models.CharField(verbose_name=_("Username"), max_length=256, unique=True)
    phone = models.CharField(verbose_name=_("Phone"), max_length=128, unique=True)
    is_phone_verified = models.BooleanField(verbose_name=_("is phone verified"), default=False)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=128, null=True, blank=True)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=128, null=True, blank=True)
    is_staff = models.BooleanField(
        verbose_name=_("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user \
            can log into this admin site."
        ),
    )
    is_superuser = models.BooleanField(verbose_name=_("Is Superuser"), default=False)
    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True,
        help_text=_(
            "Designates whether this user \
            should be treated as active. \
            Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(verbose_name=_("date joined"), default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone", "email"]

    objects = UserManager.from_queryset(UserQuerySet)()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        app_label = "accounts"
        indexes = [models.Index(fields=["email", "username", "phone"])]
        ordering = ("-id",)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __unicode__(self):
        return f"{self.username} - {self.full_name}"

    def __str__(self):
        return f"{self.username} - {self.full_name}"

    @property
    def is_student(self):
        if self.user_type == UserTypeChoice.STUDENT:
            return True
        return False

    @property
    def is_company(self):
        if self.user_type == UserTypeChoice.COMPANY:
            return True
        return False


