from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def create_turtle(color):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color)
    return turtle

turtles = []
for each in colors:
    turtles.append(create_turtle(each))

y = -150
for t in turtles:
    t.setpos(-230, y)
    y += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for race_turtle in turtles:
        if race_turtle.xcor() > 230:
            is_race_on = False
            winning_color = race_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")

            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


        rand_distance = random.randint(0, 10)
        race_turtle.forward(rand_distance)




screen.exitonclick()
# Etch-a-Sketch code
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def counter_clockwise():
#     tim.left(10)
#
# def clockwise():
#     tim.right(10)
#
# def clear():
#     screen.clearscreen()
#     tim = Turtle()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear)

