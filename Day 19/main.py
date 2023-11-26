from turtle import Turtle, Screen

tim = Turtle()
instruction = Turtle()
instruction.hideturtle()
instruction.penup()

screen = Screen()
messages = ["Use 'w' to go forwards",
            "Use 's' to go backwards",
            "Use 'a' to turn left",
            "Use 'd' to turn right",
            "Use 'c' to clear the screen",
            "Use 'h' to turn to the home position"
            ]

instruction.sety(screen.window_height() / 2 - 50)
instruction.setx(screen.window_width() / 2 - 450)


for message in messages:
    instruction.write(message, move=False, align="left", font=("Arial", 12, "bold"))
    instruction.sety(instruction.ycor() - 15)

screen.listen()


def turn_left():
    tim.setheading(tim.heading() + 5)


def turn_right():
    tim.setheading(tim.heading() - 5)


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def clear_screen():
    tim.clear()


def back_home():
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkeypress(fun=move_forwards, key='w')
screen.onkeypress(fun=move_backwards, key='s')
screen.onkeypress(fun=turn_left, key='a')
screen.onkeypress(fun=turn_right, key='d')
screen.onkeypress(fun=clear_screen, key='c')
screen.onkeypress(fun=back_home, key='h')

screen.exitonclick()
