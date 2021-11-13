from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_a =0
        self.score_b =0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Player A: {self.score_a}  Player B: {self.score_b}", False, "center", ("Arial", 24, "normal"))
        self.hideturtle()

    def rewrite_a(self):
        self.score_a += 1
        self.clear()
        self.write(f"Player A: {self.score_a}  Player B: {self.score_b}", False, "center", ("Arial", 24, "normal"))

    def rewrite_b(self):
        self.score_b += 1
        self.clear()
        self.write(f"Player A: {self.score_a}  Player B: {self.score_b}", False, "center", ("Arial", 24, "normal"))
