import pygame
from physics.snake import Snake
from random import randint

def draw_food(surface, pos, color=(255,255,255)):
    pygame.draw.circle(surface, color, pos, 3)
def draw_snake(surface,Snake):
        for snakebits in Snake.pos:
            pygame.draw.circle(surface,Snake.color,snakebits, 3)

def main():
    screen_width = 400
    screen_height = 300
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    done = False
    snake_color = (255,0,255)
    snake_speed = 5
    clock = pygame.time.Clock()
    food = [(200,200)]
    input_direction = "right"
    snake = Snake(snake_color, start_speed=snake_speed)
    while not done:

        screen.fill((0,0,0))

        if snake.pos[0] in [snake.pos[x] for x in range(1,len(snake.pos))]:
            break

        if snake.pos[0] in food:
            snake.grow_snake(snake_speed*2)
            food.pop()
            food.append(((randint(10, screen_width)//snake_speed)*snake_speed,(randint(10,(screen_height-10))//snake_speed) * snake_speed))
            print(food)
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

                if snake.direction != input_direction:
                    moved = True
                    snake.move(input_direction)

        if not moved:
            snake.move(snake.direction)
        draw_snake(screen,snake)
        clock.tick(20)
        pygame.display.flip()

main()