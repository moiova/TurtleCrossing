from turtle import Screen
from player import Player
from car_manager import CarManager
from gameboard import GameBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.up, "Up")

car_manager = CarManager()

board = GameBoard()

game_over = False
while not game_over:
    time.sleep(0.3)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            board.game_over()
            game_over = True

    if player.is_player_at_finish_line():
        board.increase_level()
        board.update_board()
        player.go_to_start()
        car_manager.speed_up_cars()

screen.exitonclick()
