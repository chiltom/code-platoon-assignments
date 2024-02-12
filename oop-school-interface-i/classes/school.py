from .staff import Staff
from .student import Student

class School:
    
    def __init__(self, name, students_file_path=None, staff_file_path=None) -> None:
        self._name = name
        self._students = Student.all_students(students_file_path)
        self._staff = Staff.all_staff(staff_file_path)
