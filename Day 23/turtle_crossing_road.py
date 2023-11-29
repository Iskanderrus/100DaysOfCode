# בס״ד
import time
from turtle import Screen
from cars import Cars
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

# Add cars
cars = Cars(screen_dimensions)

# Add event listeners
screen.listen()
screen.onkeypress(tim.up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    cars.move_cars()

    # Scoring
    if tim.ycor() >= screen_dimensions[1] / 2:
        tim.turtle_setup()
        scoreboard.update_score()
        cars.level_up()

    for car in cars.cars:
        if car.distance(tim) < 17:
            game_on = False
            turtle_color = tim.color()[0]
            car_color = car.color()[0]
            screen.clear()
            scoreboard.game_over(turtle_color=turtle_color, car_color=car_color)

screen.exitonclick()
