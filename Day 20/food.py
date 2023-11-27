# בס״ד

from turtle import Turtle
from random import choice, randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.shapesize(0.5, 0.5)
        self.color(choice(['green', 'yellow', 'orange', 'blue', 'purple']))
        self.goto(randint(-295, 295), randint(-295, 275))
