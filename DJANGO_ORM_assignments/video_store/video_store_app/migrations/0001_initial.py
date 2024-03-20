# Generated by Django 5.0.3 on 2024-03-20 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=80)),
                ('zip_code', models.IntegerField()),
                ('state', models.CharField(max_length=20)),
                ('apt_num', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('middle_init', models.CharField(blank=True, max_length=1, null=True)),
                ('age', models.IntegerField(default=18)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('number_of_employees', models.IntegerField(default=0)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('owner', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('in_stock', models.IntegerField(default=1)),
                ('rating', models.CharField(max_length=1)),
            ],
        ),
    ]
