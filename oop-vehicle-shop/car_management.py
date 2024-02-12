class CarManager:
    total_cars = 0
    all_cars = []
    
    def __init__(self, make, model, year, mileage, services = []) -> None:
        CarManager.total_cars += 1
        self._id = CarManager.total_cars
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services
        
        CarManager.all_cars.append(self) 
    
    def __str__(self) -> str:
        return f"ID: {self._id} | Year: {self._year} | Make: {self._make} | Model: {self._model} | Mileage: {self._mileage} | Services: {self._services}."
        
    def __repr__(self) -> str:
        return str(self)
    
    @property
    def get_mileage(self) -> str:
        return self._mileage
    
    @property
    def get_services(self) -> list:
        return self._services
    
    @property
    def get_id(self) -> int:
        return self._id
    
    @get_services.setter
    def set_service(self, new_service) -> None:
        self._services.append(new_service)
        
    @get_mileage.setter
    def set_milage(self, new_mileage) -> None:
        self._mileage += new_mileage

    # Prints all cars in a nice, readable format
    @staticmethod
    def print_all_cars() -> None:
        for car in CarManager.all_cars:
            print(car)
            print("\n")
    
    # Prints total number of cars
    @staticmethod
    def get_total_number_cars() -> int:
        return CarManager.total_cars
    
    # Method to see a car's details
    @staticmethod
    def see_car_details() -> None:
        user_input = int(input("Enter the ID of the car you would like to see: "))
        if CarManager.all_cars[user_input - 1] in CarManager.all_cars:
            print(CarManager.all_cars[user_input - 1])
        else:
            print("That car ID does not exist.")
    
    # Method to select which car to add a service to and input which service to add
    @staticmethod
    def add_service() -> None:
        id = int(input("What is the ID of the car you would like to add a service to? "))
        print("\n")
        car = CarManager.all_cars[id - 1]
        new_service = input("What is the service you would like to add? ")
        car.set_service = new_service
    
    @staticmethod  
    def update_mileage() -> None:
        # Get car ID
        id = int(input("What is the ID of the car you would like to update? "))
        car = CarManager.all_cars[id - 1]
        print("\n")
        # Get new milage as a string and convert it into a list for searching
        new_milage_str = input("How many miles were added to the vehicle? ")
        new_mileage_list = [*new_milage_str]
        new_milage_int = 0
        
        # Check if mileage is over 1000 and has a comma separator in it
        if new_mileage_list[-4] == ',':
            new_mileage_list.pop(-4)
            new_milage_int = int("".join(new_mileage_list))
        else:
            new_milage_int = int("".join(new_mileage_list))
        
        # Make sure that mileage update is positive
        if new_milage_int >= 0:
            car.set_milage = new_milage_int
        else:
            print("Milage must be greater than 0.")