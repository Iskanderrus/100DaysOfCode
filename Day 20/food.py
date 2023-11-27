# בס״ד

from turtle import Turtle
from random import choice, randint


COLORS = ['green', 'yellow', 'orange', 'blue', 'purple', 'red', 'pink', 'tomato', 'skyblue', 'white smoke', 'violet']

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        self.color(choice(COLORS))
        self.refresh()

    def refresh(self):
        self.color(choice(COLORS))
        self.goto(randint(-280, 280), randint(-280, 280))
