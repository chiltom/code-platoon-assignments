import random

class GuessingGame():

    def __init__(self,answer):
        self.user_guess = None
        self.answer = answer

    @property
    def get_guess(self):
        return self.user_guess
    
    def guess(self):
       
        if self.user_guess > self.answer:
            return "Too high"
        elif self.user_guess < self.answer:
            return "Too low"
        return "Correct!"
    
    @get_guess.setter
    def set_guess(self,new_guess):
        self.user_guess = int(new_guess)
    

def main():
    win = False
    answer = random.randint(1,100)
    print(answer)

    while win == False:

        user_game = GuessingGame(answer)
        user_game.set_guess = input("Enter your guess: ")
        
        if user_game.guess() == "Too high":
            print("Too high")
        elif user_game.guess() == "Too low":
            print("Too low")
        else:
            print("Correct! You win!")
            win = True


        
if __name__ == "__main__":
    main()