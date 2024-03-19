# Generated by Django 5.0.3 on 2024-03-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_alter_student_personal_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='good_student',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(default='12-12-12', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='locker_number',
            field=models.IntegerField(default=110, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='personal_email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]