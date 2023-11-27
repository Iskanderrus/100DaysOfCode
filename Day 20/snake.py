# בס״ד
from turtle import Turtle


class Snake:
    def __init__(self):
        super().__init__()
        self.segment = None
        self.snake_body = []
        self.home_x = 0
        for x in range(3):
            self.eat(x)

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_pos = self.snake_body[seg_num - 1].pos()
            self.snake_body[seg_num].goto(new_pos)

        self.snake_body[0].forward(10)

    def eat(self, x):
        self.segment = Turtle()
        self.segment.setx(self.home_x - 10 * x)

        self.segment.shape('square')
        self.segment.penup()
        self.segment.color('white')
        self.segment.shapesize(0.5, 0.5)

        self.snake_body.append(self.segment)
