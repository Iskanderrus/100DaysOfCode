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

my_label.pack(side='left')


# running the mainloop to keep the window on the screen
window.mainloop()