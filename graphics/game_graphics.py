import pygame

class Window():
    def __init__(self, Game, screen_width,screen_height, fps):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen_width = screen_width
        self.screen_heigth = screen_height
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_heigth))
        pygame.display.set_caption('Snake')
        self.food_color = (255,255,255)
        self.game = Game
        self.fps = fps

    def draw_game(self):
        self.screen.fill((0,0,0))
        self.draw_food()
        self.draw_snake()
        self.clock.tick(self.fps)
        pygame.display.flip()

    def draw_food(self):
        for pos in self.game.food.pos:
            pygame.draw.circle(self.screen, self.food_color, pos, 3)

    def draw_snake(self):
        for snakebit in self.game.snake.pos:
            pygame.draw.circle(self.screen, self.game.snake_color, snakebit, 3)



