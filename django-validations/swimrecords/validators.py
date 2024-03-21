from django.core.exceptions import ValidationError
from django.utils import timezone
import re


def validate_stroke(stroke: str) -> str:
    error_message = f'{stroke} is not a valid stroke'
    if stroke in ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']:
        return stroke
    raise ValidationError(error_message, params={'stroke': stroke})


def validate_record_date(record_date):
    error_message = "Can't set record in the future."
    if record_date <= timezone.now():
        return record_date
    raise ValidationError(error_message, params={'record_date': record_date})


def validate_record_broken_date(date):
    error_message = "Can't break record before record was set."
    if date > timezone.now():
        return date
    raise ValidationError(error_message, params={'record_broken_date': date})
