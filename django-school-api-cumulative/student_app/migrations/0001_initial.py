# Generated by Django 5.0.3 on 2024-03-23 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('student_email', models.EmailField(max_length=100)),
                ('personal_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('locker_number', models.PositiveIntegerField(default=110)),
                ('locker_combination', models.CharField(default='12-12-12', max_length=8)),
                ('good_student', models.BooleanField(default=True)),
            ],
        ),
    ]
