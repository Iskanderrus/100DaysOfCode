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

    def move(self):
        time.sleep(0.1)
        self.setpos(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        speed = self.speed()
        self.speed(speed * 1.01)
        self.x_move *= -1

