# בס״ד
import time
from turtle import Screen

from ball import Ball
from delimiter import Delimiter
from paddle import Paddle
from scoreboard import Scoreboard

# Create and customize the screen
screen = Screen()
screen.bgcolor('black')
screen.screensize(600, 600)
screen.tracer(0)
screen_delimiter = Delimiter(screen.window_height()/2)
user1 = screen.textinput("Welcome to Ping Pong!", "What is your name?").strip().title()
user2 = screen.textinput("Welcome to Ping Pong!", "What is your name?").strip().title()
screen.title(f"{user1} -*-*-*-*- Ping Pong -*-*-*-*- {user2}")

#

# Create paddles
paddle1 = Paddle('left', screen.window_width(), screen.window_height())
paddle2 = Paddle('right', screen.window_width(), screen.window_height())

# Create scoreboard
scoreboard = Scoreboard(user1=user1, user2=user2)

# Create ball
ball = Ball()

# Make screen listen to events
screen.listen()

screen.onkeypress(paddle1.up, "a")
screen.onkeypress(paddle1.down, "z")

screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")


game_on = True
while game_on:
    screen.update()
    ball.move()

    # Collision with the upper and lower walls
    if ball.ycor() > (screen.window_height() / 2 - 20) or ball.ycor() < (-screen.window_height() / 2 + 20):
        ball.bounce_y()

    # Collision with the paddles
    if ((ball.distance(paddle2) < 70 and ball.xcor() > (screen.window_width() / 2 - 40)) or
            (ball.distance(paddle1) < 70 and ball.xcor() < (-screen.window_width() / 2 + 40))):
        ball.bounce_x()

    # Scoring
    elif ball.xcor() < (-screen.window_width() / 2):
        scoreboard.increase_score(user2)
        time.sleep(1)
        ball.new_ball()
    elif ball.xcor() > (screen.window_width() / 2):
        scoreboard.increase_score(user1)
        time.sleep(1)
        ball.new_ball()






screen.exitonclick()
