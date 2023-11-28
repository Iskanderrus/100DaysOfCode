# בס״ד

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, user1, user2, screen_dimensions: tuple):
        super().__init__()
        self.color('white')
        self.speed('fastest')
        self.users = [user1, user2]
        self.scores = [0, 0]
        self.screen_width_half = screen_dimensions[0] / 4
        self.screen_height_half = screen_dimensions[1] / 2 - 35
        self.positions = [
            (-self.screen_width_half, self.screen_height_half),
            (self.screen_width_half, self.screen_height_half)
        ]
        self.penup()
        self.hideturtle()
        self.keys = ["A / Z", "Up / Down"]
        self.message()

    def message(self):
        for x in range(2):
            self.goto(self.positions[x])
            self.write(f"{self.users[x]}'s Score: {self.scores[x]}  {self.keys[x]}",
                       align='center',
                       font=('Arial', 20, 'bold'))

    def increase_score(self, user):
        self.scores[self.users.index(user)] += 1
        self.clear()
        self.message()

    def end_game(self):
        winner = self.users[self.scores.index(max(self.scores))].upper()
        self.goto(0, 0)
        self.write(f"Winner is {winner} with Score: {max(self.scores)}", align='center',
                   font=('Arial', 20, 'bold'))
        return False
