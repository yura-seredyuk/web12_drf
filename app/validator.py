from cgitb import text
from rest_framework import serializers
import re


class AddressValidator:
    message = "Validation error: "
    def __init__(self, message=None):
        self.validated_field = ''
        self.validated_data = None
        self.message = message or self.message

    def __call__(self, attrs):
        message = self.message
        text_pattern_en = re.compile('^[A-Za-z]+$')
        text_pattern_ua = re.compile('^[А-Ща-щЬьЮюЯяЇїІіЄєҐґ]+$')
        text_petern = re.compile('(^[A-Za-z]+$)||(^[А-Ща-щЬьЮюЯяЇїІіЄєҐґ]+$)')
        if 'appartaments' in attrs and attrs["appartaments"] <= 0:
            message = 'cannot be less or equal zero'
            self.raize_error(attrs, 'appartaments', message)
        if 'country' in attrs:
            if len(attrs["country"]) < 3:
                message = 'must consists with more then 2 characters'
                self.raize_error(attrs, 'country', message)
            elif not re.search(text_pattern_ua, attrs['country']) and\
                not re.search(text_pattern_en, attrs['country']):
                message = 'can contains only en or ua characters'
                self.raize_error(attrs, 'country', message)

    def raize_error(self, attrs, validated_field, message):
        message = self.message + f"The '{validated_field}' field {message}."
        self.validated_field = validated_field
        self.validated_data = attrs[validated_field]
        raise serializers.ValidationError(message, code=validated_field)

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.validated_field}={self.validated_data})>"