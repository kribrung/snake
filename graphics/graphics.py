import pygame
from physics.snake import Snake
from random import randint

def draw_food(surface, pos, color=(255,255,255)):
    pygame.draw.circle(surface, color, pos, 3)
def draw_snake(surface,Snake):
        for snakebits in Snake.pos:
            pygame.draw.circle(surface,Snake.color,snakebits, 3)

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    done = False
    snake_color = (255,0,255)
    snake = Snake(snake_color)
    clock = pygame.time.Clock()
    food = [(100,100), (50,50)]
    input_direction = "right"
    while not done:
        screen.fill((0,0,0))

        if snake.pos[0] in [snake.pos[x] for x in range(1,len(snake.pos))]:
            break

        if snake.pos[0] in food:
            snake.grow_snake(10)

        for food_pos in food:
            draw_food(screen, food_pos)
        moved = False
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:
                    input_direction = "up"
                if event.key == pygame.K_s:
                    input_direction = "down"
                if event.key == pygame.K_a:
                    input_direction = "left"
                if event.key == pygame.K_d:
                    input_direction = "right"
                moved = True
                snake.move(input_direction)
        if not moved:
            snake.move(snake.direction)
        draw_snake(screen,snake)
        clock.tick(20)
        pygame.display.flip()

main()