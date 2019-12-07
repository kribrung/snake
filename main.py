from graphics.game_graphics import *
from physics.game import *

class Main():

    def __init__(self):

        self.game = Game(400,300)
        self.graphics = Window(self.game, 400, 300, 20)
        self.done = False

    def start_game(self):

        while not self.done:
            self.graphics.draw_game()
            self.game.step()
            self.done = self.game.done

main = Main()
main.start_game()