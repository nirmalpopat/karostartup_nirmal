# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models

# project imports
from apps.accounts.constants import VALID_NUMBER_OF_ATTEMPTS


class VerificationTokenQueryset(models.QuerySet):
    def filter_valid(self):
        return self.filter(is_valid=True)

    def filter_user(self, user_id):
        return self.filter(user_id=user_id)

    def filter_token_type(self, token_type):
        return self.filter(token_type=token_type)


class VerificationTokenManager(models.Manager):
    def get_queryset(self):
        return VerificationTokenQueryset(self.model, using=self._db)
