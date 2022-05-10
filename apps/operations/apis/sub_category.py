# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet

# project imports
from apps.operations.models import SubCategory
from apps.operations.serializers.sub_category import SubCategorySerializer


class SubCategoryViewSet(ViewSet):
    model = SubCategory
    serializer_class = SubCategorySerializer

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
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, **kwargs) -> Response:
        return Response(status=status.HTTP_200_OK)
