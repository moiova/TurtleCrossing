from turtle import Turtle

MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.go_to_start()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(0, -280)

    def is_player_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

