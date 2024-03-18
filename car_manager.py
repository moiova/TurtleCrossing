import random
import time
from turtle import Turtle

CAR_COLORS = ["deep sky blue", "deep sky blue", "light steel blue", "purple", "yellow", "yellow", "yellow", "spring green", "coral", "coral", "coral", "light cyan", "lawn green"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.move_speed = 0.2
        self.all_cars = []

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 6:  # slow down car creation
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(CAR_COLORS))
            new_car.shapesize(stretch_wid=0.7, stretch_len=1.2)
            new_car.setheading(180)
            new_car.goto(300, random.randrange(-280, 280, 20))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)
