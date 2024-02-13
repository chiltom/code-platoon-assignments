from classes.school import School
from classes.student import Student
from classes.staff import Staff


school = School('Ridgemont High')

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

def display_add_a_student_menu():
    print("Add student")
    pass

def display_remove_a_student_menu():
    print("Remove student")
    pass

def display_main_menu():
    user_input = input(main_menu_message)

    match int(user_input):
        
        case 1:
            school.list_students()
            display_main_menu()    
            
        case 2:
            school.find_student_by_id()
            display_main_menu()
            
        case 3:
            display_add_a_student_menu()
            display_main_menu()
            
        case 4:
            display_remove_a_student_menu()
            display_main_menu()
            
        case 5:
            exit()
    
        
display_main_menu()