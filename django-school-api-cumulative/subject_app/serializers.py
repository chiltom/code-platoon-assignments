from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Subject


class SubjectSerializer(ModelSerializer):
    students = SerializerMethodField()
    grade_average = SerializerMethodField()

    class Meta:
        model = Subject
        fields = ["subject_name", "professor", "students", "grade_average"]

    def get_students(self, instance):
        return instance.students.count()

    def get_grade_average(self, instance):
        grades = instance.grades.all()
        return round(sum([x.grade for x in grades])/len(grades), 2)
