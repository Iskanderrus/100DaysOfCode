import random
from turtle import Turtle, Screen
from random import shuffle, randint

screen = Screen()
colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
shuffle(colors)
turtles = []
x_pos = -screen.window_width() / 2 + 20
y_pos = screen.window_height() / 2 - 30


user_guess = screen.textinput('Make your guess', ' What color will win? ')

for color in colors:
    turtle = Turtle(shape='turtle', visible=True)
    turtle.shapesize(1.75, 1.75)
    turtle.penup()
    turtle.color(color)
    turtle.sety(y_pos - (colors.index(color) * screen.window_height() / len(colors)))
    turtle.setx(x_pos)

while True:
    for runner in turtles:
        if runner.xcor() > screen.window_width():
            runner.forward(randint(1, 20))
        else:
            break


screen.exitonclick()
