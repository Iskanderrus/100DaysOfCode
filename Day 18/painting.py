import turtle
from turtle import Turtle, Screen
from random import randint

turtle.colormode(255)
screen = Screen()


def random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def walk_pattern(turtle_object, height, width, step):
    for y in range(0, int(height/step)):
        if y % 2 == 0:
            turtle_object.setheading(0)
        else:
            turtle_object.setheading(180)
        for x in range(0, width, step):
            turtle_object.color(random_color())
            turtle_object.dot(int(step / 2))
            turtle_object.penup()
            turtle_object.forward(step)
            turtle_object.dot(int(step / 2))

        turtle_object.sety(turtle_object.ycor() - step)


tim = Turtle()
tim.hideturtle()
tim.speed(100)
tim.penup()
tim.sety(400)
tim.setx(-460)

walk_pattern(tim, screen.window_height(), screen.window_width(), 60)


print()
print()

screen.exitonclick()
