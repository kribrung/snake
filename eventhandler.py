def has_snake_crashed(Snake):
    if Snake.pos[0] in [Snake.pos[x] for x in range(1, len(Snake.pos))]:
        return True
    else:
        return False
def has_snake_eaten_food(Snake,Food):
    if Snake.pos[0] in Food.pos:
        Snake.grow_snake(Snake.speed)
        Food.make_new_food()


