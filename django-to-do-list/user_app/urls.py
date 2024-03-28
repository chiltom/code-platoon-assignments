from django.urls import path
from .views import Info, Sign_up, Login, Logout

urlpatterns = [
    path('', Info.as_view(), name="info"),
    path("signup/", Sign_up.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
]
