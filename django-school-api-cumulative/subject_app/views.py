from .models import Subject
from .serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
from django.shortcuts import get_object_or_404, get_list_or_404


# Create your views here.
class All_subjects(APIView):
    def get(self, request):
        subjects = SubjectSerializer(get_list_or_404(Subject), many=True)
        return Response(subjects.data)

    def post(self, request):
        data = request.data.copy()
        new_subject = SubjectSerializer(data=data)
        if new_subject.is_valid():
            new_subject.save()
            return Response(new_subject.data, status=HTTP_201_CREATED)
        return Response(new_subject.errors, status=HTTP_400_BAD_REQUEST)


class A_subject(APIView):
    def get(self, request, subject):
        subject = SubjectSerializer(get_object_or_404(
            Subject, subject_name=subject.title()))
        return Response(subject.data)

    def put(self, request, subject):
        data = request.data.copy()
        subj = get_object_or_404(Subject, subject_name=subject.title())
        if "subject_name" in data and data.get("subject_name"):
            subj.subject_name = data.get("subject_name")
        if "professor" in data and data.get("professor"):
            subj.professor = data.get("professor")
        ser_subj = SubjectSerializer(subj, data=vars(subj))
        if ser_subj.is_valid():
            ser_subj.save()
            return Response(ser_subj.data, status=HTTP_200_OK)
        else:
            print(ser_subj.errors)
            return Response(ser_subj.errors, HTTP_400_BAD_REQUEST)
