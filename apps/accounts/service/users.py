# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals
from contextlib import suppress

# lib imports
from phonenumbers import parse, format_number, PhoneNumberFormat
from phonenumbers.phonenumberutil import NumberParseException


def normalize_phone(phone: str) -> str:
    """Normalize phone number"""
    with suppress(NumberParseException):
        phone = parse(phone)
        return format_number(phone, PhoneNumberFormat.INTERNATIONAL)
    return ""
