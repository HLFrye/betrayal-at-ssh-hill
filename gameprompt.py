from cmd import Cmd
from player import Player
from board import Board
import traceback

class GamePrompt(Cmd):
    prompt = "Game> "
    board = Board()
    player = Player()
    intro = board.get_room(player.pos).description() 
    
    def do_exit(self, inp):
        print("Farewell!")
        return True

    def do_look(self, inp):
        room = self.board.get_room(self.player.pos)
        print(f"You are in the {room.name()}")
        print("")
        print(room.description())
        print("")
        print(f"There are exits to the {', '.join(room.exits)}")

    def do_search(self, inp):
        print("After searching the room, you come up empty")

    def do_walk(self, inp):
        old_pos = self.player.pos
        try:
          self.player.move(inp)
          new_pos = self.player.pos
          room = self.board.move_to_room(new_pos, inp)
          print(room.description())
        except:
          print("We had an ooopsie doodle")
          traceback.print_exc()
          self.player.pos = old_pos
          print("A mysterious force blocks you")
