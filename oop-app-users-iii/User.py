class User:
    def __init__(self, name, email_address, dln, posts=[]):
        self.name = name
        self.email = email_address
        self.dln = dln
        self.posts = posts

    def __str__(self):
        return f"{self.name}'s email address is {self.email} and their driver's license number is {self.dln}"

    def send_message(self, user):
        return f"Sending a message to {user.name} at {user.email}"

    def create_post(self, message):
        print(message)
        self.posts.append(message)

    def view_posts(self):
        for post in range(0, len(self.posts)):
            print(self.posts[post])

    def del_post(self, post_index):
        self.posts.remove(self.posts[post_index])

#these should inherit the add_user method
class PremiumUser(User):
    def __init__(self, name, email_address, dln):
        super().__init__(name, email_address, dln)

class freeUser(User):
    def __init__(self, name, email_address, dln):
        super().__init__(name, email_address,dln)
        self.post_count = 0

    def create_post(self, message):
        if self.post_count >= 2:
            print("You have run out of posts. Upgrade to a premium user to earn unlimited posts.")
        else:
            User.create_post(self, message)
            self.post_count += 1