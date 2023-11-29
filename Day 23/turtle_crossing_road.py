# בס״ד

from turtle import Screen
from crossing_turtle import CrossingTurtle
from scoreboard import ScoreBoard

# Create the screen
screen = Screen()
screen.screensize(600, 600, 'white')
screen_dimensions = (screen.window_width(), screen.window_height())
screen.title('Turtle Crossing Road')
screen.tracer(0)

# Create a turtle
tim = CrossingTurtle(screen_dimensions)

# Add Scoreboard
scoreboard = ScoreBoard(screen_dimensions)

# Add event listeners
screen.listen()
screen.onkeypress(tim.up, "Up")

game_on = True
while game_on:
    screen.update()
    # Scoring
    if tim.ycor() >= screen_dimensions[1] / 2:
        tim.turtle_setup()
        scoreboard.update_score()

screen.exitonclick()