from django.urls import path
from .views import A_article

urlpatterns = [
    path('<str:name>', A_article.as_view(), name='a_article')
]
