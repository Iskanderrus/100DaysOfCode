# בס״ד
import sys
from tkinter import Tk, Label, Button, PhotoImage, Canvas
from PIL import Image, ImageTk


def exit_button():
    sys.exit()



# create main window
window = Tk()
window.title('Password manager')
window.config(padx=20, pady=20, bg='white')

# add icon
ico = Image.open('images/logo_image.png')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)

# create and setup canvas
canvas = Canvas(
    window,
    bg='white',
    width=550,
    height=550,
    highlightthickness=0
)
filename = PhotoImage(file="images/bg_image.png")
canvas.create_image(310, 260, image=filename)
canvas.create_text(
    310, 30,
    text='Create, save, manage and securely use safe passwords',
    width=360,
    font=('TkMenuFont', 15),
    fill='red',
)
canvas.grid(row=1, column=1)


# add buttons
exit_img = Image.open('images/exit.png')
exit_photo = ImageTk.PhotoImage(exit_img)
exit_button = Button(
    image=exit_photo,
    bg='white',
    height=30,
    width=65,
    highlightthickness=0,
    command=exit_button
)
exit_button.grid(row=0, column=2)




window.mainloop()