from .models import Grade, Student, Subject
from .serializers import GradeSerializer
from student_app.serializers import StudentAllSerializer
from subject_app.serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED
)
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.


class All_grades(APIView):
    def get(self, request):
        grades = GradeSerializer(get_list_or_404(Grade), many=True)
        return Response(grades.data, status=HTTP_200_OK)

    def post(self, request):
        data = request.data.copy()
        stud = StudentAllSerializer(
            get_object_or_404(Student, id=data.student))
        subj = SubjectSerializer(get_object_or_404(Subject, id=data.a_subject))
        new_grade = GradeSerializer(Grade(a_subject=subj, student=stud))
        if new_grade.is_valid():
            new_grade.save()
            return Response(new_grade.data, status=HTTP_201_CREATED)
        else:
            print(new_grade.errors)
            return Response(new_grade.errors, status=HTTP_400_BAD_REQUEST)


class A_grade(APIView):
    def get(self, request, id):
        grade = GradeSerializer(get_object_or_404(Grade, id=id))
        return Response(grade.data, status=HTTP_200_OK)

    def put(self, request, id):
        data = request.data.copy()
        grade = get_object_or_404(Grade, id=id)
        ser_grade = GradeSerializer(grade, data=data, partial=True)
        if ser_grade.is_valid():
            ser_grade.save()
            return Response(ser_grade.data, status=HTTP_200_OK)
        else:
            print(ser_grade.errors)
            return Response(ser_grade.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        grade = get_object_or_404(Grade, id=id)
        grade.delete()
        return Response(status=HTTP_204_NO_CONTENT)
