# בס״ד
import sys
from turtle import Turtle, Screen
from zipfile import ZipFile

import pandas as pd

# Read zip file with data
zip_file = ZipFile("../../../Desktop/100 Days of Code The Complete Python Pro Bootcamp for 2023/25 - Day 25 - Intermediate - Working with CSV Data and the Pandas Library/005 us-states-game-start.zip")

# print zip file contents
zip_file.printdir()

# read data from the zip file into dataframe and image path
data = pd.read_csv(zip_file.extract("us-states-game-start/50_states.csv"))
bg_image = zip_file.extract("us-states-game-start/blank_states_img.gif")

print(data.head(2))
print()
# setup pointer for writing states and screen
pointer = Turtle()
pointer.penup()
pointer.hideturtle()

screen = Screen()
screen.bgpic(bg_image)

tries = 50

while tries > 0:
    user_input = input("Name a state (for exit type 'q'): ").strip().title()
    if user_input.lower() == 'q':
        sys.exit()

    else:
        try:
            pass
            x_cor = float(data.x[data.state == user_input])
            y_cor = float(data.y[data.state == user_input])
            pointer.goto(x_cor, y_cor)
            pointer.write(user_input, align='center', font=('Arial', 10, 'normal'))

        except ValueError:
            print("There is no state with this name in the US. Try again.")
        finally:
            tries -= 1

screen.exitonclick()
