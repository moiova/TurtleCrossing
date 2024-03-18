from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.go_to_start()

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)

    def go_to_start(self):
        self.goto(0, -280)
