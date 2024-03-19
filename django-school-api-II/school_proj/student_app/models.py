from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=255)
    student_email = models.EmailField(unique=True)
    personal_email = models.EmailField(null=True, blank=True, unique=True)
    locker_number = models.IntegerField(
        default=110, unique=True)
    locker_combination = models.CharField(
        max_length=255, default="12-12-12")
    good_student = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.student_email} - {self.locker_number}"

    def locker_reassignment(self, num: int) -> None:
        self.locker_number = num
        self.save()

    def student_status(self, new: bool) -> bool:
        self.good_student = new
        self.save()
