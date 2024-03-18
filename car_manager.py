import random
from turtle import Turtle

CAR_COLORS = ["deep sky blue", "deep sky blue", "light steel blue", "purple", "yellow", "yellow", "yellow", "spring green", "coral", "coral", "coral", "light cyan", "lawn green"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_number = random.randint(1, 10)
        if random_number == 1 or 8:  # slow down car creation
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(CAR_COLORS))
            new_car.shapesize(stretch_wid=0.7, stretch_len=1.2)
            new_car.setheading(180)
            new_car.goto(300, random.randrange(-280, 280, 20))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def speed_up_cars(self):
        self.car_speed += MOVE_INCREMENT
