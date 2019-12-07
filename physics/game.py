from eventhandler import *
from input.input import *
from physics.snake import *
from random import randint

class Game():
    def __init__(self, screen_width,screen_height):
        self.snake_color = (255,0,255)
        self.snake_speed = 5
        self.snake = Snake(self.snake_color, self.snake_speed)
        self.keyboard = Input()
        self.food = Food(screen_width,screen_height,self.snake_speed)
        self.done = False
    def step(self):
        has_snake_eaten_food(self.snake, self.food)
        self.done = has_snake_crashed(self.snake)
        self.keyboard.get_input()
        self.snake.move(self.keyboard.input_direction)


class Food():
    def __init__(self, screen_width, screen_height, snake_speed):
        self.pos = [(50,50)]
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.snake_speed = snake_speed

    def make_new_food(self):
        self.pos.pop()
        self.pos.append(((randint(10, self.screen_width)//self.snake_speed)*self.snake_speed,(randint(10,(self.screen_height-10))//self.snake_speed) * self.snake_speed))

