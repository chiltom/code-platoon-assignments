# Generated by Django 5.0.3 on 2024-03-23 02:04

import student_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0003_alter_student_locker_combination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(default='12-12-12', max_length=10, validators=[student_app.validators.validate_combination_format]),
        ),
    ]
