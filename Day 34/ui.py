# בס״ד

from tkinter import Tk, Button, Label, Canvas

from PIL import Image, ImageTk

THEME_COLOR = 'steelblue4'


class QuizInterface:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x750')
        self.root.title('QUIZ')
        self.root.configure(bg=THEME_COLOR, padx=50, pady=15)

        self.canvas = Canvas(self.root, bg='white', border=0, highlightthickness=0)
        self.canvas.configure(width=500, height=500)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.question_text = self.canvas.create_text(
            250,
            250,
            text='Some question text',
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR)

        # buttons
        true_button_image = Image.open('images/true.png')
        true_button_image = ImageTk.PhotoImage(true_button_image)
        self.true_button = Button(
            self.root,
            image=true_button_image,
            border=0,
            activebackground=THEME_COLOR,
            bg=THEME_COLOR,
            highlightthickness=0
        )
        self.true_button.grid(row=2, column=0, padx=30, pady=10)

        false_button_image = Image.open('images/false.png')
        false_button_image = ImageTk.PhotoImage(false_button_image)
        self.false_button = Button(
            self.root,
            image=false_button_image,
            border=0,
            activebackground=THEME_COLOR,
            bg=THEME_COLOR,
            highlightthickness=0
        )
        self.false_button.grid(row=2, column=1, pady=10)

        # labels
        self.score_label = Label(
            self.root,
            text="Your Score: 0",
            font=('Arial', 15, 'bold'),
            pady=30,
            bg='steelblue4',
            foreground='white'
        )

        self.score_label.grid(row=0, column=1)

        self.root.mainloop()
