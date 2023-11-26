import sys
import time
from random import shuffle, randint
from turtle import Turtle, Screen

screen = Screen()
colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
shuffle(colors)
turtles = []
x_pos = -screen.window_width() / 2 + 20
y_pos = screen.window_height() / 2 - 50

is_race_on = True


def blinking_text(turtle_object, message: str, text_color: str) -> None:
    """
    Function to animate text of the turtle.
    :param turtle_object: a turtle object
    :param message: a message to display
    :param text_color: color of the message being displayed
    :return: None
    """
    for i in range(0, 3):
        time.sleep(0.5)
        turtle_object.clear()
        time.sleep(0.5)
        turtle_object.color(text_color)
        turtle_object.write(message, move=False, align="center", font=("Arial", 22, "bold"))


def instruction_line(message: str, *turtles) -> None:
    """
    Function to instruct user how to exit the game
    :param message: a message to display
    :param turtles: turtle objects to be cleared from the screen. Text turtle to be listed as the last
    :return: None
    """
    for turtle in turtles:
        turtle.clear()
    turtles[-1].color('blue')
    turtles[-1].write(message, move=False, align="center", font=("Arial", 22, "bold"))


def end_game(color_of_winner: str, user_bet: str) -> None:
    """
    Main game function.
    :param color_of_winner: color of the winner turtle
    :param user_bet: bet of the user
    :return: None
    """
    winner = Turtle(shape='turtle')
    winner.penup()
    winner.shapesize(2, 2)
    winner.color(color_of_winner)

    text = Turtle()
    text.hideturtle()

    winner.setx(text.xcor())

    if color_of_winner == user_bet:
        winner.sety(text.ycor() + 100)
        blinking_text(text, "Congratulations! You win!!!", 'green')

    else:
        winner.goto(text.xcor() + 50, text.ycor() + 110)
        blinking_text(text, "Winner is\n\n\nSorry... You lose", 'red')
    time.sleep(1)
    screen.clear()
    instruction_line('Click mouse to exit', winner, text)


# Create turtle objects for racing turtles according to the list of provided colors
for color in colors:
    turtle = Turtle(shape='turtle', visible=True)
    turtle.shapesize(1.75, 1.75)
    turtle.penup()
    turtle.color(color)
    turtle.sety(y_pos - (colors.index(color) * screen.window_height() / len(colors)))
    turtle.setx(x_pos)
    turtles.append(turtle)

# User being prompted for the bet until valid value from the list of the colors
valid_color = False
user_guess = ''

while not valid_color:
    if user_guess is None:
        sys.exit()
    elif user_guess.strip().lower() not in colors:
        user_guess = screen.textinput('Make your bet', f'Racing turtles: {", ".join(colors)}\nWhich color will win? ')
    else:
        valid_color = True

# Race code
while is_race_on:
    for runner in turtles:
        if runner.xcor() < (screen.window_width() / 2 - 40):
            runner.forward(randint(1, 20))
        else:
            winner_color = runner.color()[0]
            is_race_on = False

time.sleep(1)
screen.clear()

# Code to show the winner and user's result
end_game(winner_color, user_guess)
screen.exitonclick()
