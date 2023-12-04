# בס״ד
import time
from math import ceil
from tkinter import Tk, Label, Button, PhotoImage, Canvas
from playsound import playsound

from PIL import Image, ImageTk

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


# Logic

def start_timer():
    global cycle
    cycle += 1
    if cycle == 8:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text='LONG BREAK', fg=RED)
        playsound('sounds/oh-yeah-85721.mp3')

    elif cycle % 2 == 0:
        playsound('sounds/sh')
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text='SHORT BREAK', fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text='WORK', fg=GREEN)


def count_down(count):
    canvas.itemconfig(timer_text, text=f"{count // 60:02d}:{count % 60:02d}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if cycle % 2 == 0:
            check_box_label.config(text=f'{"✔" * (ceil(cycle/2))}')

window = Tk()
window.title('Pomodoro')
ico = Image.open('tomato.png')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)
window.config(padx=100, pady=50)
window.config(bg=YELLOW)

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

reset_button = Button(text='Reset', font=(FONT_NAME, 12, 'bold'), highlightthickness=0)
reset_button.grid(row=2, column=2)

window.mainloop()
