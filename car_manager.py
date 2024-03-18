import random
from turtle import Turtle

car_colors = ["black", "blue", "purple", "orange", "yellow", "green", "brown", "spring green", "coral", "light cyan", "lawn green", "magenta"]
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(car_colors))
        self.shape("square")
        self.shapesize(stretch_wid=0.7, stretch_len=1.2)
        self.setheading(180)
        self.goto(300, random.randrange(-280, 280, 20))
        self.move_speed = 0.2

    def move(self):
        self.forward(20)