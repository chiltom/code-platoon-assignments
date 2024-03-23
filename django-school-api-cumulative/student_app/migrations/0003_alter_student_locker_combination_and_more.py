# Generated by Django 5.0.3 on 2024-03-23 02:02

import django.core.validators
import student_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_alter_student_locker_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(default='12-12-12', max_length=8, validators=[student_app.validators.validate_combination_format]),
        ),
        migrations.AlterField(
            model_name='student',
            name='locker_number',
            field=models.PositiveIntegerField(default=110, unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(200)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=70, validators=[student_app.validators.validate_name_format]),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_email',
            field=models.EmailField(max_length=100, unique=True, validators=[student_app.validators.validate_school_email]),
        ),
    ]
