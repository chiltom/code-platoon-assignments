from classes.school import School
from classes.student import Student
from classes.staff import Staff


school = School('Ridgemont High', students_file_path='./data/students.csv', staff_file_path='./data/staff.csv')

# Make our terminal

main_menu_message = """
What would you like to do?
    Options:
    1. List All Students
    2. View Individual Student <student_id>
    3. Add a Student
    4. Remove a Student <student_id>
    5. Quit
"""

def display_all_students_menu():
    print(school._students)

# TODO: Change to get student by ID
def display_view_individual_student_menu():
    student_name = input("What is the name of the student? ")
    student = Student.get_student_by_name(student_name)
    if student is None:
        print("That student isn't at this school")
    else:
        print(student)

def display_add_a_student_menu():
    print("Add student")
    pass

def display_remove_a_student_menu():
    print("Remove student")
    pass

def display_main_menu():
    user_main_menu_input = input(main_menu_message)

    if user_main_menu_input == '1':
        display_all_students_menu()
        display_main_menu()
    elif user_main_menu_input == '2':
        display_view_individual_student_menu()
        display_main_menu()
    elif user_main_menu_input == '3':
        display_add_a_student_menu()
        display_main_menu()
    elif user_main_menu_input == '4':
        display_remove_a_student_menu()
        display_main_menu()
    elif user_main_menu_input == '5':
        exit()
    else:
        print("Not a valid choice. Try again.")
        
display_main_menu()