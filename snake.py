import operator


class Snake():
    ###definiing a object snake. when it has not eaten food it's size is 2 since one would not be a snake!
    def __init__(self):
        self.length = 2
        self.speed = 1                                      # The snake's current speed. will be able to decide how much an snake moves in a frame by this. the tempo will be decided by the fps.
        self.pos = [ (0,1), (0,0) ]                         # Array of tuples concerning what positions the snake is currently occupying.
        self.direction = "right"                            # Direction of travel, this is to prevent a snake going to lets say right, suddenly turning to the left.
    def move(self, input_direction):
        ###changes the self.pos to reflect the movement of the snake.###
        for pos_index in range(len(self.pos)-1,0,-1):
            self.pos[pos_index] = self.pos[pos_index-1]     # Updates the position of the snakebits from back to front. only the head is dependent on the input.

        if input_direction == "up":
            self.pos[0] = self._add_tuples(self.pos[0], (-self.speed, 0))
        if input_direction == "down":
            self.pos[0] = self._add_tuples(self.pos[0], (self.speed,  0))
        if input_direction == "left":
            self.pos[0] = self._add_tuples(self.pos[0], (0, -self.speed))
        if input_direction == "right":
            self.pos[0] = self._add_tuples(self.pos[0], (0,  self.speed))


    def _add_tuples(self, tuple_1, tuple_2): # Should maybe be moved to a tools library. remember it needs the import operator to work.
        ### used to improve readability. ###
        return tuple(map(operator.add,tuple_1,tuple_2))
    def _grow_snake(self):
        ### what happens when the snake eats food. ###
        pass