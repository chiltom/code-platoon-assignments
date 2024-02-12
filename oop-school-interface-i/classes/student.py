from .person import Person
import csv

class Student(Person):
    all_students_list = []
    
    @classmethod
    def get_student_by_id(cls, id):
        for student in cls.all_students_list:
            if id == student._school_id:
                return student
            else:
                return None
        
    # Class method to get all students from csv file and add them to all students list
    @classmethod
    def all_students(cls, path_to_file):
        
        with open(path_to_file, mode = 'r', newline = '') as csvfile:
            student_data_reader = csv.DictReader(csvfile)
            for student_data in student_data_reader:
                a_student = Student(**student_data)
                cls.all_students_list.append(a_student)
        
        return cls.all_students_list
    
    def __init__(self, name=None, age=None, role=None, school_id=None, password=None):
        super().__init__(name, age, role)
        self._school_id = int(school_id)
        self._password = password
    
    def __repr__(self):
        return f"{super().__repr__()} | School ID: {self._school_id} | Password: {self._password}"
    