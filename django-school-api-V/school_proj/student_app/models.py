from django.db import models
from django.core import validators as v
from .validators import *

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=255, validators=[validate_name_format])
    student_email = models.EmailField(
        unique=True, validators=[validate_school_email])
    personal_email = models.EmailField(null=True, blank=True, unique=True)
    locker_number = models.IntegerField(
        default=110, unique=True, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(
        default="12-12-12", max_length=255, validators=[validate_combination_format])
    good_student = models.BooleanField(default=True)

    def add_subject(self, subject_id):
        error_message = 'This students class schedule is full!'
        if self.subjects.count() >= 8:
            raise Exception(error_message)
        else:
            self.subjects.add(subject_id)

    def remove_subject(self, subject_id):
        error_message = 'This students class schedule is empty!'
        if self.subjects.count() <= 0:
            raise Exception(error_message)
        else:
            self.subjects.remove(subject_id)
