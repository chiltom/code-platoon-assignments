from .models import Subject
from .serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404, get_list_or_404


# Create your views here.
class All_subjects(APIView):
    def get(self, request):
        subjects = SubjectSerializer(get_list_or_404(Subject), many=True)
        return Response(subjects.data)


class A_subject(APIView):
    def get(self, request, subject):
        subject = SubjectSerializer(get_object_or_404(
            Subject, subject_name=subject.title()))
        return Response(subject.data)

    def put(self, request, subject):
        subj = get_object_or_404(Subject, subject_name=subject.title())
        if "subject_name" in request.data and request.data.get("subject_name"):
            subj.subject_name = request.data.get("subject_name")
        if "professor" in request.data and request.data.get("professor"):
            subj.professor = request.data.get("professor")
        ser_subj = SubjectSerializer(subj, data=vars(subj))
        if ser_subj.is_valid():
            ser_subj.save()
            return Response(ser_subj.data, status=HTTP_200_OK)
        else:
            print(ser_subj.errors)
            return Response(ser_subj.errors, HTTP_400_BAD_REQUEST)
