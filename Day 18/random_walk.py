import random
from turtle import Turtle, Screen
from random import choice

tim = Turtle()
tim.pensize(5)
tim.speed(100)
colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan',
          'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray']

directions = [0, 90, 180, 270]

for _ in range(1000):
    tim.color(choice(colors))
    tim.forward(random.randint(15, 31))
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
