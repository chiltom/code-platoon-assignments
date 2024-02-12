# your improved User class goes here
class User:
    POST_HISTORY = []
    users = 0
    
    def __init__(self, name, email, dl_number):
        User.users += 1
        self._id = User.users
        self._name = name
        self._email = email
        self._dl_number = dl_number
        self._post_number = 0
        
        # Make account construction post
        User.POST_HISTORY.append({f'{self._name}': 'Initial Post'})
    
    def __str__(self):
        return f"I am {self._name}, my email is {self._email}, and my driver's license number is {self._dl_number}"
    
    def __repr__(self):
        return str(self)
    
    @property
    def get_id(self):
        return self._id
    
    @property
    def get_name(self):
        return self._name
    
    def add_user_post(self, new_post):
        User.POST_HISTORY.append({f'{self._name}': f'{new_post}'})
        self._post_number += 1
        
    # Work on this
    def delete_user_post(self, desired_post):
        for dictionary in User.POST_HISTORY:
            if self.get_name in dictionary and dictionary.values() == desired_post:
                User.POST_HISTORY.pop(dictionary)

    def print_user_post_history(self):
        for dictionary in User.POST_HISTORY:
            if self.get_name in dictionary:
                print(dictionary)
            else:
                continue
                
    @classmethod
    def print_all_post_history(cls):
        for dictionary in cls.POST_HISTORY:
            print(dictionary)
        
    
nick = User("Nick", "nick@pizzapalace.org", 12345)
ian = User("Ian", "ian@pizzapalace.org", 13456)
brian = User("Brian", "brian@pizzapalace.org", 14567)

nick.add_user_post('I like dogs')
nick.add_user_post('And I like cats')
ian.add_user_post('Well I hate cats')

# nick.print_user_post_history()
# print("\n")
# ian.print_user_post_history()
# print("\n")
# brian.print_user_post_history()
# print("\n")
# User.print_all_post_history()

nick.delete_user_post('Initial Post')
nick.print_user_post_history()