from django.db import models
from django.core import validators as v
from .validators import *


class SwimRecord(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50)
    relay = models.BooleanField()
    stroke = models.CharField(max_length=50, validators=[validate_stroke])
    distance = models.IntegerField(validators=[v.MinValueValidator(50)])
    record_date = models.DateTimeField(validators=[validate_record_date])
    record_broken_date = models.DateTimeField(
        validators=[validate_record_broken_date])
