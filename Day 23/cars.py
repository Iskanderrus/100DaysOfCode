# בס״ד
from random import randint, choice
from turtle import Turtle

from crossing_turtle import COLORS

MAX_CARS = 10


class Cars:
    def __init__(self, screen_size: tuple):
        self.cars = []
        self.x_cor = int(screen_size[0] / 2 + 20)
        self.y_cor = int(screen_size[1] / 2)
        self.make_cars()
        self.increment = 0

    def make_cars(self):
        for x in range(randint(5, 10)):
            car = Turtle('square')
            car.shapesize(1, 2)
            car.color(choice(COLORS))
            car.penup()
            car.setheading(180)
            car.goto(self.x_cor + randint(-5, 5), randint(-self.y_cor + 80, self.y_cor - 80))
            self.cars.append(car)

    def move_cars(self, max_move=10):
        for car in self.cars:
            car.forward(randint(1, max_move + self.increment))

    def level_up(self):
        self.increment += 1
        self.make_cars()
