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
  # need a argument of letters that is default a list of all letters capitalized
  def __init__(self) -> None:
    self._board = []
    for _ in range(4):
      self._board.append(['_', '_', '_', '_'])
  
  @property
  def get_board(self) -> list:
    return self._board
  
  def print_board(self) -> None:
    for row in self.get_board:
      print(f'{" ".join(row)}')
    #nested loop to access the sub-list items
    #randomly select a letter from ALPHA_LIST and change the underscore to it
      
    # prints a random value from the list
    #list1 = [1, 2, 3, 4, 5, 6]
    #print(random.choice(list1))
      
  def shake(self) -> None:
    #set this to numbered list from 0-15
    roll_possibilities = BoggleBoard.ROLL_POSSIBILITIES.copy()
    for row in self.get_board:
      for index in range(len(row)):
        outer_list = random.choice(roll_possibilities)
        inner_index = random.randint(0, 5)
        row[index] = outer_list[0][inner_index]
        roll_possibilities.pop(roll_possibilities.index(outer_list))
    self.print_board()

