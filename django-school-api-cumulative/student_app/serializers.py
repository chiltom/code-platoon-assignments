from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Student
from subject_app.serializers import SubjectSerializer


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'student_email', 'locker_number']


class StudentAllSerializer(ModelSerializer):
    # subjects = SerializerMethodField()

    class Meta:
        model = Student
        # fields = [
        #     'name',
        #     'student_email',
        #     'personal_email',
        #     'locker_number',
        #     'locker_combination',
        #     'good_student',
        #     'subjects',
        # ]
        exclude = ['id']

    # def get_subjects(self, instance):
    #     raw_subjects = instance.subjects.all()
    #     subjects = SubjectSerializer(raw_subjects, many=True)
    #     return subjects
