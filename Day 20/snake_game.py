# בס״ד
import time
from random import randint
from turtle import Turtle, Screen
from score_board import ScoreBoard
from food import Food
from snake import Snake


score = 0

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake game")
screen.tracer(0)

# Scoreboard initialization
scoreboard = ScoreBoard()
scoreboard.goto(scoreboard.shapesize()[1] / 2, screen.window_height()/2 - 35)

# Food initialize
food = Food()

# Set up the snake
snake_body = []
home_x = 0

for x in range(3):
    segment = Snake()
    segment.setx(home_x - 10 * x)
    snake_body.append(segment)

# Making the snake move
game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    scoreboard.write(f"Score: {score}", align='center', font=('Arial', 20, 'bold'))
    for seg_num in range(len(snake_body) - 1, 0, -1):
        new_pos = snake_body[seg_num - 1].pos()
        snake_body[seg_num].goto(new_pos)

    snake_body[0].forward(10)


screen.exitonclick()
