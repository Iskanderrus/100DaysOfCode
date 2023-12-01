# בס״ד
import sys
import time
from turtle import Turtle, Screen
from zipfile import ZipFile

import pandas as pd

# Read zip file with data
zip_file = ZipFile("../../../Desktop/100 Days of Code The Complete Python Pro Bootcamp for 2023/25 - Day 25 - "
                   "Intermediate - Working with CSV Data and the Pandas Library/005 us-states-game-start.zip")

# print zip file contents
# zip_file.printdir()

# read data from the zip file into dataframe and image path
data = pd.read_csv(zip_file.extract("us-states-game-start/50_states.csv"))
bg_image = zip_file.extract("us-states-game-start/blank_states_img.gif")
# print(data.head(2))

# setup pointer for writing states and screen
pointer = Turtle()
pointer.penup()
pointer.hideturtle()

# setup screen
screen = Screen()
screen.setup(800, 800)
screen.title('Guess all US states')
screen.bgpic(bg_image)
screen.tracer(0)

# setup basic scoreboard
scoreboard = Turtle()
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.pencolor('black')


def save_data_to_learn(df, list_of_answers):
    states_not_guessed = df[~df['state'].isin(list_of_answers)]['state']
    states_not_guessed.to_csv('states_to_learn.scv')


# service data
tries = 50  # 50 tries to perfectly guess all 50 states
right_answers = []

while tries > 0:
    if len(right_answers) == 1:
        scoreboard.goto(0, 250)
        scoreboard.write(f'{len(right_answers)} state guessed correct using {50 - tries}/50 tries',
                         align='center',
                         font=('Arial', 20, 'bold'))
    else:
        scoreboard.goto(0, 250)
        scoreboard.write(f'{len(right_answers)} states guessed correct using {50 - tries}/50 tries',
                         align='center',
                         font=('Arial', 20, 'bold'))
    try:
        user_input = screen.textinput("Type your answer here", "Name a state")
        user_input = user_input.strip().title()
    # condition to exit the game
    except AttributeError:
        save_data_to_learn(df=data, list_of_answers=right_answers)
        sys.exit()

    # condition if the state was already mentioned
    if user_input in right_answers:
        scoreboard.clear()
        scoreboard.goto(0, -285)
        scoreboard.write("You already guessed this one",
                         align='center',
                         font=('Arial', 20, 'bold'))
        screen.update()
        time.sleep(3)

    # condition if the state was not mentioned before and is in the dataframe
    else:
        try:
            right_answers.append(user_input)
            x_cor = int(data.x[data.state == user_input].iloc[0])
            y_cor = int(data.y[data.state == user_input].iloc[0])
            pointer.goto(x_cor, y_cor)
            pointer.write(user_input, align='center', font=('Arial', 8, 'normal'))

        # condition if user provided a not valid value
        except IndexError:
            right_answers.remove(user_input)
            scoreboard.clear()
            scoreboard.goto(0, -285)
            scoreboard.write(f'There is no state {user_input} in the US',
                             align='center',
                             font=('Arial', 20, 'bold'))
            screen.update()
            time.sleep(3)

        # scoring
    tries -= 1
    scoreboard.clear()
    screen.update()

if len(right_answers) < 50:
    save_data_to_learn(df=data, list_of_answers=right_answers)

screen.exitonclick()
