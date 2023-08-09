from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.s_create()
        self.head = self.segments[0]

    def s_create(self):
        for position in POSITION:
            self.add_snake(position)

    def add_snake(self, position):
        mahmut = Turtle("square")
        mahmut.color("white")
        mahmut.penup()
        mahmut.goto(position)
        self.segments.append(mahmut)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(10000, 10000)
        self.segments.clear()
        self.s_create()
        self.head = self.segments[0]

    def extend(self):
        self.add_snake(self.segments[-1].position())

    def s_move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
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