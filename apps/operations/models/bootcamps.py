# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# project imports
from utils.core.models import TimeStampable
from apps.operations.constants import ModeTypeChoice

from apps.operations.models.trainers import Trainer

class Bootcamp(TimeStampable):
    """
    Bootcamp Model
    """
    trainer = models.ForeignKey(verbose_name=_("Trainer"), to = Trainer, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=_("Image"), upload_to='bootcamps/')
    class_name = models.CharField(verbose_name=_("Class Name"), max_length=30)
    mode = models.CharField(verbose_name=_("Mode"), max_length=12, choices = ModeTypeChoice.choices)
    timing = models.DateTimeField(verbose_name=_("Timing"))
    outcome = models.TextField(verbose_name=_("What will you learn"))

    def __unicode__(self):
        return f"{self.trainer.full_name} - {self.class_name}"

    def __str__(self):
        return f"{self.trainer.full_name} - {self.class_name}"
