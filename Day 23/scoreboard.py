# בס״ד
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, screen_size: tuple):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.x_cor = -screen_size[0] / 4
        self.y_cor = screen_size[1] / 2 - 55
        self.goto(self.x_cor, self.y_cor)
        self.score = 0
        self.message()

    def message(self):
        self.write(f'Level: {self.score}', align='center', font=('Arial', 20, 'bold'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.message()