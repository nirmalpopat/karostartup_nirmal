# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

from contextlib import suppress

# lib imports
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

# project imports
from apps.common.models import Notification
from utils.core.exceptions import BadRequestException
from apps.common.constants import NotificationTypeChoice
from apps.common.serializers.notifications import NotificationSerializer


class NotificationViewSet(ModelViewSet):
    model = Notification
    serializer_class = NotificationSerializer

    def get_permissions(self) -> list:
        permissions = {
            "list": [IsAuthenticated],
            "create": [IsAuthenticated],
            "retrieve": [IsAuthenticated]
        }
        permission_classes = permissions[self.action]
        return [permission() for permission in permission_classes]

    def list(self, request, **kwargs) -> Response:
        notification_entities = self.model.objects.filter(
            user_id=request.user.id,
            notification_type=NotificationTypeChoice.PUSH
        )
        serializer = self.serializer_class(notification_entities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, pk: int, request) -> Response:
        notification_entities = self.model.objects.get(
            pk=pk,
            user_id=request.user.id,
            notification_type=NotificationTypeChoice.PUSH
        )
        serializer = self.serializer_class(notification_entities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, pk: int, request) -> Response:
        with transaction.atomic():
            self.model.objects.filter(
                pk=pk,
                user_id=request.user.id,
                notification_type=NotificationTypeChoice.PUSH
            ).delete()
            return Response(
                data={"message": "notification deleted successfully"},
                status=status.HTTP_202_ACCEPTED
            )


