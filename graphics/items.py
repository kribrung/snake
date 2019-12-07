import colors
import pygame

class Button():
    def __init__(self, surface, color, position, button_text, font_size, width, height):
        pygame.init()

        self.font_size = font_size
        self.width = width
        self.height = height
        self.x, self.y = position
        self.base_color = color
        self.screen = surface
        self.hovered = False
        self.pressed = False
        self.hovered_color = tuple([color + 100 for color in self.base_color if color <= 245])
        if len(self.hovered_color) < 3:
            self.hovered_color = tuple([color - 100 for color in self.base_color])
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.clicked_color = self.base_color
        self.button_text = button_text

    def _interaction(self):
        if self.x < pygame.mouse.get_pos()[0] < self.x+self.width and self.y < pygame.mouse.get_pos()[1] < self.y + self.height:
            self.hovered = True
        else:
            self.hovered = False

    def draw(self):
        self._interaction()
        color = self.base_color
        if self.hovered:
            color = self.hovered_color
        if self.pressed:
            color = self.clicked_color
        self.text = self.font.render(self.button_text, True, colors.black, color)
        pygame.draw.rect(self.screen, color, (self.x, self.y, self.width, self.height))
        screen.blit(self.text, (self.x,self.y+1))



