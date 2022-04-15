from room import RoomData, load_all_rooms
from playedroom import PlayedRoom
from random import randint

class Deck:
  def __init__(self):
    self.rooms = load_all_rooms()
    self.top = "Grand Hallway"

  def get_next(self):
    room = list(filter(lambda x: x.name == self.top, self.rooms))[0]
    self.rooms.remove(room)
    self.top = self.rooms[randint(0, len(self.rooms) - 1)].name
    return room

class Board:
  def __init__(self):
    self.deck = Deck()

    self.spaces = {
      (0, 0): PlayedRoom(self.deck.get_next(), None, None, None)
    }

  def get_room(self, coords):
    if coords not in self.spaces:
      self.spaces[coords] = PlayedRoom(self.deck.get_next(), None, None, None)

    return self.spaces.get(coords)

    
