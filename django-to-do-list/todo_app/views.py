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


class A_list(APIView):
    def add_tasks(self, list, lst_of_task_ids):
        for task_id in lst_of_task_ids:
            if get_object_or_404(Task, id=task_id):
                list.tasks.add(task_id)
                list.save()

    def get(self, request, id):
        list = ListSerializer(get_object_or_404(List, id=id))
        return Response(list.data, status=HTTP_200_OK)

    def put(self, request, id):
        data = request.data.copy()
        list = get_object_or_404(List, id=id)
        ser_list = ListSerializer(list, data=data, partial=True)
        if ser_list.is_valid():
            ser_list.save()
            if data.get("lst_of_tasks"):
                self.add_tasks(
                    list=list, lst_of_task_ids=data.get("lst_of_tasks"))
            return Response(ser_list.data, status=HTTP_200_OK)
        else:
            return Response(ser_list.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        list = get_object_or_404(List, id=id)
        list.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class All_tasks(APIView):
    # Fix getting parent list
    def get(self, request, id):
        list = get_object_or_404(List, id=id)
        tasks = TaskSerializer(list.tasks, many=True)
        return Response(tasks.data, status=HTTP_200_OK)

    def post(self, request, id):
        data = request.data.copy()
        data["parent_list"] = id
        new_task = TaskSerializer(data=data)
        if new_task.is_valid():
            new_task.save()
            return Response(new_task.data, status=HTTP_201_CREATED)
        else:
            return Response(new_task.errors, status=HTTP_400_BAD_REQUEST)


class A_task(APIView):
    def add_sub_tasks(self, task, lst_of_sub_task_ids):
        for sub_task_id in lst_of_sub_task_ids:
            if get_object_or_404(Sub_Task, id=sub_task_id):
                task.sub_tasks.add(sub_task_id)
                task.save()

    def get(self, request, id, task_id):
        task = TaskSerializer(get_object_or_404(Task, id=task_id))
        return Response(task.data, status=HTTP_200_OK)

    def put(self, request, id, task_id):
        data = request.data.copy()
        task = get_object_or_404(Task, id=task_id)
        ser_task = TaskSerializer(task, data=data, partial=True)
        if ser_task.is_valid():
            ser_task.save()
            if data.get("lst_of_sub_tasks"):
                self.add_sub_tasks(task, data.get("lst_of_sub_tasks"))
            return Response(ser_task.data, status=HTTP_200_OK)
        else:
            return Response(ser_task.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class All_sub_tasks(APIView):
    def get(self, request, id, task_id):
        task = get_object_or_404(Task, id=task_id)
        sub_tasks = Sub_TaskSerializer(task.sub_tasks, many=True)
        return Response(sub_tasks.data, status=HTTP_200_OK)

    def post(self, request, id, task_id):
        data = request.data.copy()
        data["parent_task"] = task_id
        new_sub_task = Sub_TaskSerializer(data=data)
        if new_sub_task.is_valid():
            new_sub_task.save()
            return Response(new_sub_task.data, status=HTTP_201_CREATED)
        else:
            return Response(new_sub_task.errors, status=HTTP_400_BAD_REQUEST)


class A_sub_task(APIView):
    def get(self, request, id, task_id, sub_task_id):
        sub_task = Sub_TaskSerializer(
            get_object_or_404(Sub_Task, id=sub_task_id))
        return Response(sub_task.data, status=HTTP_200_OK)

    def put(self, request, id, task_id, sub_task_id):
        data = request.data.copy()
        sub_task = get_object_or_404(Sub_Task, id=sub_task_id)
        ser_sub_task = Sub_TaskSerializer(sub_task, data=data, partial=True)
        if ser_sub_task.is_valid():
            ser_sub_task.save()
            return Response(ser_sub_task.data, status=HTTP_200_OK)
        else:
            return Response(ser_sub_task.errors, status=HTTP_400_BAD_REQUEST)
