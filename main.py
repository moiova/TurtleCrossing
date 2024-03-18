from turtle import Screen
from player import Player
from car_manager import CarManager
import time

# TODO create a game board with a score board
#  detect collision with cars
#  increase speed when player reaches upper wall

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

cars = CarManager()

game_over = False
while not game_over:
    time.sleep(cars.move_speed)
    screen.update()

    cars.move()



screen.exitonclick()
