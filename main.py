import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    
    #Game over
    for car in car_manager.all_cars:
        if player.distance(car) < 27:
            game_is_on = False
            scoreboard.game_over()
            
        
    #next level
    if player.ycor() >= 279:
        scoreboard.add_level()
        player.reset_position()
        car_manager.add_speed()