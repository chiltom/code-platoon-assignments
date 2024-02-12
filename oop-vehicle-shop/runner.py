from car_management import *

# Method to print menu screen
def print_screen() -> None:
    print("\n")
    menu_screen = ["----  WELCOME  ----",
                   "1. Add a car",
                   "2. View all cars",
                   "3. View total number of cars",
                   "4. See a car's details",
                   "5. Service a car",
                   "6. Update mileage",
                   "7. Quit"]
    for row in menu_screen:
        print(row + "\n")

# Method to validate and gather user input
def get_input() -> int:
    valid_input = False
    user_input = 0
    while valid_input == False:
        user_input = int(input("What would you like to do? "))
        if user_input < 1 and user_input > 7:
            raise ValueError("Not a valid choice. Try again.")
        else:
            valid_input = True
    return user_input

# Method to add a car by creating an instance of car
def add_car() -> CarManager:
    print("""Great! You'd like to add a car to the inventory. 
          Please answer the questions below so we can get started.""")
    
    # Gather input for year, make, model, and mileage
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    
    # Handle commas in nums over 1,000
    miles_str = input("Mileage: ")
    miles_list = [*miles_str]
    mileage = 0
    if len(miles_list) > 3 and miles_list[-4] == ",":
        miles_list.pop(-4)
        mileage = int("".join(miles_list))
    else:
        mileage = int("".join(miles_list))
    
    
    # Gather services information and format as a list
    services = []
    service_input = input("Enter services done to the vehicle, separated by commas. If none, type None: ")
    if service_input != "None":
        services = service_input.split(",")
    
    # Return an instance of CarManager
    return CarManager(make, model, year, mileage, services)


# Main
def main() -> None:
    while True:
        # Start by printing screen and gathering user choice
        print_screen()
        choice = get_input()
        
        # Match case to run functions depending on choice
        match choice:
            case 1:
                add_car()
                print("""Great! You just added your new vehicle to the database.
                         Select option 2 or 3 next if you would like to see more details.""")
            case 2:
                print("\n")
                CarManager.print_all_cars()
            case 3:
                print("\n")
                print(f"{CarManager.get_total_number_cars()} cars on the lot.")
            case 4:
                print("\n")
                CarManager.see_car_details()
            case 5:
                print("\n")
                CarManager.add_service()
            case 6:
                print("\n")
                CarManager.update_mileage()
            case 7:
                break
                

if __name__ == "__main__":
    main()