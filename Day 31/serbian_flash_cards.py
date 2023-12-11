# בס״ד
from random import random, choice
from tkinter import Tk, Widget, Button, Entry, Label, Canvas, PhotoImage
import pandas as pd
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv('data/alphabet.csv')
to_learn = data.to_dict(orient='records')
concurrent_card = {}

def next_card():
    global concurrent_card
    current_card = choice(to_learn)
    canvas.itemconfig(cyrillic, text=current_card['Српска ћирилица'])
    canvas.itemconfig(latin, text=current_card['Српска латиница'])
    canvas.itemconfig(cyrillic_word, text=current_card['sample_cyr'])
    canvas.itemconfig(latin_word, text=current_card['sample_lat'])
    sample_image = Image.open(f"{current_card['img_url']}")
    sample_image = ImageTk.PhotoImage(sample_image)
    canvas.itemconfig(word_image, image=sample_image)



def flip_card():
    pass
    #canvas.itemconfig()

# main window
root = Tk()
root.title('Карточки сербского языка')
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

root.after(3000, func=flip_card)

# canvas
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = Image.open('images/card_front.png')
card_front_img = ImageTk.PhotoImage(card_front_img)

card_back_img = Image.open('images/card_back.png')
card_back_img = ImageTk.PhotoImage(card_back_img)

canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text='ћирилица\tЛатиница', font=('Ariel', 20, 'normal'))
cyrillic = canvas.create_text(230, 200, text='A a', font=('Ariel', 20, 'bold'))
latin = canvas.create_text(570, 200, text='A a', font=('Ariel', 20, 'bold'))
cyrillic_word = canvas.create_text(230, 250, text='', font=('Ariel', 20, 'italic'))
latin_word = canvas.create_text(570, 250, text='', font=('Ariel', 20, 'italic'))
image = Image.open('images/alphabet/car.png')
image = ImageTk.PhotoImage(image)
word_image = canvas.create_image(400, 300, image=image)



canvas.grid(row=0, column=0, columnspan=2)

# buttons
right_photo = PhotoImage(file='images/right.png')
right_button = Button(root, image=right_photo, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                      highlightthickness=0)
right_button.config(borderwidth=0)
right_button.grid(row=1, column=0)

wrong_photo = PhotoImage(file='images/wrong.png')
wrong_button = Button(root, image=wrong_photo, bg=BACKGROUND_COLOR, highlightthickness=0,
                      activebackground=BACKGROUND_COLOR, command=next_card)
wrong_button.config(borderwidth=0)
wrong_button.grid(row=1, column=1)

next_card()

root.mainloop()
