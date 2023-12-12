# בס״ד
import os
import sys
from pathlib import Path
from random import choice
from tkinter import Tk, Button, Canvas, PhotoImage, messagebox

import pandas as pd
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#B1DDC6"
SETTINGS_PATH = Path('settings/settings.csv')

# importing settings
try:
    settings = pd.read_csv(SETTINGS_PATH)
except FileNotFoundError:
    ALPHABET_STYLE = 'ћирилица'
    TRANSLATION_LANGUAGE = 'ru'

else:
    ALPHABET_STYLE = settings.ALPHABET_STYLE
    TRANSLATION_LANGUAGE = settings.TRANSLATION_LANGUAGE

# opening file with data
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/alphabet.csv')

to_learn = data.to_dict(orient='records')
current_card = {}


def reset_progress():
    path = Path('data/words_to_learn.csv')
    if path.exists():
        os.remove(path)
        if TRANSLATION_LANGUAGE == 'ru':
            messagebox.showinfo('Прогресс сброшен', 'Вы можете начать обучение сначала')
        elif TRANSLATION_LANGUAGE == 'en':
            messagebox.showinfo('Your progress was reset', 'You can start learning from scratch')
        elif TRANSLATION_LANGUAGE == 'de':
            messagebox.showinfo('Fortschritt zurückgesetzt', 'Sie können wieder mit dem Lernen beginnen')
        elif TRANSLATION_LANGUAGE == 'tr':
            messagebox.showinfo('İlerleme sıfırlama', 'Tekrar öğrenmeye başlayabilirsiniz')


def exit_button_pressed():
    sys.exit()


def is_known():
    to_learn.remove(current_card)
    to_learn_data = pd.DataFrame(to_learn)
    to_learn_data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


def next_card():
    global current_card, sample_image, sr_flag_image, flip_timer
    root.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(title, text=ALPHABET_STYLE, fill='black')
    canvas.itemconfig(letter, text=current_card[ALPHABET_STYLE], fill='black', font=('Ariel', 30, 'bold'))
    canvas.itemconfig(sample_word, text=current_card[f'sample_{ALPHABET_STYLE}'], fill='black')

    sample_image = Image.open(current_card['img_url'])
    sample_image = ImageTk.PhotoImage(sample_image)
    canvas.itemconfig(word_image, image=sample_image)

    sr_flag_image = Image.open('images/flags/sr.png')
    sr_flag_image = ImageTk.PhotoImage(sr_flag_image)
    canvas.itemconfig(flag_image_sr, image=sr_flag_image)
    canvas.itemconfig(card_background, image=card_front_img)
    root.after(3000, func=flip_card)


def flip_card():
    global current_card, sr_flag_image
    canvas.itemconfig(title, text='')
    canvas.itemconfig(letter,
                      text=f"{current_card[f'{TRANSLATION_LANGUAGE}_transcription']} - {current_card['IPA_value']}",
                      fill='white',
                      font=('Ariel', 15, 'normal'))
    canvas.itemconfig(sample_word,
                      text=f"{current_card[f'sample_{ALPHABET_STYLE}']} - "
                           f"{current_card[f'sample_{TRANSLATION_LANGUAGE}']}",
                      fill='white')

    sr_flag_image = Image.open(f'images/flags/{TRANSLATION_LANGUAGE}.png')
    sr_flag_image = ImageTk.PhotoImage(sr_flag_image)
    canvas.itemconfig(flag_image_sr, image=sr_flag_image)

    canvas.itemconfig(card_background, image=card_back_img)


# main window
root = Tk()
root.title('Алфавит сербского языка')
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = root.after(3000, func=flip_card)

# settings
# TODO: Add a window asking the user to select what type of alphabet he wants to train and preferred user language

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = Image.open('images/card_front.png')
card_front_img = ImageTk.PhotoImage(card_front_img)

card_back_img = Image.open('images/card_back.png')
card_back_img = ImageTk.PhotoImage(card_back_img)

card_background = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(200, 50, text='', font=('Ariel', 20, 'normal'))
letter = canvas.create_text(220, 200, text='A a', font=('Ariel', 20, 'bold'))
sample_word = canvas.create_text(220, 250, text='', font=('Ariel', 20, 'italic'))

sr_flag_image = Image.open('images/flags/sr.png')
sr_flag_image = ImageTk.PhotoImage(sr_flag_image)
flag_image_sr = canvas.create_image(50, 50, image=sr_flag_image)

sample_image = Image.open('images/alphabet/car.png')
sample_image = ImageTk.PhotoImage(sample_image)
word_image = canvas.create_image(570, 200, image=sample_image)

canvas.grid(row=1, column=0, columnspan=2, rowspan=4)

# service buttons
settings_photo = PhotoImage(file='images/settings.png')
settings_button = Button(root,
                         image=settings_photo,
                         bg=BACKGROUND_COLOR,
                         activebackground=BACKGROUND_COLOR,
                         highlightthickness=0,
                         command=exit_button_pressed
                         )
settings_button.config(borderwidth=0)
settings_button.grid(row=2, column=3)

reset_photo = PhotoImage(file='images/reset.png')
reset_button = Button(root,
                      image=reset_photo,
                      bg=BACKGROUND_COLOR,
                      activebackground=BACKGROUND_COLOR,
                      highlightthickness=0,
                      command=reset_progress
                      )
reset_button.config(borderwidth=0)
reset_button.grid(row=1, column=3)

exit_photo = PhotoImage(file='images/exit.png')
exit_button = Button(root,
                     image=exit_photo,
                     bg=BACKGROUND_COLOR,
                     activebackground=BACKGROUND_COLOR,
                     highlightthickness=0,
                     command=exit_button_pressed
                     )
exit_button.config(borderwidth=0)
exit_button.grid(row=0, column=3)

# main buttons
right_photo = PhotoImage(file='images/right.png')
right_button = Button(root,
                      image=right_photo,
                      bg=BACKGROUND_COLOR,
                      activebackground=BACKGROUND_COLOR,
                      highlightthickness=0,
                      command=is_known
                      )
right_button.config(borderwidth=0)
right_button.grid(row=5, column=0)

wrong_photo = PhotoImage(file='images/wrong.png')
wrong_button = Button(root,
                      image=wrong_photo,
                      bg=BACKGROUND_COLOR,
                      highlightthickness=0,
                      activebackground=BACKGROUND_COLOR,
                      command=next_card)
wrong_button.config(borderwidth=0)
wrong_button.grid(row=5, column=1)

next_card()

root.mainloop()
