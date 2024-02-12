

def to_do_list():
    myToDoList = []
    while True:
        user_input = input("Add task to list or type 'Exit' to return to home page. ")
        

        #console.print(table)

        match user_input:
            case "Exit":
                print("Returning Home")
                # phone()
                # break try using return instead of break
                return myToDoList
            case _:
                print(f"Adding {user_input} to list")
                myToDoList.append(user_input)
        print(myToDoList)

# to_do_list()
    #Create a while loop with cases, one case to exit back to home menu, any other input will append that input onto the to do list.
        
    #Make an input/option to remove item from to do list after completion.