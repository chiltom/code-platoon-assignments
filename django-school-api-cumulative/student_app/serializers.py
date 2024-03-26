from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Student
from subject_app.serializers import SubjectSerializer
import json


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'student_email', 'locker_number']


class StudentAllSerializer(ModelSerializer):
    subjects = SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        fields = "__all__"

    def get_subjects(self, instance):
        subjects = instance.subjects.all()
        ser_subjects = SubjectSerializer(subjects, many=True)
        return ser_subjects.data
