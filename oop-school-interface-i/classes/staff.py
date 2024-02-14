class Staff:
    all_staff = {}
        
    def __init__(self, name=None, age=None, role=None, employee_id=None, password=None) -> None:
        self._name = name
        self._age = age
        self._password = password
        self._role = role
        self._employee_id = employee_id
        
        