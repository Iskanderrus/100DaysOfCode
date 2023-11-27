# בס״ד

from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, user_name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.score = 0
        self.user_name = user_name.strip().title()
        self.message()

    def message(self):
        self.write(f"{self.user_name}'s Score: {self.score}", align='center', font=('Arial', 20, 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.message()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=('Arial', 20, 'bold'))
        self.goto(0, -40)
        self.write(f"{self.user_name}'s Score: {self.score}", align='center', font=('Arial', 20, 'bold'))
