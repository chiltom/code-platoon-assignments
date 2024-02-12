# your User class goes here

class User:
    
    def __init__(self, name, email, dl_number):
        self.name = name
        self.email = email
        self.dl_number = dl_number
    
    def __str__(self):
        return f"I am {self.name}, my email is {self.email}, and my driver's license number is {self.dl_number}"
    
    def __repr__(self):
        return str(self)
    
user1 = User("Nick", "nick@pizzapalace.org", 12345)
user2 = User("Ian", "ian@pizzapalace.org", 13456)
user3 = User("Brian", "brian@pizzapalace.org", 14567)

employees = [user1, user2, user3]
for employee in employees:
    print(employee)