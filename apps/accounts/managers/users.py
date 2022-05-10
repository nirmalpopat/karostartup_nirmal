# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

# project imports
from utils.core.managers.timestampable import TimeStampableMixin


class UserQuerySet(TimeStampableMixin):

    """ Custom queryset filters for User model """

    def get_by_email(self, email: str):
        return self.get(email=email)

    def filter_email(self, email: str):
        return self.filter(email=email)

    def exists_by_email(self, email: str):
        return self.filter(email=email).exists()

    def get_by_phone(self, phone: str):
        return self.get(phone=phone)

    def exists_by_phone(self, phone: str):
        return self.filter(phone=phone).exists()

    def get_by_username(self, username: str):
        return self.get(username=username)

    def exists_by_username(self, username: str):
        return self.filter(username=username).exists()

    def filter_emails(self, emails: list):
        return self.filter(emails__in=emails)

    def filter_phones(self, phones: list):
        return self.filter(phones__in=phones)

    def exclude_staff(self):
        return self.exclude(is_staff=True)

    def exclude_staff_and_self(self, current_user):
        return self.exclude(models.Q(is_staff=True) | models.Q(id=current_user.id))


class UserManager(BaseUserManager):
    def create_user(
        self, phone, email=None, first_name=None, last_name=None, password=None, **extra_fields
    ):
        """
        Creates and saves a User with the given phone,
        password and name extra data
        """
        if not phone:
            raise ValueError(_("Users must have a valid phone number"))
        email = self.normalize_email(email).lower()
        if "username" not in extra_fields:
            extra_fields["username"] = phone
        user = self.model(
            phone=phone, email=email, first_name=first_name, last_name=last_name, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, first_name, last_name, password, email, **extra_fields):
        """
        Creates and saves a superuser with the given phone and password.
        """
        user = self.create_user(
            phone=phone,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

