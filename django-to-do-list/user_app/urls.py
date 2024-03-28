from django.urls import path
from .views import Sign_up, Login

urlpatterns = [
    path("signup/", Sign_up.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
]
