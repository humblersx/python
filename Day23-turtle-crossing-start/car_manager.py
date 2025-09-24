from turtle import Turtle, Screen
import time
import random
from PIL import Image

# Open the GIF
img = Image.open("car.gif")

# Resize (e.g., 50x50 pixels)
img = img.resize((75, 75))

# Save to a new file
img.save("smallcar.gif")

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
IMAGE = "smallcar.gif"




class CarManager(Turtle):

    def __init__(self, position, car_speed):
        super().__init__()
        self.penup()
        self.goto(position)
        wn = Screen()
        wn.addshape(IMAGE)
        self.shape(IMAGE)
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=0.02, stretch_len=0.02, outline=None)
        self.speed = car_speed



    def move(self):
        self.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT










