from turtle import Turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5




class CarManager(Turtle):

    def __init__(self, position, car_speed):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2, outline=None)
        self.speed = car_speed



    def move(self):
        self.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT










