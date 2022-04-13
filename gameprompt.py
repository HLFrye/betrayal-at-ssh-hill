from cmd import Cmd

class GamePrompt(Cmd):
    prompt = "Game>"
    intro = "Welcome to Betrayal at SSH Hill!"

    def do_exit(self, inp):
        print("Farewell!")
        return True


