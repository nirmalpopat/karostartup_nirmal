# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework import routers

# project imports
from apps.operations.apis.sub_category import SubCategoryViewSet
from apps.operations.apis.categories import CategoryViewSet
from apps.operations.apis.post import PostViewSet
from apps.operations.apis.bootcamp import BootcampViewSet


router = routers.SimpleRouter()
router.register("subcategory", SubCategoryViewSet, basename="subcategory")
router.register("category", CategoryViewSet, basename="category")
router.register("post", PostViewSet, basename="post")
router.register("bootcamp", BootcampViewSet, basename="bootcamp")
urlpatterns = router.urls
