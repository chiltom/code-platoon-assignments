from django.db import models

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    number_of_pets = models.IntegerField(default=0, null=True, blank=True)


class Cat(models.Model):
    breed = models.CharField(max_length=40)
    age = models.IntegerField(default=1)
    vaccinated = models.BooleanField(default=False)
    description = models.TextField(default='Unknown', null=True, blank=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} | {self.breed} | {self.age}"


class Bird(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=1)
    vaccinated = models.BooleanField(default=False)
    description = models.TextField(default='Unknown', null=True, blank=True)
    species = models.CharField(max_length=40)


class Dog(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=1)
    vaccinated = models.BooleanField(default=False)
    description = models.TextField(default='Unknown', null=True, blank=True)
    species = models.CharField(max_length=40)


class ExoticAnimal(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=1)
    vaccinated = models.BooleanField(default=False)
    description = models.TextField(default='Unknown', null=True, blank=True)
    species = models.CharField(max_length=40)
