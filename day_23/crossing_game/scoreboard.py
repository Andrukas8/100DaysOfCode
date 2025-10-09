from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGN = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_level()

    def increase_level(self):
        self.level += 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(-60, 0)
        self.write("GAME OVER!", align=ALIGN, font=FONT)
