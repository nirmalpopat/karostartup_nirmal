# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

import uuid

# lib imports
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

# project imports
from apps.accounts import constants
from apps.accounts.managers.verification_tokens import (
    VerificationTokenManager, VerificationTokenQueryset)
from utils.core.models import TimeStampable

USER = get_user_model()


def activation_token():
    """
    generate Activation token

    Returns:
        code [str]: 4 digit code

    Raise:
        None
    """
    return str(abs(hash(f"{uuid.uuid4()}")) % (10 ** 4))


class VerificationToken(TimeStampable):
    """
    VerificationToken Model use for storing user
    activation and verification tokens
    """

    token = models.CharField(
        verbose_name=_("Token"),
        max_length=4,
        default=activation_token,
        help_text=_("token that is used for verification"),
    )

    user = models.ForeignKey(
        verbose_name=_("User"),
        to=USER,
        related_name="user_verification_tokens",
        on_delete=models.CASCADE,
        help_text=_("User for which the verification token to created"),
    )

    token_type = models.CharField(
        verbose_name=_("Token Type"),
        choices=constants.TokenType.choices,
        default=constants.TokenType.WHATSAPP_TYPE,
        max_length=32,
        help_text=_("How this token is going to be used select from the choices"),
    )

    is_valid = models.BooleanField(
        verbose_name=_("Is Valid"),
        default=False,
        help_text=_("Weather the token is valid or not (True means valid)"),
    )

    number_attempts = models.PositiveIntegerField(
        verbose_name=_("Number Attempts"),
        default=0,
        help_text=_(
            "Max number for a token be valid are {}".format(constants.VALID_NUMBER_OF_ATTEMPTS)
        ),
    )

    objects = VerificationTokenManager.from_queryset(VerificationTokenQueryset)()

    class Meta:
        app_label = "accounts"
        verbose_name = _("Verification Token")
        verbose_name_plural = _("Verification Tokens")

    def __str__(self):
        return "token = {} & token_type = {} & username = {}".format(
            self.token, self.token_type, self.user.username
        )

