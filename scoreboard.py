from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(self.level, align="center", font=("Courier", 24, "normal"))
    def next_level(self):
        self.level += 1
    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER",align="center", font=("Courier", 60, "normal") )
