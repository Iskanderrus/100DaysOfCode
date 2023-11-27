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
        while (self.head.xcor() in range(-300, 300)) and (self.head.ycor() in range(-300, 300)):
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
        self.snake_body[0].shape('circle')
        self.snake_body[0].shapesize(0.75, 1)
        self.snake_body[0].color('green')

        self.snake_body[-1].shape('circle')
        self.snake_body[-1].shapesize(0.5, 0.75)

    def up(self):
        if self.head.heading() != 270 and self.head.heading() != 90:
            self.head.setheading(90)
            self.tail_adjustment()

    def down(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(270)
            self.tail_adjustment()

    def left(self):
        if self.head.heading() != 0 and self.head.heading() != 180:
            self.head.setheading(180)
            self.tail_adjustment()

    def right(self):
        if self.head.heading() != 180 and self.head.heading() != 0:
            self.head.setheading(0)
            self.tail_adjustment()

    def tail_adjustment(self):
        width = self.snake_body[-1].shapesize()[0]
        length = self.snake_body[-1].shapesize()[1]
        self.snake_body[-1].shapesize(length, width)
