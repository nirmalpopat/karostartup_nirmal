# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import transaction
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

# project imports
from utils.permissions import IsAuthenticatedCompany, IsAuthenticatedStudent
from apps.accounts.models import StudentProfile, CompanyProfile
from apps.accounts.serializers.company_profile import CompanyProfileSerializer
from apps.accounts.serializers.student_profile import StudentProfileSerializer


class UserViewSet(ModelViewSet):

    def get_permissions(self):
        permissions = {
            "me": [IsAuthenticated, IsAuthenticatedStudent],
            "company": [IsAuthenticated, IsAuthenticatedCompany],
            "update_student": [IsAuthenticated, IsAuthenticatedStudent],
            "update_company": [IsAuthenticated, IsAuthenticatedCompany],
        }
        permission_classes = permissions.get(self.action, [IsAuthenticated])
        return [permission() for permission in permission_classes]

    serializer_classes = {
        "company": CompanyProfileSerializer,
        "me": StudentProfileSerializer,
        "update_company": CompanyProfileSerializer,
        "update_student": StudentProfileSerializer,
    }

    @action(methods=["GET"], detail=False, url_path="company")
    def company(self, request, **kwargs) -> Response:
        user_profile_entity = CompanyProfile.objects.get(user_id=request.user.id)
        serializer = self.get_serializer(user_profile_entity)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False, url_path="me")
    def me(self, request, **kwargs) -> Response:
        user_profile_entity = StudentProfile.objects.get(user_id=request.user.id)
        serializer = self.get_serializer(user_profile_entity)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=["PATCH"], detail=False, url_path="update/student")
    def update_student(self, request, **kwargs) -> Response:
        with transaction.atomic():
            serializer = self.get_serializer(request.user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

    @action(methods=["PATCH"], detail=False, url_path="update/company")
    def update_company(self, request, **kwargs) -> Response:
        with transaction.atomic():
            serializer = self.get_serializer(request.user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
