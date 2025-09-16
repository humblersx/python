from turtle import Turtle, Screen
import random
import colorgram


tim = Turtle()
tim.shape("turtle")
#tim.pensize(10)
tim.speed("fastest")

screen = Screen()

screen.colormode(255)
tim.hideturtle()
#tim.setup (width=200, height=200, startx=0, starty=0)
tim.up()
tim.setpos(-400, -350)

colors = colorgram.extract('image.png', 12)
first_color = colors[random.randint(0, 11)]
rgb = first_color.rgb
tim.pencolor(rgb[0], rgb[1], rgb[2])

# Get colors from image.png
colors = colorgram.extract('image.png', 30)
x = 1
while x < 11:
    for _ in range(10):

        first_color = colors[random.randint(0, 11)]
        rgb = first_color.rgb
        tim.pencolor(rgb[0], rgb[1], rgb[2])
        tim.down()
        tim.dot(20)
        tim.up()
        tim.forward(50)
    # even
    if x % 2 == 0:

        tim.right(90)
        tim.forward(50)
        tim.right(90)
        tim.forward(50)
    # odd
    else:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(50)

    x += 1


screen.exitonclick()






