from User import User, freeUser, PremiumUser
    
jordan = freeUser("Jordan", "jordan.edgington.dev@gmail.com", "123456789")
emma = User("Emma", "emma@emmataylor.net", "987654321")

jordan.create_post("This is my first post on the new app!")
jordan.create_post("Post number 2 going up!")
jordan.create_post("Post number 3 going up!")

