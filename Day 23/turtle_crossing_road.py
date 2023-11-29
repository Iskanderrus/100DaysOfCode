# בס״ד

from turtle import Screen
from crossing_turtle import CrossingTurtle

# Create the screen
screen = Screen()
screen.screensize(600, 600, 'white')
screen.title('Turtle Crossing Road')

# Create a turtle
tim = CrossingTurtle((screen.window_width(), screen.window_height()))

# Add event listeners
screen.listen()
screen.onkeypress(tim.up, "Up")


screen.exitonclick()