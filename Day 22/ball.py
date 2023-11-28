# בס״ד
import time
from turtle import Turtle
from random import choice

SPEED = 2
COLORS = ['green', 'yellow', 'orange', 'blue', 'purple', 'red', 'pink', 'tomato', 'skyblue', 'white smoke', 'violet']


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(SPEED)
        self.color(choice(COLORS))
        self.penup()
        self.shape('circle')
        self.shapesize(1, 1)

        self.x_move = 10
        self.y_move = 10
        self.sleep_time = 0.1

    def move(self):
        self.setpos(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.color(choice(COLORS))
        self.sleep_time *= 0.95
        self.x_move *= -1

    def new_ball(self):
        self.goto(0, 0)
        self.sleep_time = 0.1
        self.move()
