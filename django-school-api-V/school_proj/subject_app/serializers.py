from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Subject


class SubjectSerializer(ModelSerializer):
    grade_average = SerializerMethodField

    class Meta:
        model = Subject
        fields = ['subject_name', 'professor', 'students', 'grade_average']

    def get_grade_average(self, instance):
        grades = instance.grades.all()
        grade_sum = 0
        count = 0
        for x in grades:
            grade_sum += grades.grade
            count += 1
        grade_average = grade_sum / count
        return grade_average
