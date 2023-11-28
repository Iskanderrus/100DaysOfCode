# בס״ד

from turtle import Turtle

MOVE_AMOUNT = 50


class Paddle(Turtle):
    def __init__(self, side, screen_width, screen_height):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.speed('fastest')
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

    def up(self):
        if self.ycor() < (self.screen_height / 2 - 60):
            self.forward(MOVE_AMOUNT)

    def down(self):
        if self.ycor() > -(self.screen_height / 2 - 50):
            self.backward(MOVE_AMOUNT)
