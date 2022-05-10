# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

# project imports
from apps.accounts import messages
from apps.accounts.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        extra_kwargs = {"password": {"write_only": True}}
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "phone",
            "date_joined",
            "password",
        )
        read_only_fields = (
            "id",
            "is_superuser",
            "is_deleted",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions",
        )
        datetime_fields = ("create_date", "modified_date")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {"password": {"write_only": True}}
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "phone",
            "date_joined",
            "password",
        )
        read_only_fields = (
            "id",
            "is_superuser",
            "is_superuser",
            "is_deleted",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions",
        )
        datetime_fields = ("create_date", "modified_date")

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        if validated_data["password"]:
            user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.username = validated_data.get("username", instance.username)
        instance.phone = validated_data.get("phone", instance.phone)
        password = validated_data.pop("password", None)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class LoginSerializers(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        max_length=128,
        write_only=True,
    )

    def validate(self, data):
        username = data.get("email")
        password = data.get("password")

        if username and password:
            user = authenticate(
                request=self.context.get("request"), username=username, password=password
            )
            if not user:
                msg = messages.INVALID_CREDENTIALS
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = messages.USERNAME_PASS_NULL
            raise serializers.ValidationError(msg, code="authorization")

        data["user"] = user
        return data
