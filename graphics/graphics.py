from physics.snake import Snake, Food
from random import randint
from input.input import Input
from eventhandler import *
import pygame

def draw_food(surface, pos, color=(255,255,255)):
    pygame.draw.circle(surface, color, pos, 3)

def draw_snake(surface,Snake):
        for snakebits in Snake.pos:
            pygame.draw.circle(surface,Snake.color,snakebits, 3)

class Game():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_width = 400
        self.screen_height = 300
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))

        self.snake_color = (255,0,255)
        self.snake_speed = 5
        self.snake = Snake(self.snake_color, self.snake_speed)

        self.food = [(50, 50)]
        self.keyboard = Input()

        self.done = False
        self.food = Food(self.screen_width,self.screen_height,self.snake_speed)
    def main(self):
        while not self.done:
            self.screen.fill((0,0,0)) #graphics
            for food_pos in self.food.pos: #graphics
                draw_food(self.screen, food_pos)
            draw_snake(self.screen, self.snake) #graphics
            has_snake_eaten_food(self.snake, self.food)
            self.keyboard.get_input()
            self.snake.move(self.keyboard.input_direction)
            self.clock.tick(20) #graphics
            pygame.display.flip()
            self.done = self.keyboard.quit or is_snake_in_self(self.snake)
        return len(self.snake.pos)

game = Game()
print(game.main())
