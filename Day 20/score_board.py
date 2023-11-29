# בס״ד
from pathlib import Path
from turtle import Turtle


class ScoreBoard(Turtle):
    HIGH_SCORE_FILE_PATH = Path('data/high_score.txt')

    def __init__(self, user_name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.score = 0
        self.user_name = user_name.strip().title()

        if ScoreBoard.HIGH_SCORE_FILE_PATH.exists():
            contents = ScoreBoard.HIGH_SCORE_FILE_PATH.read_text()
            self.high_score = int(contents)
        else:
            self.high_score = 0
            ScoreBoard.HIGH_SCORE_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
            ScoreBoard.HIGH_SCORE_FILE_PATH.touch()
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
            ScoreBoard.HIGH_SCORE_FILE_PATH.write_text(str(self.high_score))
        self.score = 0
        self.message()
