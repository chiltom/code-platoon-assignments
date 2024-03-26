from .models import Student
from .serializers import StudentAllSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.


class All_students(APIView):
    def get(self, request):
        students = StudentAllSerializer(get_list_or_404(Student), many=True)
        return Response(students.data)


class A_student(APIView):
    # def put_subjects(self, lst_of_subjects):
    #     for subj in lst_of_subjects:
    #         if subj in

    def get(self, request, id):
        student = StudentAllSerializer(get_object_or_404(Student, id=id))
        return Response(student.data)

    def put(self, request, id):
        student = get_object_or_404(Student, id=id)
        ser_student = StudentAllSerializer(
            student, data=request.data, partial=True)
        if ser_student.is_valid():
            ser_student.save()
            return Response(ser_student.data, status=HTTP_200_OK)
        else:
            print(ser_student.errors)
            return Response(ser_student.errors, HTTP_400_BAD_REQUEST)
