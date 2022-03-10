from turtle import Turtle

COLOR = "lavender"


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.color(COLOR)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(side)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
