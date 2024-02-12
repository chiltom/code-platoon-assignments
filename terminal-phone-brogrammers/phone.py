from rich.console import Console
from rich.table import Table
from to_do_list import to_do_list
from internet_search import open_browser


def phone():
    myToDoList = []
    table = Table(title="Welcome to your Phone!")
    table.add_column("Options", style="cyan", no_wrap=True)
    table.add_column("Navigate", style="magenta")
    table.add_column("Icon", justify="center", style="green")

    table.add_row("1", "Home", "🏠")
    table.add_row("2", "Contacts", "👽")
    table.add_row("3", "Internet", "🛜")
    table.add_row("4", "Tasks", "📝")
    table.add_row("5", "Exit", "❌")

    console = Console()
    while True:
        console.print(table)
        print("Welcome to your Phone, please select an option from the menu below!")
        userInput = input("Choose one of the Options :")
        match userInput:
            case "1":
                print("Welcome Home.")
            case "2":
                print("Opening Contacts")
                # import contacts.py
            case "3":
                print("Opening a web browser")
                open_browser()
                # import internet_search.py
            case "4":
                print("Opening To Do List")
                # import to_do_list.py
                # to_do_list()
                myToDoList = to_do_list()
                print(myToDoList)
            case "5":
                print("Goodbye")
                break

            case _:
                print("Not a valid input, please select from the listed options.")
                print(f"You entered: {userInput}")

 # Give the user options, number the options( 1 = home 2 = phone 3 = date)


# The following are the menu options the assignment has asked us to implement;

# 1: Personalize the phone with images and colors.
# 2: Design a menu interface using basic Python functions.
phone()
