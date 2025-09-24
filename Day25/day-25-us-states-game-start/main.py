import turtle
import pandas
from states import States
import time

FONT = ("Courier", 24, "bold")
ALIGNMENT = "center"

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)




data = pandas.read_csv("50_states.csv")

game_is_on = True
state_count = 0

first_time = True
score = 0


while game_is_on:
    if first_time:
        # Prompt user for the first time
        answer_state = (screen.textinput(title="Guess the State", prompt="What's another state's name?")).title()
        first_time = False
    else:
        # Prompt user
        answer_state = (screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")).title()
    # Check if answer_state exists in data
    if data['state'].str.contains(answer_state).any():
        # The string exists
        state = data[data.state == answer_state]
        # print state on screen
        state_string = state['state'].to_string(index=False)
        state_xcor = int(state['x'].to_string(index=False))
        state_ycor = int(state['y'].to_string(index=False))
        print_state = States(state_string, state_xcor, state_ycor)
        #print_state.update_scoreboard()
        state_count += 1
        # Increase score
        score += 1

    # Check to see if 50 states answered
    if state_count > 49:
        final = turtle.Turtle()
        final.hideturtle()
        final.goto(0, 0)
        final.write("You win! You have guessed all 50 states!", align=ALIGNMENT, font=FONT)
        game_is_on = False








screen.exitonclick()

