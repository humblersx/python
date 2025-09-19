from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.title("PONG")
screen.tracer(0)

# Paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Ball
ball = Ball()
scoreboard = Scoreboard()

# Paddle movement
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(ball.move_speed)

    if ball.dir == "ne":
        # hits right paddle
        if ball.distance(r_paddle) < 45 and ball.xcor() > 320:
            ball.move_speed *= 0.9
            ball.move_nw()
        # hits top wall
        elif ball.ycor() > 280:
            ball.move_se()
        else:
            ball.move_ne()
    elif ball.dir == "nw":
        # hits left paddle
        if ball.distance(l_paddle) < 45 and ball.xcor() < -320:
            ball.move_speed *= 0.9
            ball.move_ne()
        # hits top wall
        elif ball.ycor() > 280:
            ball.move_sw()
        else:
            ball.move_nw()
    elif ball.dir == "se":
        # hits right paddle
        if ball.distance(r_paddle) < 45 and ball.xcor() > 320:
            ball.move_speed *= 0.9
            ball.move_sw()
        # hits bottom wall
        elif ball.ycor() < -280:
            ball.move_ne()
        else:
            ball.move_se()
    elif ball.dir == "sw":
        # hits left paddle
        if ball.distance(l_paddle) < 45 and ball.xcor() < -320:
            ball.move_speed *= 0.9
            ball.move_se()
        # hits bottom wall
        elif ball.ycor() < -280:
            ball.move_nw()
        else:
            ball.move_sw()

    # Detect when right paddle misses
    if ball.xcor() > 400:
        # change score
        scoreboard.increase_l_score()
        # reset ball
        ball.goto(0,0)
        ball.move_speed = 0.1
        time.sleep(1.0)
        ball.move_sw()
    # Detect when left paddle misses
    elif ball.xcor() < -420:
        # change score
        scoreboard.increase_r_score()
        # reset ball
        ball.goto(0, 0)
        ball.move_speed = 0.1
        time.sleep(1.0)
        ball.move_ne()







screen.exitonclick()
