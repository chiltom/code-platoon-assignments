class Person:
    
    def __init__(self, name, age, role) -> None:
        self._name = name
        self._age = int(age) #TODO: Handle casting error if age invalid
        self._role = role 
    
    def __repr__(self) -> str:
        return f"Name: {self._name} | Age: {self._age} | Role: {self._role}"