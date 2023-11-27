# בס״ד

from turtle import Turtle, Screen

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake game")

# Setup the snake
snake_body = []
home_x = 0
for x in range(3):
    snake_body = Turtle(shape='square')
    snake_body.penup()
    snake_body.color('white')
    snake_body.shapesize(0.5, 0.5)
    snake_body.setx(home_x - 10 * x)



screen.exitonclick()
