from turtle import Turtle

STARTING_POSITIONS = [(-10, 10), (-30, 10), (-50, 10)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self._create_snake()
        self.head = self.segments[0]

    def _create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def add_square(self, position):
        new_square = Turtle("square")
        new_square.penup()
        new_square.setpos(position)
        self.segments.append(new_square)

    def extend(self):
        self.add_square(self.segments[-1].position())

    def move(self):
        for square_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[square_num - 1].xcor()
            new_y = self.segments[square_num - 1].ycor()
            self.segments[square_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

  

    
