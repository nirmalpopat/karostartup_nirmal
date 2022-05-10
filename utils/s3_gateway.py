# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"


class MediaStorage(S3Boto3Storage):
    location = "media"
    default_acl = "public-read"
