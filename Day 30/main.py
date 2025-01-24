import datetime
import json
import random
import string
import sys
from pathlib import Path
from tkinter import Tk, Label, Button, PhotoImage, Canvas, Entry, simpledialog, messagebox

import pyperclip
from PIL import Image, ImageTk

FONT_NAME = 'TkMenuFont'
DATA_FILE = Path('../../../Documents/password_manager_log.json')

# default values for the password
DEFAULT_LOWER_CASE_NUMBER = 10
DEFAULT_UPPER_CASE_NUMBER = 8
DEFAULT_DIGITS_NUMBER = 5
DEFAULT_SYMBOLS_NUMBER = 5


def search_button_func():
    """Searches for a password based on website and username combination."""
    try:
        with open(DATA_FILE, 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("File does not exist",
                            "Please make your first entry and save it.")
    else:
        website = website_entry.get().strip()
        username = email_entry.get().strip()
        found = False

        for key, value in data.items():
            if key == website:
                if value.get("username") == username:
                    password = value.get("password")
                    pyperclip.copy(password)
                    messagebox.showinfo("Entry exists",
                                        f"Saved username: {username}\n"
                                        f"Saved password: {password}\n\n"
                                        f"This password is copied to clipboard.")
                    found = True
                    break

        if not found:
            messagebox.showinfo("Entry does not exist",
                                "This website and username combination was not found in your database")


def exit_button():
    """Exits the app, saving the password if generated to ensure that the password is not lost."""
    if password_entry.get():
        adding_password()
    sys.exit()


def special_requirements():
    """Adjusts password settings according to user requirements."""
    global DEFAULT_LOWER_CASE_NUMBER, DEFAULT_UPPER_CASE_NUMBER, DEFAULT_DIGITS_NUMBER, DEFAULT_SYMBOLS_NUMBER
    try:
        DEFAULT_LOWER_CASE_NUMBER = int(simpledialog.askstring(
            title="Number required!",
            prompt="How many lowercase characters are required?"))

        DEFAULT_UPPER_CASE_NUMBER = int(simpledialog.askstring(
            title="Number required!",
            prompt="How many uppercase characters are required?"))

        DEFAULT_DIGITS_NUMBER = int(simpledialog.askstring(
            title="Number required!",
            prompt="How many digits are required?"))

        DEFAULT_SYMBOLS_NUMBER = int(simpledialog.askstring(
            title="Number required!",
            prompt="How many symbols are required?"))
    except (ValueError, TypeError):
        messagebox.showinfo("Error!", "Please enter valid numbers for the password length requirements")


def check_credentials(website, username):
    """Checks if user entered valid website and username/email."""
    if len(website) <= 4 or not username or "@" not in username:
        # if one of the values is missing message popup
        messagebox.showinfo("Missing data", "Please check credentials")
        return False
    else:
        return True


def create_password(lower_case_number, upper_case_number, digits_number, symbols_number):
    """Main function to generate password."""
    # empty the field in case user wants to regenerate the password
    password_entry.delete(0, 'end')

    if check_credentials(website_entry.get(), email_entry.get()):
        try:
            new_password = (
                    random.sample(string.ascii_lowercase, k=lower_case_number) +
                    random.sample(string.ascii_uppercase, k=upper_case_number) +
                    random.sample(string.digits, k=digits_number) +
                    random.sample(string.punctuation, k=symbols_number))

            random.shuffle(new_password)
            random.shuffle(new_password)
            password_str = ''.join(new_password)
            password_entry.insert(0, password_str)
        except (TypeError, ValueError):
            messagebox.showinfo("Error",
                                "Please set the password length requirements correctly using requirements button")


def generate_password_button_func():
    """Helper function for the generation button to create the password."""
    global DEFAULT_LOWER_CASE_NUMBER, DEFAULT_UPPER_CASE_NUMBER, DEFAULT_DIGITS_NUMBER, DEFAULT_SYMBOLS_NUMBER
    create_password(DEFAULT_LOWER_CASE_NUMBER, DEFAULT_UPPER_CASE_NUMBER, DEFAULT_DIGITS_NUMBER, DEFAULT_SYMBOLS_NUMBER)


def adding_password():
    """Adds the new website, user data, and password to the file for storing."""
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get()
    date = datetime.datetime.now()
    current_date = date.strftime('%d.%m.%Y')

    new_entry = {
        website: {
            "username": email,
            "password": password,
            "logged_date": current_date
        }
    }
    if check_credentials(website, email):
        try:
            with open(DATA_FILE, 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(DATA_FILE, 'w') as data_file:
                json.dump(new_entry, data_file, indent=4)
        else:

            if website in data:  # If the website entry exists
                data[website]["username"] = email
                data[website]["password"] = password
                data[website]["logged_date"] = current_date  # update the entry
            else:
                data.update(new_entry)  # or add a new entry

        with open(DATA_FILE, 'w') as data_file:
            json.dump(data, data_file, indent=4)

        pyperclip.copy(password_entry.get())
        messagebox.showinfo("Success", "Saved and copied to clipboard")
        password_entry.delete(0, 'end')
        website_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        website_entry.insert(0, 'www.')
        email_entry.insert(0, '@')


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
    command=generate_password_button_func,
)
generate_button.grid(row=4, column=2)

search_button = Button(
    window,
    font=FONT_NAME,
    height=1,
    width=15,
    bg='#0089B4',
    fg='#F9E3E2',
    activebackground='#169700',
    activeforeground='#F9E3E2',
    highlightthickness=0,
    text='Search',
    command=search_button_func
)
search_button.grid(row=2, column=2)

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
website_entry = Entry(window, width=35)
website_entry.focus()
website_entry.insert(0, 'www.')
website_entry.grid(row=2, column=1, ipady=3, pady=5)

email_entry = Entry(window, width=52)
email_entry.insert(0, '@')
email_entry.grid(row=3, column=1, columnspan=2, ipady=3, pady=5)

password_entry = Entry(window, width=35)
password_entry.grid(row=4, column=1, ipady=3, pady=5)

window.mainloop()