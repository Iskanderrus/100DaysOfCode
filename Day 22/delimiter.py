# בס״ד

from turtle import Turtle


class Delimiter:
    def __init__(self, screen_height):
        self.delimiter = []
        y_cor = 380
        for x in range(0, 14):
            segment = Turtle('square')
            segment.penup()
            segment.shapesize(1, 0.15)
            segment.color('white')
            segment.goto(0, y_cor - x * 60)
            self.delimiter.append(segment)
