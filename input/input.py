import pygame


class Input():
    def __init__(self):
        pygame.init()
        self.input_direction = "right"
        self.quit = False
    def get_input(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w and self.input_direction != "down":
                    self.input_direction = "up"
                if event.key == pygame.K_s and self.input_direction != "up":
                    self.input_direction = "down"
                if event.key == pygame.K_a and self.input_direction != "right":
                    self.input_direction = "left"
                if event.key == pygame.K_d and self.input_direction != "left":
                    self.input_direction = "right"
