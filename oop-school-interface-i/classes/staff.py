from .person import Person
import csv

class Staff(Person):
    all_staff_list = []
    STAFF_ROLES = ['principal', 'janitor', 'teacher']
    
    # Checks for valid role in staff entry
    @classmethod
    def is_valid_role(cls, role):
        if role.lower() in cls.STAFF_ROLES:
            return True
        return False
    
    # Class method to get all staff from csv file and add them to all staff list
    @classmethod
    def all_staff(cls, path_to_file):
        
        with open(path_to_file, mode = 'r', newline = '') as csvfile:
            staff_data_reader = csv.DictReader(csvfile)
            for staff_data in staff_data_reader:
                a_staff = Staff(**staff_data)
                cls.all_staff_list.append(a_staff)
        
        return cls.all_staff_list
    
    def __init__(self, name=None, age=None, role=None, employee_id=None, password=None):
        super().__init__(name, age, role)
        self._employee_id = int(employee_id)
        self._password = password
    
    def __repr__(self):
        return f"{super().__repr__()} | Employee ID: {self._employee_id} | Password: {self._password}"
    