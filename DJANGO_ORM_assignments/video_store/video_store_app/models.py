from django.db import models

# Create your models here.


class Client(models.Model):
    account_type = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, unique=True)
    active = models.BooleanField(default=True)


class Video(models.Model):
    title = models.CharField(max_length=50, unique=True)
    in_stock = models.IntegerField(default=1)
    rating = models.CharField(max_length=1)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_init = models.CharField(max_length=1, null=True, blank=True)
    age = models.IntegerField(default=18)


class Address(models.Model):
    street = models.CharField(max_length=80)
    zip_code = models.IntegerField()
    state = models.CharField(max_length=20)
    apt_num = models.IntegerField(null=True, blank=True)


class Store(models.Model):
    name = models.CharField(max_length=60)
    number_of_employees = models.IntegerField(default=0)
    rating = models.DecimalField(decimal_places=1, max_digits=3)
    owner = models.IntegerField(default=0)
