"""
URL configuration for hello_django_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import math
from django.http import HttpResponse

from django.contrib import admin
from django.urls import path


def rectangle_area(request, height, width):
    return HttpResponse(height * width)


def rectangle_perimeter(request, height, width):
    return HttpResponse((height * 2) + (width * 2))


def circle_area(request, radius):
    return HttpResponse(math.pi * (radius ** 2))


def circle_perimeter(request, radius):
    return HttpResponse(math.pi * (radius * 2))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rectangle/area/<int:height>/<int:width>/', rectangle_area),
    path('rectangle/perimeter/<int:height>/<int:width>/', rectangle_perimeter),
    path('circle/area/<int:radius>/', circle_area),
    path('circle/perimeter/<int:radius>/', circle_perimeter),
]
