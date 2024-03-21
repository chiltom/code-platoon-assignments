from django.core.exceptions import ValidationError
import re


def validate_subject_format(subject_name: str) -> str:
    error_message = 'Subject must be in title case format.'
    regex = r'^[A-Z][a-z0-9]+$'
    good_name = re.match(regex, subject_name)
    if good_name:
        return subject_name
    raise ValidationError(error_message, params={'subject_name': subject_name})


def validate_professor_name(professor: str) -> str:
    error_message = 'Professor name must be in the format "Professor Adam".'
    regex = r'^Professor [A-Z][a-z]*$'
    good_name = re.match(regex, professor)
    if good_name:
        return professor
    raise ValidationError(error_message, params={'professor': professor})
