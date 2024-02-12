class ContactList:
    def __init__(self, name, contacts) -> None:
        self._name = name
        self._contacts = sorted(contacts, key = lambda contact: contact['name'])
    
    def __str__(self) -> str:
        return f"{self._name}: {self._contacts}"
    
    @property
    def get_name(self) -> str:
        return self._name
    
    @property
    def get_contacts(self) -> list:
        return self._contacts
    
    @get_name.setter
    def set_name(self, new_name) -> None:
        self._name = new_name
        
    @get_contacts.setter
    def set_contacts(self, new_contact_list) -> None:
        self._contacts = new_contact_list
    
    def add_contact(self, contact) -> None:
        self._contacts.append(contact)
        self._contacts = sorted(self._contacts, key = lambda contact: contact['name'])
    
    def remove_contact(self, contact_str) -> None:
        for contact in self.get_contacts:
            if contact['name'] == contact_str:
                self.get_contacts.remove(contact)
        
    def find_shared_contacts(self, contact_list) -> list:
        output = []
        
        # Loop through both lists and append shared contacts to output list
        for contact in self.get_contacts:
            for contact_two in contact_list.get_contacts:
                if contact['name'] == contact_two['name'] and contact['number'] == contact_two['number']:
                    output.append(contact)
        
        return output
