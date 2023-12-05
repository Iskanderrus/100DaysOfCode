# בס״ד
import os
import random
import string
import sys
from pathlib import Path
from tkinter import Tk, Label, Button, PhotoImage, Canvas, Entry, simpledialog, messagebox

import pyperclip
from PIL import Image, ImageTk

FONT_NAME = 'TkMenuFont'

# default values for the password
lower_case_number = 6
upper_case_number = 4
digits_number = 5
symbols_number = 4


def exit_button():
    """
    Function to exit from the app saving the password if generated to ensure that the password is not get lost
    :return:
    """
    if password_entry.get():
        adding_password()

    sys.exit()


def special_requirements():
    """
    Function to adjust the default password settings according to user requirements.
    User is prompted for each symbol group
    :return:
    """
    global lower_case_number, upper_case_number, digits_number, symbols_number
    lower_case_number = int(simpledialog.askstring(
        title="Number required!",
        prompt="How many lowercase characters are required?"))

    upper_case_number = int(simpledialog.askstring(
        title="Number required!",
        prompt="How many uppercase characters are required?"))

    digits_number = int(simpledialog.askstring(
        title="Number required!",
        prompt="How many digits are required?"))

    symbols_number = int(simpledialog.askstring(
        title="Number required!",
        prompt="How many symbols are required?"))


def check_credentials():
    """ Function to check if user entered website or username/email"""
    if len(website_entry.get()) <= 4 or not email_entry.get():
        # if one of the values is missing message popup
        messagebox.showinfo("Missing data", "Please check credentials")
    else:
        return True


def create_password():
    """
    Main function to generate password.
    :return:
    """
    global lower_case_number, upper_case_number, digits_number, symbols_number
    # empty the field in case user wants to regenerate the password
    password_entry.delete(0, 'end')

    if check_credentials():
        try:
            new_password = (
                    random.sample(string.ascii_lowercase, k=lower_case_number) +
                    random.sample(string.ascii_uppercase, k=upper_case_number) +
                    random.sample(string.digits, k=digits_number) +
                    random.sample(string.punctuation, k=symbols_number))
        except (TypeError, ValueError):
            sys.exit()
        else:
            random.shuffle(new_password)
            random.shuffle(new_password)
            password_str = ''.join(new_password)
            # insert the generated password into the entry field
            password_entry.insert(0, password_str)


def adding_password():
    """
    Function aiming two goals:
    1. Add the new website, user data and password to the file for storing
    2. Copying the newly generated password to clipboard for immediate use after saving
    :return:
    """
    if check_credentials():
        path_folder = Path('./output')
        path = Path(f'{path_folder}/my_passwords.txt')
        message = str(f'{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n')
        if not path.exists():
            Path.mkdir(path_folder, parents=True)
            path.touch()

        with open(path, mode='a') as file:
            file.write(message)
        pyperclip.copy(password_entry.get())
        password_entry.delete(0, 'end')
        website_entry.delete(4, 'end')


# create main window
window = Tk()
window.title('Password manager')
window.config(padx=20, pady=20, bg='#BEFBFF')

# add icon
image_path = './images/logo_image.png'

ico = Image.open(image_path)
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
    command=create_password,
)
generate_button.grid(row=4, column=2)

special_requirements_button = Button(
    window,
    font=FONT_NAME,
    height=1,
    bg='#C06600',
    fg='#F9E3E2',
    activebackground='#169700',
    activeforeground='#F9E3E2',
    highlightthickness=0,
    text='Requirements',
    command=special_requirements,
)
special_requirements_button.grid(row=0, column=0)

add_button = Button(
    window,
    font=FONT_NAME,
    width=51,
    bg='#0089B4',
    fg='#F9E3E2',
    activebackground='#169700',
    activeforeground='#F9E3E2',
    highlightthickness=0,
    text='Add Password',
    command=adding_password,
)

add_button.grid(row=5, column=1, columnspan=2)

# Labels
website_label = Label(
    window,
    padx=1,
    text='Website:',
    font=(FONT_NAME, 10),
    bg='#BEFBFF',
    fg='#281713',
)

website_label.grid(row=2, column=0)

email_label = Label(
    window,
    padx=1,
    text='Email/Username:',
    font=(FONT_NAME, 10),
    bg='#BEFBFF',
    fg='#281713',
)
email_label.grid(row=3, column=0)

password_label = Label(
    window,
    padx=1,
    text='Password:',
    font=(FONT_NAME, 10),
    bg='#BEFBFF',
    fg='#281713',
)
password_label.grid(row=4, column=0)

# text fields
website_entry = Entry(window, width=52)
website_entry.focus()
website_entry.insert(0, 'www.')
website_entry.grid(row=2, column=1, columnspan=2, ipady=3, pady=5)

email_entry = Entry(window, width=52)
email_entry.insert(0, 'a.n.chasovskoy@gmail.com')
email_entry.grid(row=3, column=1, columnspan=2, ipady=3, pady=5)

password_entry = Entry(window, width=35)
password_entry.grid(row=4, column=1, ipady=3, pady=5)

window.mainloop()
