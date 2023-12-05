# בס״ד
import sys
from tkinter import Tk, Label, Button, PhotoImage, Canvas, Entry
from PIL import Image, ImageTk

FONT_NAME = 'TkMenuFont'


def exit_button():
    sys.exit()


# create main window
window = Tk()
window.title('Password manager')
window.config(padx=20, pady=20, bg='#BEFBFF')

# add icon
ico = Image.open('images/logo_image.png')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)

# create and setup canvas
canvas = Canvas(
    window,
    bg='#BEFBFF',
    width=400,
    height=400,
    highlightthickness=0
)
filename = PhotoImage(file="images/bg_image.png")
canvas.create_image(225, 230, image=filename)
canvas.create_text(
    220, 30,
    text='Create, save, manage and securely use safe passwords',
    width=360,
    font=(FONT_NAME, 13, 'bold'),
    fill='#281713',
    justify='center'
)
canvas.grid(row=1, column=1)

# add buttons
exit_img = Image.open('images/exit.png')
exit_photo = ImageTk.PhotoImage(exit_img)
exit_button = Button(
    window,
    image=exit_photo,
    bg='#BEFBFF',
    height=30,
    width=65,
    highlightthickness=0,
    command=exit_button,
    anchor='se'
)
exit_button.grid(row=0, column=2, sticky='se')

generate_button = Button(
    window,
    font=FONT_NAME,
    height=1,
    bg='#0089B4',
    fg='#F9E3E2',
    activebackground='#169700',
    activeforeground='#F9E3E2',
    highlightthickness=0,
    text='Generate Password',
)

generate_button.grid(row=4, column=2)

add_button = Button(
    window,
    font=FONT_NAME,
    width=51,
    bg='#0089B4',
    fg='#F9E3E2',
    activebackground='#169700',
    activeforeground='#F9E3E2',
    highlightthickness=0,
    text='Add Password'
)

add_button.grid(row=5, column=1, columnspan=2)

# Labels
website_label = Label(
    window,
    padx=1,
    text='Website:',
    font=(FONT_NAME, 12),
    bg='#BEFBFF',
    fg='#281713',
)

website_label.grid(row=2, column=0)

email_label = Label(
    window,
    padx=1,
    text='Email/Username:',
    font=(FONT_NAME, 12),
    bg='#BEFBFF',
    fg='#281713',
)
email_label.grid(row=3, column=0)

password_label = Label(
    window,
    padx=1,
    text='Password:',
    font=(FONT_NAME, 12),
    bg='#BEFBFF',
    fg='#281713',
)
password_label.grid(row=4, column=0)

# text fields
website_entry = Entry(window, width=52)
website_entry.insert(0, 'https://')
website_entry.grid(row=2, column=1, columnspan=2, ipady=3, pady=5)

email_entry = Entry(window, width=52)
email_entry.insert(0, 'a.n.chasovskoy@gmail.com')
email_entry.grid(row=3, column=1, columnspan=2, ipady=3, pady=5)

password_entry = Entry(window, width=35)
password_entry.grid(row=4, column=1, ipady=3, pady=5)

window.mainloop()
