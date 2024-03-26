from .models import Student
from subject_app.models import Subject
from .serializers import StudentAllSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
    HTTP_201_CREATED
)
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.


class All_students(APIView):
    def add_subjects(self, student, lst_of_subject_ids):
        for subj_id in lst_of_subject_ids:
            if get_object_or_404(Subject, id=subj_id):
                student.subjects.add(subj_id)
                student.save()

    def get(self, request):
        students = StudentAllSerializer(get_list_or_404(Student), many=True)
        return Response(students.data)

    def post(self, request):
        data = request.data.copy()
        new_student = StudentAllSerializer(data=data)
        if new_student.is_valid():
            new_student.save()
            return Response(new_student.data, status=HTTP_201_CREATED)
        else:
            print(new_student.errors)
            return Response(new_student.errors, status=HTTP_400_BAD_REQUEST)


class A_student(APIView):
    def add_subjects(self, student, lst_of_subject_ids):
        for subj_id in lst_of_subject_ids:
            if get_object_or_404(Subject, id=subj_id):
                student.subjects.add(subj_id)
                student.save()

    def get(self, request, id):
        student = StudentAllSerializer(get_object_or_404(Student, id=id))
        return Response(student.data)

    def put(self, request, id):
        data = request.data.copy()
        student = get_object_or_404(Student, id=id)
        ser_student = StudentAllSerializer(
            student, data=data, partial=True)
        if ser_student.is_valid():
            ser_student.save()
            if data.get("lst_of_subjects"):
                self.add_subjects(
                    student, data.get("lst_of_subjects"))
            return Response(ser_student.data, status=HTTP_200_OK)
        else:
            print(ser_student.errors)
            return Response(ser_student.errors, status=HTTP_400_BAD_REQUEST)
