# בס״ד

from turtle import Turtle
from random import choice


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.shapesize(0.35, 0.35)
        self.color(choice(['green', 'yellow', 'orange', 'blue', 'purple']))

