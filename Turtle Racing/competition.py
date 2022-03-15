import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
UP = 90


class Competition:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            new_car = Turtle("turtle")
            new_car.shapesize(stretch_len=1, stretch_wid=1)
            new_car.setheading(UP)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_x = random.randint(-300, 300)
            new_car.goto(random_x, 300)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT

