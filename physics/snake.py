import operator


class Snake():
    ###definiing a object snake. when it has not eaten food it's size is 2 since one would not be a snake!
    def __init__(self, color = (255,255,255), start_length = 10, start_speed = 5, right_bound=400, bottom_bound = 300 ):
        self.right_bound = right_bound
        self.left_bound = 0
        self.bottom_bound = bottom_bound
        self.top_bound = 0
        self.color = color
        self.speed = start_speed                               # The snake's current speed. will be able to decide how much an snake moves in a frame by this. the tempo will be decided by the fps.
        self.pos = [(x,0) for x in range(start_length, 0, -1)]                         # Array of tuples concerning what positions the snake is currently occupying.
        self.direction = "right"                        # Direction of travel, this is to prevent a snake going to lets say right, suddenly turning to the left.
    def move(self, input_direction):
        ###changes the self.pos to reflect the movement of the snake.###
        for pos_index in range(len(self.pos)-1,0,-1):
            self.pos[pos_index] = self.pos[pos_index-1]     # Updates the position of the snakebits from back to front. only the head is dependent on the input.

        if input_direction == "up" and not self.direction == "down":
            self.direction = "up"
            self.pos[0] = self._add_tuples(self.pos[0], (0, -self.speed))

        if input_direction == "down" and not self.direction == "up":
            self.direction = "down"
            self.pos[0] = self._add_tuples(self.pos[0], (0, self.speed))

        if input_direction == "left" and not self.direction == "right":
            self.direction = "left"
            self.pos[0] = self._add_tuples(self.pos[0], (-self.speed,0))

        if input_direction == "right" and not self.direction == "left":
            self.direction = "right"
            self.pos[0] = self._add_tuples(self.pos[0], (self.speed,  0))

        x, y = self.pos[0]
        if x > self.right_bound:
            x = self.left_bound
        if x < self.left_bound:
            x = self.right_bound
        if y > self.bottom_bound:
            y = self.top_bound
        if y < self.top_bound:
            y = self.bottom_bound
        self.pos[0] = (x,y)



    def _add_tuples(self, tuple_1, tuple_2): # Should maybe be moved to a tools library. remember it needs the import operator to work.
        ### used to improve readability. ###
        return tuple(map(operator.add,tuple_1,tuple_2))
    def grow_snake(self, growthlength):
        ### what happens when the snake eats food. ###
        for _ in range(growthlength):
            self.pos.append((-10,-10))
