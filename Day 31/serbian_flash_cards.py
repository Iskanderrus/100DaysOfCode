# בס״ד
from tkinter import Tk, Widget, Button, Entry, Label, Canvas, PhotoImage

# main window
root = Tk()
root.title('Карточки сербского языка')

# canvas
canvas = Canvas(root, height=600, width=600, highlightthickness=0)
filename = PhotoImage('images/card_front.png')
canvas.create_image(300, 300, image=filename)
canvas.grid(row=0, column=0)

# buttons




root.mainloop()