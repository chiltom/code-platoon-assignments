from django.urls import path
from .views import A_location

urlpatterns = [
    path('<str:location>', A_location.as_view(), name='a_location')
]
