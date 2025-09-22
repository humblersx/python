import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()


turtle = Player()

# Turtle movement
screen.listen()
screen.onkey(turtle.go_up, "Up")


list_of_cars = []
car_speed = 5
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    interval = random.randint(1, 6)

    # 1 out of 6 times, create a new car and add to list
    if interval == 6:
        # Create car at random position
        y_cor = random.randint(-240, 250)
        car = CarManager((260, y_cor), car_speed)
        list_of_cars.append(car)

    # move cars
    for each in list_of_cars:
        each.move()

        # if car hits turtle
        if each.distance(turtle) < 25 and turtle.xcor() < each.xcor():
            game_is_on = False
            scoreboard.game_over()

        # if car reaches end, remove it
        if each.xcor() < -300:
            list_of_cars.remove(each)
            each.hideturtle()

    # if turtle reaches top
    if turtle.ycor() > 270:
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        turtle.goto(0, -280)
        car_speed += 5

        for each in list_of_cars:
            each.increase_speed()























screen.exitonclick()