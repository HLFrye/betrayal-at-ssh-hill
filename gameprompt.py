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


