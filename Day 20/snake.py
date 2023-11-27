# בס״ד
from turtle import Turtle

MOVE_DISTANCE = 10


class Snake:
    def __init__(self):
        self.snake_body = []
        self.home_x = 0
        self.make_body()
        self.head = self.snake_body[0]

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_pos = self.snake_body[seg_num - 1].pos()
            self.snake_body[seg_num].goto(new_pos)

        self.snake_body[0].forward(MOVE_DISTANCE)

    def make_body(self):
        for x in range(3):
            segment = Turtle()
            segment.setx(self.home_x - 10 * x)

            segment.shape('square')
            segment.penup()
            segment.color('white')
            segment.shapesize(0.5, 0.5)

            self.snake_body.append(segment)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
