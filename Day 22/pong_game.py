# בס״ד

from turtle import Turtle, Screen
from paddle import Paddle

# Create and customize the screen
screen = Screen()
screen.bgcolor('black')
screen.screensize(600, 600)
# user1 = screen.textinput("Welcome to Ping Pong!", "What is your name?").strip().title()
# user2 = screen.textinput("Welcome to Ping Pong!", "What is your name?").strip().title()
# screen.title(f"{user1} -*-*-*-*- Ping Pong -*-*-*-*- {user2}")
#

# Create paddles
paddle1 = Paddle('left', screen.window_width(), screen.window_height())
paddle2 = Paddle('right', screen.window_width(), screen.window_height())

# Make screen listen to events
screen.listen()

screen.onkeypress(paddle1.up, "a")
screen.onkeypress(paddle1.down, "z")

screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")




screen.exitonclick()