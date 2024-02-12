class Student:
    def __init__(self, name, age = 13, grade = "12th"):
        self._name = name
        self._age = age
        self._grade = grade
        self._subject = None
        
    def __str__(self):
        return f"{self}: Name: {self._name}, Age: {self._age}, Grade: {self._grade}"
    
    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, new_name):
        # new_list = [*new_name]
        alpha_string = 'abcdefghijklmnopqrstuvwxyz'
        # alpha_list = [*alpha_string]
        if isinstance(new_name, str) and len(new_name) >= 3 and " " not in new_name and new_name == new_name.title():
            for char in new_name:
                if char in alpha_string:
                    self._name = new_name
        else:
            print("Name must have only letters a-z, be three letters or more, and be in title format")

    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age,int) and new_age > 11 and new_age < 18:
            self._age = new_age
        else:
            print("Age must be an int and between 11 and 18.")
    
    @property
    def get_grade(self):
        return self._grade
    
    @get_grade.setter
    def set_grade(self, new_grade):
        list_grades = ['9th', '10th', '11th', '12th']
        if new_grade in list_grades:
            self._grade = new_grade
        else:
            return "Grade must be 9th - 12th"
    
    def advanced(self, years_advanced = 1):
        if self._grade == '9th':
            self._grade = str(int(self._grade[0]) + years_advanced) + 'th'
        else:
            self._grade = str(int(self._grade[0:2]) + years_advanced) + 'th'
        
        return f"{self._name} has advanced to the {self._grade} grade"
    
    def study(self, subject):
        self._subject = subject
        return f"{self.name} is studying {self._subject}"
    
# student1 = Student('Alice')
# student1.set_age = 14
# print(student1.get_age)