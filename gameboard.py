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

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", move=False, align='center', font=('Arial', 44, 'normal'))

    def increase_level(self):
        self.level += 1
