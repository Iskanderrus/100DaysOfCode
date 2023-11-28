# בס״ד

from turtle import Turtle, Screen
from paddle import Paddle
from delimiter import Delimiter
from scoreboard import Scoreboard
from ball import Ball

# Create and customize the screen
screen = Screen()
screen.bgcolor('black')
screen.screensize(600, 600)
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




screen.exitonclick()