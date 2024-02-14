class Student:
    all_students = {}
    
    @classmethod    
    def list_students(cls) -> None:
        counter = 0
        for school_id in cls.all_students:
            counter += 1
            print(f"{counter}. {cls.all_students[school_id]._name} {school_id}")
            
    @classmethod
    def find_student_by_id(cls, student_id_str):
        if student_id_str in cls.all_students:
            return cls.all_students[student_id_str]
        else:
            print(f"Student ID {student_id_str} does not exist.")
            
    @classmethod
    def add_student(cls, dict) -> None:
        instance = cls(**dict)
        cls.all_students[instance._school_id] = instance
        
    def __init__(self, name=None, age=None, role=None, school_id=None, password=None) -> None:
        self._name = name
        self._age = age
        self._password = password
        self._role = role
        self._school_id = school_id
    
    def __str__(self) -> str:
        return f"{self._name.capitalize()}\n------------------\nAge: {self._age}\nID: {self._school_id}"
    
    # def __repr__(self) -> str:
    #     return str(self)
    
    @property
    def get_id(self) -> int:
        return int(self._school_id)
    
    
