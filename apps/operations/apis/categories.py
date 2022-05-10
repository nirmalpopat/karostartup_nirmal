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

# project imports
from apps.operations import messages
from apps.operations.models import Category
from apps.operations.serializers.categories import CategorySerializer


class CategoryViewSet(ViewSet):
    model = Category
    serializer_class = CategorySerializer

    def get_permissions(self):
        permissions = {
            "create": [AllowAny],
        }
        permission_classes = permissions[self.action]
        return [permission() for permission in permission_classes]

    def create(self, request, **kwargs) -> Response:
        with transaction.atomic():
            serializer = self.serializer_class(request.user.id, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = {"detail": messages.DEVICE_REGISTERED, "data": serializer.data}
            return Response(data=data, status=status.HTTP_201_CREATED)

    def list(self, request, **kwargs) -> Response:
        return Response(status=status.HTTP_200_OK)
