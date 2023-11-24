import random
import turtle
from turtle import Turtle, Screen
from random import choice

turtle.colormode(255)
tim = Turtle()

tim.speed(100)
tim.pensize(1)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


angle = 5
for x in range(int(360 / angle)):
    tim.left(angle)
    tim.color(random_color())
    tim.circle(120)

screen = Screen()
screen.exitonclick()
