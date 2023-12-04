# בס״ד
from math import ceil
from tkinter import Tk, Label, Button, PhotoImage, Canvas

from PIL import Image, ImageTk
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
cycle = 0
my_timer = None


# Logic

def reset_timer():
    global cycle
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text='TIMER', fg=GREEN)
    check_box_label.config(text='')
    cycle = 0


def start_timer():
    """
    function to start the timer based on the cycle number
    :return:
    """
    global cycle
    cycle += 1
    # last cycle - long break
    if cycle == 8:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text='LONG BREAK', fg=RED)
        playsound('sounds/lie_down_for_a_while_and_have_a_rest..mp3')
    # every second cycle - a short pause
    elif cycle % 2 == 0:
        playsound('sounds/lets_have_a_break.mp3')
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text='SHORT BREAK', fg=PINK)
    # every odd cycle - working time
    else:
        playsound('sounds/get_back_to_work.mp3')
        count_down(WORK_MIN * 60)
        title_label.config(text='WORK', fg=GREEN)


def count_down(count):
    """
    function to count down without breaking mainloop of the program
    :param count: time in seconds
    :return:
    """
    global my_timer
    canvas.itemconfig(timer_text, text=f"{count // 60:02d}:{count % 60:02d}")
    if count > 0:
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if cycle % 2 == 0:
            check_box_label.config(text=f'{"✔" * (ceil(cycle / 2))}')


# create and set up the window
window = Tk()
window.title('Pomodoro')

# adding the icon to the program
ico = Image.open('tomato.png')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)
window.config(padx=100, pady=50)
window.config(bg=YELLOW)

# create and setup canvas
canvas = Canvas(width=206, height=224, highlightthickness=0)
filename = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=filename)

timer_text = canvas.create_text(103, 135, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.config(bg=YELLOW)
canvas.grid(row=1, column=1)

# Labels
title_label = Label(text='Timer', font=(FONT_NAME, 55, 'bold'), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

check_box_label = Label(font=(FONT_NAME, 30, 'bold'), bg=YELLOW, fg=GREEN)
check_box_label.grid(row=3, column=1)

# Buttons
start_button = Button(text='Start', font=(FONT_NAME, 12, 'bold'), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', font=(FONT_NAME, 12, 'bold'), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
