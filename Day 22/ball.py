# בס״ד

from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(2)
        self.color('white')
        self.penup()
        self.shape('circle')
        self.shapesize(1, 1)

    def move(self):
        self.forward(10)

