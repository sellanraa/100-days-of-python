from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        with open(r"/Users/connorbell/Documents/_vscode/100-days-of-python/day_024_files_directories_paths/snake_game_improved/data.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    # This allows tracking a high score from game to game
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"/Users/connorbell/Documents/_vscode/100-days-of-python/day_024_files_directories_paths/snake_game_improved/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

