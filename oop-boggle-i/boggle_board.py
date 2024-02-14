import random

class BoggleBoard:
  ROLL_POSSIBILITIES = [
    ['AAEEGN'],
    ['ELRTTY'],
    ['AOOTTW'],
    ['ABBJOO'],
    ['EHRTVW'],
    ['CIMOTU'],
    ['DISTTY'],
    ['EIOSST'],
    ['DELRVY'],
    ['ACHOPS'],
    [['H', 'I', 'M', 'N', 'Qu', 'U']],
    ['EEINSU'],
    ['EEGHNW'],
    ['AFFKPS'],
    ['HLNNRZ'],
    ['DEILRX']]
    
  def __init__(self) -> None:
    self._board = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
  
  @property
  def get_board(self) -> list:
    return self._board
  
  def print_board(self) -> None:
    print(f"{self.get_board[:4]}")
    print(f"{self.get_board[4:8]}")
    print(f"{self.get_board[8:12]}")
    print(f"{self.get_board[12:]}")
          
  def shake(self) -> None:
    roll_possibilities = BoggleBoard.ROLL_POSSIBILITIES.copy()
    for index in range(len(self.get_board)):
      outer_poss_list = random.choice(roll_possibilities)
      inner_poss_index = random.randint(0, 5)
      self._board[index] = outer_poss_list[0][inner_poss_index]
      roll_possibilities.pop(roll_possibilities.index(outer_poss_list))
    self.print_board()

  def include_word(self, word) -> bool:
    # loop through list and grab index and char
        # if char matches word[0]
          # compare to letters to left and right, up and down, and diagonals
    for index, char in enumerate(self.get_board):
      if char == word[0] and index == 0:
        pass
    
    pass


board = BoggleBoard()
board.shake()
