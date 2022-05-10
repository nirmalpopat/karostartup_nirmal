# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework import routers

# project imports
from apps.common.apis.device_token import DeviceTokenViewSet
from apps.common.apis.notifications import NotificationViewSet


router = routers.SimpleRouter()
router.register("notifications", NotificationViewSet, basename="notifications")
router.register("device_register", DeviceTokenViewSet, basename="device-token")
urlpatterns = router.urls
