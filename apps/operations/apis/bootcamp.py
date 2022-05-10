# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

from contextlib import suppress

# lib imports
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet

# project imports
from apps.operations import messages
from apps.operations.models import Bootcamp
from apps.operations.serializers.bootcamp import BootcampSerializer


class BootcampViewSet(ModelViewSet):
    model = Bootcamp
    serializer_class = BootcampSerializer
    queryset = Bootcamp.objects.all()
    http_method_names = ['get']