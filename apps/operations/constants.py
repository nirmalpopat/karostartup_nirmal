# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db.models import TextChoices
from django.utils.translation import ugettext_lazy as _


class ModeTypeChoice(TextChoices):
    FREE = _("Free")
    PAID = _("Paid")