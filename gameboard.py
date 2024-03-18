from turtle import Turtle

class GameBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)
        self.level = 0
        self.update_board()
    def update_board(self):
        self.clear()
        self.write(f"Level:  {self.level}", move=False, align='center', font=('Arial', 14, 'normal'))

    def increment_level(self):
        self.level += 1
        self.update_board()