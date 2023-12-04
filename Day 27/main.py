# בס״ד

import tkinter

# create a window
window = tkinter.Tk()
# window title
window.title('My first GUI program')

# window size
window.minsize(width=800, height=800)

# Label
my_label = tkinter.Label(text='This is a label', font=('Arial', 24, 'bold italic'))

my_label.grid(column=0, row=0)
my_label.config(text='This is a new text')


# Button

# function for button to execute. Used in the command argument of the Button class
def button_clicked():
    my_label.config(text=user_input.get())


button = tkinter.Button(text='Click me', command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text='Click me', command=button_clicked)
new_button.grid(column=2, row=0)



# Entry

user_input = tkinter.Entry(width=10)
user_input.grid(column=3, row=2)


# running the mainloop to keep the window on the screen
window.mainloop()
