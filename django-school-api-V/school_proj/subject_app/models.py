from django.db import models
from django.core import validators as v
from .validators import *
from student_app.models import Student

# Create your models here.


class Subject(models.Model):
    subject_name = models.CharField(max_length=75, validators=[
                                    validate_subject_format])
    professor = models.CharField(max_length=60, validators=[
                                 validate_professor_name])
    students = models.ManyToManyField(Student, related_name='subjects')

    def __str__(self):
        return f"{self.subject_name} - {self.professor} - {self.students.count()}"

    def add_a_student(self, student_id):
        error_message = 'This subject is full!'
        if self.students.count() >= 31:
            raise Exception(error_message)
        else:
            self.students.add(student_id)

    def drop_a_student(self, student_id):
        error_message = 'This subject is empty!'
        if self.students.count() <= 0:
            raise Exception(error_message)
        else:
            self.students.remove(student_id)
