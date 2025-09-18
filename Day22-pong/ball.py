from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.dir = "ne"
        self.move_speed = 0.1




    def move_ne(self):
        self.dir = "ne"

        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def move_nw(self):
        self.dir = "nw"
        new_x = self.xcor() - 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def move_se(self):
        self.dir = "se"
        new_x = self.xcor() + 10
        new_y = self.ycor() - 10
        self.goto(new_x, new_y)

    def move_sw(self):
        self.dir = "sw"
        new_x = self.xcor() - 10
        new_y = self.ycor() - 10
        self.goto(new_x, new_y)