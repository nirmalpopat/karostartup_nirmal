# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models


class TimeStampableMixin(models.QuerySet):
    def filter_ids(self, ids: list):
        return self.filter(id__in=ids)

    def get_by_id(self, obj_id: int):
        return self.get(id=obj_id)

    def filter_is_active(self, is_active: bool = True):
        return self.filter(is_active=is_active)

    def filter_is_delete(self, is_deleted: bool = False):
        return self.filter(is_deleted=is_deleted)
