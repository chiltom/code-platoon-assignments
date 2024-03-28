from django.db import models
from django.core import validators as v
from user_app.models import User

# Create your models here.


class List(models.Model):
    # id linked to tasks by fk, one-to-many relationship
    list_name = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"List: {self.list_name}"


class Task(models.Model):
    # id linked to subtasks by fk, one-to-many relationship
    task_name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    parent_list = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self) -> str:
        return f"Task: {self.task_name}"


class Sub_Task(models.Model):
    sub_task_name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    parent_task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="sub_tasks")

    def __str__(self) -> str:
        return f"Sub_Task: {self.sub_task_name}"
