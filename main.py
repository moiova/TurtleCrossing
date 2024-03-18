from turtle import Screen
from player import Player
from car_manager import CarManager
from gameboard import GameBoard
import time

# TODO put multiple cars on board
#  increase speed when player reaches upper wall

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

cars = []

new_car = CarManager()

board = GameBoard()

game_over = False
while not game_over:
    time.sleep(new_car.move_speed)
    screen.update()

    new_car.move()

    if player.distance(new_car) < 15:
        print("Game over")
        game_over = True

    if player.ycor() > 290:
        board.increment_level()
        player.go_to_start()

screen.exitonclick()
