from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import List, Task, Sub_Task


class Sub_TaskSerializer(ModelSerializer):

    class Meta:
        model = Sub_Task
        fields = "__all__"


class TaskSerializer(ModelSerializer):
    sub_tasks = Sub_TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = "__all__"


class ListSerializer(ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    users = SerializerMethodField()

    class Meta:
        model = List
        fields = "__all__"

    def get_users(self, instance):
        users = instance.users.all()
        ser_users = [{'email': x.email} for x in users]
        return ser_users
