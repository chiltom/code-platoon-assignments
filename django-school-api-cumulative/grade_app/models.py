from django.db import models
from django.core import validators as v
from student_app.models import Subject, Student

# Create your models here.


class Grade(models.Model):
    grade = models.DecimalField(max_digits=5, decimal_places=2, default=100.00, validators=[
                                v.MinValueValidator(0.00), v.MaxValueValidator(100.00)])
    a_subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, blank=True, null=True, related_name="grades")
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, blank=True, null=True, related_name="grades")

    def __str__(self) -> str:
        return f"{self.student} - {self.a_subject} - {self.grade}"
