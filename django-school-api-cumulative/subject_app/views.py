from .models import Subject
from .serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404


# Create your views here.
class All_subjects(APIView):
    def get(self, request):
        subjects = SubjectSerializer(get_list_or_404(Subject), many=True)
        return Response(subjects.data)
