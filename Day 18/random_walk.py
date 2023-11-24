import random
import turtle
from turtle import Turtle, Screen
from random import choice

turtle.colormode(255)
tim = Turtle()

tim.pensize(10)
tim.speed(10)
directions = [0, 90, 180, 270]


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


for _ in range(1000):
    tim.pencolor(random_color())
    tim.forward(random.randint(15, 31))
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
