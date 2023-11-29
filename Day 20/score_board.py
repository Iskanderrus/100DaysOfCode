# בס״ד
from pathlib import Path
from turtle import Turtle

path = Path('data/high_score.txt')


class ScoreBoard(Turtle):
    def __init__(self, user_name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.score = 0
        self.user_name = user_name.strip().title()
        if path.exists():
            contents = path.read_text()
            self.high_score = int(contents)
        else:
            self.high_score = 0
            Path('data').mkdir(parents=True)
            Path('data/high_score.txt').touch()
        self.message()

    def message(self):
        self.clear()
        self.write(
            f"{self.user_name}'s Score: {self.score} // High score: {self.high_score}",
            align='center',
            font=('Arial', 20, 'bold')
        )

    def increase_score(self):
        self.score += 1
        self.message()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            path.write_text(str(self.high_score))
        self.score = 0
        self.message()
