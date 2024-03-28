from django.urls import path
from .views import Sign_up, Login, Logout

urlpatterns = [
    path("signup/", Sign_up.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
]
