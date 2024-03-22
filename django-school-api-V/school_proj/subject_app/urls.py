from .views import All_subjects
from django.urls import path

urlpatterns = [
    path('', All_subjects.as_view(), name="all_subjects")
]
