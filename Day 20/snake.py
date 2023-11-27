# בס״ד
from turtle import Turtle


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(0.5, 0.5)
