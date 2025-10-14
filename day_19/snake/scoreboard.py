from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.update_score()

    def get_highscore(self):
        with open("data.txt", mode="r") as data:
            return int(data.read())

    def write_new_highscore(self, h_score):
        with open("data.txt", mode="w") as data:
            data.write(h_score)

    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.get_highscore()}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_new_highscore(str(self.high_score))
        self.score = 0

    def game_over(self):
        self.update_score()
        self.reset()
