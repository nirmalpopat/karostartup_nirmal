# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework import routers

# project imports
from apps.accounts.apis.users import UserViewSet
from apps.accounts.apis.education import EducationViewSet
from apps.accounts.apis.verification_tokens import VerificationTokenViewSet


router = routers.SimpleRouter()
router.register("otp", VerificationTokenViewSet, basename="otp")
router.register("user", UserViewSet, basename="user")
router.register("education", EducationViewSet, basename="education")
urlpatterns = router.urls
