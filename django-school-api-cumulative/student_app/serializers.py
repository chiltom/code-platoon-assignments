from rest_framework.serializers import ModelSerializer
from .models import Student
from subject_app.serializers import SubjectSerializer


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'student_email', 'locker_number']


class StudentAllSerializer(ModelSerializer):
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Student
        fields = "__all__"