from django.db import models
from .validators import *

# Create your models here.


class Subject(models.Model):
    subject_name = models.CharField(max_length=100, unique=True, validators=[
                                    validate_subject_format])
    professor = models.CharField(
        max_length=50, default="Mr. Cahan", validators=[validate_professor_name])
    # students = related_name field from m2m relationship

    def __str__(self) -> str:
        return f'{self.subject_name} - {self.professor} - {self.students.count()}'

    def add_a_student(self, student_id: int) -> None:
        error_message = "This subject is full!"
        if self.students.count() > 30:
            raise Exception(error_message)
        else:
            self.students.add(student_id)

    def drop_a_student(self, student_id: int) -> None:
        error_message = "This subject is empty!"
        if self.students.count() < 1:
            raise Exception(error_message)
        else:
            self.students.remove(student_id)
