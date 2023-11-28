# בס״ד

from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(10)
        self.color('white')
        self.penup()
        self.shape('circle')
        self.shapesize(1, 1)