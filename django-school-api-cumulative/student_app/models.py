from django.db import models
from django.core import validators as v

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=70)
    student_email = models.EmailField(max_length=100)
    personal_email = models.EmailField(max_length=100, blank=True, null=True)
    locker_number = models.PositiveIntegerField(default=110)
    locker_combination = models.CharField(default="12-12-12", max_length=8)
    good_student = models.BooleanField(default=True)
