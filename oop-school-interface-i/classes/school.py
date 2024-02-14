from classes.student import Student
from classes.staff import Staff
import csv

class School:
    
    def __init__(self, name) -> None:
        self._name = name
        self.load_data()
        self._staff = Staff.all_staff
        self._students = Student.all_students
        
    def load_data(self) -> None:
        # Students
        with open("./data/students.csv", mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for student_data in reader:
                student_inst = Student(**student_data)
                Student.all_students[student_data['school_id']] = student_inst
        # Staff
        with open("./data/staff.csv", mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for staff_data in reader:
                staff_inst = Staff(**staff_data)
                Staff.all_staff[staff_data['employee_id']] = staff_inst
     
    @staticmethod
    def display_menu_input_validation() -> int:
        valid_input = False
        while valid_input == False:
            # Try to typecast input to an int
            try:
                user_input = int(input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n"))
            except ValueError:
                print(f"{user_input} is not a number. Try again.")
                continue
            # Validate int is an option
            if user_input < 1 and user_input > 5:
                print(f"{user_input} is not a valid choice. Try again")
                continue
            else:
                valid_input = True
                return user_input
    
    @classmethod
    def manage_school(cls) -> None:
        
        while True:
            
            user_input = cls.display_menu_input_validation()
            
            match user_input:
                
                case 1:
                    Student.list_students()
                case 2:
                    student_id = input('Enter student ID: ')
                    student = Student.find_student_by_id(student_id)
                    print(student)
                case 3:
                    student_data = {'role': 'student'}
                    student_data['name'] = input("Enter student name: ")
                    student_data['age'] = input("Enter student age: ")
                    student_data['school_id'] = input("Enter school ID: ")
                    student_data['password'] = input("Enter student password: ")
                    
                    Student.add_student(student_data)
                case 4:
                    school_id = input("Enter the students school ID: ")
                    print(f"Student: {Student.all_students[school_id]._name} being deleted from school records.")
                    Student.all_students.pop(school_id)
                case 5:
                    print("Thank you for working with us!")
                    break