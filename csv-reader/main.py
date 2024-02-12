import csv

class Dog:
    
    def __init__(self, name, age, breed) -> None:
        self._name = name
        self._age = age
        self._breed = breed
    
    def __str__(self) -> str:
        return f"{self._name} is a {self._age} year old {self._breed}."
    
class Cat:
    
    def __init__(self, name, age, breed) -> None:
        self._name = name
        self._age = age
        self._breed = breed
    
    def __str__(self) -> str:
        return f"{self._name} is a {self._age} year old {self._breed}."
    
    
    
def main():
    # Make an empty list for all of the chosen animals from user_choice
    animal_list = []
    user_choice = input("Enter type of animal you would like to look at: ").lower()
    
    # Make a dialect to skip initial spaces so that keys and values have no spaces in them
    csv.register_dialect('my_dialect', skipinitialspace=True)
    
    # Open the CSV file and append all entries (dictionaries) to animal_list
    try:
        # Open the CSV file
        with open(f'./data/{user_choice}.csv', newline = '') as csvfile:
            # Create an instance of DictReader to return rows as a dictionary with key: value pairs
            reader = csv.DictReader(csvfile, dialect = 'my_dialect')
            # For each row that the reader opens, append it to animal_list
            for row in reader:
                animal_list.append(row)
    except:
        print(f"Sorry, we don't have any {user_choice}.")

    # Create instances of all the chosen animals in animal_list
    for animal in animal_list:
        if user_choice == 'cats':
            animal = Cat(animal['name'], animal['age'], animal['breed'])
            print(animal)
        else:
            animal = Dog(animal['name'], animal['age'], animal['breed'])
            print(animal)
        
    

if __name__ == "__main__":
    main()