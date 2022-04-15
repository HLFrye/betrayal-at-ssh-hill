from cmd import Cmd
from player import Player
from board import Board

class GamePrompt(Cmd):
    prompt = "Game>"
    board = Board()
    player = Player()
    intro = board.get_room(player.pos).description() 
    
    def do_exit(self, inp):
        print("Farewell!")
        return True

    def do_look(self, inp):
        print("You look, but don't find anything")
    
    def do_search(self, inp):
        print("After searching the room, you come up empty")

    def do_walk(self, inp):
        try:
          self.player.move(inp)
          new_pos = self.player.pos
          room = self.board.get_room(new_pos)
          print(room.description())
        except: 
          print("A mysterious force blocks you")
