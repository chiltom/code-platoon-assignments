from django.db import models
from django.core import validators as v
from .validators import *
from subject_app.models import Subject

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
    subjects = models.ManyToManyField(Subject, related_name="students")

    def __str__(self) -> str:
        return f"{self.name} - {self.student_email} - {self.locker_number}"

    def locker_reassignment(self, num: int) -> None:
        self.locker_number = num

    def student_status(self, new: bool) -> None:
        self.good_student = new

    def add_subject(self, subject_id: int) -> None:
        error_message = 'This students class schedule is full!'
        if self.subjects.count() > 7:
            raise Exception(error_message)
        else:
            self.subjects.add(subject_id)

    def remove_subject(self, subject_id: int) -> None:
        error_message = 'This students class schedule is empty!'
        if self.subjects.count() < 1:
            raise Exception(error_message)
        else:
            self.subjects.remove(subject_id)
