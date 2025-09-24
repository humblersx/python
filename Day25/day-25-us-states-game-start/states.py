from turtle import Turtle, Screen
FONT = ("Courier", 12, "bold")
ALIGNMENT = "center"



class States(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(state, align=ALIGNMENT, font=FONT)
        #self.goto(x, y)
        # self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    #
     # def update_scoreboard(self):
     #     self.write(f"Level: {self.score} ", align=ALIGNMENT, font=FONT)
    #
    # def increase_score(self):
    #     self.score += 1
    #     self.clear()
    #     self.update_scoreboard()
