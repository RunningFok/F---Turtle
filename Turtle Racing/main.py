import time
from turtle import Screen
from player import Player
from competition import Competition
from scoreboard import Scoreboard

RACE_TIME = 10

screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("adjusted_ocean_2.gif")
screen.bgcolor("white")
screen.tracer(0)
player = Player()
competition = Competition()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")


race_time = RACE_TIME
race_on = True

while race_on:
    time.sleep(0.1)
    race_time -= 0.1
    screen.update()

    competition.create_cars()
    competition.move_cars()

    for car in competition.all_cars:
        if car.distance(player) < 20:
            race_on = False
            scoreboard.game_over()

    if race_time <= 0:
        print("next_level")
        competition.level_up()
        scoreboard.increase_level()
        race_time = + 10


screen.exitonclick()
