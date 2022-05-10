# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import transaction
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token

# project imports
from utils.whatsapp_gateway import whatsapp_send_message
from utils.core.exceptions import BadRequestException
from apps.accounts.service import users as user_service
from apps.accounts.constants import UserTypeChoice
from apps.accounts.models import User, VerificationToken, StudentProfile, CompanyProfile
from apps.common.models import ActivityConfig
from apps.common.constants import ActivityChoice
from apps.accounts import constants


class VerificationTokenViewSet(ModelViewSet):
    model = VerificationToken

    def get_permissions(self):
        permissions = {
            "request_otp": [AllowAny],
            "verify_otp": [AllowAny],
            "verify_profile": [IsAuthenticated]
        }
        permission_classes = permissions[self.action]
        return [permission() for permission in permission_classes]

    @action(methods=["POST"], detail=False, url_path="request_otp")
    def request_otp(self, request, **kwargs):
        phone, user_type = request.data.get("phone"), str(request.data.get("user_type")).capitalize()
        if user_type not in (UserTypeChoice.COMPANY, UserTypeChoice.STUDENT):
            raise BadRequestException("user type invalid or not received")
        if not phone:
            raise BadRequestException("Phone number not received")
        phone = user_service.normalize_phone(phone)
        with transaction.atomic():
            try:
                user_entity = User.objects.get(Q(phone=phone) | Q(whatsapp_phone_number=phone))
            except User.DoesNotExist:
                user_entity = User.objects.create_user(phone=phone, user_type=user_type)
            if user_type == UserTypeChoice.COMPANY:
                if not CompanyProfile.objects.filter(user_id=user_entity.pk).exists():
                    CompanyProfile.objects.create(user_id=user_entity.pk)
            elif user_type == UserTypeChoice.STUDENT:
                if not StudentProfile.objects.filter(user_id=user_entity.pk).exists():
                    StudentProfile.objects.create(user_id=user_entity.pk)
            otp_request = self.model.objects.create(user_id=user_entity.pk, is_valid=True)
            activity_config_entity = ActivityConfig.objects.get(activity_name=ActivityChoice.OTP_TRIGGER)
            body = activity_config_entity.whatsapp_template.format(otp=otp_request.token)
            whatsapp_send_message(body=body, to=phone)
            return Response(data={"message": "otp sent successfully"}, status=status.HTTP_201_CREATED)

    @action(methods=["POST"], detail=False, url_path="verify_otp")
    def verify_otp(self, request, **kwargs):
        phone, otp = request.data.get("phone"), request.data.get("otp")
        if not (phone or otp):
            raise BadRequestException("phone/otp not received")
        phone = user_service.normalize_phone(phone)
        try:
            user_entity = User.objects.get(Q(phone=phone) | Q(whatsapp_phone_number=phone))
        except User.DoesNotExist:
            raise BadRequestException("User not registered")
        verification_token_entity = self.model.objects.filter_user(
            user_id=user_entity.pk).filter_valid().last()
        if verification_token_entity:
            verification_token_entity.number_attempts = verification_token_entity.number_attempts + 1
            if (verification_token_entity.token == otp
                    or verification_token_entity.number_attempts == constants.VALID_NUMBER_OF_ATTEMPTS):
                verification_token_entity.is_valid = False
                token, created = Token.objects.get_or_create(user=user_entity)
                return Response({
                    "user_type": user_entity.user_type,
                    "token": token.key
                }, status=status.HTTP_200_OK)
            verification_token_entity.save()
        raise BadRequestException("Invalid/Expired Token")

    @action(methods=["POST"], detail=False, url_path="request_verify_profile")
    def request_verify_profile(self, request, **kwargs):
        verification_type = request.deta.get("type")
        if verification_type not in ["email", "whatsapp_phone_number", "phone"]:
            BadRequestException("Verification_type invalid or not received")
        with transaction.atomic():
            otp_request = self.model.objects.create(user_id=request.user.id, is_valid=True, extra_data={
                "type": verification_type})
            activity_config_entity = ActivityConfig.objects.get(activity_name=ActivityChoice.OTP_TRIGGER)
            if verification_type == "whatsapp_phone_number":
                body = activity_config_entity.whatsapp_template.format(otp=otp_request.token)
                whatsapp_send_message(body=body.whatsapp_template, to=request.user.whatsapp_phone_number)
            if verification_type == "email":
                body = activity_config_entity.email_template.format(otp=otp_request.token)
                # todo: Add ses gateway
            if verification_type == "phone":
                body = activity_config_entity.sms_template.format(otp=otp_request.token)
                # todo: add sns gateway
        return Response(data={"message": "otp sent successfully"}, status=status.HTTP_201_CREATED)

    @action(methods=["POST"], detail=False, url_path="verify_profile")
    def verify_profile(self, request, **kwargs):
        verification_type, otp = request.deta.get("type"), request.deta.get("otp")
        if verification_type not in ["email", "whatsapp_phone_number", "phone"]:
            BadRequestException("Verification_type invalid or not received")
        verification_token_entity = self.model.objects.filter_user(
            user_id=request.user.id).filter_valid().filter(data__type=verification_type)
        if verification_token_entity:
            verification_token_entity.number_attempts = verification_token_entity.number_attempts + 1
            if (verification_token_entity.token == otp
                    or verification_token_entity.number_attempts == constants.VALID_NUMBER_OF_ATTEMPTS):
                verification_token_entity.is_valid = False
                user_entity = User.objects.get(pk=request.user.id)
                if verification_type == "email":
                    user_entity.is_email_verified = True
                elif verification_type == "whatsapp_phone_number":
                    user_entity.is_whatsapp_phone_number_verified = True
                elif verification_type == "phone":
                    user_entity.is_phone_verified = True
                verification_token_entity.save()
        return Response(data={"message": f"{verification_type} verified successfully"}, status=status.HTTP_201_CREATED)

