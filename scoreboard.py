from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, 180)
        self.score_left = 0
        self.score_right = 0
        self.current_score()

    def current_score(self):
        self.clear()
        self.write(arg=f"{self.score_left}  {self.score_right}", align="center", font=("courier", 40, "normal"))

    def increase_left(self):
        self.score_left += 1

    def increase_right(self):
        self.score_right += 1






