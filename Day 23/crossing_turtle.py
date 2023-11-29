# בס״ד
from random import choice
from turtle import Turtle

COLORS = ['green', 'yellow', 'orange', 'blue', 'purple', 'red', 'pink', 'tomato', 'violet']


class CrossingTurtle(Turtle):
    def __init__(self, screen_size: tuple):
        super().__init__()
        self.x_cor = 0
        self.y_cor = -screen_size[1]/2 + 20
        self.turtle_setup()

    def turtle_setup(self):
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.color(choice(COLORS))
        self.goto(self.x_cor, self.y_cor)

    def up(self):
        self.forward(10)
