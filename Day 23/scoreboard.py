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

    def game_over(self, turtle_color, car_color):
        self.clear()
        self.color(car_color)
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Arial', 20, 'bold'))
        self.goto(0, 50)
        self.color(turtle_color)
        sin_pl_turtles = ['turtle', 'turtles']
        if self.score == 1:
            turtles = sin_pl_turtles[0]
        else:
            turtles = sin_pl_turtles[1]
        self.write(
            f'{turtle_color.title()} turtle died under a {car_color} car after {self.score} {turtles} crossed the road',
            align='center',
            font=('Arial', 18, 'normal')
        )
