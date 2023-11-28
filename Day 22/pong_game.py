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
screen.screensize()
screen.tracer(0)
screen_delimiter = Delimiter(screen.window_height() / 2)
user1 = screen.textinput("Welcome to Ping Pong!", "What is your name?").strip().title()
user2 = screen.textinput("Welcome to Ping Pong!", "What is your name?").strip().title()
screen.title(f"{user1} -*-*-*-*- Ping Pong -*-*-*-*- {user2}")

# Create paddles
paddle1 = Paddle('left', screen.window_width(), screen.window_height())
paddle2 = Paddle('right', screen.window_width(), screen.window_height())

# Create scoreboard
scoreboard = Scoreboard(
    screen_dimensions=(screen.window_width(), screen.window_height()),
    user1=user1,
    user2=user2
)

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
    if (ball.ycor() > (screen.window_height() / 2 - 20) or
            ball.ycor() < (-screen.window_height() / 2 + 20)):
        ball.bounce_y()

    # Collision with the paddles
    if (ball.distance(paddle2) < 70 and
            ball.xcor() > (screen.window_width() / 2 - 40)):
        paddle2.color(ball.color()[0])
        ball.bounce_x()

    elif (ball.distance(paddle1) < 70 and
          ball.xcor() < (-screen.window_width() / 2 + 40)):
        paddle1.color(ball.color()[0])
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

    # Color management
    if ball.color()[0] == paddle1.color()[0] == paddle2.color()[0]:
        scoreboard.color(ball.color()[0])
    else:
        scoreboard.color('white')

    # Finishing the game
    if max(scoreboard.scores) == 15:
        for segm in screen_delimiter.delimiter:
            segm.hideturtle()
        ball.hideturtle()
        paddle1.hideturtle()
        paddle2.hideturtle()
        scoreboard.clear()
        screen.update()
        game_on = scoreboard.end_game()

screen.exitonclick()
