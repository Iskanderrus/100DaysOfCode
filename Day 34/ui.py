# בס״ד

from tkinter import Tk, Button, Label, Canvas, E, W, NE, NW, SW

from PIL import Image, ImageTk

root = Tk()
root.geometry('600x750')
root.title('QUIZ')
root.configure(bg='steelblue4', padx=50, pady=15)

canvas = Canvas(root,  bg='white', border=0, highlightthickness=0)
canvas.configure(width=500, height=500)
canvas.grid(row=1, column=0, columnspan=2)

# buttons
true_button_image = Image.open('images/true.png')
true_button_image = ImageTk.PhotoImage(true_button_image)
true_button = Button(
    root,
    image=true_button_image,
    border=0,
    activebackground='steelblue4',
    bg='steelblue4',
    highlightthickness=0
)
true_button.grid(row=2, column=0, padx=30, pady=10)

false_button_image = Image.open('images/false.png')
false_button_image = ImageTk.PhotoImage(false_button_image)
false_button = Button(
    root,
    image=false_button_image,
    border=0,
    activebackground='steelblue4',
    bg='steelblue4',
    highlightthickness=0
)
false_button.grid(row=2, column=1,pady=10)

# labels
score_label = Label(root, text="Your Score: ", font=('Arial', 15, 'bold'), pady=30, bg='steelblue4', foreground='white')
score_label.grid(row=0, column=1)

root.mainloop()