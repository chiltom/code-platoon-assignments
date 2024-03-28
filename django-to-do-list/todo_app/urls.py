from django.urls import path
from .views import All_lists, A_list, All_tasks

urlpatterns = [
    path('', All_lists.as_view(), name="all_lists"),
    path('<int:id>/', A_list.as_view(), name="a_list"),
    path('<int:id>/tasks/', All_tasks.as_view(), name="all_tasks"),
]
