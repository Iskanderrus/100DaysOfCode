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


def blinking_text(turtle_object, message, text_color):
    for i in range(0, 3):
        time.sleep(0.5)
        turtle_object.clear()
        time.sleep(0.5)
        turtle_object.color(text_color)
        turtle_object.write(message, move=False, align="center", font=("Arial", 22, "bold"))


def instruction_line(message: str, *turtles) -> None:
    for turtle in turtles:
        turtle.clear()
    turtles[-1].color('blue')
    turtles[-1].write(message, move=False, align="center", font=("Arial", 22, "bold"))


def end_game(color_of_winner, user_bet):
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


for color in colors:
    turtle = Turtle(shape='turtle', visible=True)
    turtle.shapesize(1.75, 1.75)
    turtle.penup()
    turtle.color(color)
    turtle.sety(y_pos - (colors.index(color) * screen.window_height() / len(colors)))
    turtle.setx(x_pos)
    turtles.append(turtle)

valid_color = False
user_guess = ''

while not valid_color:
    if user_guess not in colors:
        user_guess = screen.textinput('Make your bet', f'Racing turtles: {", ".join(colors)}\nWhich color will win? ')
    else:
        valid_color = True

while is_race_on:
    for runner in turtles:
        if runner.xcor() < (screen.window_width() / 2 - 40):
            runner.forward(randint(1, 20))
        else:
            winner_color = runner.color()[0]
            is_race_on = False

time.sleep(1)
screen.clear()

end_game(winner_color, user_guess)
screen.exitonclick()
