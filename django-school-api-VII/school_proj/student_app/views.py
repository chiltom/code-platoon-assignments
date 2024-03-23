from django.shortcuts import render
from .models import Student
from .serializers import StudentAllSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.


class All_students(APIView):
    def get(self, request):
        students = StudentAllSerializer(Student.objects.all(), many=True)
        return Response(students.data)

class A_student(APIView):
    def get(self, request, id):
        student = StudentAllSerializer(get_object_or_404(Student, id=id))
        return Response(student.data)