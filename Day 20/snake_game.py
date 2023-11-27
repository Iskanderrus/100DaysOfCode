# בס״ד
import time
from turtle import Screen

from food import Food
from score_board import ScoreBoard
from snake import Snake


# Screen setup
def create_screen():
    screen_instance = Screen()
    screen_instance.setup(width=600, height=600)
    screen_instance.bgcolor('black')
    screen_instance.title("Snake game")
    screen_instance.tracer(0)
    return screen_instance


screen = create_screen()
user_name = screen.textinput("Provide your name", "What is your name?")

# Scoreboard initialization
scoreboard = ScoreBoard(user_name=user_name)

# Food initialize
food = Food()

# Set up the snake
snake = Snake()
screen.listen()

# Making the snake move
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    food_color = food.color()[0]

    if snake.is_collided_with(food):
        snake.grow()
        for section in snake.snake_body[1:]:
            section.color(food_color)
        snake.snake_speed *= 1.001
        scoreboard.increase_score()

        food.refresh()
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        screen.clear()
        create_screen()
        scoreboard.game_over()

    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            screen.clear()
            create_screen()
            scoreboard.game_over()

screen.exitonclick()
