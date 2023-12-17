# בס״ד
import time
from _tkinter import TclError
from tkinter import Tk, Button, Label, Canvas

from PIL import Image, ImageTk
from models import Quiz

THEME_COLOR = 'steelblue4'


class QuizInterface:
    def __init__(self, quiz_brain: Quiz):
        self.right_answers_count = 0
        self.question_answer = None
        self.q_text = None
        self.quiz = quiz_brain
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
            width=480,
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
            highlightthickness=0,
            command=self.true_button_pressed
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
            highlightthickness=0,
            command=self.false_button_pressed
        )
        self.false_button.grid(row=2, column=1, pady=10)

        # labels
        self.score_label = Label(
            self.root,
            text=f"Your Score: {self.quiz.score}",
            font=('Arial', 15, 'bold'),
            pady=30,
            bg='steelblue4',
            foreground='white'
        )

        self.score_label.grid(row=0, column=1)
        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        self.canvas.config(background='white')
        try:
            self.q_text, self.question_answer = self.quiz.chose_question()
        except TypeError:
            self.score_label.destroy()
            self.canvas.config(background='white')
            self.canvas.itemconfig(
                self.question_text,
                text=f'No questions left\nYour Score: {self.quiz.score} out of {len(self.quiz.questions)}'
            )
        else:
            self.canvas.itemconfig(self.question_text, text=self.q_text)

    def scorer(self):
        try:
            self.score_label.config(text=f'Your Score: {self.quiz.score}')
        except TclError:
            pass
        else:
            self.quiz.question_number += 1

    def false_button_pressed(self):
        self.quiz.user_respond = 'False'
        if self.quiz.assessment():
            self.canvas.config(background='green')
            self.root.after(1000, self.get_next_question)
        else:
            self.canvas.config(background='red')
            self.root.after(1000, self.get_next_question)
        self.scorer()

    def true_button_pressed(self):
        self.quiz.user_respond = 'True'
        if self.quiz.assessment():
            self.canvas.config(background='green')
            self.root.after(1000, self.get_next_question)
        else:
            self.canvas.config(background='red')
            self.root.after(1000, self.get_next_question)
        self.scorer()