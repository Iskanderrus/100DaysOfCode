# בס״ד
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, side, screen_width, screen_height):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.speed(100)
        self.side = side
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.shapesize(1, 6)
        self.setheading(90)
        self.select_side()

    def select_side(self):
        if self.side == 'left':
            self.setx(-(self.screen_width / 2) + 10)
        elif self.side == 'right':
            self.setx((self.screen_width / 2) - 14)
        else:
            print("Please provide valid side!")

    def up(self):
        if self.ycor() < 380:
            self.forward(40)

    def down(self):
        if self.ycor() > -380:
            self.backward(40)
