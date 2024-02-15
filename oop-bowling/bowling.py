from player import Player
from frame import Frame
from random import *

class Game:

    PLAYERS = {}
    
    def __init__(self) -> None:
        self._frames = 0
        while True:
            user_input = input("Enter player name. If no more players, input Exit: ").title()
            
            if user_input != 'Exit':
                new_player = Player(user_input)
                Game.PLAYERS[user_input] = new_player
                continue
            else:
                break
                
    @property
    def get_frames(self) -> int:
        return self._frames
    
    
    def play(self) -> None:
        print("Let's Play!")
        # First 9 frames
        while self.get_frames <= 9:
            # Start new frame
            self._frames += 1
            # For each player, play a frame
            for player in self.PLAYERS:
                strike, spare = False, False
                roll_one = random.randint(1, 10)
                # If roll_one is a strike, set strike to True and skip second roll
                if roll_one == 10:
                    strike = True
                # If roll_one is not a strike, roll again with remaining pins
                else:
                    roll_two = random.randint(1, 10 - roll_one)
                new_score = roll_one + roll_two
                # If roll_two added up to a spare, set spare to True
                if roll_one != 10 and new_score == 10:
                    spare = True
                # Create frame instance and append it to player
                frame = Frame(self._frames, new_score, spare, strike)
                player.add_frame(frame)
                # If previous frame was a strike, add value of both rolls to it
                if player.get_frames[self._frames - 1].is_strike == True:
                    player.get_frames[self._frames - 1].add_score(new_score)
                # If previous frame was a spare, add value of first roll to it
                elif player.get_frames[self._frames - 1].is_spare == True:
                    player.get_frames[self._frames - 1].add_score(roll_one)
                # TODO: If score is not automatically updated from previous frames, delay score addition in Player class with a method or within add_frame method
        # Play 10th frame
        for player in self.PLAYERS:
            strike, spare = False, False
            roll_one = random.randint(1, 10)
            # If roll_one is a strike, set strike to True but continue rolling
            if roll_one == 10:
                strike = True
            # Account for if first roll was a strike or not and play second roll
            roll_two = None
            if strike == True:
                roll_two = random.randint(1, 10)
            else:
                roll_two = random.randint(1, 10 - roll_one)
            # Account for if previous frame was strike or spare
            if player.get_frames[self._frames - 1].is_strike == True:
                player.get_frames[self._frames - 1].add_score(roll_one + roll_two)
            elif player.get_frames[self._frames - 1].is_spare == True:
                player.get_frames[self._frames - 1].add_score(roll_one)
            # Play third roll and account for prior pin counts
            roll_three = None
            if roll_one + roll_two >= 10 and strike == False:
                spare = True
                roll_three = random.randint(1, 10)
            elif strike == True and roll_two < 10:
                roll_three = random.randint(1, 10 - roll_two)
            elif strike == False and roll_one + roll_two < 10:
                roll_three = random.randint(1, 10 - (roll_one + roll_two))
            
                
            
        
                



            
            

game = Game()
print(game.PLAYERS)
