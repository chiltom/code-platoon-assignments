# You should re-use and modify your old BoggleBoard class to support the new requirements
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
    self._board = []
    for _ in range(4):
      self._board.append(['_', '_', '_', '_'])
  
  @property
  def get_board(self) -> list:
    return self._board
  
  def print_board(self) -> None:
    for row in self.get_board:
      print(f'{" ".join(row)}')

  def shake(self) -> None:
    roll_possibilities = BoggleBoard.ROLL_POSSIBILITIES.copy()
    for row in self.get_board:
      for index in range(len(row)):
        outer_list = random.choice(roll_possibilities)
        inner_index = random.randint(0, 5)
        row[index] = outer_list[0][inner_index]
        roll_possibilities.pop(roll_possibilities.index(outer_list))
    self.print_board()
    
  def include_word(self):
    pass