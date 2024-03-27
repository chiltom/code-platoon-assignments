from django.contrib import admin
from .models import List, Task, Sub_Task

# Register your models here.
admin.site.register([List, Task, Sub_Task])
