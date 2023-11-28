# בס״ד
from turtle import Turtle


class Paddle:
    def __init__(self, side, screen_width):
        self.paddle = []
        self.side = side
        self.screen_width = screen_width
        home_y = 0
        for x in range(5):
            segment = Turtle()
            segment.penup()
            segment.shape('square')
            segment.color('white')
            segment.sety(home_y + x * 20)
            segment.speed(100)
            self.paddle.append(segment)
        self.select_side()

    def select_side(self):
        if self.side == 'left':
            for segment in self.paddle:
                segment.setx(-(self.screen_width / 2)+10)
        elif self.side == 'right':
            for segment in self.paddle:
                segment.setx((self.screen_width / 2)-14)
        else:
            print("Please provide valid side!")
