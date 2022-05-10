# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# project imports
from utils.core.models import TimeStampable


class Trainer(TimeStampable):
    """
    Trainer Model who give speech in bootcamp
    """
    first_name = models.CharField(verbose_name=_("First Name"), max_length=24)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=24)
    photo = models.ImageField(verbose_name=_("Profile Photo"), upload_to='trainers/', blank=True, null=True)
    description = models.TextField(_("Description"))
    
    class Meta:
        app_label = "operations"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __unicode__(self):
        return f"{self.first_name} - {self.last_name}"

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"