from turtle import Turtle

FONT = ("Courier", 42, "normal")
ALIGNMENT = 'center'


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 240)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score_left}  {self.score_right}", align=ALIGNMENT, font=FONT)

    def increase(self, left, right):
        if left:
            self.score_left += 1
        elif right:
            self.score_right += 1
        self.update_score()
