# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

from contextlib import suppress

# lib imports
from django.db import transaction
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ViewSet

# project imports
from apps.accounts import messages
from apps.accounts.models import Education
from apps.accounts.serializers.education import EducationSerializer


class EducationViewSet(ViewSet):
    model = Education
    serializer_class = EducationSerializer

    def get_permissions(self):
        permissions = {
            "create": [IsAuthenticated],
            "search_education": [IsAuthenticated],
        }
        permission_classes = permissions[self.action]
        return [permission() for permission in permission_classes]

    @action(methods=["GET"], detail=True)
    def retrieve(self, pk, request, **kwargs):
        return Response(status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False, url_path="search")
    def search(self, request, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def create(self, request):
        with transaction.atomic():
            return Response(status=status.HTTP_201_CREATED)

    def update(self, pk, request):
        with transaction.atomic():
            return Response(status=status.HTTP_201_CREATED)
