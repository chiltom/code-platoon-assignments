from .staff import Staff
from .student import Student

class School:
    
    def __init__(self, name) -> None:
        self._name = name
        self._students = Student.all_students()
        self._staff = Staff.all_staff()

    def __str__(self) -> str:
        return f"This is {self._name}."
    
    def __repr__(self) -> str:
        return str(self)
    
    def list_students(self):
        count = 0
        for student in self._students:
            count += 1
            print(f"{count}. {student._name} {student._school_id}")
    
    @staticmethod            
    def find_student_by_id():
        id = int(input("Enter student ID: "))
        return Student.get_student_by_id(id)