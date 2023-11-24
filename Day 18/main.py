from turtle import Turtle, Screen
from random import choice, randint

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')
timmy.pensize(width=5)
directions = ['left', 'right']
colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan',
          'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray']
timmy.penup()
timmy.sety(450)
timmy.pendown()


def draw_figure(sides):
    angle = 360 / x
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle=angle)


for x in range(3, 16):
    timmy.color(choice(colors))
    draw_figure(x)

screen = Screen()
screen.exitonclick()
