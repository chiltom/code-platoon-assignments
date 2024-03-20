from django.core.exceptions import ValidationError
import re


def validate_name_format(name: str) -> str:
    error_message = 'Name must be in the format "First Middle Initial. Last"'
    regex = r'^([A-Z][a-z]+)\s([A-Z][.]+)\s([A-Z][a-z]+)$'
    good_name = re.match(regex, name)
    if good_name:
        return name
    raise ValidationError(error_message, params={'name': name})


def validate_school_email(email: str) -> str:
    error_message = 'Invalid school email format. Please use an email ending with "@school.com".'
    regex = r'^([\w.-]+)@(school.com)'
    good_email = re.match(regex, email)
    if good_email:
        return email
    raise ValidationError(error_message, params={'email': email})


def validate_combination_format(combination: str) -> str:
    error_message = 'Combination must be in the format "12-12-12"'
    regex = r'^[0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]'
    good_combo = re.match(regex, combination)
    if good_combo:
        return combination
    raise ValidationError(error_message, params={'combination': combination})
