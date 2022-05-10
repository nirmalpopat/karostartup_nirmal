# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import transaction
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ViewSet

# project imports
from utils.permissions import IsAuthenticatedCompany, IsAuthenticatedStudent
from apps.operations.models import Post
from apps.operations.serializers.post import PostSerializer


class PostViewSet(ViewSet):
    model = Post
    serializer_class = PostSerializer

    def get_permissions(self) -> list:
        permissions = {
            "create": [AllowAny],
            "update": [IsAuthenticated, IsAuthenticatedCompany],
            "apply": [IsAuthenticated, IsAuthenticatedStudent],
            "my_application": [IsAuthenticated, IsAuthenticatedStudent],
            "list": [IsAuthenticated, IsAuthenticatedCompany]
        }
        permission_classes = permissions[self.action]
        return [permission() for permission in permission_classes]

    def create(self, request, **kwargs) -> Response:
        with transaction.atomic():
            serializer = self.serializer_class(request.user.id, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, pk, request, **kwargs) -> Response:
        return Response(status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False, url_path="search")
    def search(self, request, **kwargs) -> Response:
        return Response(status=status.HTTP_200_OK)

    def update(self, pk, request, **kwargs) -> Response:
        with transaction.atomic():
            return Response(status=status.HTTP_201_CREATED)

    @action(methods=["POST"], detail=False, url_path="apply")
    def apply(self, pk, request, **kwargs) -> Response:
        with transaction.atomic():
            return Response(status=status.HTTP_201_CREATED)

    def list(self, request, **kwargs) -> Response:
        return Response(status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False, url_path="list_applied")
    def list_applied(self, company_id, request, **kwargs) -> Response:
        with transaction.atomic():
            return Response(status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False, url_path="my_application")
    def my_application(self, request, **kwargs) -> Response:
        return Response(status=status.HTTP_200_OK)
