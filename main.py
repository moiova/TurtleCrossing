from turtle import Screen
import time

# TODO create a player (black turtle) on the bottom of the screen positioned in the middle
#  make it movable up and down

# TODO create the cars randomly (turtles in form of squares)
#  make them move horizontally

# TODO create a game board with a score board
#  detect collision with cars
#  increase speed when player reaches upper wall

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_over = False
while not game_over:
    #time.sleep(cars.move_speed)
    screen.update()


screen.exitonclick()
