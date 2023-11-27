# בס״ד
import time
from turtle import Screen

from food import Food
from score_board import ScoreBoard
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
scoreboard.goto(scoreboard.shapesize()[1] / 2, screen.window_height() / 2 - 35)

# Food initialize
food = Food()

# Set up the snake
snake = Snake()

# Making the snake move
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    scoreboard.write(f"Score: {score}", align='center', font=('Arial', 20, 'bold'))
    snake.move()

screen.exitonclick()
