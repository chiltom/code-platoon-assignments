# Generated by Django 5.0.3 on 2024-03-28 14:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=50, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=False)),
                ('parent_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todo_app.list')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_task_name', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=False)),
                ('parent_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_tasks', to='todo_app.task')),
            ],
        ),
    ]
