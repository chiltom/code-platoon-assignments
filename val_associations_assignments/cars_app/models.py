from django.db import models
from django.core import validators as v
from django.utils import timezone

# Create your models here.


class Owner(models.Model):
    age = models.PositiveIntegerField(
        default=25, validators=[v.MinValueValidator(18), v.MaxValueValidator(100)])
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    num_of_vehicles = models.PositiveIntegerField(default=0)


class Engine(models.Model):
    size = models.PositiveIntegerField(default=4, validators=[
                                       v.MinValueValidator(4), v.MaxValueValidator(12)])
    custom = models.BooleanField(default=False)


class Car(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    mileage = models.PositiveIntegerField(default=0)
    year = models.PositiveIntegerField(default=2024, validators=[
                                       v.MinValueValidator(1920), v.MaxValueValidator(2100)])
    owners = models.ManyToManyField(Owner)
    engine = models.OneToOneField(Engine, on_delete=models.CASCADE)
    number_of_tires = models.PositiveIntegerField(
        default=4, validators=[v.MinValueValidator(4), v.MaxValueValidator(5)])


class Tires(models.Model):
    section_width = models.PositiveIntegerField(default=30)
    aspect_ratio = models.PositiveIntegerField(default=15)
    rim_size = models.PositiveIntegerField(default=16)
    vehicle_type = models.CharField(max_length=30)
    vehicle = models.OneToOneField(Car, on_delete=models.CASCADE)


class ServiceRecord(models.Model):
    date = models.DateTimeField(default=timezone.now)
    reason = models.CharField(max_length=255, default='Unknown')
    completed = models.BooleanField(default=False)
    place_of_service = models.CharField(max_length=100)
    notes = models.TextField(default='None')
    vehicle = models.ForeignKey(Car, on_delete=models.CASCADE)
