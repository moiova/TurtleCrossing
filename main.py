from turtle import Screen
from player import Player
from car_manager import CarManager
from gameboard import GameBoard
import time

# TODO
#  increase speed when player reaches upper wall

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.up, "Up")

car_manager = CarManager()

board = GameBoard()

game_over = False
while not game_over:
    time.sleep(car_manager.move_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            print("Game over")
            game_over = True

    if player.ycor() > 290:
        board.increment_level()
        player.go_to_start()

screen.exitonclick()
