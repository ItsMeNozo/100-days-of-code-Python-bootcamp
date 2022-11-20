import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.move, "Up")
screen.listen()

while game_is_on:
    time.sleep(0.05)
    screen.update()
    car_manager.move_cars()
    if player.detect_finish_line():
        scoreboard.update_scoreboard()
        player.go_to_start()
        car_manager.increase_speed()

    for car in car_manager.car_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.print_game_over()
screen.exitonclick()

