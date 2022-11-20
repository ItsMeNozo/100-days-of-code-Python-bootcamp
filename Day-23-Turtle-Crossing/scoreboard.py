from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.lvl = 1
        self.print_scoreboard()

    def update_scoreboard(self):
        self.lvl += 1
        self.clear()
        self.print_scoreboard()

    def print_scoreboard(self):
        self.goto(-250, 250)
        self.write(arg=f"Level {self.lvl}", font=FONT)

    def print_game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
