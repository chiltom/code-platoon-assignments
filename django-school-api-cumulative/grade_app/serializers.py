from rest_framework.serializers import ModelSerializer, SerializerMethodField
from student_app.serializers import StudentAllSerializer
from subject_app.serializers import SubjectSerializer
from .models import Grade


class GradeSerializer(ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"

    # def get_a_subject(self, instance):
    #     subject = instance.a_subject
    #     ser_subject = {'subject_name': subject.subject_name,
    #                    'professor': subject.professor}
    #     return ser_subject

    # def get_student(self, instance):
    #     student = instance.student
    #     ser_student = {'name': student.name}
    #     return ser_student
