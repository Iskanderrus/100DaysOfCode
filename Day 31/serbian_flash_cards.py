# בס״ד
from tkinter import Tk, Widget, Button, Entry, Label, Canvas, PhotoImage

from PIL import Image, ImageTk


BACKGROUND_COLOR = "#B1DDC6"

# main window
root = Tk()
root.title('Карточки сербского языка')
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas
canvas = Canvas(root, height=600, width=600, highlightthickness=0)
filename = PhotoImage('images/card_front.png')
canvas.create_image(300, 300, image=filename)
canvas.grid(row=0, column=3)

# buttons
right_photo = PhotoImage(file='images/right.png')
right_button = Button(root, image=right_photo, bg=BACKGROUND_COLOR, borderwidth=0)
right_button.config( borderwidth=0)
right_button.grid(row=2, column=2)


wrong_photo = PhotoImage(file='images/wrong.png')
wrong_button = Button(root, image=wrong_photo, bg=BACKGROUND_COLOR, borderwidth=0)
wrong_button.grid(padx=20, pady=20, row=2, column=4)

root.mainloop()