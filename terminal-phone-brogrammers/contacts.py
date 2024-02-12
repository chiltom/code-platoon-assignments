

def contact_function():
   
    selection1 = ''

    contact_book = {
        'albert' : '7021238888',
        'james' : '5558037826',
        'brett' : "1237886523",
        'joel' : "0987643212",  
    }

    while selection1.lower() != 'exit':
        selection2 = ''
        selection1 = input(f'"view", "create", "update", "delete" a contact or "exit" (exit to main menu): ')

        if (selection1.lower() == "view"):
                for key in contact_book:
                    print(f'{key}: {contact_book[key]}')

        elif (selection1.lower() == "create"):       
                new_contact_name = input("Please enter a name for your new contact: ")
                new_contact_num = input("Please enter a phone number for your new contact: ")
                contact_book[new_contact_name] = new_contact_num
                
        elif (selection1.lower() == "update"):
                for key in contact_book:
                    print(f'{key}: {contact_book[key]}')
                selection1 = input("Please enter the name of the contact that you would like to update: ")
                if (selection1.lower() in contact_book):
                    selection2 = input(f'Please enter a new phone number for {selection1}: ')
                    contact_book[selection1] = selection2
                    print(f'{selection1}\'s phone number is now set to {selection2}')
                else:
                    print ("No such contact exists")

        elif (selection1.lower() == "delete"):
                for key in contact_book:
                    print(f'{key}: {contact_book[key]}')

                delete_this_contact = input("Please enter the name of the contact that you would like to delete: ")
                if delete_this_contact.lower() in contact_book:
                    del contact_book[delete_this_contact.lower()]
                    print(f"{delete_this_contact} has been deleted from your contact list")
                else:
                    print(f"{delete_this_contact} is not in your contact list")

        else:
             print ("Invalid selection")

    return

contact_function()











        
