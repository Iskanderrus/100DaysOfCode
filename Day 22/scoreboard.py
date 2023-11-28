from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, user1, user2):
        super().__init__()
        self.color('white')
        self.speed('fastest')
        self.users = [user1, user2]
        self.scores = [0, 0]
        self.positions = [(-250, 375), (250, 375)]
        self.penup()
        self.hideturtle()
        self.keys = ["A / Z", "Up / Down"]
        self.message()

    def message(self):
        for x in range(2):
            self.goto(self.positions[x])
            self.write(f"{self.users[x]}'s Score: {self.scores[x]}  {self.keys[x]}", align='center', font=('Arial', 20, 'bold'))

    def increase_score(self, user):
        self.scores[self.users.index(user)] += 1
        self.clear()
        self.message()
