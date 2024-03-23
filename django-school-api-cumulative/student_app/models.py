from django.db import models
from django.core import validators as v
from .validators import *

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=70, validators=[validate_name_format])
    student_email = models.EmailField(
        max_length=100, unique=True, validators=[validate_school_email])
    personal_email = models.EmailField(
        max_length=100, blank=True, null=True, unique=True)
    locker_number = models.PositiveIntegerField(default=110, unique=True, validators=[
                                                v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(
        default="12-12-12", max_length=10, validators=[validate_combination_format])
    good_student = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.student_email} - {self.locker_number}"

    def locker_reassignment(self, num: int) -> None:
        self.locker_number = num

    def student_status(self, new: bool) -> None:
        self.good_student = new
