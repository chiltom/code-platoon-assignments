from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators as v

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(
        max_length=255, unique=True, verbose_name='email address')
    age = models.PositiveIntegerField(
        default=18, validators=[v.MinValueValidator(18), v.MaxValueValidator(110)])
    display_name = models.CharField(max_length=25, unique=True, validators=[
                                    v.MinLengthValidator(6)])
    address = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
