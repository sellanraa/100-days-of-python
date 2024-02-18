from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 48, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(20, 250)
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score_l} - {self.score_r} ", align=ALIGNMENT, font=FONT)
    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score_l(self):
        self.score_l += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_r(self):
        self.score_r += 1
        self.clear()
        self.update_scoreboard()