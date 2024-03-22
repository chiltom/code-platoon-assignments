from .views import All_students
from django.urls import path

urlpatterns = [
    path('', All_students.as_view(), name="all_students")
]
