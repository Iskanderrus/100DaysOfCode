# בס״ד
import time
from turtle import Turtle
from random import randint

SPEED = 2

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(SPEED)
        self.color('white')
        self.penup()
        self.shape('circle')
        self.shapesize(1, 1)

        self.x_move = 10
        self.y_move = 10
        self.sleep_time = 0.1

    def move(self):
        time.sleep(self.sleep_time)
        self.setpos(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.sleep_time *= 0.99
        self.x_move *= -1

    def new_ball(self):
        self.goto(0, 0)
        self.move()