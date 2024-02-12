class Animal:
    
    def __init__(self, name, species, sound = 'Animal sound') -> None:
        self.name = name
        self.species = species
        self.sound = sound
        
    # def __str__(self):
    #     pass
    
    def speak(self) -> str:
        return f"{self.sound}"
    
class Mammal(Animal):
    
    def __init__(self, name, species) -> str:
        super().__init__(name, species)
    
    def give_birth(self) -> None:
        return f"{self.name} the {self.species} has given birth"

class Bird(Animal):
    
    def __init__(self, name, species, wingspan) -> None:
        super().__init__(name, species)
        self.wingspan = wingspan
        
class Reptile(Animal):
    
    def __init__(self, name, species) -> None:
        super().__init__(name, species)
        
    def bask_in_sun(self) -> str:
        return f"{self.name} the {self.species} is basking in the sun"

class Primate(Mammal):
    
    def __init__(self, name, species) -> None:
        super().__init__(name, species)
        
    def climb_trees(self) -> str:
        return f"{self.name} the {self.species} is climbing trees"

class Marsupial(Mammal):
    
    def __init__(self, name, species) -> None:
        super().__init__(name, species)
        
    def carry_baby(self) -> str:
        return f'{self.name} the {self.species} is carrying its baby'

class Aviary:

    def __init__(self) -> None:
        self.birds = []
        
class ReptileEnclosure:
    
    def __init__(self) -> None:
        self.reptiles = []