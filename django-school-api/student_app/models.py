from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=100)
    personal_email = models.EmailField(max_length=100, null=True)
    locker_number = models.IntegerField(default=1)
    locker_combination = models.CharField(max_length=8)
    good_student = models.BooleanField(default=True)
