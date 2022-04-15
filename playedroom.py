from enum import Enum

class MoveDirection(Enum):
  NORTH = 1
  SOUTH = 2
  EAST = 3
  WEST = 4
  UP = 5
  DOWN = 6

class PlayedRoom:
  def __init__(self, data, enter_from, item, fate):
    self.data = data
    self.item = item
    self.fate = fate
    self.enter_from = enter_from

  def description(self):
    return self.data.enter_text

  def name(self):
    return self.data.name

  def move(self, direction: MoveDirection):
    pass

  
