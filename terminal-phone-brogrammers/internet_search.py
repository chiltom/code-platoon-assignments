from webbrowser import open

search_history = []

# Helper function to get user input and append to search history
def user_query():
    user_query_input = input("What would you like to search? ")
    return user_query_input

# Function to open a web browser
def open_browser():
    user_choice = input("Would you like to search Google (Y/N)? ")
    if user_choice != "Y" and user_choice != "N":
        raise ValueError("Not a valid choice.")
    while user_choice == "Y":
        query_choice = user_query()
        search_history.append(query_choice)
        open(url = f"https://www.google.com/search?q={query_choice}", new = 2)
        user_choice = input("Would you like to search again (Y/N)? ")
        if user_choice != "Y" and user_choice != "N":
            raise ValueError("Not a valid choice.")
    if user_choice == "N":
        history_query = input("Would you like to print your search history (Y/N)? ")
        if history_query != "Y" and history_query != "N":
            raise ValueError("Not a valid choice.")
        elif history_query == "Y":
            for elem in search_history:
                print(elem)
        elif history_query == "N":
            pass