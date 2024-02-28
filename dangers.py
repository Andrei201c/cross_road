from turtle import Turtle
import random

STEP = 5

color_list = [
    "Red",
    "Green",
    "Blue",
    "Yellow",
    "Orange",
    "Purple",
    "Pink",
    "Brown",
    "Cyan",
    "Magenta",
    "Lime",
    "Teal",
    "Indigo",
    "Olive",
    "Maroon",
    "Navy",
    "Silver",
    "Gold",
    "Black"
]


class Dangers:
    def __init__(self):
        self.cars = []
        self.car_speed = STEP

    def create_car(self):
        random_num = random.randint(1, 5)
        if random_num == 1:
            car = Turtle('square')
            car.shapesize(1, 2)
            car.penup()
            color = random.choice(color_list)
            car.color(color)
            y_pos = random.randint(-180, 180)
            car.goto(500, y_pos)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += STEP

    def reset(self):
        self.car_speed = STEP
