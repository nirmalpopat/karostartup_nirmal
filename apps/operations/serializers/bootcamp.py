# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework import serializers

# project imports
from apps.operations.models import Bootcamp, Trainer

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"

        datetime_fields = ("create_date", "modified_date")

class BootcampSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(TrainerSerializer)
    class Meta:
        model = Bootcamp
        fields = "__all__"
        
        # print(fields)
        datetime_fields = ("create_date", "modified_date")