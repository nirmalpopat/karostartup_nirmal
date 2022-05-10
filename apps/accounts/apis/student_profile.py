# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

from contextlib import suppress

# lib imports
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ViewSet

# project imports
from apps.accounts import messages
from apps.accounts.models import StudentProfile
from apps.accounts.serializers.education import StudentProfileSerializer


class StudentProfileViewSet(ViewSet):
    model = StudentProfile
    serializer_class = StudentProfileSerializer

    def get_permissions(self):
        permissions = {
            "create": [AllowAny],
            "me": [IsAuthenticated],
        }
        permission_classes = permissions[self.action]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, **kwargs):
        return Response(data=data, status=status.HTTP_200_OK)




