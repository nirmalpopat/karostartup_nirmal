# # -*- coding: utf-8 -*-
# # python imports
# from __future__ import unicode_literals
#
# from contextlib import suppress
#
# # lib imports
# from django.db import transaction
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.viewsets import ViewSet
#
# # project imports
# from apps.accounts import messages
# from apps.accounts.models import CompanyProfile
# from apps.accounts.serializers.company_profile import CompanyProfileSerializer
#
#
# class CompanyProfileViewSet(ViewSet):
#     model = CompanyProfile
#     serializer_class = CompanyProfileSerializer
#
#     def get_permissions(self):
#         permissions = {
#             "create": [AllowAny],
#             "me": [IsAuthenticated],
#         }
#         permission_classes = permissions[self.action]
#         return [permission() for permission in permission_classes]
#
#     def create(self, request, **kwargs):
#         with transaction.atomic():
#             serializer = self.serializer_class(request.user.id, data=request.data, partial=True)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             data = {"detail": messages.DEVICE_REGISTERED, "data": serializer.data}
#             return Response(data=data, status=status.HTTP_201_CREATED)
#
#     def me(self, request, **kwargs):
#
#         return Response(data=data, status=status.HTTP_200_OK)
#
#
#
#
