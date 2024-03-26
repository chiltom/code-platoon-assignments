from django.contrib import admin
from .models import Grade, Subject, Student

# Register your models here.
admin.site.register([Grade, Subject, Student])
