from .models import Student
from .serializers import StudentAllSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.


class All_students(APIView):
    def get(self, request):
        students = StudentAllSerializer(get_list_or_404(Student), many=True)
        return Response(students.data)
