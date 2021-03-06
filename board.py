from room import RoomData, load_all_rooms
from fates import load_all_fates
from item import load_all_items
from playedroom import PlayedRoom
from random import randint


def orient_room(board, played_room, coords, drn):
  exit_dir = ""
  match drn:
    case "east":
      exit_dir = "west"
    case "west":
      exit_dir = "east"
    case "north":
      exit_dir = "south"
    case "south":
      exit_dir = "north"

  all_other_dirs = ["north", "south", "east", "west"]
  all_other_dirs.remove(exit_dir)
  other_exits = all_other_dirs[:(played_room.data.num_exits - 1)]
  played_room.exits = [exit_dir, *other_exits]

class Deck:
  def __init__(self, cards, top=None):
    self.cards = cards
    self.top = top or cards[0].name

  def get_next(self):
    room = list(filter(lambda x: x.name == self.top, self.cards))[0]
    self.cards.remove(room)
    self.top = self.cards[randint(0, len(self.cards) - 1)].name
    return room

class Board:
  def __init__(self):
    self.rooms = Deck(load_all_rooms(), "Grand Hallway")
    self.items = Deck(load_all_items())
    self.fates = Deck(load_all_fates())


    self.spaces = {
      (0, 0): PlayedRoom(self.rooms.get_next(), None, None, None)
    }

  def get_room(self, coords):
    if coords not in self.spaces:
      room = self.rooms.get_next()
      fate = self.fates.get_next() if randint(0, 10) == 0 else None
      item = self.items.get_next if randint(0, 5) == 0 else None
      played_room = PlayedRoom(self.rooms.get_next(), None, item, fate)
      orient_room(self, played_room, coords)
      self.spaces[coords] = played_room
    return self.spaces.get(coords)

  def move_to_room(self, coords, drn):
    if coords not in self.spaces:
      room = self.rooms.get_next()
      fate = self.fates.get_next() if randint(0, 10) == 0 else None
      item = self.items.get_next if randint(0, 5) == 0 else None
      played_room = PlayedRoom(self.rooms.get_next(), None, item, fate)
      orient_room(self, played_room, coords, drn)
      self.spaces[coords] = played_room
    return self.spaces.get(coords)
    
