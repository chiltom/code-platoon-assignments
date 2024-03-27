from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from .models import List, Task, Sub_Task
from .serializers import ListSerializer, TaskSerializer, Sub_TaskSerializer
from django.shortcuts import get_object_or_404, get_list_or_404


# Create your views here.
class All_lists(APIView):
    def get(self, request):
        lists = ListSerializer(get_list_or_404(List), many=True)
        return Response(lists.data, status=HTTP_200_OK)

    def post(self, request):
        data = request.data.copy()
        new_list = ListSerializer(data=data)
        if new_list.is_valid():
            new_list.save()
            return Response(new_list.data, status=HTTP_201_CREATED)
        else:
            return Response(new_list.errors, status=HTTP_400_BAD_REQUEST)
